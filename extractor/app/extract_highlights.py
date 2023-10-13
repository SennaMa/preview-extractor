import fitz


def request_path() -> str:
    print("Hi! We'll need a few details before we can run the extractions for you.")
    doc = input("Please enter the path that contains the PDF you want to extract: ")
    return doc


def extract_highlights(path_to_pdf: str) -> list:
    """Loads PDF and searches each page for highlights.
    Highlighted text is saved in list.

    Args:
        doc (str): path to PDF. Loaded by Fitz.

    Returns:
        list: highlighted text
    """
    loaded_doc = fitz.open(path_to_pdf)
    highlighted_text = []

    for i in range(len(loaded_doc)):
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
        print("Finished exporting highlighted text.")
        print(f"Visit {file} to see results")
