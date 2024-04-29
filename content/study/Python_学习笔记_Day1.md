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

> [!tips]
> 
> - 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数 字打头。例如，可将变量命名为message_1 ，但不能将其命名为1_message 。 
> - 变量名不能包含空格，但能使用下划线来分隔其中的单词。例如，变量名 greeting_message 可行，但变量名greeting message 会引发错误。 
> - 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的 单词，如print (请参见附录A.4)。 
> - 变量名应既简短又具有描述性。例如，name 比n 好，student_name 比s_n 好，name_length 比length_of_persons_name 好。
> - 慎用小写字母i和大写字母O ，因为它们可能被人错看成数字1 和0 。


### 排版注释