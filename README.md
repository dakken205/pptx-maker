# pptx-maker

DA研のための定例会資料作成支援ツール

## Project Structure

- `/backend`
  - .pptx ファイル作成のための Python プロジェクト
- `/frontend`
  - UI や API 連携のための Vue.js プロジェクト

## Deployment

- バックエンド
  - [AWS Lambda](https://aws.amazon.com/jp/lambda/)
    - 依存ライブラリ群を [zip](/backend/layer.zip) でまとめています（linux で pre-compile 済み）
      - レイヤとしてそのまま使用可

- フロントエンド
  - [GitHub Pages](https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages)
    - [GitHub Actions](https://github.co.jp/features/actions) によって自動でデプロイされます。詳しくは[ワークフロー](https://github.com/dakken205/pptx-maker/blob/main/.github/workflows/static.yml)を確認してください
  - [Firebase](https://firebase.google.com/)

## Author

- [Koyama Akiyuki](https://github.com/llillillj)
