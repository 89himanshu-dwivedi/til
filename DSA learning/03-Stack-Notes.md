# 🥞 STACK (LIFO) — Crisp Interview Notes

> **One-liner:** Last-In, First-Out — push/pop only at the **top**, both O(1). Powers function calls, undo, and backtracking.

```
   top → [15] (last in, first out)
         [10]
bottom → [ 5] (first in, last out)
```

## ⚡ Complexity Cheat Sheet

| Operation | Time | Note |
|---|---|---|
| `push(x)` | **O(1)** | add to top |
| `pop()` | **O(1)** | remove top |
| `peek()` | **O(1)** | read top, no removal |
| `isEmpty()` | O(1) | check size == 0 |
| search | O(n) | not its purpose |

## 🧠 Mental Model

```
push 5 → push 10 → push 15
                       ↓
pop() → returns 15 first   (LIFO)
```

**Call stack in action:**
```
push main frame
  push a() frame
    push b() frame
  b returns → pop b
a returns → pop a
main returns → pop main
```

## ⚠️ Rules & Traps

- Pop/peek on empty stack → **underflow** — always `isEmpty()` check first.
- Need FIFO instead? → use a **Queue**, not a stack.
- Never reach into the middle — push/pop/peek only.
- Unbounded growth (deep recursion) → **stack overflow** — prefer explicit stack over deep recursion.

## ✅ Best For / ❌ Avoid

| Best when | Avoid when |
|---|---|
| Naturally LIFO / nested problems | You need FIFO ordering |
| Undo-redo, bracket matching | You need random/middle access |
| DFS & backtracking | |

## 🎯 Interview Signal

> **Balanced brackets:** push opening brackets, pop & match on closing → empty at end = balanced. Classic stack problem.

## 🌍 Real Uses

Editors (undo/redo) · Compilers (expression parsing, bracket matching) · Language runtime (the call stack itself) · DFS & backtracking algorithms

## 🔐 Security & Reliability

- Bound recursion/stack depth on **untrusted input** (stack-exhaustion DoS).
- Validate before pop to avoid crashes.
- Test empty, single-element, and many-element sequences.

## 💻 Code (push / pop / peek + balanced brackets)

```python
# Python
stack = []
stack.append(5)      # push
stack.append(10)
top = stack[-1]       # peek → 10
stack.pop()           # pop  → 10 (LIFO)

def is_balanced(s: str) -> bool:
    st = []
    for ch in s:
        if ch == "(": st.append(ch)
        elif ch == ")":
            if not st: return False
            st.pop()
    return not st
```

```java
// Java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(5); stack.push(10);
int top = stack.peek();   // 10
stack.pop();              // 10
```

```typescript
// TypeScript
const stack: number[] = [];
stack.push(5); stack.push(10);
const top = stack[stack.length - 1]; // peek → 10
stack.pop();                          // 10
```

```apex
// Salesforce Apex — List as a stack
List<String> stack = new List<String>();
stack.add('(');                        // push
String top = stack[stack.size() - 1];  // peek
stack.remove(stack.size() - 1);        // pop

// Balanced brackets check
public static Boolean isBalanced(String s) {
    List<String> st = new List<String>();
    for (String ch : s.split('')) {
        if (ch == '(') st.add(ch);
        else if (ch == ')') {
            if (st.isEmpty()) return false;
            st.remove(st.size() - 1);
        }
    }
    return st.isEmpty();
}
```

## 🔶 Salesforce Reality

- No dedicated `Stack` class — use `List<T>`.
  - Push → `myList.add(x)`
  - Pop → `myList.remove(myList.size() - 1)`
  - Peek → `myList[myList.size() - 1]`
- Apex governor limits enforce a **real call-stack depth** (~1000 nested method calls).
- **FDE tip:** Use a List-as-stack for bracket/tag validation, or to flatten recursive hierarchy processing into an **iterative loop with an explicit stack** — avoids hitting Apex's max call-stack depth on deep record trees.

## ⚙️ Quick Setup

```bash
# Salesforce
sf apex run --file scripts/apex/stack.apex --target-org fde-dev

# Python / TypeScript
python stack.py
npx ts-node stack.ts
```

---
### 🎯 Remember This
> **Stack → "Last one in, first one out."**
> O(1) push/pop/peek. Underflow if empty. Use explicit stack over deep recursion.
