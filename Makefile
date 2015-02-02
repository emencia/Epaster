
.PHONY: help install clean delpyc

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- to proceed to a new install of this project. Use clean command before if you want to reset a current install"
	@echo "  clean  -- to clean your local repository from all stuff created by buildout and instance usage"
	@echo "  delpyc  -- to remove all *.pyc files, this is recursive from the current directory"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc 
	rm -Rf bin docs/_build include eggs lib parts develop-eggs .installed.cfg local

install:
	virtualenv --no-site-packages --setuptools --python python2 .
	bin/pip install 'setuptools==7.0'
	bin/pip install 'pip==1.5.6'
	mkdir -p eggs
	bin/python bootstrap.py --setuptools-version=7.0 --config-file=buildout.cfg --version=2.2.5
	bin/buildout -v
