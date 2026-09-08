# 🔍 BINARY SEARCH TREE (BST) — Crisp Interview Notes

> **One-liner:** Ordered binary tree — **left < node < right**. That invariant lets search/insert/delete skip half the tree each step → **O(log n)** when balanced.

```
            50
           /  \
        30      70
       /  \    /  \
     20   40  60   80
```

## ⚡ Complexity Cheat Sheet

| Operation | Balanced | Worst (skewed) |
|---|---|---|
| `search` | **O(log n)** | O(n) |
| `insert` | **O(log n)** | O(n) |
| `delete` | **O(log n)** | O(n) |

**Why skewed happens:** inserting already-sorted data into a plain BST → a straight line → O(n), basically a linked list.

## 🧠 Mental Model

```
search(60) starting at root 50:
  60 vs 50 → larger → go right
  60 vs 70 → smaller → go left
  60 vs 60 → equal   → FOUND
                        (3 comparisons ≈ log n)
```

**Key invariant (never forget):** left subtree < node < right subtree — this is what makes inorder traversal give **sorted order**.

## ⚠️ Rules & Traps

- **Sorted input → plain BST → O(n)** — this is the #1 interview trap. Fix: self-balancing tree (AVL, Red-Black).
- **Delete with two children** — replace node with its **inorder successor** (smallest in right subtree), don't just unlink.
- Deep recursion on huge/attacker-controlled trees → stack overflow — guard depth or go iterative.
- Don't hand-roll a BST when a `HashMap` (O(1), no ordering needed) already solves the problem.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Need both fast search **and** fast insert/delete | Pure key lookup, no ordering needed (use HashMap) |
| Range queries / sorted iteration | Input arrives pre-sorted (skews a plain BST) |
| Ordered statistics / percentiles | You'd need to hand-roll balancing — use library `TreeMap`/`TreeSet` instead |

## 🎯 Interview Signal

> **"What breaks a BST's O(log n)?"**
> Inserting **sorted data** — the tree degenerates into a straight line (skewed) = O(n). Self-balancing trees (AVL / Red-Black) prevent this by rebalancing on every insert.

## 🌍 Real Uses

Database **B-tree indexes** & range queries · Ordered event timelines / scheduling · Autocomplete (sorted prefix ranges) · Ordered statistics / percentiles

## 🔐 Security & Reliability

- **Algorithmic-complexity DoS:** attacker feeds sorted input to skew a naive BST → O(n) ops — mitigate with a self-balancing tree.
- Guard recursion depth; bound tree size from untrusted input.
- Self-balancing trees guarantee **log-time worst case**.
- Test skewed, balanced, and delete-with-two-children cases specifically.

## 📈 Scalability

The BST idea scales into **B-trees / B+ trees** — high-fanout, disk-optimized balanced trees behind virtually every relational database index and file system.

## 💻 Code (insert / search + balanced alternative)

```python
# Python — BST insert & search
class Node:
    def __init__(self, v): self.v, self.left, self.right = v, None, None

def insert(root, v):
    if root is None: return Node(v)
    if v < root.v: root.left = insert(root.left, v)
    elif v > root.v: root.right = insert(root.right, v)
    return root

def search(root, v):
    while root:
        if v == root.v: return True
        root = root.left if v < root.v else root.right
    return False
```

```java
// Java — TreeMap/TreeSet ARE balanced BSTs (Red-Black tree), use these in prod
TreeMap<Integer, String> tm = new TreeMap<>();
tm.put(50, "a"); tm.put(30, "b");
tm.firstKey();                 // 30 (sorted)
tm.ceilingKey(40);             // 50 (range query)
```

```typescript
// TypeScript — no built-in balanced tree; sort, or use a library
const sorted = [50, 30, 70].sort((a, b) => a - b);
```

```apex
// Salesforce Apex — Comparable sort (BST-like ordered output)
public class ScoredLead implements Comparable {
    public Integer score;
    public Integer compareTo(Object o) {
        Integer other = ((ScoredLead) o).score;
        return score == other ? 0 : (score < other ? -1 : 1);
    }
}
List<ScoredLead> leads = getLeads();
leads.sort();   // ascending, like an inorder BST traversal

// Prefer the DB for ordered/range search:
List<Opportunity> top = [SELECT Id, Amount FROM Opportunity
                          WHERE Amount > 1000 ORDER BY Amount DESC LIMIT 10];
```

## 🔶 Salesforce Reality

- **No native BST/TreeMap in Apex.**
- For sorted needs: `myList.sort()` (implement `Comparable` for custom sort), or let SOQL `ORDER BY` do it.
- Salesforce field indexes **are B-trees** — a selective, indexed `WHERE` query gives you O(log n) search at platform scale.
- **FDE tip:** Don't hand-build trees in Apex — push ordering and range filtering into SOQL (`ORDER BY`, indexed `WHERE`). The database's B-tree index is your real O(log n) structure.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/bst.apex --target-org fde-dev

# Python / TypeScript
python bst.py
npx ts-node bst.ts
```

---
### 🎯 Remember This
> **BST → "Left is smaller, right is bigger — so I only look at half each time."**
> O(log n) balanced, O(n) skewed. Inorder = sorted. Sorted input is the trap. Use `TreeMap`/`ORDER BY` in production, don't hand-roll.
