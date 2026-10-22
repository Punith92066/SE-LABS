# Static Analysis Issues — Museum Artifact Catalog

> This table is based on inspection of the original code supplied in the lab. Verify the exact line numbers against your starter file and use the reports generated on your own system as evidence.

| Issue | Type / Severity | Approx. location in original | Description | Fix approach |
|---|---|---|---|---|
| SQL query built by string concatenation | Security — High | `addArtifact()` INSERT | Title and era are concatenated into SQL, allowing special input to alter the query. | Use parameterized SQL placeholders (`?`) and pass values as a tuple. |
| Shell invocation with `shell=True` | Security — Medium | `backupNote()` | Invokes a shell unnecessarily and can become dangerous if untrusted input is added later. | Use `subprocess.run()` with an argument list and `shell=False`. |
| Hard-coded curator password | Security/configuration — Medium | Global constant | A credential in source code can be exposed in repository history; it is also unused. | Remove it if unnecessary, or load secrets from environment configuration/secret manager. |
| Missing input validation | Robustness — Medium | `addArtifact()` | Empty titles/eras, negative values, or invalid display flags could be stored. | Validate arguments and add database constraints. |
| Missing check for unknown artifact ID | Bug/robustness — Medium | `displayStatus()` | `fetchone()` returns `None` for an unknown ID; indexing it raises an unclear error. | Check for `None` and raise a clear `ValueError`. |
| Inefficient total calculation in Python | Maintainability/performance — Low | `totalValue()` | Fetches each value and sums in Python instead of using SQL aggregation. | Use `SUM()` with `COALESCE()`. |
| Non-PEP 8 function naming | Style — Low | Function definitions | Names use camelCase instead of Python snake_case. | Rename to `add_artifact`, `total_value`, etc. |
| Missing docstrings | Maintainability — Low | File/functions | Purpose and expected behaviour are not documented. | Add concise docstrings. |
| Unused import | Style — Low | Import section | `datetime` is imported but unused. | Remove the import. |
| Demo runs on import | Maintainability — Low | Final `main()` call | Importing the module automatically runs the demonstration. | Use an `if __name__ == "__main__":` guard. |
