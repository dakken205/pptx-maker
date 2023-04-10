from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt

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
        'font-size' : Pt(24),
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


datefmt = '20230407'
output_filename = f'{datefmt}.pptx'
input_filename = 'template.pptx'
input_path = f'./inputs/{input_filename}'


def set_title_slide(slide, text):
    shapes = slide.shapes
    shapes.titile.text = text


prs = Presentation(input_path)
slide_layout_5 = prs.slide_layouts[5]
slides = prs.slides
start_slide = slides[0]

# for shape_idx in range(len(start_slide.shapes)):
#     shape = start_slide.shapes[shape_idx]
#     print(f'shape[{shape_idx}]:')
#     if not shape.has_text_frame:
#         continue
#     for paragraph_idx in range(len(shape.text_frame.paragraphs)):
#         paragraph = shape.text_frame.paragraphs[paragraph_idx]
#         print(f'\tparagraph[{paragraph_idx}] text:', paragraph.text)
#         print(f'\tparagraph[{paragraph_idx}] obj:', paragraph)


# 日付の記入処理
date_shape = start_slide.shapes[1]
data_paragraph = date_shape.text_frame.paragraphs[0]
data_paragraph.text = '4月8日'
data_paragraph.font.bold = True
data_paragraph.font.size = Pt(100)
data_paragraph.font.color.rgb = RGBColor(64, 64, 64)

# パワポの追加
if len(contents):
    print('スライドの追加処理が実行されました')
    for content in contents:
        new_slide = prs.slides.add_slide(slide_layout_5)
        print()
else:
    print('スライドの追加処理は実行されませんでした')

slide = slides[1]
# text_runs = []
# for shape in slide.shapes:
#     print('shape:')
#     if not shape.has_text_frame:
#         continue
#     for paragraph in shape.text_frame.paragraphs:
#         for run in paragraph.runs:
#             text_runs.append(run.text)

title = slide.shapes.title
title.text = '新しいタイトル'
prs.save('./outputs/output.pptx')