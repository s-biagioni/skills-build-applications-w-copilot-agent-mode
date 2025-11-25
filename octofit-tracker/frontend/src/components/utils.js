export function getColumns(items) {
  if (!items || items.length === 0) return [];
  const first = items.find(it => it && typeof it === 'object');
  if (!first) return ['value'];
  return Object.keys(first);
}

export function formatValue(value) {
  if (value === null || value === undefined) return '';
  if (typeof value === 'object') return JSON.stringify(value);
  return String(value);
}

export function ensureItems(json) {
  if (!json) return [];
  if (Array.isArray(json)) return json;
  if (json && json.results) return json.results;
  return [json];
}
