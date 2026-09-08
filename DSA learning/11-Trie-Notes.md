# 🔤 TRIE (Prefix Tree) — Crisp Interview Notes

> **One-liner:** A tree keyed by **characters** — words sharing a prefix share nodes. Lookup/prefix search = **O(L)**, proportional to word length, not word count. The engine behind autocomplete.

```
Insert "cat" then "car" (shared prefix "ca"):

root
 └─ c
     └─ a
         ├─ t (end-of-word) → "cat"
         └─ r (end-of-word) → "car"
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Note |
|---|---|---|
| `insert(word)` | **O(L)** | L = word length |
| `search(word)` | **O(L)** | independent of dictionary size |
| `startsWith(prefix)` | **O(L)** | prefix existence check |
| autocomplete | O(L + results) | walk to prefix node, then DFS subtree |

## 🧠 Mental Model

```
insert "car" after "cat" already exists:
  c → exists, reuse
  a → exists, reuse
  r → missing → create new child
  mark r as end-of-word

search(word):
  walk each char
  path exists AND last node is end-of-word? → found
  (path exists but NOT end-of-word → it's only a prefix, not a full word!)
```

## ⚠️ Rules & Traps

- **Must track an end-of-word flag** — don't infer word-completeness from "no children" (a word can be a prefix of another word, e.g. "car" and "card").
- Using a trie for **exact-match only** is overkill — a `HashSet` is simpler and smaller.
- Uncompressed tries waste memory on long unique suffixes — compress single-child chains into a **radix tree** for large dictionaries.
- Normalize case/Unicode **before** insert, or lookups silently fail / homoglyphs slip through.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Prefix search / autocomplete dominates | Only exact-match lookup needed (use HashSet) |
| Spell-check, dictionary validation | Alphabet is huge and words are short (memory overhead not worth it) |
| Longest-prefix match (IP/URL routing) | |

## 🎯 Interview Signal

> **"How does autocomplete work?"**
> Store words in a trie → walk to the prefix node (**O(L)**) → DFS its subtree to collect all completions.
> Cost to reach the prefix is independent of how many words are stored.

## 🌍 Real Uses

Autocomplete / typeahead · Spell-check & dictionary validation · Longest-prefix IP/URL routing · Search-as-you-type & inverted indexes (Elasticsearch-style)

## 🔐 Security & Reliability

- Bound word length/count from untrusted input (memory-exhaustion DoS).
- **Normalize Unicode** to prevent homoglyph tricks bypassing matches.
- Validate character sets before inserting.
- Test shared-prefix, empty-string, and single-char edge cases.

## 📈 Scalability

Tries scale into **radix trees** for routing tables, **suffix structures** for full-text search — conceptually behind every search-as-you-type feature and inverted index at scale.

## 💻 Code (insert / search / startsWith)

```python
# Python — trie via nested dicts
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True            # end-of-word marker
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node: return False
            node = node[ch]
        return "$" in node
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node: return False
            node = node[ch]
        return True                  # O(L)
```

```typescript
// TypeScript / LWC-style — client typeahead
class Trie {
  root: any = {};
  insert(w: string){ let n=this.root; for(const c of w) n=n[c] ??= {}; n.end=true; }
  startsWith(p: string){ let n=this.root; for(const c of p){ if(!n[c]) return false; n=n[c]; } return true; }
}
```

```apex
// Salesforce Apex — prefer SOSL/SOQL for search (no native trie)
List<Account> results = [SELECT Id, Name FROM Account WHERE Name LIKE 'car%'];
// Or SOSL across many objects:
// List<List<SObject>> s = [FIND 'car*' IN NAME FIELDS RETURNING Account(Id, Name)];
```

## 🔶 Salesforce Reality

- You **rarely build a trie in Apex.**
- Server-side prefix/typeahead search: **SOSL `FIND`** or **SOQL `LIKE 'car%'`** — indexed, server-side.
- Client-side instant suggestions: a **JS trie inside an LWC** for offline/no-round-trip typeahead.
- **FDE tip:** For typeahead in an LWC, cache a small dictionary and use a JS trie for instant, offline prefix matching; fall back to SOSL for the full dataset. Snappy UX, no server round-trip per keystroke.

## ⚙️ Quick Setup

```bash
# Python / TypeScript
python trie.py
npx ts-node trie.ts

# Salesforce
sf apex run --file scripts/apex/search.apex --target-org fde-dev
```

---
### 🎯 Remember This
> **Trie → "Shared prefixes, shared nodes — I search by word length, not word count."**
> O(L) insert/search/prefix. Must mark end-of-word explicitly. Salesforce: SOSL/LIKE server-side, JS trie client-side in LWC.
