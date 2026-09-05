# 🚶 QUEUE (FIFO) — Crisp Interview Notes

> **One-liner:** First-In, First-Out — add at the **rear**, remove from the **front**. Like a line at a counter. Both O(1) with the right backing store.

```
front → [4] [8] [15] ← rear
          ↓
  dequeue returns 4 first (FIFO)
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Note |
|---|---|---|
| `enqueue(x)` | **O(1)** | add rear |
| `dequeue()` | **O(1)*** | remove front |
| `peek()` | O(1) | read front, no removal |
| search | O(n) | not its purpose |

`*` O(1) only with a **linked list** or **circular array**. A naive plain-array front-removal is O(n) (shifting).

## 🧠 Mental Model

```
enqueue 4 → enqueue 8 → enqueue 15
                            ↓
dequeue() → returns 4 first   (opposite of Stack's LIFO)
```

**Producer/Consumer via queue:**
```
Producer → enqueue task1 → enqueue task2 → Queue
Consumer → dequeue → gets task1 first (FIFO)
```

## 🔀 Variants

| Variant | What's different |
|---|---|
| Deque | insert/remove at **both** ends |
| Circular queue | fixed buffer, wraps around — O(1) dequeue without shifting |
| Priority queue | order by **priority**, not arrival time |

## ⚠️ Rules & Traps

- Removing from front of a **plain array** → O(n) shift. Use linked list / circular array / `deque` instead.
- Need LIFO instead? → use a **Stack**, not a queue.
- Unbounded queue growth → OOM — always **bound size** for backpressure.
- Ignoring consumer failures → lost/stuck messages — use **dead-letter queues** + retries.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Fair, ordered (arrival-order) processing | You need LIFO / most-recent-first |
| Producer-consumer decoupling | Order should be priority-based (use priority queue) |
| BFS traversal | |

## 🎯 Interview Signal

> **Stack vs Queue?** Stack = LIFO. Queue = FIFO.
> **BFS uses a queue; DFS uses a stack.**

## 🌍 Real Uses

Job/print queues · Kafka / SQS / Pub-Sub message pipelines · BFS traversal · Salesforce Queueable/Batch async processing

## 🔐 Security & Reliability

- Bound size → prevent memory-exhaustion DoS.
- Validate/authorize enqueued work items.
- At-least-once delivery + **idempotent consumers**.
- Test empty, full, and interleaved enqueue/dequeue sequences.

## 📈 Scalability

The FIFO buffer concept scales into **distributed message queues** (Kafka, SQS, Pub/Sub) — decoupling microservices, smoothing load spikes, enabling event-driven architecture at massive scale.

## 💻 Code (enqueue / dequeue / peek)

```python
# Python — collections.deque (O(1) both ends)
from collections import deque
q = deque([4, 8])
q.append(15)      # enqueue rear  O(1)
front = q[0]      # peek → 4
q.popleft()       # dequeue front O(1) → 4
```

```java
// Java
Queue<Integer> q = new LinkedList<>();
q.offer(4); q.offer(8);
int f = q.peek();   // 4
q.poll();           // 4 (FIFO)
```

```typescript
// TypeScript (array as queue — O(n) shift, fine for small queues)
const q: number[] = [];
q.push(4); q.push(8);
const front = q[0]; // 4
q.shift();          // 4
```

```apex
// Salesforce Apex — List as a queue
List<Integer> queue = new List<Integer>();
queue.add(4);                 // enqueue
queue.add(8);
Integer front = queue[0];     // peek → 4
queue.remove(0);              // dequeue → 4 (FIFO)

// Real async queue on-platform
public class NotifyJob implements Queueable {
    public void execute(QueueableContext ctx) {
        // async work here
    }
}
// System.enqueueJob(new NotifyJob());
```

## 🔶 Salesforce Reality

- No dedicated `Queue` class — use `List<T>`.
  - Enqueue → `myList.add(x)`
  - Dequeue → `myList.remove(0)`
- The **platform itself is queue-driven**: Queueable Apex, Batch Apex, Platform Events all process work asynchronously in FIFO-ish order.
- **FDE tip:** For large async workloads, chain Queueable jobs or use Batch Apex — these are the platform's *real* queues, letting you process millions of records within governor limits, decoupled from the user transaction.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/queue.apex --target-org fde-dev

# Python / TypeScript
python queue_demo.py
npx ts-node queue.ts
```

---
### 🎯 Remember This
> **Queue → "First one in, first one out."**
> O(1) enqueue/dequeue (with linked list or circular array). BFS's best friend.
