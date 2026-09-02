# GitHub's Mermaid rejects `A -- "text" --> B`

*2026-09-01*

Every architecture diagram in two repos showed **"Unable to render rich display"**. The
syntax is valid in the Mermaid docs and renders in local previews:

```text
N0 -- "docker run nginx" --> N1
```

GitHub's renderer refuses it. Quoted labels only work in the pipe form:

```text
N0 -->|"docker run nginx"| N1
```

Diagrams with plain `-->` arrows and no labels rendered fine, which is why it looked like
"all the diagrams broke" - only the labelled ones did, and those were every architecture
diagram.

Also worth knowing: Mermaid renders on **github.com file view only**. On GitHub Pages with
Jekyll it stays a plain code block, no matter how correct the syntax is.

**Why it surprised me:** the error message says nothing about syntax, and the failing form is
documented as valid. I nearly rewrote the diagrams before checking the exact link syntax.

**Source:** 202 diagrams fixed across two repos
