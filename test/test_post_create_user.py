import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_reqres import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(3)
def test_create_user_normal():
    name = "DAFFA FAWWAZ MAULANA"
    job = "SDET"
    payload = {
        "name": name,
        "job": job
    }
    req = requests.post(url.api_list_user, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_response = req.json()

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_response.get("name")).is_equal_to(name)
    assert_that(verify_response.get("job")).is_equal_to(job)
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=post_create_user_normal)


@pytest.mark.TestManagement(3)
def test_create_user_empty_name():
    name = ""
    job = "SDET"
    payload = {
        "name": name,
        "job": job
    }
    req = requests.post(url.api_list_user, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_response = req.json()

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_response.get("name")).is_equal_to(name)
    assert_that(verify_response.get("job")).is_equal_to(job)
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=post_create_user_normal)


@pytest.mark.TestManagement(3)
def test_create_user_without_payload_name():
    job = "SDET"
    payload = {
        "job": job
    }
    req = requests.post(url.api_list_user, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_response = req.json()

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_response.get("job")).is_equal_to(job)
    assert_that(verify_latency).is_less_than(general.max_latency)


@pytest.mark.TestManagement(3)
def test_create_empty_job():
    name = "DAFFA FAWWAZ MAULANA"
    job = ""
    payload = {
        "name": name,
        "job": job
    }
    req = requests.post(url.api_list_user, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_response = req.json()

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_response.get("name")).is_equal_to(name)
    assert_that(verify_response.get("job")).is_equal_to(job)
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=post_create_user_normal)


@pytest.mark.TestManagement(3)
def test_create_without_payload_job():
    name = "DAFFA FAWWAZ MAULANA"
    payload = {
        "name": name,
    }
    req = requests.post(url.api_list_user, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_response = req.json()

    # ASSERT
    assert_that(verify_status_code).is_equal_to(201)
    assert_that(verify_response.get("name")).is_equal_to(name)
    assert_that(verify_latency).is_less_than(general.max_latency)
