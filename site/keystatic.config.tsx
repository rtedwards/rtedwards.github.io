import { collection, config, fields, singleton } from '@keystatic/core';
import { block, wrapper } from '@keystatic/core/content-components';

// Custom components the posts use. Names match the components registered in src/pages/posts/[slug].astro.
const postComponents = {
  Callout: wrapper({ label: 'Callout', schema: {} }),
  Note: wrapper({ label: 'Margin note', schema: {} }),
  Pair: wrapper({ label: 'Two equations side by side', schema: {} }),
  Cell: wrapper({ label: 'Column of a pair', schema: {} }),
  Chart: block({
    label: 'Chart',
    schema: { name: fields.text({ label: 'Chart name' }) },
  }),
  StatsTable: block({
    label: 'Stats table',
    schema: { name: fields.text({ label: 'Stats name' }) },
  }),
};

// Editing runs in `astro dev` at /keystatic. Each save writes the MDX file in
// src/content/posts/, so the change is an ordinary git diff.
export default config({
  storage: { kind: 'local' },
  singletons: {
    about: singleton({
      label: 'About',
      path: 'src/content/about',
      format: { contentField: 'content' },
      schema: {
        name: fields.text({ label: 'Name' }),
        tagline: fields.text({ label: 'Tagline' }),
        description: fields.text({ label: 'Page description', multiline: true }),
        content: fields.mdx({ label: 'Body' }),
      },
    }),
  },
  collections: {
    posts: collection({
      label: 'Posts',
      slugField: 'title',
      path: 'src/content/posts/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Title' } }),
        description: fields.text({ label: 'Description', multiline: true }),
        date: fields.date({ label: 'Date' }),
        categories: fields.array(fields.text({ label: 'Category' }), {
          label: 'Categories',
          itemLabel: (props) => props.value,
        }),
        draft: fields.checkbox({ label: 'Draft', defaultValue: false }),
        content: fields.mdx({ label: 'Content', components: postComponents }),
      },
    }),
  },
});
