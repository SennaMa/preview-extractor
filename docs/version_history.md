# Version History

**This document tracks versions and next steps.**

### Version 0.1.0

Features:
- Extract text that's highlighted by colour
- Hardcoded doc string (user must enter path)
- Output is .txt

Details:
- Cycle once through the document
- For each page, check if there is an annotation and the type. Annotation Type is "PDF_ANNOT_HIGHLIGHT 8"
- Grab the boundaries for the annotated text
- Grab the text from the page
- Output the file as a .txt


### Version 0.1.1

Features:
- Ability to decide which pages to cycle through
- Hard-coded colour stroke

Details:
- Enter the pages that you want to extract 
- Check that it matches the hardcoded colour
