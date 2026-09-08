# 🧠 DSA — Compact Problem-Solving Master Sheet
### Java · JavaScript · TypeScript · Python

> **Goal:** Question dekho → pattern pehchano → DS choose karo → solve karo → complexity bolo.
>
> For every DS: **Why → Where → Real life → Problem trigger → How to solve → Code → Complexity → Watch-outs**

---

## 📖 Topics

1. Array
2. Linked List
3. Stack
4. Queue
5. HashMap
6. HashSet
7. Tree
8. BST
9. Heap / Priority Queue
10. Trie
11. Graph

---

# 1. Array

### Why
**O(1) index access**. Most DSA problems start from arrays.

### Where / Real life
Ordered records, prices, scores, pixels, buffers, batch data.

### 🧩 Problem trigger
Think **Array** when you see:
- index / position / kth element
- subarray / contiguous
- in-place
- maximum / minimum
- sorted array
- sliding window / two pointers

### How to solve
```text
1. Is data sorted?
2. Contiguous range? → Sliding Window
3. Sorted + pair/range? → Two Pointers / Binary Search
4. Need fast lookup? → HashMap/Set
5. Need modify without extra space? → In-place / two pointers
```

### Core code

**Java**
```java
int[] a = {10,20,30};
int x = a[1];
```

**JS**
```js
const a = [10,20,30];
const x = a[1];
a.push(40);
```

**TS**
```ts
const a: number[] = [10,20,30];
const x = a[1];
```

**Python**
```python
a = [10,20,30]
x = a[1]
a.append(40)
```

**Complexity:** index O(1), search O(n), sort usually O(n log n)

**⚠️ Watch:** front/middle insertion can be O(n).

---

# 2. Linked List

### Why
Insert/delete at head or a **known node** can be O(1); no array shifting.

### Where / Real life
Playlist chains, browser history, undo chains, LRU-style structures.

### 🧩 Problem trigger
Think **Linked List** when you see:
- reverse list
- cycle
- middle node
- merge two sorted lists
- remove nth node
- `head`, `next`, `node`
- fast/slow pointer

### How to solve
```text
Reverse:
prev ← curr → next
save next → reverse curr.next → move forward

Cycle / middle:
slow = 1 step
fast = 2 steps

Nth from end:
move fast N steps → move slow + fast together
```

### Core Node

**Java**
```java
class Node {
    int val; Node next;
    Node(int v){ val=v; }
}
```

**JS**
```js
class Node {
  constructor(val, next=null) {
    this.val=val; this.next=next;
  }
}
```

**TS**
```ts
class Node {
  constructor(public val:number, public next:Node|null=null) {}
}
```

**Python**
```python
class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next
```

### Reverse pattern

**Java**
```java
Node prev=null, cur=head;
while(cur!=null){
    Node next=cur.next;
    cur.next=prev;
    prev=cur;
    cur=next;
}
head=prev;
```

**JS / TS**
```ts
let prev: Node|null=null, cur=head;
while(cur){
  const next=cur.next;
  cur.next=prev;
  prev=cur;
  cur=next;
}
head=prev;
```

**Python**
```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
head = prev
```

**Complexity:** traversal O(n), known-node insert/delete O(1)

**⚠️ Watch:** always save `next` before changing a pointer.

---

# 3. Stack — LIFO

### Why
**Last In → First Out**. Push/pop are O(1).

### Where / Real life
Ctrl+Z, browser back, function call stack, parsing.

### 🧩 Problem trigger
Think **Stack** for:
- valid parentheses
- nested structures
- undo/back
- next greater/smaller
- expression evaluation
- DFS / backtracking

### How to solve
```text
Latest item must resolve first?
        ↓
      STACK

Opening → push
Closing → pop + validate
DFS → push next nodes
```

### Core code

**Java**
```java
Deque<Integer> st = new ArrayDeque<>();
st.push(10);
int x = st.pop();
```

**JS**
```js
const st=[];
st.push(10);
const x=st.pop();
```

**TS**
```ts
const st:number[]=[];
st.push(10);
const x=st.pop()!;
```

**Python**
```python
st=[]
st.append(10)
x=st.pop()
```

**Complexity:** push/pop O(1)

**⚠️ Watch:** empty-stack pop must be handled.

---

# 4. Queue — FIFO

### Why
**First In → First Out**. Natural engine for BFS.

### Where / Real life
Job queues, print queues, support tickets, message/event processing.

### 🧩 Problem trigger
Think **Queue** for:
- BFS
- level-order traversal
- shortest path in an **unweighted** graph
- arrival order
- first-come-first-served processing

