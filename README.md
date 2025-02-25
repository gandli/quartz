# [Quartz v4](https://github.com/jackyzha0/quartz)

1. 将本地更新推送的储存库

   ```bash
   npx quartz sync
   ```

2. 本地构建

   ```bash
   npx quartz build --serve
   ```

3. 获取最新的 Quartz 更新

   ```bash
   npx quartz update
   ```

4. 格式化 md 文件，提交 commit message 并 git push
   `npx @lint-md/cli content/**/* --fix && git add . && npx czg ai && git push`

5. `sparse-checkout` 和 `bootstrap.sh`
   使用稀疏模式检出 `content templates quartz`

   ```bash
   chmod +x ./bootstrap.sh
   ./bootstrap.sh content
   ```

   改变注意，不使用稀疏模式

   ```bash
   git sparse-checkout disable
   git pull
   ```

6. 新的提交方式

   ```bash
   npx quartz update &&  npm run format && git add . && npx czg ai && git push
   ```
