import { getPublishedPosts } from '../lib/posts';
import rss from '@astrojs/rss';
import type { APIContext } from 'astro';

// Same path as the Quarto feed (index.xml), so existing subscribers keep working.
export async function GET(context: APIContext) {
  const posts = await getPublishedPosts();
  return rss({
    title: "The Bear's Toes",
    description: 'Statistics, machine learning, distributed systems and geospatial notes.',
    site: context.site!,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.date,
      link: `/posts/${post.id}/`,
      categories: post.data.categories,
    })),
  });
}
