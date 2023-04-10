from pptx import Presentation

# フォントのルール
style_format = {
    'date' : {
        'font' : 'メイリオ',
        'font-size' : 40,
    },
    'department-presentor' : {
        'font' : 'メイリオ',
        'font-size' : 24,
    },
    'department-content' : {
        'font' : 'メイリオ',
        'font-size' : 20,
    },
    'title' : {
        'font' : 'メイリオ',
        'font-size' : 44,
    },
    'content' : {
        'font' : 'メイリオ',
        'font-size' : 24,
    },
}
# その他のルール
# *~~~* : 太字

prs = Presentation('./inputs/sample.pptx')
slides = prs.slides
slide = slides[1]
title = slide.shapes.title
title.text = '新しいタイトル'
prs.save('./outputs/output.pptx')