import fitz

doc = fitz.open("/Users/senna/Desktop/highlight_example.pdf")

"""
color stoke guide:
yellow: (0.9803919792175293, 0.8039219975471497, 0.35294100642204285)
blue: (0.4117650091648102, 0.6901959776878357, 0.9450979828834534)
green: (0.48627498745918274, 0.784313976764679, 0.4078429937362671)
"""
"""
Version 1 Features:
- Extract text that's highlighted by colour
- You have to enter the colour

How:
- Cycle once
- Enter the pages that you want to extract 
- For each page, check if there is an annotation. Then check the type.
- Annotation Type is "PDF_ANNOT_HIGHLIGHT 8"
- Check that it matches the hardcoded colour
- Extract the text and store in lists
- Go through the pages
- Output the file as a .txt
"""
    # to retrieve highlighted pages and rect
    # bbox stands for bounding box, made up of longitudes and latitudes. bbox = left,bottom,right,top or minimum x , minimum y , maximum x , maximum y.


# where I left off : 

for i in range(len(doc)):
    page = doc[i]
    annots = page.annots()

    for annot in annots:
        annot_bbox = annot.rect
        content = page.get_textbox(annot_bbox)
        print(content)

## Clean up
## Stores annot bbox and page_n
# h_bbox = {}
# for i in range(len(doc)):
#     page = doc[i]
#     key = 'page' + str(i)

#     if key not in h_bbox.keys():
#         h_bbox[key] = []
    
#     annots = page.annots()
#     h_annot = []
#     for annot in annots:
#         if str(annot.type) == "(8, 'Highlight')":
#             h_annot.append(annot.rect)
#         h_bbox[key] = h_annot
# # output 
# {'page2': [Rect(93.18000030517578, 566.5672607421875, 465.127197265625, 589.1067504882812)],
#  'page3': [Rect(102.18000030517578, 53.8673095703125, 474.12030029296875, 76.40679931640625),
#   Rect(102.18000030517578, 485.61639404296875, 474.0863952636719, 508.15582275390625),
#   Rect(102.18000030517578, 420.64727783203125, 474.1422119140625, 456.14471435546875)]}