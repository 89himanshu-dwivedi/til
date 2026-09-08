# ⛰️ HEAP (Priority Queue) — Crisp Interview Notes

> **One-liner:** A complete binary tree where every parent is smaller (min-heap) or larger (max-heap) than its children. **O(1) peek**, **O(log n) insert/extract** — the engine behind priority queues.

```
Min-heap (stored as array, but drawn as tree):

            5  (idx 0)
           /  \
        9      8      (idx 1, 2)
       /  \    /
     15   20  17       (idx 3, 4, 5)

parent(i) = (i-1)/2   left(i) = 2i+1   right(i) = 2i+2
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Note |
|---|---|---|
| `peek()` (min/max) | **O(1)** | always at index 0 |
| `insert(x)` | **O(log n)** | append + bubble up |
| `extract-min/max()` | **O(log n)** | root → last elem → sift down |
| `heapify(array)` | **O(n)** | build heap from scratch, faster than n inserts |

## 🧠 Mental Model

```
INSERT 1 (bubbles up):
  append 1 at end
  1 < parent? → swap up
  still smaller? → swap up again
  ...until heap property holds → new root = 1

EXTRACT-MIN:
  take root (the min)
  move LAST element to root
  sift DOWN: swap with smaller child until property holds
```

**Critical:** a heap is **only partially ordered** — root is guaranteed min/max, but the rest is NOT sorted. Don't assume left-to-right order.

## ⚠️ Rules & Traps

- **Not fully sorted** — only the root is guaranteed to be the extreme. Searching for an arbitrary value is O(n).
- Sorting a whole array just to repeatedly grab min/max = wasteful — use a heap instead.
- For **top-K**, keep a **bounded heap of size K** (push, pop if size > K) — don't let it grow unbounded.
- `heapify` an existing array in O(n) — don't do n individual inserts (that's O(n log n)).

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Always need the next highest/lowest priority item | You need to search for arbitrary values |
| Top-K problems | You need the whole thing sorted (just sort it) |
| Scheduling, Dijkstra, Prim, heap sort | Full ordering matters more than repeated extremes |

## 🎯 Interview Signal

> **"Find the K largest elements"** — keep a **min-heap of size K**; push each item, pop if size > K.
> Result: **O(n log K)** — much better than sorting the whole array (O(n log n)) when K is small.

## 🌍 Real Uses

Job/task priority scheduling · **Dijkstra's shortest path** & Prim's MST · Top-K / streaming percentiles · Event-driven simulation & timers · Heap sort (O(n log n) in-place)

## 🔐 Security & Reliability

- Bound heap size from untrusted input (memory-exhaustion DoS).
- Validate priorities to prevent **starvation** (low-priority items never processed).
- Guard against unbounded task floods.
- Test insert/extract interleavings and duplicate priorities.

## 📈 Scalability

Priority queues scale into **task schedulers**, **rate limiters**, and **event-driven simulation**; distributed systems use **partitioned queues** with per-partition heaps for scale.

## 💻 Code (insert / peek / extract + top-K)

```python
# Python — heapq (min-heap) & top-K
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 3)
heapq.heappush(h, 8)
print(h[0])              # peek min → 3    O(1)
print(heapq.heappop(h))  # extract min → 3  O(log n)

# K largest with a bounded min-heap
def k_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k: heapq.heappop(h)
    return sorted(h, reverse=True)
```

```java
// Java — PriorityQueue
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
minHeap.add(5); minHeap.add(3); minHeap.add(8);
int min = minHeap.peek();   // 3  O(1)
minHeap.poll();             // 3  O(log n)

// max-heap: new PriorityQueue<>(Collections.reverseOrder())
```

```apex
// Salesforce Apex — sort for small priority needs (no native heap)
List<Integer> scores = new List<Integer>{ 5, 3, 8, 1 };
scores.sort();                 // ascending
Integer smallest = scores[0];  // 1
// For scale, prefer SOQL ORDER BY ... LIMIT k
```

## 🔶 Salesforce Reality

- **No native Heap/PriorityQueue in Apex.**
- Small top-K needs: sort a `List` (implement `Comparable` for custom priority).
- Scalable priority processing: let the **database rank** with `ORDER BY ... LIMIT k`, or orchestrate priority via async queues (Queueable / Flow / Platform Events).
- **FDE tip:** For "top 10 opportunities by amount," don't load everything and sort in Apex — use `ORDER BY Amount DESC LIMIT 10`. The platform's indexed ranking **is** your heap at database scale.

## ⚙️ Quick Setup

```bash
# Python
python -c "import heapq; h=[]; [heapq.heappush(h,x) for x in (5,3,8)]; print(heapq.heappop(h))"

# Java / Salesforce
javac HeapDemo.java && java HeapDemo
sf apex run --file scripts/apex/heap.apex --target-org fde-dev
```

---
### 🎯 Remember This
> **Heap → "I always know the min/max instantly, and I can update it in log(n)."**
> O(1) peek, O(log n) insert/extract, O(n) heapify. Only the root is guaranteed extreme — not fully sorted. Bounded heap = top-K's best friend.
