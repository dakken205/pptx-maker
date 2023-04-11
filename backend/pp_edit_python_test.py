from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt, Cm

# フォントのルール
style_format = {
    'date' : {
        'font' : 'メイリオ',
        'font-size' : Pt(40),
        'font-color' : RGBColor(64, 64, 64),
    },
    'department-presentor' : {
        'font' : 'メイリオ',
        'font-size' : Pt(24),
        'font-color' : RGBColor(64, 64, 64),
    },
    'department-content' : {
        'font' : 'メイリオ',
        'font-size' : Pt(20),
        'font-color' : RGBColor(64, 64, 64),
    },
    'title' : {
        'font' : 'メイリオ',
        'font-size' : Pt(44),
        'font-color' : RGBColor(64, 64, 64),
    },
    'content' : {
        'font' : 'メイリオ',
        'font-size' : Pt(30),
        'font-color' : RGBColor(64, 64, 64),
    },
}
# その他のルール
# *~~~* : 太字


contents = [
    {
        'title' : 'title1',
        'content' : 'content1',
    },
    {
        'title' : 'title2',
        'content' : 'content2',
    },
]


def set_type(slide, text):
    width = Cm(29.21)
    height = Cm(3.68)
    left = Cm(0.89)
    top = Cm(0.8)
    textbox = slide.shapes.add_textbox(
        left=left,
        top=top,
        width=width,
        height=height,
    )
    textbox.text = text
    paragraph = textbox.text_frame.paragraphs[0]
    paragraph.font.name = 'メイリオ'
    paragraph.font.size = Pt(60)
    paragraph.font.bold = True
    paragraph.font.color.rgb = RGBColor(255, 255, 255)


def apply_format(pptx_obj, target):
    pptx_obj.font.name = style_format[target]['font']
    pptx_obj.font.size = style_format[target]['font-size']
    pptx_obj.font.color.rgb = style_format[target]['font-color']


def set_content(slide, text):
    width = Cm(29.21)
    height = Cm(12.09)
    left = Cm(2.33)
    top = Cm(5.07)
    textbox = slide.shapes.add_textbox(
        left=left,
        top=top,
        width=width,
        height=height,
    )
    textbox.text = text

    paragraphs = textbox.text_frame.paragraphs
    apply_format(paragraphs[0], 'title')
    paragraphs[0].font.bold = True

    for paragraph in paragraphs[1:]:
        apply_format(paragraph, 'content')

    textbox.text_frame.word_wrap = True

def set_title_bg(slide):
    width = Cm(33.87)
    height = Cm(3.68)
    left = Cm(0)
    top = Cm(0)
    fill_color = RGBColor(68, 114, 196)
    shape = slide.shapes.add_shape(
        autoshape_type_id=1,  # 1は四角形を表す
        left=left,
        top=top,
        width=width,
        height=height
    )
    shape.z_order = 0
    fill = shape.fill
    fill.solid()
    fill.fore_color.rgb = fill_color

def add_slide(prs):
    slide_layout_6 = prs.slide_layouts[6]
    prs.slides.add_slide(slide_layout_6)


def set_date_text(slides):
    start_slide = slides[0]
    date_shape = start_slide.shapes[1]
    data_paragraph = date_shape.text_frame.paragraphs[0]
    data_paragraph.text = '4月8日'
    apply_format(data_paragraph, 'date')
    data_paragraph.font.bold = True

datefmt = '20230407'
output_filename = f'{datefmt}.pptx'
input_filename = 'sample.pptx'
input_path = f'./inputs/{input_filename}'

prs = Presentation(input_path)
slides = prs.slides

for content in contents:
    add_slide(prs)
    slide_cnt = len(slides)
    slide = slides[slide_cnt-1]
    set_title_bg(slide)
    set_type(slide, 'set_typeが正常に実行')
    set_content(slide, 'set_contentが正常に実行\nset_contentが正常に実行set_contentが正常に実行set_contentが正常に実行set_contentが正常に実行set_contentが正常に実行set_contentが正常に実行')

prs.save('./outputs/output.pptx')