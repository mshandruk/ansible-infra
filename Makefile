.DEFAULT_GOAL := help
.PHONY: help check-uv setup lint

help:
	@echo "Targets:"
	@echo "	setup	Create virtual environment and install dependencies"
	@echo "	lint    Run ansible-lint"

check-uv:
	@command -v uv >/dev/null || { \
		echo "uv is required: https://docs.astral.sh/uv/"; \
		exit 1; \
	}

setup: check-uv
	uv venv
	. .venv/bin/activate && uv pip install -r requirements.txt
	@echo ""
	@echo "Setup completed."
	@echo ""
	@echo "Activate the environment:"
	@echo "source .venv/bin/activate"

lint:
	. .venv/bin/activate && ansible-lint
