# backend

## Examples

- payload

  ```json
  {
    "departments_contents": {
      "ds": ["明日からmachine-coder始めます"],
      "de": ["ABC333"],
      "biz": ["起業準備"],
      "cc": ["特になし"]
    },
    "datefmt": "2023年12月20日（水）",
    "datefmt_filename": "20231220",
    "info_contents": [
      {
        "content": "この後17:30から解析コンペします\n現地参加組は部室でお願いします．",
        "title": "解析コンペ"
      }
    ]
  }
  ```

- response

  ```json
  {
      "file": "UEsDBBQAAAAIAE+...AALAAsAFYNAADYcAAAAAA=",
      "filename": "20231220.pptx"
  }
  ```
