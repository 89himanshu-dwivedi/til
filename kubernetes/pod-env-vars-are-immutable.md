# A running Pod's env vars cannot be changed - but the image does not need rebuilding

*2026-09-02*

Changed an environment variable in a Pod manifest, re-applied, and got rejected:

```text
The Pod "demo-pod" is invalid: spec: Forbidden: pod updates may not change fields
other than `spec.containers[*].image`, `spec.initContainers[*].image`,
`spec.activeDeadlineSeconds`, `spec.tolerations` (only additions to existing
tolerations) or `spec.terminationGracePeriodSeconds`
```

So a running Pod is almost entirely immutable - only those five things can change in place.
An env var change needs a **new Pod**:

```bash
kubectl delete -f pod-env.yaml
kubectl apply  -f pod-env.yaml
kubectl exec demo-pod -- printenv UI_COLOR
```

**Why it surprised me:** I had understood "environment variables mean you avoid a rebuild" as
"you avoid a restart". It does not - the container process reads env vars once at start, which
is a Linux property, not a Kubernetes limitation. You skip the *image build*, not the restart.
A Deployment hides this by rolling out new Pods for you.

**Source:** k3d lab, module 18
