import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
function element(name) {
  return {name,handlers:{},children:[],textContent:'',hidden:false,addEventListener(event,handler){this.handlers[event]=handler;},setAttribute(){},appendChild(e){this.children.push(e);},scrollIntoView(){this.scrolled=true;},focus(){this.focused=true;}};
}
const select=element('select');select.value='program-nmap';
const status=element('status');
const go=element('go');
const target=element('anchor');target.nextElementSibling=element('heading');
const pre=element('pre');pre.textContent='nmap -sT -p 8000 127.0.0.1';pre.querySelector=()=>null;pre.parentNode={insertBefore(){}};
const created=[];const copied=[];let selectionMade=false;
const context={document:{getElementById(id){return {'program-jump':select,status,'jump-button':go,'program-nmap':target}[id];},querySelectorAll(){return [pre];},createElement(name){const e=element(name);created.push(e);return e;},createRange(){return {selectNodeContents(){}};}},navigator:{clipboard:{async writeText(text){copied.push(text);}}},location:{hash:''},window:{getSelection(){return {removeAllRanges(){},addRange(){selectionMade=true;}};}},setTimeout(){return 1;},clearTimeout(){}};
vm.runInNewContext(fs.readFileSync(new URL('../assets/app.js',import.meta.url),'utf8'),context);
go.handlers.click();
assert.equal(context.location.hash,'program-nmap');
assert.ok(target.scrolled);assert.ok(target.nextElementSibling.focused);
const copy=created.find(e=>e.name==='button');
await copy.handlers.click();
assert.deepEqual(copied,[pre.textContent]);
assert.equal(copy.textContent,'Copied');
context.navigator.clipboard=undefined;
await copy.handlers.click();
assert.ok(selectionMade);
assert.match(status.textContent,/Code selected/);
select.value='not-a-real-guide';go.handlers.click();
assert.equal(context.location.hash,'program-nmap');
console.log('PASS: jump, focus, copy, clipboard fallback and missing-target behavior.');
