// @ts-check
import { defineConfig } from 'astro/config';

import { unified } from '@astrojs/markdown-remark';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import react from '@astrojs/react';
import keystatic from '@keystatic/astro';
import rehypeMathjax from 'rehype-mathjax';
import remarkMath from 'remark-math';
import doubleSpace from './plugins/double-space.mjs';

// https://astro.build/config
export default defineConfig({
  // Feeds the sitemap, RSS links and Open Graph tags, as `website.site-url` did in Quarto.
  site: 'https://bear-toes.pages.dev',
  // Keystatic's editor routes need a server, so they are added to `astro dev` only.
  integrations: [mdx(), sitemap(), react(), ...(process.argv.includes('dev') ? [keystatic()] : [])],
  markdown: {
    // Shiki highlights Python, Rust and anything else at build time, with no runtime JS.
    // Both themes are emitted as CSS variables, so styles/global.css picks one per colour scheme.
    shikiConfig: {
      themes: { light: 'gruvbox-light-hard', dark: 'gruvbox-dark-hard' },
      defaultColor: false,
    },
    // The unified pipeline keeps remark/rehype plugins. KaTeX renders $...$ and $$...$$
    // at build time, as Quarto did. doubleSpace keeps the house-style double space visible.
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeMathjax, doubleSpace],
    }),
  },
});
