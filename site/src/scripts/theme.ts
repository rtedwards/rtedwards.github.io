// Shared theme state for the page and its charts. The toggle sets data-theme on <html>
// and saves the choice; without one, the system colour scheme decides.
export type Theme = 'light' | 'dark';

const systemDark = matchMedia('(prefers-color-scheme: dark)');

export function currentTheme(): Theme {
  const explicit = document.documentElement.dataset.theme as Theme | undefined;
  return explicit ?? (systemDark.matches ? 'dark' : 'light');
}

export function setTheme(theme: Theme) {
  document.documentElement.dataset.theme = theme;
  try {
    localStorage.setItem('theme', theme);
  } catch {}
  window.dispatchEvent(new Event('themechange'));
}

// Calls back with the new theme whenever the toggle or the system setting changes.
export function onThemeChange(callback: (theme: Theme) => void) {
  const fire = () => callback(currentTheme());
  window.addEventListener('themechange', fire);
  systemDark.addEventListener('change', fire);
}
