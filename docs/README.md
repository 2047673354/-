# docs 目录说明

本仓库使用 GitHub Actions 自动把 PDF 转换为可复制的 TXT 文本，放在 `docs/pdf_text/` 目录下，便于后续做逐节精读、加页码/图号引用与生成 2000 字+原创报告。

## 如何触发

- 手动触发：在 GitHub 仓库顶部进入 **Actions**，选择 **Extract PDFs to text** 工作流，点击 **Run workflow**。
- 自动触发：当向仓库 push PDF 文件或更新现有 PDF 时，工作流会自动运行。

## 查看输出

- 转换结果位于：`docs/pdf_text/`，文件名与 PDF 同名（后缀改为 `.txt`）。
- 转换命令使用 `pdftotext -layout`，尽量保留原始版式，便于我精读与引用。

## 注意事项

- 若 PDF 含大量矢量图/公式，文本可能存在少量排版偏移；如需高保真公式，还请在对话中补充关键公式的截图或 LaTeX。
- 如需我对特定 PDF 出具逐节精读与带页码/图号的总结，请在对话里告知文件名。