import logging
from extract_highlights import *

LOG_FORMAT = "%(asctime)s: %(levelname)-8s - %(name)s - line %(lineno)3d - %(message)s"

output_path = "/Users/senna/Desktop/py_projects/preview-extractor/preview-extractor/data/highlighted_text.txt"
txt_file = "highlighted_text.txt"


def check_path() -> str:
    pdf = request_path()

    if pdf.lower().find(".pdf") < 1:
        print("That's not right.")
        return request_path()
    else:
        print("Thank you!")
    return pdf.lower()


def extract_highlighted_text() -> list:
    path_to_pdf = check_path()
    extract_highlights(path_to_pdf)


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    highlighted_text = extract_highlighted_text()

    export_text(output_path, txt_file, highlighted_text)


if __name__ == "__main__":
    main()
