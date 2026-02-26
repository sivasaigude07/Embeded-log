# Embedded Log Labs (Python) — Generator ➜ Capture ➜ Parse ➜ Panic Detect ➜ CSV Report ➜ Pytest ➜ CI

This repo is a **7-lab mini project**:
1) Simulate device logs using a Python generator
2) Capture logs to file
3) Build parser
4) Add panic detection
5) Generate CSV report
6) Write pytest cases
7) Integrate into CI (GitHub Actions)

## Prereqs
- Python 3.10+ (3.11 recommended)

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt
```

## Lab 1 — Simulate Device Logs (Generator)
```bash
python -m embedded_log_labs.simulator --lines 50 --panic-prob 0.05
```

## Lab 2 — Capture Logs to File
```bash
python -m embedded_log_labs.capture --out logs/device.log --lines 200 --panic-prob 0.02
```

## Lab 3 + 4 + 5 — Parse Logs + Panic Detection + CSV Report
```bash
python -m embedded_log_labs.analyze --in logs/device.log --csv reports/report.csv
```

## Lab 6 — Pytest
```bash
pytest -q
```

## Lab 7 — CI (GitHub Actions)
Workflow file: `.github/workflows/ci.yml`

## One-command demo (full pipeline)
```bash
python main.py --lines 200 --panic-prob 0.02 --log logs/device.log --csv reports/report.csv
```
