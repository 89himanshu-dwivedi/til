# 🌳 TREE — Crisp Interview Notes

> **One-liner:** Hierarchical nodes — one root, each node has children. Models hierarchies (org charts, file systems, DOM) and powers fast search when balanced.

```
            50 (root)
           /          \
        30             70
       /   \          /   \
     20     40      60    (nil)
   (leaf)  (leaf)  (leaf)
```

## ⚡ Complexity Cheat Sheet

| Operation | Balanced | Skewed (worst) |
|---|---|---|
| Search (BST) | **O(log n)** | O(n) — degrades to a list |
| Insert / Delete | **O(log n)** | O(n) |
| Traversal (any) | O(n) | O(n) — visits every node |

## 🧠 Traversal Cheat Sheet

| Traversal | Order | Uses | Good for |
|---|---|---|---|
| **Preorder** | Root → L → R | stack/recursion (DFS) | copy / serialize |
| **Inorder** | L → Root → R | stack/recursion (DFS) | **sorted order on a BST** |
| **Postorder** | L → R → Root | stack/recursion (DFS) | delete / evaluate expression |
| **Level-order** | by depth | **queue** (BFS) | shortest-path-like, level processing |

```
DFS (pre/in/post) → uses a Stack (or recursion)
BFS (level-order) → uses a Queue
```

## ⚠️ Rules & Traps

- Unbalanced tree → degrades to **O(n)**, basically a linked list.
- Deep recursion on untrusted/huge trees → **stack overflow** — use iterative traversal (explicit stack/queue) instead.
- Wrong traversal for the task = wrong answer (e.g., using preorder when you need sorted output).
- Never mutate a tree while traversing it.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Hierarchical data (org chart, categories, DOM) | Data has no natural hierarchy |
| Need O(log n) search on sorted data (balanced BST) | Tree can go deeply unbalanced (use self-balancing: AVL/Red-Black) |
| Range queries, prefix search | Simple flat key lookup (HashMap is simpler & O(1)) |

## 🎯 Interview Signal

> **"Inorder traversal of a BST gives what?"**
> Elements in **sorted ascending order**. One of the most-used tree properties in interviews.

## 🌍 Real Uses

Org charts / category trees / BOM · Database **B-tree indexes** · The DOM & component trees · Salesforce role hierarchy & parent-child records

## 🔐 Security & Reliability

- Limit depth/size from untrusted input (stack-exhaustion DoS, "billion laughs" style nested payloads).
- Validate tree-shaped input (XML/JSON) against depth limits.
- Self-balancing trees guarantee **log-time worst case**.
- Test skewed, balanced, empty, and single-node trees.

## 📈 Scalability

Trees scale into **B-trees / B+ trees** (database & filesystem indexes), **tries** (prefix search), and **segment/interval trees** (range queries over huge datasets).

## 💻 Code (traversals)

```python
# Python — binary tree + traversals
class Node:
    def __init__(self, v):
        self.v, self.left, self.right = v, None, None

def inorder(n, acc):        # Left, Root, Right → sorted on a BST
    if not n: return
    inorder(n.left, acc); acc.append(n.v); inorder(n.right, acc)

def bfs(root):
    from collections import deque
    q, out = deque([root]), []
    while q:
        n = q.popleft(); out.append(n.v)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return out
```

```typescript
// TypeScript — preorder
class TNode { left: TNode|null=null; right: TNode|null=null; constructor(public v:number){} }
function preorder(n: TNode|null, acc:number[]=[]): number[] {
  if(!n) return acc;
  acc.push(n.v); preorder(n.left, acc); preorder(n.right, acc);
  return acc;   // Root, Left, Right
}
```

```apex
// Salesforce Apex — build parent-child tree & BFS traverse
Map<Id, List<Account>> children = new Map<Id, List<Account>>();
for (Account a : [SELECT Id, ParentId FROM Account]) {
    if (a.ParentId == null) continue;
    if (!children.containsKey(a.ParentId)) children.put(a.ParentId, new List<Account>());
    children.get(a.ParentId).add(a);
}
// BFS from a root using a queue (List)
List<Id> queue = new List<Id>{ rootId };
while (!queue.isEmpty()) {
    Id cur = queue.remove(0);
    for (Account child : children.get(cur) ?? new List<Account>())
        queue.add(child.Id);
}
```

## 🔶 Salesforce Reality

Salesforce is full of trees: the **role hierarchy**, parent-child (master-detail/lookup) records, and record-type/category structures.

- Build tree in memory: `Map<Id, List<sObject>>` — parent → children.
- Traverse hierarchy chains **iteratively**, not recursively, to avoid limits.
- **FDE tip:** To process a deep account/role hierarchy, build a `Map<Id, List<Id>>` from **one query**, then traverse iteratively with a queue (BFS) — avoids both SOQL-in-loop and Apex's max call-stack-depth limit.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/tree.apex --target-org fde-dev

# Python / TypeScript
python tree.py
npx ts-node tree.ts
```

---
### 🎯 Remember This
> **Tree → "Hierarchy, and I can search it in log(n) if I stay balanced."**
> Inorder on a BST = sorted. DFS = stack. BFS = queue. Unbalanced = it's just a slow linked list.
