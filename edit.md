# 編集作業について
## 特定の項目について編集中
- [ ] 前回の状態からの変更を確認
- [ ] 変更されていることが確認出来たら、firestoreで編集中の状態であることを取得
  - [ ] 編集中のユーザの名前を識別できるようなデータの持ち方にする
- [ ] 編集中の状態は他のユーザはその項目がdisableにされる

## 下書き保存時の処理
- [ ] ローディングの実行
- [ ] ログへの追加
- [ ] onSnapshotで同期させる
- [ ] 保存状態の更新時、ログイン中のユーザは変更された部分だけを更新するようにする
- [ ] 下書き保存していない状態以下の処理をしようとした際には、アラートを表示
  - [ ] 今開いているページを閉じようとしたとき
  - [ ] 他のログを表示しようとしたとき
  - [ ] パワポを発行しようとしたとき（これで発行を強行すると、編集前の状態で発行するようにする）