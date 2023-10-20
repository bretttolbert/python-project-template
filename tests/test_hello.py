import pytest

from python_project_template.hello import hello

def test_hello():
    assert hello() == 'hello world'
