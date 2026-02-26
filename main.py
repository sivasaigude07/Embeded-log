from __future__ import annotations

import argparse
from pathlib import Path

from embedded_log_labs.capture import capture_to_file
from embedded_log_labs.analyze import analyze_file, verdict, write_csv

def main() -> int:
    p = argparse.ArgumentParser(description="Run full pipeline: simulate -> capture -> analyze -> report.")
    p.add_argument("--log", default="logs/device.log")
    p.add_argument("--csv", default="reports/report.csv")
    p.add_argument("--lines", type=int, default=200)
    p.add_argument("--panic-prob", type=float, default=0.02)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--error-threshold", type=int, default=2)
    args = p.parse_args()

    log_path = Path(args.log)
    capture_to_file(log_path, lines=args.lines, panic_prob=args.panic_prob, seed=args.seed)

    summary = analyze_file(log_path)
    v = verdict(summary, error_threshold=args.error_threshold)
    write_csv(summary, Path(args.csv), v)

    print(f"Done. Verdict={v}. Log={log_path} CSV={args.csv}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
