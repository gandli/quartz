---
title: 使用quartz
draft: false
tags:
  - quartz
---

1. 克隆 quartz

    ```bash
    git clone https://github.com/jackyzha0/quartz.git
    cd quartz
    npm i
    npx quartz create
    ```

2. 创作内容
  在`content`目录下创建md文件

    ```markdown
    ---
    title: Example Title
    draft: false
    tags:
    - example-tag
    ---

    The rest of your content lives here. You can use **Markdown** here :)
    ```

3. 本地构建

    ```bash
    npx quartz build --serve
    ```

4. 将本地更新推送的储存库

    ```bash
    npx quartz sync
    ```

5. 获取最新的 Quartz 更新

    ```bash
    npx quartz update
    ```

6. 添加rss（可选）
    `quartz.layout.ts`

    ```ts
     "RSS":"https://blog.chenxuexin.com/index.xml"
    ```

7. 添加评论功能（可选）
      基于 [giscus](https://giscus.app/zh-CN)，[使用方法](https://github.com/xy-241/CS-Notes/commit/d4748776fc18382e293421266084c3a165a04afd)
  