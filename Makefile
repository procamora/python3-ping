#!/usr/bin/env make

OUTPUTEGG=procamora_sqlite3.egg-info/
OUTPUTDIST=dist/


# python3 -m pip install --user --upgrade setuptools wheel twine

dist:
	python3 setup.py sdist


#https://twine.readthedocs.io/en/latest/
upload:
	twine upload dist/* -u procamora --verbose 


clean:
	[ ! -d $(OUTPUTEGG) ] || rm -rf $(OUTPUTEGG) 
	[ ! -d $(OUTPUTDIST) ] || rm -rf $(OUTPUTDIST) 



.PHONY: dist clean
