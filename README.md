# pokeapi

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![codecov](https://codecov.io/gh/kohdice/pokeapi/branch/main/graph/badge.svg?token=LOL05HLA7R)](https://codecov.io/gh/kohdice/pokeapi)

## 1. Table of Contents
- [1. Table of Contents](#1-table-of-contents)
- [2. About This Repository](#2-about-this-repository)
- [3. Usage](#3-usage)
  - [3.1. Install Docker](#31-install-docker)
  - [3.2. Clone Repository](#32-clone-repository)
  - [3.3. Create .env File](#33-create-env-file)
  - [3.4. Testing the Functionality](#34-testing-the-functionality)
- [4. Specifications](#4-specifications)
- [5. Setup Development Environment](#5-setup-development-environment)
  - [5.1. Requirements](#51-requirements)
  - [5.2. Install Poetry](#52-install-poetry)
  - [5.3. Create Development Virtual Environment](#53-create-development-virtual-environment)
  - [5.4. Scripts](#54-scripts)
- [6. Setup Development Environment Using Dev Containers](#6-setup-development-environment-using-dev-containers)
  - [6.1. Requirements](#61-requirements)
  - [6.2. Install Extension](#62-install-extension)
  - [6.3. Build Dev Containers](#63-build-dev-containers)
  - [6.4. Scripts](#64-scripts)


## 2. About This Repository
- This repository contains the source code for an API that returns Pokémon data, as well as the development environment.
- This API is built using [Elasticsearch](https://www.elastic.co/elasticsearch/) and [FastAPI](https://fastapi.tiangolo.com/).

## 3. Usage

### 3.1. Install Docker
1. Download and install Docker Desktop from the [Docker official website](https://www.docker.com/products/docker-desktop/).

### 3.2. Clone Repository
1. Clone this repository ([https://github.com/kohdice/pokeapi](https://github.com/kohdice/pokeapi)) to your development machine and create a local repository.

### 3.3. Create .env File
1. Copy the `.env.tmp` file located in the `docker` directory of the local repository to the same directory.
2. Rename the copied file to `.env`.
3. If you want to change the project name, modify the value of `COMPOSE_PROJECT_NAME` in the `.env` file.
- The `.env` file is intentionally not tracked by Git.

### 3.4. Testing the Functionality
1. Move to the `docker` directory.
```bash
cd docker
```
2. Build the containers.
```bash
docker-compose up -d --build
```
3. Access [localhost:8000](http://localhost:8000/).<br>
If the following message is displayed, the functionality test is complete.
```bash
{"message":"Welcome to Pokédex!"}
```

## 4. Specifications
- For detailed specifications of the API, refer to [this page](https://kohdice.github.io/pokeapi/).
- The following Pokémon are available for search (data inserted as test data):[^1]
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

## 5. Setup Development Environment

### 5.1. Requirements
- Python 3.10+
- Containers are built following the steps in the [Usage](#3-usage) section.
- Neovim is recommended. (If using VSCode, proceed to step [6.](#6-setting-up-the-development-environment-using-dev-containers))

### 5.2. Install Poetry
- Install Poetry by referring to the [official documentation](https://python-poetry.org/docs/).

### 5.3. Create Development Virtual Environment
1. Create a virtual environment.
```bash
poetry install
```
2. Activate the virtual environment.
```bash
poetry shell
```
3. Once the virtual environment is active, setup is complete.

### 5.4. Scripts
- Run tests
```bash
task test
```
- Run formatters
```bash
task fmt
```
- Run linters
```bash
task lint
```

## 6. Setup Development Environment Using Dev Containers

### 6.1. Requirements
- Complete steps [3.1.](#31-installing-docker) through [3.3.](#33-creating-the-env-file) in the [Usage](#3-usage) section.
- VSCode is installed.
- If the `.venv` directory exists, delete it before using Dev Containers.

### 6.2. Install Extension
Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VSCode.

### 6.3. Build Dev Containers
1. Click on the icon resembling `><` at the lower-left corner of VSCode and select `Reopen in Container`.
2. Press any key when the following message appears in the terminal.
```bash
Done. Press any key to close the terminal.
```
3. Access [localhost:8000](http://localhost:8000/).<br>
If the following message is displayed, setup is complete.
```bash
{"message":"Welcome to Pokédex!"}
```
4. If using dotfiles<br>
Uncomment the following section in `.devcontainer/devcontainer.json` and replace it with your own dotfiles.
```json
// "dotfiles.repository": "<your dotfiles repository>",
// "dotfiles.targetPath": "~/dotfiles",
// "dotfiles.installCommand": "~/dotfiles/install.sh"
```

### 6.4. Scripts
- Run tests
```bash
poetry run task test
```
- Run formatters
```bash
poetry run task fmt
```
- Run linters
```bash
poetry run task lint
```


[^1]: Only Japanese language search is supported.
