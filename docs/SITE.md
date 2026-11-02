# Matte-black single-page version

[Home](../README.md)

The complete cheat sheet stays on one page in its familiar sequence. There is no sidebar, category tree or hidden content. The top program selector jumps to the section you choose; browser Find searches the entire document. Command blocks have copy buttons with a manual-selection fallback.

## Read locally

Open index.html from a downloaded copy, or serve the repository folder with Python on loopback. All styling/scripts are local. GitHub's Markdown renderer does not accept custom CSS; the README includes a matte-black header, but your GitHub theme controls the rest of the repository view.

## Rebuild after editing Markdown

Requires Node 20+ and the pinned Marked package:

```bash
npm install --ignore-scripts
npm run build
```

The committed index.html is ready to read without a build. Edit the individual Markdown guides under docs/programs/ and run the build. It regenerates the program area of README.md and the styled index.html while preserving the README introduction and closing notes. programs.json records the original tool order.

## Optional GitHub Pages hosting

If Pages is enabled for the repository, select main and the repository root in Settings → Pages → Build and deployment. The root index.html is the entry point. This is a static site and needs no account login, database, analytics, external fonts or CDN.
