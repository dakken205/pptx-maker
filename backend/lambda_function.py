# -*- coding: utf-8 -*-

import base64
import io
import json

from pptx import Presentation
from pptx.util import Inches
from src.pptx_helper import (add_department_slide, add_info_share,
                             add_outline_slide, add_start_slide)


def lambda_handler(event, context):
    data = json.loads(event['body'])
    hasInfo = bool(len(data['info_contents']))

    prs = Presentation()
    prs.slide_width = Inches(16 * 5 / 6)
    prs.slide_height = Inches(9 * 5 / 6)

    add_start_slide(prs, data['datefmt'])
    add_outline_slide(prs, hasInfo)
    add_department_slide(prs, data['departments_contents'])
    add_info_share(prs, data['info_contents'])

    # powerpointファイルをメモリ上に保存する
    ppt_file = io.BytesIO()
    prs.save(ppt_file)
    ppt_file.seek(0)

    # ファイルをbase64エンコーディング
    ppt_file_b64 = base64.b64encode(ppt_file.getvalue()).decode()

    return {
        'statusCode':
        200,
        'body':
        json.dumps({
            'file': ppt_file_b64,
            'filename': data['datefmt_filename'] + '.pptx'
        }),
    }
