"""Development tasks for django-flags."""
from invoke import task, run

PYTHON_MODULES = ['flags']


# pylint: disable=unused-argument
@task(name='format')
def format_python(ctx):
    """Run python autoformating."""
    run('isort --line-width=100 --recursive flags')
    run('yapf --in-place --style=config/style.yapf --recursive flags tasks.py')


@task(name='lint')
def lint_python(ctx):
    """Run python linting."""
    run('pylint --reports=n --rcfile=config/pylint.rc tasks.py ' + ' '.join(PYTHON_MODULES))
    run('mypy --ignore-missing-imports flags')


@task(name='test')
def test_python(ctx):
    """Run python tests."""
    run('./runtests.py')
