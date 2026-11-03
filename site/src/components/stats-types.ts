// Shape of the stats.json files written by scripts/build_artifacts.py.
export interface Stats {
  n: number;
  rows: { series: string; mean: number; var: number }[];
}
