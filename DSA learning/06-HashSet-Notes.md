# 🎯 HASHSET — Crisp Interview Notes

> **One-liner:** A collection of **unique** values — average **O(1)** add/contains/remove. Same hashing as HashMap, but keys only. Built for de-duplication and fast membership tests.

```
value → hash(value) → index = hash mod capacity
                            ↓
   bucket 0: (empty)
   bucket 1: value          ← duplicates never stored twice
   bucket 2: (empty)
```

## ⚡ Complexity Cheat Sheet

| Operation | Average | Worst | Note |
|---|---|---|---|
| `add(x)` | **O(1)** | O(n) | rejected if already present |
| `contains(x)` | **O(1)** | O(n) | worst = heavy collisions |
| `remove(x)` | **O(1)** | O(n) | |

## 🧠 Mental Model

```
add(value)
  hash(value) → bucket
    already there?  → reject duplicate
    not there?       → store, size + 1

De-dup a stream:
  add "apple" → new, stored
  add "sky"   → new, stored
  add "apple" again → rejected, size unchanged
```

Internally: **a HashMap where the value is a placeholder** — same buckets, same hashing, same collision chains.

## ⚠️ Rules & Traps

- Needs correct `equals()` **+** `hashCode()` on custom elements — same contract as HashMap.
- **Mutable elements** that change hash after insertion → "lost" entries, broken lookups.
- Don't rely on iteration order of a plain `HashSet` — use `LinkedHashSet` (insertion order) or `TreeSet` (sorted) if order matters.
- Nested loops to find duplicates = O(n²) — a set does it in **O(n)**.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Uniqueness enforcement | You need key→value pairs (use HashMap) |
| Fast membership tests | You need ordered/sorted iteration (plain HashSet) |
| De-duplicating ids/records | |

## 🎯 Interview Signal

> **"Find duplicates in an array"** — iterate once, `add()` each to a set; if `add` returns *false* (already present), it's a duplicate.
> **O(n)** with a set vs **O(n²)** with nested loops.

## 🌍 Real Uses

De-duplicating data feeds · Sets of permissions/roles · Distinct counts in analytics · Salesforce `Set<Id>` before a bulk query

## 🔐 Security & Reliability

- **Hash-flooding DoS** mitigated by seeded/randomized hashing.
- Bound size from untrusted input; validate elements before adding.
- Correct `equals`/`hashCode` + immutable elements → consistent membership checks.
- Use concurrent sets for multi-threaded access.

## 📈 Scalability

Set semantics scale into **distributed sets** (Redis `SET`), **Bloom filters** (probabilistic membership at huge scale), and dedupe stages in large data pipelines.

## 💻 Code (add / contains / remove + dedup)

```python
# Python — set
s = {"apple", "sky"}
s.add("pear")          # O(1)
print("apple" in s)     # True, O(1)
s.discard("sky")        # remove O(1)

nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)      # {1, 2, 3}
```

```java
// Java
Set<String> set = new HashSet<>();
set.add("apple");
boolean has = set.contains("apple"); // true
```

```typescript
// TypeScript
const set = new Set<string>();
set.add("apple");
const present = set.has("apple");     // true
```

```apex
// Salesforce Apex — unique ids for a bulk query
Set<Id> accountIds = new Set<Id>();
for (Contact c : Trigger.new) accountIds.add(c.AccountId);   // auto-dedup

Map<Id, Account> accs = new Map<Id, Account>(
    [SELECT Id, Name FROM Account WHERE Id IN :accountIds]); // ONE query

Set<String> seen = new Set<String>();
for (String email : emails)
    if (!seen.add(email)) System.debug('duplicate: ' + email);
```

## 🔶 Salesforce Reality

- `Set<T>` **is** a hash set — the standard way to gather **unique ids/keys** during a loop, then query once.
  - Collect: `Set<Id> ids = new Set<Id>();` → `ids.add(c.AccountId)`
  - Bulk query: `WHERE Id IN :ids`
  - Membership check: `ids.contains(x)` — O(1)
- **FDE tip:** Always gather related record ids into a `Set<Id>` inside your loop, then run **ONE SOQL** with `WHERE Id IN :ids`. The set auto-dedups and keeps you under the **100-SOQL governor limit**.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/hashset.apex --target-org fde-dev

# Python / TypeScript
python set_demo.py
npx ts-node set.ts
```

---
### 🎯 Remember This
> **HashSet → "No duplicates allowed, and I'll tell you in O(1)."**
> Same hashing as HashMap, values only. Collect ids in a `Set` → one bulk query, not one per loop.
