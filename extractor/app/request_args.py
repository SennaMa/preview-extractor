import fitz


def request_path() -> str:
    print("Hi! We'll need a few details before we can run the extractions for you.")
    doc = input("Please enter the path that contains the PDF you want to extract: ")
    return doc


def request_page_selection() -> list:
    print("Please enter the range of pages that you'd like to extract.")
    pr_from = int(input("From: "))
    pr_to = int(input("To: "))

    page_range = [pr_from, pr_to]
    page_range.sort()
    return page_range


def load_and_test_extraction_inputs(
    path_to_pdf: str, extract_page_range: list
) -> object | IndexError:
    try:
        loaded_doc = fitz.open(path_to_pdf)
    except:
        raise
    else:
        if extract_page_range[1] > len(loaded_doc):
            raise IndexError(
                f"The requested page range ({extract_page_range[1]}) is greater than the total number of pages in the pdf. \n"
                "please try again"
            )
        else:
            return True
