// Adds a copy button to every code block on the page.
// If the clipboard is unavailable (for example, an insecure context), no buttons
// are added, so the page still works without them.

const clipboardIcon = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>`;
const checkIcon = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20 6 9 17l-5-5"/></svg>`;

async function copy(pre: HTMLPreElement, button: HTMLButtonElement) {
  try {
    await navigator.clipboard.writeText(pre.innerText);
    button.innerHTML = checkIcon;
    button.setAttribute('aria-label', 'Copied');
  } catch {
    button.setAttribute('aria-label', 'Copy failed');
  }
  setTimeout(() => {
    button.innerHTML = clipboardIcon;
    button.setAttribute('aria-label', 'Copy code to clipboard');
  }, 1500);
}

if (navigator.clipboard) {
  for (const pre of document.querySelectorAll<HTMLPreElement>('pre')) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-code';
    button.innerHTML = clipboardIcon;
    button.setAttribute('aria-label', 'Copy code to clipboard');
    button.title = 'Copy code';
    button.addEventListener('click', () => copy(pre, button));

    pre.append(button);
  }
}
