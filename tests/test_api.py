import pytest
from airflow_project.common_lib.api import API


@pytest.fixture(scope="module")
def api():
    return API()


def test_whater(api: API):
    assert api.whater('São Paulo')
