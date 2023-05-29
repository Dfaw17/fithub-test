import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_reqres import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(11)
def test_get_list_user_normal():
    req = requests.get(url.api_list_user)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_data = req.json().get("data")
    verify_page = req.json().get("page")
    verify_per_page = req.json().get("per_page")
    verify_total = req.json().get("total")
    verify_total_pages = req.json().get("total_pages")

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_data).is_type_of(list)
    assert_that(verify_page).is_not_none()
    assert_that(verify_per_page).is_not_none()
    assert_that(verify_total).is_not_none()
    assert_that(verify_total_pages).is_not_none()
    assert_that(verify_data[0]["id"]).is_not_none()
    assert_that(verify_data[0]["email"]).is_not_none()
    assert_that(verify_data[0]["first_name"]).is_not_none()
    assert_that(verify_data[0]["last_name"]).is_not_none()
    assert_that(verify_data[0]["avatar"]).is_not_none()
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=get_list_user_normal)


@pytest.mark.TestManagement(12)
def test_get_list_user_wrong_method():
    req = requests.patch(url.api_list_user)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(404)
    assert_that(verify_latency).is_less_than(general.max_latency)


@pytest.mark.TestManagement(13)
def test_get_list_user_wrong_url():
    req = requests.get(url.api_list_user+"-QU")

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_latency).is_less_than(general.max_latency)
