#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

export ANALYSIS_READY_FILE="${ANALYSIS_READY_FILE:-$PROJECT_ROOT/data/processed/analysis_ready_responses.csv}"
export DISSERTATION_ANALYSIS_OUTPUT="${DISSERTATION_ANALYSIS_OUTPUT:-$PROJECT_ROOT/results}"
export JUPYTER_CONFIG_DIR="${JUPYTER_CONFIG_DIR:-$PROJECT_ROOT/.jupyter-local}"
export JUPYTER_DATA_DIR="${JUPYTER_DATA_DIR:-$PROJECT_ROOT/.jupyter-local/data}"
export JUPYTER_RUNTIME_DIR="${JUPYTER_RUNTIME_DIR:-$PROJECT_ROOT/.jupyter-local/runtime}"
export IPYTHONDIR="${IPYTHONDIR:-$PROJECT_ROOT/.ipython-local}"

mkdir -p "$JUPYTER_RUNTIME_DIR"

"$PYTHON_BIN" -m jupyter nbconvert \
  --to notebook \
  --execute "$PROJECT_ROOT/notebooks/03_comprehensive_dissertation_analysis_colab.ipynb" \
  --output prompt-sensitivity-analysis-executed.ipynb \
  --output-dir "${TMPDIR:-/tmp}" \
  --ExecutePreprocessor.timeout=1800

"$PYTHON_BIN" "$PROJECT_ROOT/scripts/validate_project.py"

echo "Analysis complete: $DISSERTATION_ANALYSIS_OUTPUT"
