import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    categories: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

// The About page is a single document, edited in Keystatic as a singleton.
const about = defineCollection({
  loader: glob({ pattern: 'about.mdx', base: './src/content' }),
  schema: z.object({
    name: z.string(),
    tagline: z.string(),
    description: z.string(),
  }),
});

export const collections = { posts, about };
