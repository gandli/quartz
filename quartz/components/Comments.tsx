import { QuartzComponentConstructor } from "./types"

export default (() => {
  function Footer() {
    return (
      <script
        src="https://giscus.app/client.js"
        data-repo="gandli/quartz"
        data-repo-id="R_kgDOLpUd-w"
        data-category="comments"
        data-category-id="DIC_kwDOLpUd-84CebZF"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async
      ></script>
    )
  }
  return Footer
}) satisfies QuartzComponentConstructor
