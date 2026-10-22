# Lab 5 — Static Code Analysis: Museum Artifact Catalog

## Deliverables
- `museum_catalog.py` — revised program
- `issues.md` — issue table
- `reflection.md` — four reflection answers

## Setup (Windows CMD)
```bat
py -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8
```

## Run the program
```bat
python museum_catalog.py
```
Expected output:
```text
on display
135000
catalog backup complete
```

## Run the tools and save reports
```bat
pylint museum_catalog.py > pylint_report.txt
bandit -r museum_catalog.py > bandit_report.txt
flake8 museum_catalog.py > flake8_report.txt
```
Pylint may return a non-zero exit code when it finds messages; the report can still be written. Open all reports and review them.

## Verify after fixing
```bat
python museum_catalog.py
pylint museum_catalog.py
bandit -r museum_catalog.py
flake8 museum_catalog.py
```
Do not claim a warning is fixed unless the rerun confirms it. Check the line references in `issues.md` against your exact starter file. Include the generated report files if your instructor requests evidence.

## Security note
The original program contains a hard-coded `CURATOR_PASSWORD` that is not used. The revised demonstration omits it. In a real application, load necessary secrets from environment configuration or a secret manager; never commit real credentials to Git.
