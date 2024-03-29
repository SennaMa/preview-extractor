import logging
import os

from datetime import datetime
from extract_highlights import extract_highlights, export_text
from request_args import (
    load_and_test_extraction_inputs,
    request_path,
    request_page_selection,
)


LOG_FORMAT = "%(asctime)s: %(levelname)-8s - %(name)s - line %(lineno)3d - %(message)s"
PROJ_PATH = os.getcwd()

time_of_extraction = datetime.now().strftime("%m-%d-%y %H:%M:%S")
txt_file = "highlighted_text"
output_path = f"{PROJ_PATH}/extractor/data/{txt_file}_{time_of_extraction}.txt"


def check_path() -> str:
    pdf = request_path()

    if pdf.lower().find(".pdf") < 1:
        print("That's not right.")
        return request_path()
    else:
        print("Thank you!")
    return pdf.lower()


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    path_to_pdf = check_path()
    extract_page_range = request_page_selection()
    verified_inputs = load_and_test_extraction_inputs(path_to_pdf, extract_page_range)

    if verified_inputs:
        highlighted_text = extract_highlights(path_to_pdf, extract_page_range)

    # if error No such file or directory: output path then create text file.
    if output_path:
        try:
            export_text(output_path, txt_file, highlighted_text)
        except FileNotFoundError:
            f = open(output_path, "x")
            f.close()
            export_text(output_path, txt_file, highlighted_text)


if __name__ == "__main__":
    main()
