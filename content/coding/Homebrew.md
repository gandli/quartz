---
title: Homebrew
draft: false
tags:
  - Homebrew
  - macOS
---
## 一键更新、清理、备份

```bash
brew update && brew upgrade && mas upgrade && brew cu -afy && brew cleanup --prune=all && brew autoremove && brew bundle dump --describe --force --file="~/Brewfile" && gh gist edit 74ed569a197e4f4e0ec522d73869904f -a ~/Brewfile
```

## 导入软件清单

```bash
curl -L https://gist.githubusercontent.com/gandli/74ed569a197e4f4e0ec522d73869904f/raw > /tmp/Brewfile && brew bundle --file=/tmp/Brewfile && rm /tmp/Brewfile
```
