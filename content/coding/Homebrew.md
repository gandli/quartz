---
title: 一键更新 Homebrew
draft: false
tags:
  - Homebrew
  - macOS
---
```bash
brew update && brew upgrade && mas upgrade && brew cu -afy && brew cleanup --prune=all && brew autoremove && brew bundle dump --describe --force --file="~/Brewfile" && gh gist edit 74ed569a197e4f4e0ec522d73869904f -a ~/Brewfile
```