### How to solve
```text
start → enqueue
       ↓
dequeue front
       ↓
process
       ↓
enqueue next/unvisited
```

### Core code

**Java**
```java
Queue<Integer> q=new ArrayDeque<>();
q.offer(10);
int x=q.poll();
```

**JS**
```js
const q=[]; let head=0;
q.push(10);
const x=q[head++];
```

**TS**
```ts
const q:number[]=[]; let head=0;
q.push(10);
const x=q[head++];
```

**Python**
```python
from collections import deque
q=deque([10])
x=q.popleft()
```

**Complexity:** enqueue/dequeue O(1)

**⚠️ Watch:** for large JS/TS queues, prefer a head index over repeated `shift()`.

---

# 5. HashMap

### Why
**Key → Value**, average O(1) lookup. Often converts O(n²) into O(n).

### Where / Real life
Phonebook, cache, frequency counter, record correlation, `Id → Record`.

### 🧩 Problem trigger
Think **HashMap** for:
- frequency/count
- Two Sum
- pair lookup
- group by
- `already seen?` + need associated value
- fast ID → object lookup

### How to solve
```text
1. Decide KEY
2. Decide VALUE (count/index/object/etc.)
3. Loop once
4. Check map before/while inserting
5. Replace nested search with O(1)-average lookup
```

### Core code

**Java**
```java
Map<String,Integer> m=new HashMap<>();
m.put("A",10);
int x=m.getOrDefault("A",0);
```

**JS**
```js
const m=new Map();
m.set("A",10);
const x=m.get("A") ?? 0;
```

**TS**
```ts
const m=new Map<string,number>();
m.set("A",10);
const x=m.get("A") ?? 0;
```

**Python**
```python
m={"A":10}
x=m.get("A",0)
```

**Complexity:** average lookup/insert O(1)

**⚠️ Watch:** worst-case hashing can degrade; don't mutate key state in ways that break hashing semantics.

---

# 6. HashSet

### Why
Average O(1) **membership + uniqueness**.

### Where / Real life
Unique emails, unique visitors, visited records/nodes, duplicate prevention.

### 🧩 Problem trigger
Think **HashSet** for:
- duplicate
- unique
- distinct
- visited
- "does this exist?"
- only need **yes/no**, not a value

### How to solve
```text
for each x:
    if x already in Set → duplicate / visited
    else → add x
```

### Core code

**Java**
```java
Set<Integer> s=new HashSet<>();
s.add(10);
boolean ok=s.contains(10);
```

**JS**
```js
const s=new Set([10,20]);
const ok=s.has(10);
```

**TS**
```ts
const s=new Set<number>([10,20]);
const ok=s.has(10);
```

**Python**
```python
s={10,20}
ok=10 in s
```

**Complexity:** average add/contains/remove O(1)

**⚠️ Watch:** Set answers membership; Map stores an associated value.

---

# 7. Tree — Binary Tree

### Why
Natural model for **hierarchy**.

### Where / Real life
Folders, org charts, DOM, JSON/XML, parent-child records.

### 🧩 Problem trigger
Think **Tree** for:
- parent / child
- root / leaf
- subtree
- ancestor
- depth / height
- serialize / deserialize
- level-by-level hierarchy

### How to solve
```text
Need to go deep?        → DFS
Need level by level?    → BFS

Before coding:
1. Find root
2. Find children
3. Decide what each node contributes
4. Choose traversal
```

### Traversals
```text
Preorder  = Root → Left → Right
Inorder   = Left → Root → Right
Postorder = Left → Right → Root
Level     = BFS
```

### Core Node

**Java**
```java
class TNode{
    int val; TNode left,right;
    TNode(int v){val=v;}
}
```

**JS**
```js
class TNode{
  constructor(val){
    this.val=val; this.left=null; this.right=null;
  }
}
```

**TS**
```ts
class TNode{
  left:TNode|null=null;
  right:TNode|null=null;
  constructor(public val:number){}
}
```

**Python**
```python
class TNode:
    def __init__(self,val):
        self.val=val
        self.left=self.right=None
```

### DFS

**Java**
```java
void dfs(TNode n){
    if(n==null) return;
    dfs(n.left);
    dfs(n.right);
}
```

**JS / TS**
```ts
function dfs(n:TNode|null):void{
  if(!n) return;
  dfs(n.left);
  dfs(n.right);
}
```

**Python**
```python
def dfs(n):
    if not n: return
    dfs(n.left)
    dfs(n.right)
```

**Complexity:** visiting all nodes O(n)

**⚠️ Watch:** very deep trees can make recursion unsafe; iterative DFS may be better.

---

# 8. BST — Binary Search Tree

