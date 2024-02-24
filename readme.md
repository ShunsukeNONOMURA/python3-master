# 概要
python実行環境の簡易構築セット

## 使い方
```
git clone https://github.com/ShunsukeNONOMURA/python3-master.git
cd python3-master
docker compose up
```

## コマンドチートシート

| コマンド                  | 説明                                       |
| ------------------------- | ------------------------------------------ |
| poetry new <project-name> | poetry環境作成                             |
| poetry add -G dev <lib>   | 開発環境ライブラリ追加                     |
| poetry add <lib>          | 本番環境ライブラリ追加                     |
| poetry remove <lib>       | ライブラリ削除                             |
| poetry install --no-root  | pyproject.tomlからライブラリをインストール |
| poetry run python <file>  | poetry経由でのpython実行                   |
