---
title: macOS 调教
draft: false
tags:
  - macOS
  - zsh
  - zplug
  - tmux
  - iterm2
  - pyenv
  - fnm
  - jenv
  - vim
  - python
  - nodejs
  - java
  - rust
  - raycast
---
## 系统设置

### 清空`dock`

```bash
defaults delete com.apple.dock persistent-apps # 包含启动台等图标
defaults delete com.apple.dock persistent-others
killall Dock
```

### 取消 4 位数密码限制

`pwpolicy -clearaccountpolicies`

### 程序坞自动隐藏加速

```bash
# 设置启动坞动画时间设置为 0.5 秒 
defaults write com.apple.dock autohide-time-modifier -float 0.5 && killall Dock

# 设置启动坞响应时间最短
defaults write com.apple.dock autohide-delay -int 0 && killall Dock

# 恢复启动坞默认动画时间
defaults delete com.apple.dock autohide-time-modifier && killall Dock

# 恢复默认启动坞响应时间
defaults delete com.apple.Dock autohide-delay && killall Dock
```

### 启动台自定义行和列

```bash
# 设置列数
defaults write com.apple.dock springboard-columns -int 7

# 设置行数
defaults write com.apple.dock springboard-rows -int 6

# 重启 Dock 生效
killall Dock

# 恢复默认的列数和行数
defaults write com.apple.dock springboard-rows Default
defaults write com.apple.dock springboard-columns Default

# 重启 Dock 生效
killall Dock
```

### 允许安装任意来源的 App

`sudo spctl --master-disable`

## 软件安装

### 安装 Xcode Command Line Tools

`xcode-select --install`

### 安装[[Homebrew]]

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

#### 国内环境安装命令

`/bin/bash -c "$(curl -fsSL <https://gitee.com/ineo6/homebrew-install/raw/master/install.sh>)"`

### 安装cask便于后面软件的安装

`brew install cask`

### 安装mas

`brew install mas`

### 安装raycast

`brew install --cask raycast`

### 安装zsh + starship ~~oh-my-zsh~~ + zplug

```bash
brew install zsh gawk git zplug
# sh -c "$(curl -fsSL <https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh>)"
brew install starship
```

### 安装iterm2

`brew install --cask iterm2`

### 安装tmux

`brew install tmux`

### 安装vim

`brew install vim`

### 安装zoxide、fzf

`brew install zoxide fzf`

### 安装jenv

`brew install --cask homebrew/cask-versions/zulu11 homebrew/cask-versions/zulu13 homebrew/cask-versions/zulu15 homebrew/cask-versions/zulu17 homebrew/cask-versions/zulu21 homebrew/cask-versions/zulu7 homebrew/cask-versions/zulu8 zulu`

### 安装fnm

`brew install fnm`

### 安装pyenv

`brew install pyenv`

### 安装rust

`brew install rustup-init`

### 安装rime

[Rime输入法安装脚本](https://github.com/Mark24Code/rime-auto-deploy)

```bash
git clone --depth=1 https://github.com/Mark24Code/rime-auto-deploy.git --branch latest
cd rime-auto-deploy
./installer.rb
```

## `zshrc`

`vim ~/.zshrc`

```
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
#if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
#fi

source ~/.zplug/init.zsh

# History config
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# zplug plugins
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

# Install packages that have not been installed yet
if ! zplug check --verbose; then
    printf "Install? [y/N]: "
    if read -q; then
        echo; zplug install
    else
        echo
    fi
fi
zplug load

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
#[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# pyenv
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# starship
eval "$(starship init zsh)"

# zoxide
eval "$(zoxide init zsh)"

# fnm
eval "$(fnm env --use-on-cd)"

export PATH="/opt/homebrew/opt/curl/bin:$PATH"

# pnpm
export PNPM_HOME="/Users/chi/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end

# 此脚本用于检查当前使用的终端是否为 Apple Terminal 或 iTerm2。如果是，
# 它将尝试连接到一个名为 mySession 的现有 Tmux 会话。如果这个会话不存在，
# 脚本会创建一个新的会话。此脚本旨在简化终端会话管理，特别适用于那些
# 喜欢使用 Tmux 进行多窗口管理的用户。适用于需要快速恢复工作环境的场景。

# 当前终端程序是苹果终端或 iTerm2 时，才执行以下操作
if [ "$TERM_PROGRAM" = "Apple_Terminal" ] || [ "$TERM_PROGRAM" = "iTerm.app" ]; then
    # 尝试查找名为 mySession 的 Tmux 会话，输出重定向到 /dev/null（即不显示任何输出）
    tmux has-session -t mySession &> /dev/null
    
    # 检查上一条命令的退出状态
    # 如果 $? 不等于 0，表示没有找到名为 mySession 的会话
    if [ $? != 0 ]; then
        # 创建一个新的名为 mySession 的 Tmux 会话
        tmux new-session -s mySession
    # 如果上一个命令执行成功（即找到了名为 mySession 的会话），
    # 但当前不在任何 Tmux 会话内（即 $TMUX 环境变量为空）
    elif [ -z "$TMUX" ]; then
        # 则附加到名为 mySession 的会话
        tmux attach-session -t mySession
    fi
fi
# jenv
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"

# completions
fpath=(
  /opt/homebrew/share/zsh-completions(N-/)
  /opt/homebrew/share/zsh/site-functions(N-/)
  ~/.config/zsh/zsh-completions(N-/)
  /opt/homebrew/share/zsh/site-functions(N-/)
  $fpath
)
```
