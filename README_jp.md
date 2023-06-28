# pokeapi

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kohdice/b741bc9aa065ec27ebd515d2a63c3c79/raw/pytest-coverage-comment.json)

## 1. 目次
- [1. 目次](#1-目次)
- [2. このリポジトリについて](#2-このリポジトリについて)
- [3. 使用方法](#3-使用方法)
  - [3.1. Dockerのインストール](#31-dockerのインストール)
  - [3.2. リポジトリのクローン](#32-リポジトリのクローン)
  - [3.3. .envファイルの作成](#33-envファイルの作成)
  - [3.4. 動作確認](#34-動作確認)
- [4. 仕様](#4-仕様)
- [5. 開発環境のセットアップ](#5-開発環境のセットアップ)
  - [5.1. 必要環境](#51-必要環境)
  - [5.2. Poetryのインストール](#52-poetryのインストール)
  - [5.3. 開発用仮想環境の作成](#53-開発用仮想環境の作成)
  - [5.4. スクリプト](#54-スクリプト)
- [6. Dev Containersを使用した開発環境のセットアップ](#6-dev-containersを使用した開発環境のセットアップ)
  - [6.1. 必要環境](#61-必要環境)
  - [6.2. 拡張機能のインストール](#62-拡張機能のインストール)
  - [6.3. Dev Containersのビルド](#63-dev-containersのビルド)
  - [6.4. スクリプト](#64-スクリプト)


## 2. このリポジトリについて
- このリポジトリには、ポケモンのデータを返すAPIのソースコードと開発環境が含まれています。
- このAPIは、[Elasticsearch](https://www.elastic.co/elasticsearch/)と[FastAPI](https://fastapi.tiangolo.com/)を使用して構築されています。

## 3. 使用方法

### 3.1. Dockerのインストール
1. [Docker公式ウェブサイト](https://www.docker.com/products/docker-desktop/)からDocker Desktopをダウンロードしてインストールしてください。

### 3.2. リポジトリのクローン
1. このリポジトリ（[https://github.com/kohdice/pokeapi](https://github.com/kohdice/pokeapi)）を開発マシンにクローンし、ローカルリポジトリを作成してください。

### 3.3. .envファイルの作成
1. ローカルリポジトリの`docker`ディレクトリにある`.env.tmp`ファイルを同じディレクトリにコピーしてください。
2. コピーしたファイルの名前を`.env`に変更してください。
3. プロジェクト名を変更したい場合は、`.env`ファイル内の`COMPOSE_PROJECT_NAME`の値を変更してください。
- `.env`ファイルはgitに補足されませんが、これは正しい挙動です。

### 3.4. 動作確認
1. `docker`ディレクトリに移動してください。
```bash
cd docker
```
2. 以下のコマンドを実行してコンテナをビルドしてください。
```bash
docker-compose up -d --build
```
3. [localhost:8000](http://localhost:8000/)にアクセスします。<br>
以下のメッセージが表示されれば、動作確認は完了です。
```bash
{"message":"Welcome to Pokédex!"}
```

## 4. 仕様
- APIの詳細な仕様については、[このページ](https://kohdice.github.io/pokeapi/)を参照してください。
- 以下のポケモンの検索が利用可能です（テストデータとして挿入されているもの）：[^1]
  - フシギダネ
  - フシギソウ
  - フシギバナ
  - メガフシギバナ
  - ヒトカゲ
  - リザード
  - リザードン
  - メガリザードンＸ
  - メガリザードンＹ
  - ゼニガメ
  - カメール
  - カメックス
  - メガカメックス
  - ピカチュウ
  - ライチュウ
  - ライチュウ（アローラのすがた）
  - ミュウツー
  - メガミュウツーＸ
  - メガミュウツーＹ
  - ミュウ
  - オタチ
  - オオタチ
  - カイオーガ
  - ゲンシカイオーガ
  - グラードン
  - ゲンシグラードン
  - ミミッキュ（ばけたすがた）
  - ミミッキュ（ばれたすがた）

## 5. 開発環境のセットアップ

### 5.1. 必要環境
- Python 3.10以上
- [使用方法](#3-使用方法)の手順に従ってコンテナがビルドされていること。
- Neovimの使用を推奨します。（VSCodeを使用する場合は、ステップ[6.](#6-dev-containersを使用した開発環境のセットアップ)に進んでください）

### 5.2. Poetryのインストール
- [公式ドキュメント](https://python-poetry.org/docs/)を参照してPoetryをインストールしてください。

### 5.3. 開発用仮想環境の作成
1. 以下のコマンドで仮想環境を作成してください。
```bash
poetry install
```
2. 以下のコマンドで仮想環境をアクティベートしてください。
```bash
poetry shell
```
3. 仮想環境がアクティベートされれば、セットアップは完了です。

### 5.4. スクリプト
- テストを実行する
```bash
task test
```
- フォーマッタを実行する
```bash
task fmt
```
- リンターを実行する
```bash
task lint
```

## 6. Dev Containersを使用した開発環境のセットアップ

### 6.1. 必要環境
- [使用方法](#3-使用方法)の手順[3.1.](#31-dockerのインストール)から[3.3.](#33-envファイルの作成)までを完了していること。
- VSCodeがインストールされていること。
- `.venv`ディレクトリが存在する場合は、Dev Containersを使用する前に削除してください。

### 6.2. 拡張機能のインストール
VSCodeに[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストールしてください。

### 6.3. Dev Containersのビルド
1. VSCodeの左下隅にある`><`に似たアイコンをクリックし、`Reopen in Container`を選択してください。
2. ターミナルに次のメッセージが表示されたら、任意のキーを押してください。
```bash
Done. Press any key to close the terminal.
```
3. [localhost:8000](http://localhost:8000/)にアクセスします。<br>
次のメッセージが表示されれば、セットアップは完了です。
```bash
{"message":"Welcome to Pokédex!"}
```
4. dotfilesを使用する場合<br>
`.devcontainer/devcontainer.json`の以下の部分のコメント化を解除し、自身のdotfilesに書き換えてください。
```json
// "dotfiles.repository": "<your dotfiles repository>",
// "dotfiles.targetPath": "~/dotfiles",
// "dotfiles.installCommand": "~/dotfiles/install.sh"
```

### 6.4. スクリプト
- テストを実行する
```bash
poetry run task test
```
- フォーマッタを実行する
```bash
poetry run task fmt
```
- リンターを実行する
```bash
poetry run task lint
```


[^1]: 日本語での検索のみサポートされています。
