---
title: macOS 调教
draft: false
tags:
  - macOS
  - zsh
  - zplug
  - tmux
  - iterm2
---
# `zshrc`:
```
# 初始化 Powerlevel10k 即时提示符。应该放在 ~/.zshrc 的顶部附近。
# 需要控制台输入的初始化代码（密码提示、[y/n]确认等）必须放在此块上方；
# 其他所有内容可以放在下方。
# if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#   source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
# fi

# 📦 加载 zplug 插件管理器
source ~/.zplug/init.zsh

# 🔧 历史记录配置
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# 🚀 zplug 插件列表
# zplug "romkatv/powerlevel10k", as:theme, depth:1
zplug 'zplug/zplug', hook-build:'zplug --self-manage'
zplug "zsh-users/zsh-completions"
zplug "zsh-users/zsh-history-substring-search"
zplug "zsh-users/zsh-autosuggestions"
zplug "zdharma/fast-syntax-highlighting"
zplug "zpm-zsh/ls"
zplug "plugins/docker", from:oh-my-zsh
zplug "plugins/composer", from:oh-my-zsh
zplug "plugins/extract", from:oh-my-zsh
zplug "lib/completion", from:oh-my-zsh
zplug "plugins/sudo", from:oh-my-zsh
zplug "b4b4r07/enhancd", use:init.sh

# 如果还有未安装的包，则安装它们
if ! zplug check --verbose; then
    printf "Install? [y/N]: "
    if read -q; then
        echo; zplug install
    else
        echo
    fi
fi
zplug load

# 自定义提示符，请运行 `p10k configure` 或编辑 ~/.p10k.zsh。
# [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# 🐍 pyenv 环境变量配置
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# 🌌 Starship 提示符初始化
eval "$(starship init zsh)"

# 📂 zoxide 目录跳转
eval "$(zoxide init zsh)"

# 📦 fnm Node.js 版本管理
eval "$(fnm env --use-on-cd)"

# 更新 PATH 环境变量
export PATH="/opt/homebrew/opt/curl/bin:$PATH"

# 📦 pnpm 环境变量配置
export PNPM_HOME="/Users/chi/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm 配置结束

# 🖥️ Tmux 会话管理脚本
# 用于在 Apple Terminal 或 iTerm2 使用时自动管理 Tmux 会话。
# 如果名为 mySession 的会话不存在，则创建它；如果存在，则连接到它。
if [ "$TERM_PROGRAM" = "Apple_Terminal" ] || [ "$TERM_PROGRAM" = "iTerm.app" ]; then
    tmux has-session -t mySession &> /dev/null
    if [ $? != 0 ]; then
        tmux new-session -s mySession
    elif [ -z "$TMUX" ]; then
        tmux attach-session -t mySession
    fi
fi
```
