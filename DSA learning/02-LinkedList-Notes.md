# 🔗 LINKED LIST — Crisp Interview Notes

> **One-liner:** Linked List = no shifting; rewire pointers to connect/disconnect nodes.

```
HEAD
 ↓
[10 | •] → [20 | •] → [30 | null]
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Why |
|---|---|---|
| Access by index | O(n) | must traverse |
| Search | O(n) | traverse + compare |
| Insert / Delete **head** | **O(1)** 🔥 | just rewire `head` |
| Insert **tail** (no tail ptr) | O(n) | traverse to end |
| Insert **tail** (with tail ptr) | **O(1)** | direct rewire |
| Insert / Delete at **known node** | **O(1)** | pointer rewiring |
| Delete **by value** | O(n) | search first, then O(1) unlink |

## 🧠 Node Types

```
Singly:   [value | next]              10 → 20 → 30 → null
Doubly:   [prev | value | next]       null ← 10 ↔ 20 ↔ 30 → null
Circular: tail.next → head            10 → 20 → 30 ─┐
                                        ↑____________┘
```

## 🧠 Mental Model

```
HEAD INSERT (new = 5)
new.next = head
head = new
→ O(1)

TAIL INSERT (no tail pointer)
must walk 10→20→30 to find end → O(n)
(with tail pointer kept updated → O(1))
```

## ⚠️ Important Interview Catch

> "Linked List insertion is O(1)" is true **only** when the node/location is already known.

```
Need to search first?
Search  → O(n)
Insert  → O(1)
─────────────────
Overall → O(n)
```

## 🔁 Cycle Detection — Floyd's Algorithm

```
10 → 20 → 30
     ↑     ↓
     └─────┘

slow moves 1 step, fast moves 2 steps
if slow == fast → cycle exists
```

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Frequent insert/delete at known node | Index-based access needed often |
| Head insert/delete heavy | Random access needed |
| Building queues/stacks | Cache locality matters a lot |

## 🌍 Real Uses
LRU Cache · Queue / Deque · Undo-Redo · Graph adjacency lists · Hash-table bucket chains

## 💻 Code (insert at head)

```javascript
// JavaScript
class Node { constructor(v, next = null) { this.value = v; this.next = next; } }
let head = new Node(20);
head = new Node(10, head);   // O(1)
```

```python
# Python
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

head = Node(20)
head = Node(10, head)   # O(1)
```

```java
// Java
class Node { int value; Node next; Node(int v) { value = v; } }
Node head = new Node(20);
Node n = new Node(10); n.next = head; head = n;   // O(1)
```

```typescript
// TypeScript
class Node {
  constructor(public value: number, public next: Node | null = null) {}
}
let head: Node | null = new Node(20);
head = new Node(10, head);   // O(1)
```

```apex
// Salesforce Apex
class Node { Integer value; Node next; Node(Integer v) { value = v; } }
Node head = new Node(20);
Node n = new Node(10); n.next = head; head = n;   // O(1)
```

## 🔶 Salesforce Reality

- Apex has **no built-in LinkedList** — use `List<T>` / `Map<K,V>` instead.
- Custom `Node` class is possible but **rarely used** in real Salesforce dev.

---
### 🎯 Remember This
> **Linked List → "Mujhe nodes ko easily connect/disconnect karna hai."**
> O(n) access/search, O(1) insert/delete at known node.
