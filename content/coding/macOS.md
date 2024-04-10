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

### 安装 cask 便于后面软件的安装

`brew install cask`

### 安装 mas

`brew install mas`

### 安装 raycast

`brew install --cask raycast`

### 安装 zsh + starship ~~oh-my-zsh~~ + zplug

```bash
brew install zsh gawk git zplug
# sh -c "$(curl -fsSL <https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh>)"
brew install starship
```

### 安装 iterm2

`brew install --cask iterm2`

### 安装 tmux

`brew install tmux`

### 安装 vim

`brew install vim`

### 安装 zoxide、fzf

`brew install zoxide fzf`

### 安装 jenv

`brew install --cask homebrew/cask-versions/zulu11 homebrew/cask-versions/zulu13 homebrew/cask-versions/zulu15 homebrew/cask-versions/zulu17 homebrew/cask-versions/zulu21 homebrew/cask-versions/zulu7 homebrew/cask-versions/zulu8 zulu`

### 安装 fnm

`brew install fnm`

### 安装 pyenv

`brew install pyenv`

### 安装 rust

`brew install rustup-init`

### 安装 rime

[Rime 输入法安装脚本](https://github.com/Mark24Code/rime-auto-deploy)

```bash
git clone --depth=1 https://github.com/Mark24Code/rime-auto-deploy.git --branch latest
cd rime-auto-deploy
./installer.rb
```

## `zshrc`

`vim ~/.zshrc`

```shell
# 启用 Powerlevel10k 即时提示符功能，应该放置于 ~/.zshrc 文件顶部附近。
# 需要控制台输入的初始化代码（如密码提示、[y/n]确认等）必须放在此块之上；
# 其他所有内容可以放在下方。
#if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
#fi
 
# 🚀 加载 zplug，一个社区驱动的插件管理器
source ~/.zplug/init.zsh
 
# 🔧 历史记录配置
HISTSIZE=10000  # 历史记录大小
SAVEHIST=10000  # 保存的历史记录数量
HISTFILE=~/.zsh_history  # 历史记录文件路径
 
# 🎨 zplug 插件
# zplug "romkatv/powerlevel10k", as:theme, depth:1  # 主题配置，当前为注释状态
zplug 'zplug/zplug', hook-build:'zplug --self-manage'  # zplug 自管理
zplug "zsh-users/zsh-completions"  # zsh 补全插件
zplug "zsh-users/zsh-history-substring-search"  # 历史记录子字符串搜索
zplug "zsh-users/zsh-autosuggestions"  # 命令自动建议
zplug "zdharma/fast-syntax-highlighting"  # 快速语法高亮
zplug "zpm-zsh/ls"  # ls 命令增强
zplug "plugins/docker", from:oh-my-zsh  # Docker 插件
zplug "plugins/composer", from:oh-my-zsh  # Composer 插件
zplug "plugins/extract", from:oh-my-zsh  # 解压插件
zplug "lib/completion", from:oh-my-zsh  # 补全库
zplug "plugins/sudo", from:oh-my-zsh  # sudo 插件
zplug "b4b4r07/enhancd", use:init.sh  # 增强型cd命令
 
# 如果有尚未安装的包，进行安装
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
#[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
 
# 🐍 设置 pyenv 环境变量
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
 
# 🚀 配置 starship 提示符
eval "$(starship init zsh)"
 
# 📁 使用 zoxide 进行目录跳转
eval "$(zoxide init zsh)"
 
# 📦 配置 fnm (Fast Node Manager)
eval "$(fnm env --use-on-cd)"
 
# 更新 PATH 环境变量以包含 homebrew 安装的 curl
export PATH="/opt/homebrew/opt/curl/bin:$PATH"
 
# 📦 配置 pnpm 环境变量
export PNPM_HOME="~/Library/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm 配置结束
 
# 🖥️ Tmux 会话管理：若当前终端为 Apple Terminal 或 iTerm2，则尝试连接或创建名为 mySession 的会话
if [ "$TERM_PROGRAM" = "Apple_Terminal" ] || [ "$TERM_PROGRAM" = "iTerm.app" ]; then
    # 首先检查是否有任何会话被附加
    if ! tmux list-sessions | grep -q "attached"; then
        # 检查名为 mySession 的会话是否存在
        tmux has-session -t mySession &> /dev/null
        if [ $? != 0 ]; then
            # 不存在则创建名为 mySession 的会话
            tmux new-session -s mySession
        elif [ -z "$TMUX" ]; then
            # 存在且当前不在 tmux 会话中，则附加到 mySession 会话
            tmux attach-session -t mySession
        fi
    fi
fi
 
# 📦 配置 jenv，Java 版本管理器
export PATH="$HOME/.jenv/bin:$PATH"
eval "$(jenv init -)"
 
# 🔧 配置 zsh 补全路径
fpath=(
  /opt/homebrew/share/zsh-completions(N-/)  # Homebrew 安装的 zsh 补全
  /opt/homebrew/share/zsh/site-functions(N-/)  # Homebrew 安装的 site-functions
  ~/.config/zsh/zsh-completions(N-/)  # 用户自定义的 zsh 补全
  /opt/homebrew/share/zsh/site-functions(N-/)  # 重复的路径，可能需要删除
  $fpath
)
# Hishtory Config:
export PATH="$PATH:/Users/user/.hishtory"
source /Users/user/.hishtory/config.zsh
# atuin
eval "$(atuin init zsh)"
```
