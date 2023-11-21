import sender_stand_request
import data


def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


def positive_assert(name):
    new_body_kit_positive = get_kit_body(name)
    response_kit_positive = sender_stand_request.post_new_client_kit(new_body_kit_positive)
    assert response_kit_positive.status_code == 201
    assert response_kit_positive.json()["name"] == name


def negative_assert(name):
    new_body_kit_positive = get_kit_body(name)
    response_kit_positive = sender_stand_request.post_new_client_kit(new_body_kit_positive)
    assert response_kit_positive.status_code == 400


def negative_assert_no_name_parameter(kit_body):
    response_kit_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
    assert response_kit_negative_no_name.status_code == 400


# Test 1
def test_create_kit_1_symbol_name_get_success_response():
    positive_assert("a")


# Test 2
def test_create_kit_511_symbols_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Test 3
def test_create_kit_empty_name_get_error_response():
    negative_assert("")


# Test 4
def test_create_kit_512_symbols_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Test 5
def test_create_kit_english_symbols_name_get_success_response():
    positive_assert("QWErty")


# Test 6
def test_create_kit_russian_symbols_name_get_success_response():
    positive_assert("Мария")


# Test 7
def test_create_kit_special_symbols_name_get_success_response():
    positive_assert("\"№%@\",")


# Test 8
def test_create_kit_symbols_with_space_name_get_success_response():
    positive_assert(" Человек и КО ")


# Test 9
def test_create_kit_numbers_name_get_success_response():
    positive_assert("123")


# Test 10
def test_create_kit_no_name_get_error_response():
    current_kit_body_no_name = data.kit_body.copy()
    current_kit_body_no_name.pop("name")
    negative_assert_no_name_parameter(current_kit_body_no_name)


# Test 11
def test_create_kit_wrong_parameter_name_get_error_response():
    negative_assert(123)
