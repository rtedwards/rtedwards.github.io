import { getCollection } from 'astro:content';

// Drafts are visible under `astro dev` and hidden in production builds.
export function getPublishedPosts() {
  return getCollection('posts', ({ data }) => import.meta.env.DEV || !data.draft);
}
