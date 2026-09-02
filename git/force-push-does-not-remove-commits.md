# Force push does not remove commits from GitHub

*2026-09-02*

Rewrote a repository to a single root commit and force pushed, expecting the old history to
be gone. The branch pointer moved, but the old commits were still readable by direct SHA:

```bash
git checkout --orphan clean && git add -A && git commit -m "..."
git branch -D main && git branch -m main
git push --force origin main
```

```bash
gh api repos/<owner>/<repo>/commits/<old-sha>   # still returns 200
```

Force push makes commits **unreachable from a branch**. GitHub keeps unreachable objects, and
`github.com/<owner>/<repo>/commit/<sha>` keeps working - there is no automatic garbage
collection you can rely on. Forks keep their own copy too.

The only options that actually work:

| Option | Result |
| --- | --- |
| Contact GitHub Support to purge | Works, takes days, depends on them |
| **Delete and recreate the repository** | Instant and total - old SHAs return 404 |

**Why it surprised me:** every guide describes force push as "rewriting history", which reads
like deletion. It is not. If the reason for the rewrite is that something should not be
public, force push alone has not solved your problem.

**Source:** verified against the GitHub API before and after
