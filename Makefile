.PHONY: test lint check

test:
	cd backend && python -m pytest tests -v

lint:
	cd backend && python -m ruff check app tests

check: lint test