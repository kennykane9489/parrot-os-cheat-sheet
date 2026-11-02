(() => {
  'use strict';
  const select = document.getElementById('program-jump');
  const status = document.getElementById('status');
  let timer;
  function say(message) {
    status.textContent = message; status.hidden = false;
    clearTimeout(timer); timer = setTimeout(() => { status.hidden = true; }, 3500);
  }
  function jump() {
    const target = document.getElementById(select.value);
    if (!target) return;
    location.hash = select.value;
    target.scrollIntoView({block:'start'});
    const heading = target.nextElementSibling;
    if (heading) { heading.tabIndex = -1; heading.focus({preventScroll:true}); }
  }
  document.getElementById('jump-button').addEventListener('click', jump);
  select.addEventListener('keydown', event => { if (event.key === 'Enter') jump(); });
  document.querySelectorAll('pre').forEach(pre => {
    const wrap = document.createElement('div'); wrap.className = 'code-wrap';
    pre.parentNode.insertBefore(wrap,pre); wrap.appendChild(pre);
    const button = document.createElement('button'); button.type = 'button'; button.className = 'copy';
    button.textContent = 'Copy'; button.setAttribute('aria-label','Copy this command block');
    button.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(pre.querySelector('code')?.textContent || pre.textContent);
        button.textContent = 'Copied'; say('Copied. Read the command before running it.');
        setTimeout(() => { button.textContent = 'Copy'; }, 1700);
      } catch {
        const range=document.createRange();range.selectNodeContents(pre);
        const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);
        say('Code selected. Use your device’s Copy command.');
      }
    });
    wrap.appendChild(button);
  });
})();
