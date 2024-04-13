---
title: git 的稀疏检出和部分克隆
draft: false
tags:
  - git
  - 稀疏检出
  - 部分克隆
  - sparse-checkout
  - bootstrap.sh
---

1. 本地已有仓库

   ```bash
   $ git sparse-checkout set client/android

   $ ls
   bootstrap.sh*  client/  LICENSE.md  README.md

   $ ls client/
   android/

   $ find . -type f | wc -l
   62
   ```

2. 克隆远程仓库时，稀疏检出和部分克隆

   ```bash
   $ git clone --filter=blob:none --no-checkout <https://github.com/derrickstolee/sparse-checkout-example>
   Cloning into 'sparse-checkout-example'...
   Receiving objects: 100% (373/373), 75.98 KiB | 2.71 MiB/s, done.
   Resolving deltas: 100% (23/23), done.

   $ cd sparse-checkout-example/

   $ git sparse-checkout set --cone

   $ git checkout main
   remote: Enumerating objects: 2, done.
   remote: Counting objects: 100% (2/2), done.
   remote: Compressing objects: 100% (2/2), done.
   remote: Total 3 (delta 0), reused 1 (delta 0), pack-reused 1
   Receiving objects: 100% (3/3), 1.41 KiB | 1.41 MiB/s, done.
   Already on 'main'
   Your branch is up to date with 'origin/main'.

   $ git sparse-checkout set client/android
   remote: Enumerating objects: 3, done.
   remote: Counting objects: 100% (3/3), done.
   remote: Compressing objects: 100% (3/3), done.
   remote: Total 26 (delta 0), reused 1 (delta 0), pack-reused 23
   Receiving objects: 100% (26/26), 985.91 KiB | 13.69 MiB/s, done.
   ```

   如果检出多个目录，使用`git sparse-checkout set client/android web/browser`
