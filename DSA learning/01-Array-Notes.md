# 📦 ARRAY — Crisp Interview Notes

> **One-liner:** Array = fast access, costly front/middle insert-delete (shifting).

```
Index:   0    1    2    3
Array: [10] [20] [30] [40]
        ↑ base + index × size = direct jump
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Why |
|---|---|---|
| Access `arr[i]` | **O(1)** 🔥 | direct address calc |
| Search (unsorted) | O(n) | linear scan |
| Insert / Delete **front** | O(n) | shift everything |
| Insert / Delete **middle** | O(n) | shift remaining |
| Insert / Delete **end** | **O(1)** amortized | no shift needed |
| Resize (dynamic array) | O(n) | rare — copy to new block |

## 🧠 Mental Model

```
INSERT 99 at index 1
[10][20][30]  →  [10][99][20][30]
                      ← shifted right

DELETE index 1
[10][20][30]  →  [10][30]
                    ← shifted left
```

**Dynamic array growth:** capacity full → allocate bigger block → copy old → add new → occasional O(n), but **append averages O(1) (amortized)**.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Index-based access | Frequent front insert/delete |
| Sequential iteration | Frequent middle insert/delete |
| Read-heavy workload | |
| Cache performance matters | |

**Alternatives:** Map (key lookup) · Set (uniqueness) · Deque (front ops) · Linked List (known-node insert/delete)

⚠️ **Trap:** Repeated `insert(0, x)` in a loop → O(n) each → **O(n²)** overall.

## 🌍 Real Uses
Buffers · Batch processing · Lookup tables · Analytics · AI vectors/embeddings

## 💻 Code (append / access / insert)

```javascript
// JavaScript
const arr = [10, 20, 30];
arr.push(40);          // O(1) amortized
arr[1];                // O(1)
arr.splice(1, 0, 99);  // O(n)
```

```python
# Python
arr = [10, 20, 30]
arr.append(40)     # O(1) amortized
arr[1]              # O(1)
arr.insert(1, 99)   # O(n)
```

```java
// Java
List<Integer> arr = new ArrayList<>(List.of(10, 20, 30));
arr.add(40);        // O(1) amortized
arr.get(1);         // O(1)
arr.add(1, 99);     // O(n)
```

```typescript
// TypeScript
const arr: number[] = [10, 20, 30];
arr.push(40);          // O(1) amortized
arr[1];                 // O(1)
arr.splice(1, 0, 99);   // O(n)
```

```apex
// Salesforce Apex
List<Integer> arr = new List<Integer>{10, 20, 30};
arr.add(40);         // O(1) amortized
arr[1];              // O(1)
arr.add(1, 99);      // O(n)
```

## 🔶 Salesforce Reality

- `List<T>` = dynamic-array-like collection.
- SOQL results usually come back as a `List`.
- **Bulkification pattern:** collect records in a `List` inside the loop → single bulk DML **after** the loop (never DML per iteration).

```
Loop → collect in List → loop ends → 1 bulk DML   ✅
Loop → DML every record                            ❌
```

---
### 🎯 Remember This
> **Array → "Mujhe data jaldi access karna hai."**
> O(1) access, O(n) shifting for front/middle ops.
