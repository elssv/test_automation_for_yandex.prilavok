import pytest

import sender_stand_request
import data


def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


@pytest.mark.parametrize("name", [
    pytest.param("a", id="Test 1 - 1 symbol"),
    pytest.param("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",
                 id="Test 2 - 511 symbols"),
    pytest.param("QWErty", id="Test 5 - english symbols"),
    pytest.param("Мария", id="Test 6 - russian symbols"),
    pytest.param("\"№%@\",", id="Test 7 - special symbols"),
    pytest.param(" Человек и КО ", id="Test 8 - spaces"),
    pytest.param("123", id="Test 9 - numbers"),
])
def test_positive_assert_name(name):
    new_body_kit_positive = get_kit_body(name)
    response_kit_positive = sender_stand_request.post_new_client_kit(new_body_kit_positive)
    assert response_kit_positive.status_code == 201
    assert response_kit_positive.json()["name"] == name


@pytest.mark.parametrize("name", [
    pytest.param("", id="Test 3 - blank field"),
    pytest.param("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",
                 id="Test 4 - 512 symbols"),
    pytest.param(123, id="Test 11 - wrong parameter")
])
def test_negative_assert_name(name):
    new_body_kit_positive = get_kit_body(name)
    response_kit_positive = sender_stand_request.post_new_client_kit(new_body_kit_positive)
    assert response_kit_positive.status_code == 400


def negative_assert_no_name_parameter(kit_body):
    response_kit_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
    assert response_kit_negative_no_name.status_code == 400


def test_create_kit_no_name_get_error_response():
    current_kit_body_no_name = data.kit_body.copy()
    current_kit_body_no_name.pop("name")
    negative_assert_no_name_parameter(current_kit_body_no_name)