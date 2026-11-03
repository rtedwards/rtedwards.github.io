// Browsers collapse runs of spaces, so the two spaces after a sentence end in the
// source would render as one. This rehype plugin swaps those two spaces for two
// no-break spaces. They keep their width, and a line never breaks between them.
// Code is left alone.
const SKIP_TAGS = new Set(['pre', 'code']);

function walk(node, inCode) {
  if (node.type === 'text' && !inCode) {
    node.value = node.value.replace(/([.!?]) {2}(?=\S)/g, '$1  ');
  }
  if (node.children) {
    const childInCode = inCode || (node.type === 'element' && SKIP_TAGS.has(node.tagName));
    for (const child of node.children) walk(child, childInCode);
  }
}

export default function doubleSpace() {
  return (tree) => walk(tree, false);
}