### Why
Ordered tree. Balanced BST gives O(log n) search/insert/delete.

### Rule
```text
Left < Root < Right
```

### Where / Real life
Ordered data structures and index concepts. In enterprise systems, prefer database/platform indexes rather than hand-building a BST.

### 🧩 Problem trigger
Think **BST** for:
- kth smallest/largest
- closest value
- range query
- validate BST
- sorted output without separately sorting
- search in an ordered tree

### How to solve
```text
target < node → LEFT
target > node → RIGHT
target == node → FOUND

Sorted output → INORDER
```

### Core search

**Java**
```java
Node cur=root;
while(cur!=null){
    if(cur.val==target) return cur;
    cur=target<cur.val ? cur.left : cur.right;
}
return null;
```

**JS**
```js
let cur=root;
while(cur){
  if(cur.val===target) return cur;
  cur=target<cur.val ? cur.left : cur.right;
}
return null;
```

**TS**
```ts
let cur=root;
while(cur){
  if(cur.val===target) return cur;
  cur=target<cur.val ? cur.left : cur.right;
}
return null;
```

**Python**
```python
cur=root
while cur:
    if cur.val==target: return cur
    cur=cur.left if target<cur.val else cur.right
return None
```

**Complexity:** balanced O(log n), skewed worst O(n)

**⚠️ Watch:** plain BST can become a linked list if inserted in bad order.

---

# 9. Heap / Priority Queue

### Why
Fast access to the **highest/lowest priority** item.

### Where / Real life
ER triage, task scheduler, priority tickets, Top-K, shortest path.

### 🧩 Problem trigger
Think **Heap** for:
- Top K
- kth largest/smallest
- min/max repeatedly
- highest priority
- merge K sorted lists
- median stream
- Dijkstra

### How to solve
```text
Repeated minimum → Min Heap
Repeated maximum → Max Heap
Largest K → Min Heap of size K
Smallest K → Max Heap of size K
Weighted shortest path → Min Heap
```

### Core code

**Java**
```java
PriorityQueue<Integer> pq=new PriorityQueue<>();
pq.offer(30);
pq.offer(10);
int min=pq.poll();
```

**Python**
```python
import heapq
h=[]
heapq.heappush(h,30)
heapq.heappush(h,10)
min_val=heapq.heappop(h)
```

**JS / TS**
```text
No native standard PriorityQueue.
Use a tested heap implementation/library when a real heap is required.
```

**Complexity:** peek O(1), insert/extract O(log n)

**⚠️ Watch:** Heap is NOT fully sorted; only the top priority is guaranteed.

---

# 10. Trie — Prefix Tree

### Why
Prefix operations in O(L), where **L = word/prefix length**.

### Where / Real life
Search autocomplete, IDE suggestions, spell-check, contact search.

### 🧩 Problem trigger
Think **Trie** for:
- prefix
- startsWith
- autocomplete
- dictionary search
- longest common prefix
- suggestions for typed characters

### How to solve
```text
Each character → node

insert("cat"):
c → a → t → END

startsWith("ca"):
c → a → exists? → yes

For suggestions:
prefix node → explore children
```

### Core structure

**Java**
```java
class TrieNode{
    Map<Character,TrieNode> child=new HashMap<>();
    boolean end;
}
```

**JS**
```js
class TrieNode{
  constructor(){
    this.child=new Map();
    this.end=false;
  }
}
```

**TS**
```ts
class TrieNode{
  child=new Map<string,TrieNode>();
  end=false;
}
```

**Python**
```python
class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
```

**Complexity:** insert/search O(L)

**⚠️ Watch:** mark END; `car` and `carpet` share a path but are different complete words.

---

# 11. Graph

### Why
Models **arbitrary relationships**, including cycles.

### Where / Real life
Social networks, maps, flights, dependencies, integrations, connected systems.

### 🧩 Problem trigger
Think **Graph** for:
- connections / network
- reach X from Y
- islands / regions
- shortest path
- dependency order
- cycles
- arbitrary node-to-node relationships

### How to solve
```text
Unweighted shortest path → BFS
Connectivity / exploration → DFS
Weighted shortest path → Dijkstra + Heap
Dependency ordering → Topological Sort
Components / connectivity → Union-Find
```

### Core BFS

**Java**
```java
Map<String,List<String>> g=new HashMap<>();
Queue<String> q=new ArrayDeque<>();
Set<String> seen=new HashSet<>();

q.offer("A");
seen.add("A");

while(!q.isEmpty()){
    String u=q.poll();
    for(String v:g.getOrDefault(u,List.of())){
        if(seen.add(v)) q.offer(v);
    }
}
```

