import logging
from extract_highlights import (
    request_path,
    request_page_selection,
    extract_highlights,
    export_text,
)

LOG_FORMAT = "%(asctime)s: %(levelname)-8s - %(name)s - line %(lineno)3d - %(message)s"

txt_file = "highlighted_text.txt"
output_path = (
    f"/Users/senna/Desktop/py_projects/preview-extractor/extractor/data/{txt_file}"
)


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
    extract_page_range = request_page_selection()
    return extract_highlights(path_to_pdf, extract_page_range)


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    highlighted_text = extract_highlighted_text()

    export_text(output_path, txt_file, highlighted_text)


if __name__ == "__main__":
    main()
