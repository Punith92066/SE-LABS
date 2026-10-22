# Lab 5: Static Code Analysis — Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were style and maintainability problems, such as the unused `datetime` import, inconsistent function naming, and missing docstrings. These changes were straightforward and did not alter the intended behaviour.

The harder issues were the SQL injection risk in `addArtifact()` and the shell invocation in `backupNote()`. The SQL statement was built by concatenating values into the query, so special SQL characters in a title or era could change the query. I replaced concatenation with parameterized SQL. I also changed the backup command to use `subprocess.run()` with an argument list and `shell=False`. Input validation and handling unknown artifact IDs required explicit decisions about expected behaviour.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

A warning about `shell=True` can be context-dependent. In the original program, the command is a fixed string, so the immediate command-injection risk is lower than it would be if untrusted input were inserted into the command. However, the warning is still useful because shell execution is unnecessary here and could become dangerous if the command changes later.

I cannot confirm that the tools reported a false positive without reviewing the actual Pylint, Bandit, and Flake8 output files. This answer should be updated if the reports from my run identify a specific false positive.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Pylint, Flake8, and Bandit during development and before committing changes. I would prioritize security and correctness findings, document issues that need a decision, and rerun the tools after making fixes. I would also configure continuous integration, such as GitHub Actions, to run checks on each push and pull request. This makes problems visible early and helps prevent regressions. Tool output should be reviewed in context rather than accepted blindly.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The revised code uses parameterized SQL, validates artifact inputs, and reports unknown artifact IDs clearly. It also uses a safer subprocess call, removes an unused import, follows snake_case naming, adds docstrings, and avoids running the demo when imported as a module. The total-value query uses SQLite's `SUM()` function instead of fetching every matching row into Python.

These changes improve readability, maintainability, and robustness while reducing SQL injection risk. The tools must be rerun to verify which warnings have been resolved and to record the final Pylint score.
