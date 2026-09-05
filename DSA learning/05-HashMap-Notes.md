# 🗺️ HASHMAP (Hash Table) — Crisp Interview Notes

> **One-liner:** Key → value store with **average O(1)** get/put. A hash function maps each key to a bucket; collisions chain. The most important practical data structure.

```
key → hash(key) → index = hash mod capacity
                        ↓
   bucket 0: (empty)
   bucket 1: entry → entry   (collision chain)
   bucket 2: (empty)
```

## ⚡ Complexity Cheat Sheet

| Operation | Average | Worst | Note |
|---|---|---|---|
| `get(k)` | **O(1)** | O(n) | worst = all keys collide into one bucket |
| `put(k,v)` | **O(1)** | O(n) | store or update |
| `remove(k)` | **O(1)** | O(n) | |
| resize | — | O(n) | occasional, when load factor exceeded |

## 🧠 Mental Model

```
put(k, v)
  hash(k) → bucket → store entry → avg O(1)

get(k)
  hash(k) → bucket → scan short chain for k → avg O(1)

RESIZE
  load factor > threshold?
    yes → double capacity, rehash ALL entries → O(n) (rare)
    no  → just store, O(1)
```

## ⚠️ Rules & Traps

- Keys need **consistent** `hashCode()` **+** `equals()` — override both together, never one alone.
- **Mutable keys** → break lookup if the key changes after insertion. Use immutable keys (strings, IDs, primitives).
- Don't rely on iteration order (unless using `LinkedHashMap` / ordered variant).
- Poor hash function / heavy collisions → degrades toward O(n).
- Plain map + multi-threading → use a **concurrent map**, not a shared plain HashMap.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Fast keyed lookup / insert / delete | You need sorted/ordered iteration |
| Caching, indexing, de-duplication | Only membership matters (use a Set) |
| Correlating records by ID | Multi-threaded without synchronization |

## 🎯 Interview Signal

> **"Why must equal keys have equal hashCodes?"**
> Otherwise equal keys could land in *different* buckets — the map would fail to find an entry it actually stored. The `equals`/`hashCode` contract is what keeps lookups correct.

## 🌍 Real Uses

In-memory caches · Fast id/email indexing · Counting & grouping (word count, dedup) · Salesforce `Map<Id, sObject>` bulk correlation

## 🔐 Security & Reliability

- **Hash-flooding DoS:** attacker-crafted colliding keys force worst-case O(n) buckets → use randomized/seeded hashing.
- Bound map size from untrusted input.
- Immutable keys + correct `equals`/`hashCode` → consistent, reliable lookups.
- Use concurrent maps for multi-threaded access.

## 📈 Scalability

The hash-bucket idea scales via **consistent hashing** into distributed key-value stores — Redis, DynamoDB, Cassandra — and database hash indexes, keeping O(1) keyed access across a cluster.

## 💻 Code (put / get / remove + grouping)

```python
# Python — dict
prices = {"apple": 5, "sky": 9}
prices["pear"] = 3          # put   O(1)
v = prices.get("apple")      # get   O(1) → 5
del prices["sky"]            # remove O(1)

counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1   # grouping / word count
```

```java
// Java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 5);
int v = map.getOrDefault("apple", 0);   // 5
```

```typescript
// TypeScript
const m = new Map<string, number>();
m.set("apple", 5);
const val = m.get("apple");             // 5
```

```apex
// Salesforce Apex — Map for O(1) correlation
Map<Id, Account> accById = new Map<Id, Account>(
    [SELECT Id, Name, Industry FROM Account LIMIT 200]);

for (Contact c : Trigger.new) {
    Account a = accById.get(c.AccountId);   // O(1) lookup, no query in loop
    if (a != null) c.Description = a.Industry;
}

// Word count (grouping)
Map<String, Integer> counts = new Map<String, Integer>();
for (String w : text.split(' ')) {
    counts.put(w, counts.containsKey(w) ? counts.get(w) + 1 : 1);
}
```

## 🔶 Salesforce Reality

- `Map<K,V>` **is** a hash map — central to **bulkification**.
- The `Map<Id, sObject>` constructor built directly from a SOQL result is the **#1 pattern** for O(1) record correlation.
  - Build: `new Map<Id, Account>([SELECT ...])`
  - Lookup: `accById.get(con.AccountId)` — O(1), zero queries in the loop
  - Group: `Map<Id, List<Child>>` for parent-to-children relationships
- **FDE tip:** Replacing a "query inside a loop" with a single query into a `Map<Id, sObject>` turns **O(n) SOQL calls into O(1) lookups** — the single most impactful optimization for governor-safe Apex.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/hashmap.apex --target-org fde-dev

# Python — benchmark dict vs list lookup
python -m timeit -s "d={i:i for i in range(100000)}" "99999 in d"   # O(1)
python -m timeit -s "a=list(range(100000))" "99999 in a"           # O(n)

# Java / TypeScript
javac MapDemo.java && java MapDemo
npx ts-node map.ts
```

---
### 🎯 Remember This
> **HashMap → "Give me the key, I'll jump straight to the value."**
> Average O(1) get/put. `equals` + `hashCode` together, always. Query-in-a-loop → Map-in-a-loop is the #1 Apex fix.
