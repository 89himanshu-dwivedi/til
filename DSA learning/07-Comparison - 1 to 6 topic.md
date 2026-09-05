# 🧭 Data Structures — Master Comparison (Array · LinkedList · Stack · Queue · HashMap · HashSet)

> **One-liner:** Pick by **access pattern**, not by habit — index? key? order? uniqueness?

## ⚡ Complexity Comparison

| Structure | Access | Search | Insert | Delete | Order |
|---|---|---|---|---|---|
| **Array** | O(1) | O(n) | O(n) front/mid · O(1) end | O(n) front/mid · O(1) end | Index order |
| **Linked List** | O(n) | O(n) | O(1) head/known-node · O(n) tail* | O(1) head/known-node | Sequential |
| **Stack** | — | O(n) | O(1) top only | O(1) top only | LIFO |
| **Queue** | — | O(n) | O(1) rear | O(1) front* | FIFO |
| **HashMap** | O(1) avg by key | O(1) avg | O(1) avg | O(1) avg | No order guaranteed |
| **HashSet** | — | O(1) avg (contains) | O(1) avg | O(1) avg | No order guaranteed |

`*` O(1) only with the right backing store (tail pointer for queue/list; else O(n)).

## 🧠 One-Line Mental Model Each

```
Array      → "Give me the index, I jump straight there."
LinkedList → "I don't shift, I rewire pointers."
Stack      → "Last one in, first one out."       (LIFO)
Queue      → "First one in, first one out."      (FIFO)
HashMap    → "Give me the key, I jump to the value."
HashSet    → "No duplicates, and I know in O(1)."
```

## 🎯 When to Use — Short & Important

| Need | Use |
|---|---|
| Fast **index-based** access + sequential iteration | **Array** |
| Frequent insert/delete at **known node**, no shifting | **Linked List** |
| **Undo/redo**, bracket matching, DFS, function calls | **Stack** |
| **Fair ordering**, BFS, task/job processing, buffering | **Queue** |
| Fast **key → value** lookup, caching, correlation | **HashMap** |
| **Uniqueness**, de-duplication, fast membership check | **HashSet** |

## ⚠️ Quick Decision Traps (Interview Gold)

- **Need random access by position?** → Array, never Linked List.
- **Need most-recent-first?** → Stack, not Queue.
- **Need arrival-order-first?** → Queue, not Stack.
- **Need key→value mapping?** → HashMap, not HashSet.
- **Only need "have I seen this before?"** → HashSet, not HashMap (don't waste a value slot).
- **Frequent front insert/delete on a plain array?** → Red flag, switch to Linked List / Deque.

## 🔶 Salesforce Cheat Line (all 6 in one breath)

```
List<T>      → Array (also doubles as Stack/Queue: add/remove(size-1) or remove(0))
(custom)     → Linked List (rare, build Node class yourself)
Map<K,V>     → HashMap (Map<Id, sObject> = #1 bulkification pattern)
Set<T>       → HashSet (Set<Id> before WHERE Id IN :ids — auto-dedup)
```

**FDE golden rule:** *Collect in a `Set<Id>` → correlate via `Map<Id, sObject>` → never query or DML inside a loop.* This one pattern covers 90% of governor-limit-safe Apex.

## 🌍 Real-World Pairing Cheat Sheet

| Scenario | Structure |
|---|---|
| Undo history in an editor | Stack |
| Print job / task queue | Queue |
| Caching API responses by id | HashMap |
| De-duping incoming records | HashSet |
| Sequential log buffer | Array |
| Building a custom graph/tree traversal chain | Linked List |

---
### 🎯 Remember This
> **Array = index. Linked List = pointer. Stack = LIFO. Queue = FIFO. HashMap = key. HashSet = unique.**
> Pick the structure that matches the *access pattern* the problem actually needs — not the one you're most comfortable with.
