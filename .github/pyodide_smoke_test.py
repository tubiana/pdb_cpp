"""Smoke test: run a real af_analysis analysis inside Pyodide (used by pyodide-wheel.yml)."""
import af_analysis
from af_analysis import analysis

d = af_analysis.Data("/tmp/afa/tests/inputs/beta_amyloid_dimer_cf_1.5.5")
print("format:", d.format, "| models:", len(d.df))
analysis.pdockq(d)
analysis.pdockq2(d)
print(d.df.filter(regex="query|rank|plddt|pdockq").head())
print("AF_ANALYSIS RUNS IN PYODIDE")
