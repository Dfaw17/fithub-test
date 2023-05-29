import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_reqres import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(3)
def test_delete_user_normal():
    req = requests.delete(url.api_list_user+"/1")
    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(204)
    assert_that(verify_latency).is_less_than(general.max_latency)

