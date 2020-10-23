
# Programs
PIP:=pip3
PYTHON:=python3
JUPYTER:=jupyter

# Directories
DIR_SRC:=taylorseries
DIR_TEST:=tests

init:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(DIR_SRC)/taylorseries.py

test:
	$(PYTHON) -m unittest -v $(DIR_TEST)/test_taylorseries.py

jupyter:
	$(JUPYTER) notebook --allow-root

readme:
	$(JUPYTER) nbconvert --to notebook --inplace --execute README.ipynb
	$(JUPYTER) nbconvert --to markdown README.ipynb