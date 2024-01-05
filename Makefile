json-editor:
	python -m build .

debug_install:
	python -m pip install -e .

test:
	python -m pytest --junitxml=test_reports/results.xml

.PHONY : json-editor debug_install
