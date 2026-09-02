# CrashLoopBackOff: read the previous container, not the current one

*2026-09-02*

A Pod was stuck in `CrashLoopBackOff` and `kubectl logs` printed nothing, so I assumed the
container was producing no output at all.

It was. I was reading the wrong container - the one that had just been restarted and had not
printed anything yet. The output I wanted belonged to the instance that died:

```bash
kubectl logs <pod>              # the new container - usually empty
kubectl logs <pod> --previous   # the one that actually crashed
```

Also worth knowing: `BackOff` is the **delay**, not the crash. Kubernetes waits ~10s, 20s,
40s, doubling up to a five-minute cap - so a Pod crashing for an hour only retries every
five minutes.

**Why it surprised me:** the status names the symptom so clearly that it never occurred to me
I was looking at a different container than the one in the message.

**Source:** k3d lab, module 15
