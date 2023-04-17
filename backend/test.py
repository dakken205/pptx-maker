from pp_edit_python_test import add_start_slide
from pptx import Presentation
from pptx.util import Inches

datefmt = '2023年4月7日（金）'
prs = Presentation()
prs.slide_width = Inches(16 * 5 / 6)
prs.slide_height = Inches(9 * 5 / 6)

add_start_slide(prs, datefmt)

prs.save('./outputs/test.pptx')