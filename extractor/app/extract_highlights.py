import fitz
import logging


def extract_highlights(path_to_pdf: str, extract_page_range: list) -> list:
    """Loads PDF and searches the selected page range for highlights.
    The highlighted text is saved in list.

    Args:
        doc (str): path to PDF. Loaded by Fitz.

    Returns:
        list: highlighted text
    """

    highlighted_text = []
    loaded_doc = fitz.open(path_to_pdf)

    logging.info(
        f"Extracting highlighted text from pages {extract_page_range[0]} to {extract_page_range[1]}..."
    )
    for i in range(extract_page_range[0], extract_page_range[1] + 1, 1):
        page = loaded_doc[i]
        annots = page.annots()

        for annot in annots:
            if str(annot.type) == "(8, 'Highlight')":
                annot_bbox = annot.rect
                content = page.get_textbox(annot_bbox)
                highlighted_text.append(content)
    return highlighted_text


def export_text(output_path: str, file: str, highlighted_text: list) -> None:
    """Append highlighted text to a txt file.
    Optional: If the file doesn't exist, create one.

    Args:
        path_to_txt (str): path for where you want the output file
        to be stored. Default value is used
    """
    with open(output_path, "a") as fp:
        for blurb in highlighted_text:
            fp.write(blurb + "\n")
        logging.info("Finished exporting highlighted text.")
        logging.info(f"Visit {file} to see results")