**JS**
```js
const g={A:["B","D"],B:["A","C"]};
function bfs(start){
  const seen=new Set([start]);
  const q=[start]; let head=0;
  while(head<q.length){
    const u=q[head++];
    for(const v of g[u]||[]){
      if(!seen.has(v)){seen.add(v);q.push(v);}
    }
  }
}
```

**TS**
```ts
const g:Record<string,string[]>={A:["B","D"],B:["A","C"]};
function bfs(start:string){
  const seen=new Set([start]);
  const q:string[]=[start]; let head=0;
  while(head<q.length){
    const u=q[head++];
    for(const v of g[u]||[]){
      if(!seen.has(v)){seen.add(v);q.push(v);}
    }
  }
}
```

**Python**
```python
from collections import deque

def bfs(g,start):
    seen={start}
    q=deque([start])
    while q:
        u=q.popleft()
        for v in g.get(u,[]):
            if v not in seen:
                seen.add(v)
                q.append(v)
```

**Complexity:** BFS/DFS O(V+E)

**⚠️ Watch:** always use a `visited/seen` Set when cycles are possible.

> **Important:** Dijkstra is not simply BFS. BFS is for unweighted shortest paths; Dijkstra uses a min-priority queue for non-negative weighted edges.

---

# 🚀 Problem-Solving Decision Tree

```text
START
 |
 +-- index / contiguous / in-place? --------→ ARRAY
 |
 +-- head / next / reverse / cycle? --------→ LINKED LIST
 |
 +-- latest item first / nested / undo? ----→ STACK
 |
 +-- first come / level / BFS? -------------→ QUEUE
 |
 +-- key → value / count / pair lookup? ----→ HASHMAP
 |
 +-- unique / duplicate / visited? ---------→ HASHSET
 |
 +-- parent → child / hierarchy? -----------→ TREE
 |       |
 |       +-- ordered tree? ----------------→ BST
 |
 +-- min/max priority / Top-K? -------------→ HEAP
 |
 +-- prefix / autocomplete? ----------------→ TRIE
 |
 +-- arbitrary connections / cycles? -------→ GRAPH
```

---

# 🔥 5 Questions Before Writing Code

```text
1. INPUT?
   Size, type, sorted/unsorted, constraints?

2. OUTPUT?
   Number, boolean, index, list, node, path?

3. WHAT MUST I REMEMBER?
   Count? Index? Visited? Parent? Priority?

4. WHICH DS MAKES THAT FAST?
   Map / Set / Stack / Queue / Tree / Heap / Trie / Graph?

5. TIME + SPACE?
   Can brute force be improved?
```

---

# 🧩 Pattern → Data Structure

| Problem says... | Think... |
|---|---|
| duplicate / unique | HashSet |
| count frequency | HashMap |
| Two Sum / pair lookup | HashMap |
| contiguous subarray | Array + Sliding Window |
| sorted pair | Two Pointers |
| sorted search | Binary Search |
| reverse / cycle / middle | Linked List |
| brackets / nested / undo | Stack |
| level-by-level | Queue + BFS |
| hierarchy | Tree |
| ordered tree / kth smallest | BST |
| Top-K / priority | Heap |
| prefix / autocomplete | Trie |
| connections / reachability | Graph |
| weighted shortest path | Dijkstra + Heap |
| dependency order | Graph + Topological Sort |

---

# 🎯 One-Glance Complexity

| DS | Superpower | Typical |
|---|---|---:|
| Array | index access | O(1) |
| Linked List | known-node insert/delete | O(1) |
| Stack | push/pop | O(1) |
| Queue | enqueue/dequeue | O(1) |
| HashMap | key lookup | O(1) avg |
| HashSet | membership | O(1) avg |
| Tree | hierarchy/traversal | O(n) traversal |
| BST | ordered search | O(log n) balanced |
| Heap | top priority | O(1) peek |
| Trie | prefix search | O(L) |
| Graph | relationships | O(V+E) BFS/DFS |

---

# ☁️ Salesforce / Enterprise FDE Mapping

```text
Id → Record                 → HashMap
Unique record IDs           → HashSet
Account / Role hierarchy    → Tree
Arbitrary relationships     → Graph
Async job flow              → Queue
Priority processing         → Heap
Search autocomplete         → Trie
Ordered in-memory data      → Array/List
```

### Enterprise mental model

```text
SOQL once
   ↓
Map / Set
   ↓
Fast correlation
   ↓
Bulk processing
   ↓
Scalable solution
```

> **Golden rule:** Don't choose a DS because you know it.  
> Choose it because its **access pattern matches the problem**.
