# TIL

**Today I Learned** - short notes from daily engineering work.

One file per thing learned. Written the day it happened, kept small on purpose. If a note
grows past a screen it belongs in one of the full courses instead, not here.

> Written by **Himanshu Kumar** - Technical Lead & Solution Architect.
> Longer material lives in my [zero-to-architect](https://github.com/89himanshu-dwivedi?tab=repositories) courses.

---

## Why this exists

Most things you learn are lost within a week. Not because they were hard, but because
nothing was written down at the moment it clicked.

The rules that keep this useful:

1. **Write it the same day.** A note written next week is a note never written.
2. **Keep it under a screen.** The problem, the answer, the proof. Nothing else.
3. **Include the command or code.** A note you cannot act on is a blog post, not a note.
4. **Say why it surprised you.** That sentence is what makes it findable later.
5. **Never edit for polish.** Fix errors, ignore prose.

---

## How to add one

```bash
cp _template.md <category>/<short-descriptive-name>.md
# write it, then:
python build-index.py
git add -A && git commit -m "TIL: <title>" && git push
```

`build-index.py` regenerates the index below from the files themselves - never edit that
section by hand.

---

<!-- INDEX:START -->

## 6 notes

### docker  <sub>1</sub>

- [Multi-stage builds save nothing unless you copy only the artifact](docker/multi-stage-copy-only-the-artifact.md) <sub>2026-09-01</sub>

### git  <sub>2</sub>

- [Force push does not remove commits from GitHub](git/force-push-does-not-remove-commits.md) <sub>2026-09-02</sub>
- [GitHub's Mermaid rejects `A -- "text" --> B`](git/github-mermaid-rejects-dash-quote-syntax.md) <sub>2026-09-01</sub>

### kubernetes  <sub>2</sub>

- [CrashLoopBackOff: read the previous container, not the current one](kubernetes/crashloopbackoff-read-previous-logs.md) <sub>2026-09-02</sub>
- [A running Pod's env vars cannot be changed - but the image does not need rebuilding](kubernetes/pod-env-vars-are-immutable.md) <sub>2026-09-02</sub>

### powershell  <sub>1</sub>

- [.NET methods in PowerShell use the process directory, not your shell location](powershell/system-io-uses-process-directory.md) <sub>2026-08-30</sub>

### Latest

- `2026-09-02` **git** - [Force push does not remove commits from GitHub](git/force-push-does-not-remove-commits.md)
- `2026-09-02` **kubernetes** - [CrashLoopBackOff: read the previous container, not the current one](kubernetes/crashloopbackoff-read-previous-logs.md)
- `2026-09-02` **kubernetes** - [A running Pod's env vars cannot be changed - but the image does not need rebuilding](kubernetes/pod-env-vars-are-immutable.md)
- `2026-09-01` **docker** - [Multi-stage builds save nothing unless you copy only the artifact](docker/multi-stage-copy-only-the-artifact.md)
- `2026-09-01` **git** - [GitHub's Mermaid rejects `A -- "text" --> B`](git/github-mermaid-rejects-dash-quote-syntax.md)
- `2026-08-30` **powershell** - [.NET methods in PowerShell use the process directory, not your shell location](powershell/system-io-uses-process-directory.md)

*Index rebuilt 2026-09-02*

<!-- INDEX:END -->

---

## Categories

New categories are just new folders. Current ones:

| Folder | For |
| --- | --- |
| `docker` | Images, layers, builds, runtime |
| `kubernetes` | Pods, workloads, cluster operations |
| `salesforce` | Apex, LWC, platform, integrations |
| `git` | Version control, history, remotes |
| `powershell` | Windows shell and scripting |
| `python` | Language and tooling |
| `ai` | LLMs, agents, prompting, MCP |

---

## About me

- Technical Lead & Solution Architect at **CRISIL Ltd, an S&P Global company**
- 8 years across Salesforce architecture, integrations, and enterprise GenAI
- [GitHub](https://github.com/89himanshu-dwivedi) · [Trailblazer](https://www.salesforce.com/trailblazer/hdwivedi2) · **LinkedIn** · **X (Twitter)**

---

## Licence

See [LICENSE](LICENSE) - proprietary, all rights reserved.
