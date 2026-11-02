import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
import { marked } from 'marked';
const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const slug = s => s.toLowerCase().replace(/[^\p{L}\p{N}_\- ]/gu, '').replaceAll(' ', '-');
const catalog = JSON.parse(fs.readFileSync(path.join(root, 'programs.json'), 'utf8'));
let source = fs.readFileSync(path.join(root, 'README.md'), 'utf8');
// Source guides regenerate only the program area; keep introduction and closing notes intact.
let programArea = '';
for (const item of catalog) {
  let text = fs.readFileSync(path.join(root, item.path), 'utf8');
  text = text.slice(text.indexOf('\n\n') + 2).replace(/^\[All programs\].*\n\n/, '');
  text = text.replace(/\n## Updates and removal\n[\s\S]*?(?=\n## Reference and compatibility)/, '');
  text = text.replace(/## Reference and compatibility\n\n\[Upstream documentation\]\(([^)]+)\)[\s\S]*/, '**Reference:** [Official documentation]($1).');
  for (const other of catalog) text = text.replaceAll('](' + other.slug + '.md)', '](#program-' + other.slug + ')');
  text = text.replace(/^(#{2,5}) /gm, '#$1 ');
  programArea += '<a id="program-' + item.slug + '"></a>\n\n## ' + item.title + '\n\n' + text.trim() + '\n\n[Back to top](#jump-to-a-program)\n\n---\n\n';
}
const start = source.indexOf('<a id="program-' + catalog[0].slug + '">');
const end = source.indexOf('## Local viewing and checks', start);
if (start < 0 || end < 0) throw new Error('README program boundaries missing');
source = source.slice(0, start) + programArea + source.slice(end);
fs.writeFileSync(path.join(root, 'README.md'), source);
const counts = new Map();
const renderer = new marked.Renderer();
renderer.heading = function ({tokens, depth}) {
  const text = this.parser.parseInline(tokens);
  const base = slug(text.replace(/<[^>]*>/g, ''));
  const n = counts.get(base) || 0; counts.set(base, n + 1);
  return `<h${depth} id="${base}${n ? '-' + n : ''}">${text}</h${depth}>\n`;
};
let body = marked.parse(source, {renderer, gfm:true});
body = body.replace(/<p><img[^>]*banner\.svg[^>]*><\/p>\n?/g, '');
body = body.replace(/<table>/g, '<div class="table-wrap"><table>').replace(/<\/table>/g,'</table></div>');
body = body.replace(/href="([^"#]+\.md)(#[^"]*)?"/g, (_, file, anchor='') => `href="https://github.com/kennykane9489/parrot-os-cheat-sheet/blob/main/${esc(file)}${anchor}"`);
// This sentence is useful on GitHub but redundant inside the already-styled view.
body = body.replace(/<p><strong>Find a tool:<\/strong>.*?<\/p>/s,'');
const options = catalog.map(x=>`<option value="program-${x.slug}">${esc(x.title)}</option>`).join('');
const html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="One-page Parrot OS cheat sheet with installation, practical examples and troubleshooting for 61 tools."><meta name="theme-color" content="#111214"><title>Parrot OS Cheat Sheet</title><link rel="stylesheet" href="assets/style.css"><script defer src="assets/app.js"></script></head><body><a class="skip" href="#cheat-sheet">Skip to cheat sheet</a><header class="toolbar"><a class="wordmark" href="#parrot-os-cheat-sheet"><span aria-hidden="true">&gt;_</span> PARROT OS</a><div class="jump"><label for="program-jump">Jump to program</label><select id="program-jump"><option value="">Choose a tool…</option>${options}</select><button type="button" id="jump-button">Go</button></div><a class="repo" href="https://github.com/kennykane9489/parrot-os-cheat-sheet">GitHub ↗</a></header><main id="cheat-sheet" class="sheet" tabindex="-1">${body}</main><footer class="footer">One page. Your tools. Your lab. <a href="#parrot-os-cheat-sheet">Back to top ↑</a></footer><div id="status" class="toast" role="status" aria-live="polite" hidden></div><noscript><p class="noscript">All commands remain readable. Use the jump links or your browser’s Find command; copy manually.</p></noscript></body></html>`;
fs.writeFileSync(path.join(root,'index.html'),html);
console.log(`Built continuous index.html: ${catalog.length} programs, ${Buffer.byteLength(html)} bytes.`);
