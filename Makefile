.PHONY: format lint clean-notebooks

format:
	black .

lint:
	black --check .
	ruff check .

# Strips output/metadata from all notebooks before committing (requires
# nbstripout — uncomment it in requirements.txt first)
clean-notebooks:
	find notebooks -name '*.ipynb' -exec nbstripout {} \;
