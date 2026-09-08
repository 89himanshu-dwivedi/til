# 🕸️ GRAPH — Crisp Interview Notes

> **One-liner:** Vertices connected by edges — the **most general** structure. Models networks, relationships, maps, dependencies. May have **cycles** (unlike trees). Traversed with BFS (queue) or DFS (stack).

```
Adjacency List:
A → [B, D]
B → [A, C, E]
C → [B, F]
D → [A, E]
E → [B, D, F]
F → [C, E]
```

## ⚡ Complexity Cheat Sheet

| Operation | Adjacency List | Adjacency Matrix |
|---|---|---|
| Add edge | O(1) | O(1) |
| BFS / DFS | **O(V + E)** | O(V²) |
| Check edge exists | O(degree) | O(1) |
| Space | O(V + E) — good for **sparse** | O(V²) — good for **dense** |

**Dijkstra (weighted shortest path, heap-backed):** O((V+E) log V)

## 🧠 Mental Model

```
BFS from A (queue, level by level):
  visit A → enqueue neighbours B, D
  visit B → enqueue C, E
  visit D → (E already queued)
  → finds SHORTEST PATH in an unweighted graph

DFS (stack/recursion, goes deep first):
  visit A → go to B → go to C → go to F → backtrack...
  → good for cycle detection, topological sort
```

## ⚠️ Rules & Traps

- **Always track a `visited` set** — graphs can have cycles; skipping this = infinite loop.
- Adjacency **matrix** on a huge **sparse** graph → O(V²) memory waste. Use adjacency **list** instead.
- Recursive DFS on very deep/large graphs → stack overflow. Go **iterative** with an explicit stack.
- BFS finds shortest path only for **unweighted** graphs — for weighted, use **Dijkstra**.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Modeling arbitrary relationships/networks | Data is strictly hierarchical (use Tree — simpler) |
| Shortest path (BFS unweighted, Dijkstra weighted) | Graph is dense and small (matrix may be simpler) |
| Dependency ordering, cycle detection | |

## 🎯 Interview Signal

> **"BFS vs DFS?"**
> **BFS** = queue, explores level-by-level, gives **shortest path** in unweighted graphs.
> **DFS** = stack/recursion, explores deep first, suits **cycle detection** & **topological sort**.
> Both are **O(V + E)**.

## 🌍 Real Uses

Social/CRM relationship graphs · Maps & logistics routing (shortest path) · Build/deploy dependency order (topological sort) · Fraud-ring detection · Recommendation systems

## 🔐 Security & Reliability

- Bound size/depth from untrusted graph input (DoS via huge/malicious graphs).
- **Cycle detection** prevents infinite processing loops.
- Validate edges to prevent malicious dependency injection.
- Test disconnected, cyclic, and single-node graphs specifically.

## 📈 Scalability

Graphs scale into **graph databases** (Neo4j), **distributed graph processing** (Pregel, GraphX), and recommendation/fraud systems over **billions of edges**. Salesforce relationships form an implicit graph.

## 💻 Code (BFS + DFS)

```python
# Python — BFS & DFS
from collections import deque
graph = {"A": ["B", "D"], "B": ["A", "C", "E"], "C": ["B", "F"],
         "D": ["A", "E"], "E": ["B", "D", "F"], "F": ["C", "E"]}

def bfs(start):
    seen, q, order = {start}, deque([start]), []
    while q:
        u = q.popleft(); order.append(u)
        for v in graph[u]:
            if v not in seen: seen.add(v); q.append(v)
    return order

def dfs(u, seen=None, order=None):
    seen = seen or set(); order = order if order is not None else []
    seen.add(u); order.append(u)
    for v in graph[u]:
        if v not in seen: dfs(v, seen, order)
    return order
```

```typescript
// TypeScript — adjacency + BFS
const graph: Record<string, string[]> = { A:["B","D"], B:["A","C"], C:["B"], D:["A"] };
function bfs(start: string): string[] {
  const seen = new Set([start]); const q = [start]; const order: string[] = [];
  while (q.length) {
    const u = q.shift()!; order.push(u);
    for (const v of graph[u]) if (!seen.has(v)) { seen.add(v); q.push(v); }
  }
  return order;
}
```

```apex
// Salesforce Apex — adjacency map + BFS with visited set
Map<Id, List<Id>> adj = buildAdjacency();     // from relationship query
Set<Id> visited = new Set<Id>();
List<Id> queue = new List<Id>{ startId };
visited.add(startId);
while (!queue.isEmpty()) {
    Id u = queue.remove(0);                     // dequeue
    for (Id v : adj.get(u) ?? new List<Id>()) {
        if (!visited.contains(v)) {             // visited guard = no cycles
            visited.add(v);
            queue.add(v);
        }
    }
}
```

## 🔶 Salesforce Reality

Salesforce data **is a graph** — lookups, master-detail, junction objects form arbitrary relationships (with possible cycles via lookups).

- Adjacency: `Map<Id, List<Id>>` built from a relationship query.
- Traverse: **iterative** BFS with a `List` as queue + a `Set<Id>` visited guard.
- Visited set is what prevents infinite loops on circular references.
- **FDE tip:** To walk a network of related records (account hierarchies, referral chains) in Apex, build a `Map<Id, List<Id>>` adjacency from **one bulk query**, then BFS with a `Set<Id>` visited guard — governor-safe and cycle-proof.

## ⚙️ Quick Setup

```bash
# Python / TypeScript
python graph.py
npx ts-node graph.ts

# Salesforce
sf apex run --file scripts/apex/graph.apex --target-org fde-dev
```

---
### 🎯 Remember This
> **Graph → "Anything can connect to anything, and cycles are allowed."**
> BFS = queue = shortest path (unweighted). DFS = stack = deep-first, cycles, topo sort. Always keep a visited set.
