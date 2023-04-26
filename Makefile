.PHONY: setup
setup:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install pre-commit && \
	pre-commit install && \
	pre-commit autoupdate

.PHONY: run-all
run-all:
	@. .venv/bin/activate && \
	number=1 ; while [[ $$number -le 25 ]] ; do \
		echo Running Day $${number} ; \
		python3 -m day$${number}.run ; \
		((number = number + 1)) ; \
		echo ; \
    done

.PHONY: run
run:
	@. .venv/bin/activate && python3 -m day$(day).run

.PHONY: pre-commit
pre-commit:
	@. .venv/bin/activate && pre-commit run --all-files
