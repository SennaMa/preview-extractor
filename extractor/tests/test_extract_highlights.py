import os

import fitz
from datetime import datetime
import pytest


from app.extract_highlights import extract_highlights, export_text

TEST_PATH = os.getcwd()
path_to_pdf = f"{TEST_PATH}/data/test_extractions.pdf"
extract_page_range = [0, 0]

time_of_extraction = datetime.now().strftime("%m-%d-%y %H:%M:%S")
OUTPUT_TEST_PATH = f"{TEST_PATH}/data/test_extractions_output_{time_of_extraction}.txt"
OUTPUT_FILE = f"test_extractions_output_{time_of_extraction}.txt"


highlighted_text = extract_highlights(path_to_pdf, extract_page_range)


@pytest.mark.extract_text
def test_extract_highlights_annotation_length():
    assert len(highlighted_text) != 0


def test_extract_highlights_annotation_type():
    underline_annots = [text for text in highlighted_text if text.find("underline") > 0]
    assert len(underline_annots) == 0


@pytest.mark.export
def test_export_test():
    export_text(OUTPUT_TEST_PATH, OUTPUT_FILE, highlighted_text)
    assert os.path.exists("OUTPUT_TEST_PATH") == False
