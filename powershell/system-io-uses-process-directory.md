# .NET methods in PowerShell use the process directory, not your shell location

*2026-08-30*

Ran this after `cd`-ing into a project folder and the file appeared somewhere else entirely:

```powershell
cd 'D:\projects\my-app'
[System.IO.File]::WriteAllText('index.md', $content)   # NOT written to D:\projects\my-app
```

`Set-Location` changes PowerShell's *provider* location. It does not change the .NET
process's current working directory, which is wherever the process was started. Any
`System.IO` call resolves relative paths against that instead.

```powershell
[System.IO.Directory]::GetCurrentDirectory()   # the real one .NET uses
$PWD.Path                                      # the one you think you are in
```

Fix - always pass an absolute path:

```powershell
[System.IO.File]::WriteAllText((Join-Path $PWD 'index.md'), $content)
```

**Why it surprised me:** it fails silently and successfully. No error, a file is written, it
is just not where you are looking - so you conclude the code did not run.

**Source:** lost 20 minutes to a stray file at a repo root
