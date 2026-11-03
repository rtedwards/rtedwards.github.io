import { getPublishedPosts } from '../lib/posts';
import type { APIContext } from 'astro';

// The llms.txt convention (https://llmstxt.org): a title, a summary, then links with
// short descriptions. Generated from the post collection so it never goes stale.
export async function GET(context: APIContext) {
  const site = context.site!.toString().replace(/\/$/, '');
  const posts = (await getPublishedPosts())
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  const lines = [
    "# The Bear's Toes",
    '',
    '> A personal blog by Robert Edwards on statistics, machine learning, distributed systems, geospatial work and programming languages such as Python and Rust.',
    '',
    '## Posts',
    '',
    ...posts.map(
      (post) =>
        `- [${post.data.title}](${site}/posts/${post.id}/): ${post.data.description} (${post.data.date.toISOString().slice(0, 10)})`,
    ),
    '',
    '## Optional',
    '',
    `- [About](${site}/about/): who writes the blog`,
    `- [RSS feed](${site}/index.xml): new posts as they are published`,
    '',
  ];

  return new Response(lines.join('\n'), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
