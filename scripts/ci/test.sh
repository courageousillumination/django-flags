#!/bin/bash
mkdir -p build
env/bin/mypy --junit-xml=build/python-mypy.xml --ignore-missing-imports flags ||:
env/bin/pylint --reports=n --rcfile=config/pylint.rc --output-format=parseable flags/*/ > build/python-lint.txt ||:
env/bin/python runtests.py --with-xunit --xunit-file=build/python-tests.xml --coverage --cover-xml --cover-xml-file=build/python-coverage.xml ||:
