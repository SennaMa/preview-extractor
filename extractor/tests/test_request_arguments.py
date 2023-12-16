import pytest
import os

from app.request_args import (
    request_path,
    request_page_selection,
    load_and_test_extraction_inputs,
)

TEST_PATH = os.getcwd()


@pytest.mark.request_arguments
@pytest.mark.parametrize(
    "path_to_pdf, expected_result",
    [
        ("user/user/Desktop/pdf_to_extract.pdf", True),
        ("user/Bob/Desktop/Text.pdf", True),
        (1, False),
        ([2, 3], False),
    ],
)
def test_request_path_type(monkeypatch, path_to_pdf, expected_result):
    monkeypatch.setattr("builtins.input", lambda _: path_to_pdf)
    i = type(request_path())
    assert (i == str) == expected_result


@pytest.mark.request_arguments
@pytest.mark.parametrize(
    "from_page, to_page, expected_result",
    [
        (2, 5, True),
        (1, 10, True),
    ],
)
def test_request_page_selection_is_list(
    monkeypatch, from_page, to_page, expected_result
):
    inputs = iter([from_page, to_page])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    i = type(request_page_selection())
    assert (i == list) == expected_result


@pytest.mark.request_arguments
@pytest.mark.parametrize(
    "from_page, to_page, expected_result",
    [
        (16, "3", True),
        (16, 3, True),
    ],
)
def test_request_page_selection_input_values(
    monkeypatch, from_page, to_page, expected_result
):
    """First test case is True because request_page_selection()
    converts list inputs to int.
    """
    inputs = iter([from_page, to_page])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    i = request_page_selection()
    assert ([type(page) for page in i] == [int, int]) == expected_result


@pytest.mark.request_arguments
def test_load_and_test_extraction_inputs_FileError():
    with pytest.raises(Exception) as excinfo:
        path_to_pdf = "123.pdf"
        extract_page_range = [0, 1]

        load_and_test_extraction_inputs(path_to_pdf, extract_page_range)
    assert str(excinfo.value) == f"no such file: '{path_to_pdf}'"


def test_load_and_test_extraction_inputs_IndexError():
    with pytest.raises(IndexError) as excinfo:
        path_to_pdf = f"{TEST_PATH}/data/test_extractions.pdf"
        extract_page_range = [0, 5]

        load_and_test_extraction_inputs(path_to_pdf, extract_page_range)
    assert str(excinfo.typename) == "IndexError"
