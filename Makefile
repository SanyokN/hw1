.PHONY: run
run:
	@echo ';)'
	@echo 'qwerty'
	@echo '321'
	@python main.py

.PHONY: build-win
build-win:
	python.exe -m pip install --upgrade pip
	pip install poetry
	poetry config --local virtualenvs.in-project true
	poetry init -n
	poetry install