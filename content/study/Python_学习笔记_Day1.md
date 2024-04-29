---
title: 学习笔记：Python Day 1
draft: false
tags:
  - python
  - 基础知识
  - coding
  - Study
date: 2024-04-29
---
## 环境安装

- [pyenv](https://github.com/pyenv/pyenv) :简单的 Python 版本管理
- [pdm](https://github.com/pdm-project/pdm):支持最新 PEP 标准的现代 Python 包和依赖项管理器
- [ruff](https://github.com/astral-sh/ruff):一个非常快的 Python linter 和代码格式化程序，用 Rust 编写

![[Pasted image 20240429091642.png]]


```shell
brew install pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

exec "$SHELL"

brew install openssl readline sqlite3 xz zlib tcl-tk
pyenv install --list
pyenv install 3.10.14
pyenv global 3.10.14
python -V
```

## 基本语法

### 变量类型

### 排版注释