# import pytest

# from app.extract_highlights import extract_highlights

# @pytest.mark.extract_text
# @pytest.fixture.parametrize('path_to_pdf, from_page, to_page, expected_results', [
#     # ('user/user/Desktop/pdf_to_extract.pdf', 3, False),
#     # ('user/user/Desktop/pdf_to_extract.pdf', 1000, False),
#     # ('user/user/Desktop/pdf_to_extract.pdf', 3, True),
#     (, does_not_raise()),
#     ('user/user/Desktop/123.pdf', pytest.raises(FileNotFoundError)),
# ])
# def test_extract_highlights_raise_file_not_found_error(monkeypatch, path_to_pdf, to_page, from_page, expected_results):
#     with expected_results:
#         assert is not None


#     inputs = iter([path_to_pdf, from_page, to_page])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))

#     pytest.raises((FileNotFoundError, IndexError), extract_highlights(), inputs)
#     assert


# # Extract highlights
#     # fitz.open does not raise an error
#     # fitz.open raises an error if pdf does not exist
#     # check that page.annots() works.
#         # "(8, 'Highlight')" should be an available option in annot.type
#     # revisit page.get_textbox(annot_bbox) again and see if we can write a test
