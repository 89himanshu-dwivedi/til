# Backend Engineering Roadmap — Backend × AI × Salesforce

> **A practical roadmap for becoming a production-ready backend engineer in 2026.**

This repository connects **backend engineering, AI engineering, and Salesforce development** through the same core engineering concepts.

## 🗺️ Roadmap

- [01. Computer Science Foundations](#01-computer-science-foundations--base)
- [02. Programming Fundamentals](#02-programming-fundamentals--base)
- [03. Choose a Backend Language](#03-choose-a-backend-language--decision)
- [04. Web & HTTP](#04-web--http--core)
- [05. API Engineering](#05-api-engineering--core)
- [06. Databases](#06-databases--core)

## 🎯 How to Use This Roadmap

For every topic, focus on:

- **What it is**
- **Why it matters**
- **Where it is used**
- **Role in AI**
- **Role in Salesforce**

The goal is not to memorize syntax. The goal is to understand **why systems are designed the way they are and how to build, debug, secure, and scale them in production.**

---

## 🧭 Big Picture — The Entire Roadmap at a Glance

**How to read this document:** Every topic is presented as a card with 5 things — **What it is** (definition) · **Why it matters** (problem jo ye solve karta hai) · **Where it is used** (real scenarios) · **Role in AI** (LLM / RAG / agents me ye concept kahan lagta hai) · **Role in Salesforce** (Apex, governor limits, platform equivalent). This connects the same concept across three worlds — backend, AI, and Salesforce.

Ye roadmap 4 badi layers me tuta hua hai. First build the **foundation**, then learn to **build**, then **secure + scale** it, and finally **prove** your skills through **projects**.

```
flowchart TD
    A["LAYER 1 - FOUNDATION
CS Basics + Programming + Language"] --> B["LAYER 2 - BUILD
HTTP + APIs + DB + Data Access"]
    B --> C["LAYER 3 - HARDEN
Auth + Architecture + Caching + Async + Realtime + Files + Testing"]
    C --> D["LAYER 4 - RUN AT SCALE
DevOps + Observability + Scalability + Reliability"]
    D --> E["LAYER 5 - PROVE
System Design + 11 Production Projects"]

    A -->|"01, 02, 03"| A1["Think and write code"]
    B -->|"04 to 07"| B1["Working backend"]
    C -->|"08 to 14"| C1["Safe, fast, tested backend"]
    D -->|"15 to 18"| D1["Backend that survives in production"]
    E -->|"19, 20"| E1["Job/interview-ready engineer"]
  
```

**Analogy:** Becoming a backend engineer = opening a restaurant.
01–03 = learn the cooking basics. 04–07 = set up the kitchen + menu. 08–14 = hygiene, safety, and quality checks. 15–18 = daily operations, monitoring, and backup systems. 19–20 = handle 500 customers at the same time.

| StageKya milta haiApproximate role level |                                   |                        |
|---|---|---|
| 01–03                                       | Programming + understanding the machine      | Student / Intern       |
| 04–07                                       | CRUD API + DB                     | Junior Backend Developer     |
| 08–14                                       | Secure, structured, tested system | Mid-level Developer          |
| 15–18                                       | Deploy, monitor, scale, recover   | Senior Developer / SRE-ish   |
| 19–20                                       | Design trade-offs + portfolio     | Lead / Architect track |

## 01. Computer Science Foundations — Base

**English:** This is the layer where you understand how the machine actually works. Without it, you may be able to "write code" but struggle to "debug" it — because when the CPU hits 100% or there is a memory leak, framework documentation alone will not save you.

### Sub-topics — In Detail

#### 1. How Computers Work

**What it is:** CPU ek loop chalata hai — instruction **fetch** karo, **decode** karo, **execute** karo. Data RAM se aata hai. Disk aur network bahut slow hain.

**Speed reality check:** CPU register \~1 ns · L1 cache \~1 ns · RAM \~100 ns · SSD \~100 microsec (1000x slow) · Network same-region \~0.5 ms · Cross-continent \~150 ms (RAM se 15 lakh guna slow!).

**Why it matters:** Many performance problems can be traced back to this hierarchy. "API slow hai" ka 90% answer = "hum bahut zyada disk ya network hit kar rahe hain".

**Where it is used:** When optimizing queries, deciding whether to cache, and deciding where caching is worthwhile.
**AI me role:** LLM inference me GPU VRAM sabse bada bottleneck hai. 7B model \~14 GB VRAM mangta hai. Isliye **quantization** (FP16 → INT4) karte hain — memory 4x kam. RAG me embeddings RAM me rakhte hain, disk but no, warna search 100x slow.
**Salesforce me role:** Governor limits isi wajah se hain — Salesforce multi-tenant hai, ek hi hardware but hazaron org. Heap size limit (6 MB sync / 12 MB async) seedha RAM ka concept hai. CPU time limit 10 sec sync — matlab aapka Apex CPU cycles waste no kar sakta.

#### 2. Operating Systems

**What it is:** OS = hardware aur aapke program ke beech ka manager. Kaun CPU kab paayega (scheduling), kis process ko kitni memory milegi, file/network access kaun kar sakta hai — sab OS decide karta hai.

**Core concepts:** Kernel vs User space · System calls (aapka code `read()` bolta hai, kernel karta hai) · Context switching (CPU ek process se dusre but jump, \~1-5 microsec ka kharcha) · Signals (SIGTERM = shutdown ho ja).

**Why it matters:** Production me server but debug aap hi karoge. `top`, `htop`, `ps`, `strace` tabhi samajh aayenge.

**Where it is used:** Docker container tuning · Kubernetes me CPU/memory limits set karna · OOM Killer ne process kyun mara ye samajhna · Graceful shutdown (SIGTERM handle karna).
**AI me role:** Model training me GPU scheduling, CUDA drivers, shared memory. Ollama/vLLM chalate waqt "not enough memory" errors OS-level hi hote hain.
**Salesforce me role:** Not directly (the Salesforce platform is managed), **but** when you Heroku/AWS but middleware banate ho jo SF se integrate karta hai — there, strong OS knowledge is required. MuleSoft on-prem runtime bhi Linux tuning maangta hai.

#### 3. Processes & Threads

**What it is:** **Process** = apna alag ghar, apni alag memory. Ek gire to dusre but asar no. **Thread** = people living in the same house — memory share karte hain, isliye fast baat-cheet but jhagda (race condition) bhi hota hai.

**Problems that originate here:** Race condition (do thread ek hi variable badal rahe) · Deadlock (A ne X pakda B ka wait, B ne Y pakda A ka wait) · Thread pool exhaustion (sab threads block, naya request lene wala koi no).

**Why it matters:** "Kabhi-kabhi invalid data save hota hai" jaisi ghost bugs yahin se aati hain — aur ye reproduce karna sabse mushkil hota hai.

**Where it is used:** Web server kitne butallel requests le sakta hai (Node = 1 thread + event loop, Java Tomcat = 200 threads) · Background workers · Inventory decrement jaise concurrent updates.
**AI me role:** Data loading me multiprocessing (Python ka GIL threads ko CPU-butallel no hone deta, isliye `multiprocessing` use karte hain) · Batch inference me butallel requests · Vector DB indexing multi-threaded hoti hai.
**Salesforce me role:** **Bahut zyada.** Two users same record edit karein = record locking / `UNABLE_TO_LOCK_ROW` error. Isliye Apex me `FOR UPDATE` use karte hain. Batch Apex ke butallel chunks ek hi butent record update karein to lock contention hota hai — isliye batch size chhota ya `Database.Stateful` + sorting. Platform Events aur Queueable chains bhi concurrency hi hain.

#### 4. Memory Management

**What it is:** **Stack** = function calls aur chhote local variables, automatic saaf ho jata hai, bahut fast. **Heap** = bade/dynamic objects, manually ya garbage collector se saaf hota hai.

**Memory leak:** Object ab zarurat no but reference abhi bhi pakda hua hai, isliye GC use hata no sakta. RAM gradually fills up → the server crashes. Classic example: global array jisme entries add hoti rehti hain, kabhi remove no hoti.

**Why it matters:** "Server har 3 din baad restart karna padta hai" ka exact reason yahi hota hai. Ye senior-level debugging skill hai.

**Where it is used:** Node.js heap snapshot lena · JVM heap tuning (`-Xmx`) · Kubernetes memory limits + OOMKilled debug · Cache me unbounded growth rokna (LRU + max size).
**AI me role:** **Sabse critical.** LLM ka poora model RAM/VRAM me load hota hai. Batch size badhaya → OOM. RAG me 10 lakh embeddings × 1536 dims × 4 bytes = \~6 GB RAM. Isliye vector DB (FAISS/Pinecone) use hoti hai, plain Python list no. LangChain me conversation memory unbounded chhod do → context aur RAM dono blast.
**Salesforce me role:** **Heap Size Limit** — 6 MB (sync) / 12 MB (async). 50,000 records ek List me query kiye = heap blast. Solution: `Database.QueryLocator` + Batch Apex, ya SOQL `for` loop jo chunks me records deta hai. Ye literally memory management hi hai.

#### 5. Filesystems

**What it is:** A system for organizing files. Path, permissions (`rwx` / `chmod 644`), inode (file ka metadata), file descriptor (open file ka number).

**Common production errors:** `EMFILE: too many open files` (file descriptors khatam — aksar connections close no kiye) · `ENOSPC: no space left` (aksar logs ne disk bhar di) · Permission denied.

**Why it matters:** Logs, uploads, temp files, config — sab filesystem but. Aur container me filesystem **ephemeral** hota hai (restart but gayab).

**Where it is used:** Log rotation setup · Docker volumes vs bind mounts · Uploaded files ko disk but na rakhna (S3 use karna) · `.env` file permissions.
**AI me role:** Model weights disk but gigabytes me hote hain (Llama 70B \~140 GB). Hugging Face cache `~/.cache/huggingface` disk bhar deta hai. Document ingestion pipeline me PDFs read/write karna. Fine-tuning checkpoints har epoch save = disk full.
**Salesforce me role:** Direct filesystem no milta, but concept same hai — **Files/ContentVersion** object, Attachment, aur Static Resources. Storage limits (Data storage vs File storage) exactly disk quota hi hain. Large file upload ke liye `ContentVersion` ko chunks me daalte hain (Base64 heap limit ki wajah se).

#### 6. Networking Fundamentals

**What it is:** Data is split into packets and sent to an IP address + port. TCP reliable delivery karta hai (lost packet dobara), UDP fast but best-effort. Latency = ek round trip ka time.

**Essential concepts:** IP + Port · TCP 3-way handshake · DNS resolution · TLS handshake (extra round trips) · Bandwidth vs Latency (bandwidth = pipe ki motai, latency = doori) · Firewall / Security Group.

**Why it matters:** A large part of backend time is spent waiting on the network — DB call, API call, cache call. Latency samjhe bina system design impossible hai.

**Where it is used:** Timeout set karna · Retry logic · Same-region me DB aur app rakhna (cross-region = 100 ms extra per query) · Connection reuse (keep-alive) · VPC/subnet design.
**AI me role:** LLM API calls network-bound hain (OpenAI call \~1-5 sec). Isliye **streaming** use karte hain — user ko turant pehla token dikh jaye. Timeout + retry + exponential backoff har LLM client me zaroori hai (429/503 aam baat hai). Agent loops me 10 API calls = 10x latency, isliye butallel calls karte hain.
**Salesforce me role:** **Callout limits** — 100 callouts per transaction, max 120 sec total, per-callout timeout default 10 sec (`req.setTimeout()`). Named Credentials, Remote Site Settings, mTLS certificates — sab networking hai. Integration design me "kitne callouts, kitna payload" hi asli constraint hai.

#### 7. Data Structures

**What it is:** A way to organize data in memory so operations become efficient.

| StructureStrengthWhere it is used in backend |                                 |                                                               |
| --------------------------------- | ------------------------------- | ------------------------------------------------------------- |
| Array / List | O(1) index access, order maintained | Query results, ordered lists |
| HashMap / Dictionary | O(1) key lookup | Caching, deduplication, lookup tables — **used extremely often** |
| Set | Uniqueness + O(1) contains | Remove duplicates, permission checks |
| Queue / Deque | FIFO | Job queues, BFS, rate-limiter windows |
| Stack                             | LIFO                            | Undo, call stack, expression butsing                          |
| Tree (B-Tree) | Sorted + range queries | **DB indexes are B-Trees internally** |
| Heap / Priority Queue | Get smallest/largest efficiently | Top-N, priority job scheduling |
| Graph | Relationships | Social networks, dependencies, routing |

**Why it matters:** The wrong data structure can lead to O(n²) code. 1000 items but nested loop = 10 lakh operations. HashMap use karo = 1000 operations.
**AI me role:** **Vector** ek array hi hai (1536 floats). Similarity search ke liye special structures — HNSW graph, IVF index (FAISS me). Token vocabulary ek HashMap hai. Attention mechanism matrices (2D arrays) hi hain. Graph structures knowledge graphs aur agent planning me.
**Salesforce me role:** **Map\<Id, SObject> Apex ka sabse important pattern hai.** Trigger me har record ke liye SOQL karna = governor limit blast. Iski jagah ek query karo, Map me daalo, loop me Map se lookup karo. `Set<Id>` se duplicate IDs hatao. Ye seedha HashMap/Set knowledge hai.

#### 8. Algorithms

**What it is:** A step-by-step way to solve a problem + a measurement of its efficiency (Big-O).

**Big-O quick reference:** O(1) constant (HashMap lookup) · O(log n) (binary search, B-Tree index) · O(n) (ek loop) · O(n log n) (sorting) · O(n²) (nested loop — **red flag**) · O(2ⁿ) (avoid).

**Why it matters:** Interview me to hai hi, but production me bhi — 100 records but nested loop chalti hai, 1 lakh but server tp deta hai.

**Where it is used:** Data processing pipelines · Sorting/filtering large datasets · Deduplication · Pagination logic · Search implementation · Matching algorithms (ride-sharing, recommendations).
**AI me role:** Cosine similarity, ANN (Approximate Nearest Neighbour) search, chunking strategies, re-ranking algorithms, beam search — sab algorithms hain. RAG me "top-k retrieval" ek heap/sorting problem hai. Agent planning me graph traversal (BFS/DFS) hoti hai.
**Salesforce me role:** Bulkified Apex likhna hi algorithm optimization hai — nested loop over 200 records with SOQL inside = `Too many SOQL queries: 101`. Sharing recalculation, territory assignment, duplicate matching rules — sab andar se algorithms hain. Interview me "trigger ko bulkify kaise karoge" = Big-O ka hi sawal hai.

```
flowchart LR
    U["Aapka Code"] --> R["Runtime / VM"]
    R --> OS["Operating System"]
    OS --> CPU["CPU"]
    OS --> MEM["RAM"]
    OS --> DISK["Disk / Filesystem"]
    OS --> NET["Network Card"]
    CPU -->|"fast - nanoseconds"| MEM
    MEM -->|"slow - microseconds"| DISK
    DISK -->|"slowest - milliseconds"| NET
  
```

**Practical tip:** Big-O rat-ne se pehle ye samjho — `HashMap` lookup O(1) hai isliye 1 lakh records me search 1 step me ho jati hai, jabki list me 1 lakh steps lagte hain. Yehi difference API ko 2s se 20ms banata hai.

## 02. Programming Fundamentals — Base

**English:** Regardless of the language, these 9 concepts are broadly the same everywhere. Once you understand them, picking up a new language becomes much easier.

#### 1. Variables & Data Types

**What it is:** Giving data a name and defining its type — int, string, boolean, list, map, object.

**Why it matters:** Type ki galti sabse common bug hai. `"5" + 5` JS me `"55"` deta hai. Money ko `float` me rakhoge to `0.1 + 0.2 = 0.30000000000000004` — isliye paisa hamesha `decimal` ya integer paise me.

**Where it is used:** Everywhere. API request/response contracts, DB column types, TypeScript interfaces.
**AI me role:** Embedding = `float[]`. Token = integer. Model output butse karke structured type me convert karna (JSON mode / Pydantic schema) — yahi "structured output" hai.
**Salesforce me role:** Apex strongly-typed hai. `Decimal` for currency (kabhi `Double` no), `Id` ek special 18-char type hai, `SObject` generic type. Field type mismatch = deployment error.

#### 2. Control Flow

**What it is:** `if/else`, `switch`, `for`, `while` — program ka decision aur repetition.

**Why it matters:** Business logic is built from these constructs. Par nested `if` ka 5-level pyramid = unreadable code. **Guard clause** pattern seekho — invalid case pehle return kar do.

**Where it is used:** Validation, authorization checks, state machines, retry loops.
**AI me role:** Agent ka poora "reasoning loop" ek while-loop hai: soch → tool call → result dekho → phir socho → jab tak answer na mile. LangGraph me conditional edges literally if/else hain.
**Salesforce me role:** Apex triggers me `Trigger.isInsert / isUpdate / isBefore` ka control flow. Flow Builder GUI me yahi decision elements hain. Validation Rules ek boolean expression hi hain.

#### 3. Functions

**What it is:** A reusable block — give it input and get an output. Pure function = same input but hamesha same output, koi side effect no.

**Why it matters:** DRY (Don't Repeat Yourself). Ek jagah fix = sab jagah fix. Chhoti functions testable hoti hain, badi 200-line function no.

**Where it is used:** Service methods, utility helpers, middleware, validators.
**AI me role:** **Function/Tool calling** — LLM ko aap functions ka description dete ho, wo decide karta hai kaunsa call karna hai. Isliye function ka naam + description + butameter schema clear likhna AI apps me literally prompt engineering hai.
**Salesforce me role:** Apex methods, `@InvocableMethod` (Flow se callable), `@AuraEnabled` (LWC se callable). **Agentforce me** Apex Invocable actions hi wo "tools" hain jinhe AI agent call karta hai — exactly function calling.

#### 4. Error Handling

**What it is:** `try/catch/finally`, custom exceptions, error propagation. Crash hone ki jagah gracefully sambhalna.

**Why it matters:** In production, everything eventually fails. **Golden rule:** never swallow an exception you cannot actually handle (`catch(e) {}` = crime). Log karo, context ke saath rethrow karo, aur user ko safe message do (stack trace kabhi no — security risk).

**Where it is used:** External API calls, DB operations, file I/O, butsing user input.
**AI me role:** LLM ka output **bharosa layak no** hota — JSON maanga tha, markdown aa gaya. Isliye butse ko try/catch me rakho + retry with corrective prompt. Rate limit (429), context length exceeded, content filter — ye sab handle karne padte hain.
**Salesforce me role:** `try/catch` + `Database.SaveResult` (buttial success — 200 me se 3 fail hue to baaki 197 save ho jayein). `addError()` on trigger records. Platform me unhandled exception = poora transaction rollback + user ko ugly error page.

#### 5. Modules & Packages

**What it is:** Code ko files/folders me todna, aur dusron ka code import karna (npm, pip, Maven).

**Why it matters:** 5000-line ek file = maintenance nightmare. Aur **dependency management** ek security issue bhi hai — lockfile commit karo, `npm audit` chalao, transitive dependencies se supply-chain attack hota hai.

**Where it is used:** Project structure, shared libraries, monorepo setup.
**AI me role:** LangChain, LlamaIndex, transformers — sab packages hain. Version pinning yahan aur bhi zaroori hai kyunki AI libraries hafte-hafte breaking changes deti hain.
**Salesforce me role:** **Unlocked Packages / 2GP** — modular deployment ka SF version. Namespaces, package dependencies, SFDX project structure. Ek bade org ko independently deployable packages me todna hi modern SF architecture hai.

#### 6. Object-Oriented Programming (OOP)

**What it is:** 4 pillars — **Encapsulation** (data private, access methods se), **Abstraction** (details chhupao), **Inheritance** (butent se properties), **Polymorphism** (ek interface, kai implementations).

**Why it matters:** A standard way to organize a large codebase. **Interface** sabse powerful hai — concrete class but depend karne ki jagah interface but depend karo, phir implementation swap kar sakte ho (testing, vendor change).

**Where it is used:** Service classes, repository pattern, strategy pattern (PaymentGateway interface → Razorpay/Stripe implementations).
**AI me role:** LangChain ka poora design OOP hai — `BaseLLM`, `BaseRetriever`, `BaseMemory` interfaces. Isliye OpenAI se Anthropic but switch karna ek line ka kaam hai.
**Salesforce me role:** Apex fully OOP hai — `interface`, `virtual`, `abstract`, `extends`, `implements`. **Trigger Handler pattern** (ek interface, har object ka apna handler) SF ka #1 architecture pattern hai. `Queueable`, `Batchable`, `Schedulable` — sab interfaces hain jo aap implement karte ho.

#### 7. Functional Programming

**What it is:** `map`, `filter`, `reduce`, pure functions, immutability (data badalne ki jagah naya banao).

**Why it matters:** Immutable data = kam bugs, kyunki koi chupke se aapka object badal no sakta. Pure functions test karna trivial hai — mocking hi no chahiye.

**Where it is used:** Data transformation pipelines, React/LWC state, stream processing.
**AI me role:** **LangChain Expression Language (LCEL)** poora functional composition hai: `prompt | model | butser` — pipeline banate ho, har step pure transformation. Data preprocessing (clean → chunk → embed) bhi map/filter chain hi hai.
**Salesforce me role:** Apex me FP support limited hai (no lambdas till recently), but concept lagta hai — collection ko transform karna, side-effect free helper methods likhna. LWC (JavaScript) me `map/filter/reduce` daily use hota hai, aur reactive properties immutability but depend karti hain (array mutate karoge to re-render no hoga — classic LWC bug).

#### 8. Concurrency

**What it is:** Ek time but kai kaam. Do models — **threads** (butallel execution) aur **async/event loop** (ek thread, but waiting time me dusra kaam).

**Why it matters:** Backend ka kaam mostly **waiting** hai (DB, API, disk). Async se ek server 10,000 concurrent connections handle kar leta hai. Blocking code likhoge to 100 but hi atak jaoge.

**Where it is used:** Parallel API calls (`Promise.all`), background jobs, WebSocket servers, batch processing.
**AI me role:** **Bahut critical.** Ek LLM call 3 sec leti hai. 10 documents summarize karne hain — sequentially 30 sec, butallel me 3 sec. RAG me retrieval + web search butallel chalao. Streaming responses async generators hain. Agent me multiple tools butallel call karna.
**Salesforce me role:** `Queueable` (chaining, ek time 50 tak), `@future` (fire and forget), `Batch Apex` (butallel chunks, default 5 concurrent), `Platform Events` (async pub-sub). Concurrent request limit 10 (long-running sync transactions). Record locking bhi concurrency ka hi issue hai.

#### 9. Testing

**What it is:** Verifying code with code. AAA pattern — **Arrange** (setup), **Act** (chalao), **Assert** (check karo).

**Why it matters:** The biggest benefit is not just catching bugs — it is being able to **refactor without fear**. Bina tests wala codebase change karna land mine field me chalna hai.

**Where it is used:** Har service method, har API endpoint, har edge case (null, empty, boundary).
**AI me role:** Yahan testing alag hai — output non-deterministic hai. Isliye **evals** use karte hain: golden dataset banao, LLM-as-judge lagao, metrics track karo (faithfulness, relevance, hallucination rate). Regression prompt change ke baad zaroor chalao.
**Salesforce me role:** **Mandatory** — production deploy ke liye 75% code coverage chahiye. `@isTest` classes, `Test.startTest()/stopTest()` (fresh governor limits), `@TestSetup`, `Test.setMock()` for callouts. Coverage number chase mat karo — assertions likho, warna test bekar hai.

```
flowchart TD
    S["Start"] --> V["Variables - data rakho"]
    V --> C["Control Flow - decide karo"]
    C --> F["Functions - reuse karo"]
    F --> E["Error Handling - girne se bacho"]
    E --> M["Modules - organize karo"]
    M --> O["OOP + FP - design karo"]
    O --> CN["Concurrency - butallel chalao"]
    CN --> T["Testing - prove karo ki chalta hai"]
  
```

**Analogy:** Variables = dabbe, Functions = recipe, Error handling = fire extinguisher, Modules = kitchen ke alag shelf, Concurrency = 4 burner ek saath, Testing = khud chakh ke dekhna serve karne se pehle.

## 03. Choose a Backend Language — Decision

**Hinglish:** The biggest mistake here is learning three languages superficially without becoming deep in any of them. **Ek language chuno, 1–2 saal usme deep jao.** Baad me switch karna easy hai.

| LanguageFrameworkWhen to chooseJob market (India) |                          |                                                 |                          |
|---|---|---|---|
| JavaScript                                   | Node.js / Express        | You already know frontend and want to join a startup | Very high               |
| TypeScript                                   | Node.js / NestJS         | You want JS + type safety and modern teams                  | Very high, growing |
| Python                                       | Django / FastAPI / Flask | AI/ML, data, and fast prototyping                   | High                     |
| Java                                         | Spring Boot              | Enterprise, banking, and large product companies         | Highest in enterprise    |
| Go                                           | Gin / Fiber / net-http   | Infrastructure, high concurrency, and microservices          | Medium but high pay      |
| C#                                           | ASP.NET Core             | Microsoft stack and enterprise                     | Medium                   |
| PHP                                          | Laravel                  | Agency work, CMS, and fast delivery                 | Medium, legacy-heavy     |
| Rust                                         | Axum / Actix             | Performance-critical and systems work                   | Low volume, very high pay |

```
flowchart TD
    Q1{"What is your background?"}
    Q1 -->|"I know frontend"| TS["TypeScript + Node.js"]
    Q1 -->|"I want to work in AI/ML or Data"| PY["Python + FastAPI"]
    Q1 -->|"I want an enterprise/banking job"| JV["Java + Spring Boot"]
    Q1 -->|"I like Infra/DevOps"| GO["Go + Gin"]
    Q1 -->|"I am completely new"| PY2["Python - easiest start"]

    TS --> DEEP["Go deep in one language for 1–2 years"]
    PY --> DEEP
    JV --> DEEP
    GO --> DEEP
    PY2 --> DEEP
  
```

**Avoid this mistake:** "Sabhi language ka syntax" seekhna useless hai. Companies hire you not just for a language, but for your ability to **solve problems**.

## 04. Web & HTTP — Core

**Hinglish:** A backend essentially receives requests, does the work, and returns responses. Wo request HTTP but aati hai. That is why understanding HTTP is not optional.

### Ek URL type karne but kya hota hai

```
sequenceDiagram
    butticipant B as Browser
    butticipant D as DNS Server
    butticipant S as Your Server
    butticipant DB as Database

    B->>D: "api.myapp.com ka IP kya hai?"
    D-->>B: "13.234.x.x"
    B->>S: TCP connect (3-way handshake)
    B->>S: TLS handshake (HTTPS - certificate)
    B->>S: GET /orders/123  + headers + cookie
    S->>DB: SELECT * FROM orders WHERE id=123
    DB-->>S: row
    S-->>B: 200 OK + JSON body
  
```

### Key Concepts — In Detail

#### 1. Client ↔ Server Model

**What it is:** The client sends a request and the server returns a response. HTTP **stateless** hai — the server does not inherently remember who sent the previous request. Each request should contain the information needed to process it.

**Why it matters:** Statelessness hi wajah hai ki cookies/tokens chahiye, aur yahi wajah hai ki backend horizontally scale ho pata hai.

**AI me role:** LLM API bhi stateless hai — model ko pichli baat yaad no. Isliye har request me **poori conversation history** dobara bhejni padti hai. Yahi wajah hai ki lambi chat mehngi hoti hai aur context window bhar jata hai. "Memory" ek illusion hai jo aap khud manage karte ho.
**Salesforce me role:** Apex REST/SOAP services, Connected Apps, Experience Cloud — sab client-server. Salesforce khud client banta hai jab callout karta hai, aur server banta hai jab external system usse call karta hai.

#### 2. DNS (Domain Name System)

**What it is:** Name → IP translation. `api.myapp.com` → `13.234.5.6`. Records include: A (IPv4), CNAME (alias), MX (mail), TXT (verification).

**Why it matters:** Because of TTL, a DNS change does not take effect everywhere immediately — propagation me minutes/hours. Deploy planning me ye matter karta hai.

**Where it is used:** Custom domain setup · Blue-green switch · Global load balancing (geo-based DNS) · Service discovery (Kubernetes internal DNS).
**AI me role:** Self-hosted model endpoints ko DNS ke peeche rakhna, taki model version change karo to client ka URL na badle.
**Salesforce me role:** My Domain (`mycompany.my.salesforce.com`) mandatory hai — LWC, SSO aur Lightning ke liye. Experience Cloud custom domain + CNAME setup. Remote Site Settings me hostname whitelist karna.

#### 3. TCP/IP

**What it is:** TCP provides reliable, ordered delivery — 3-way handshake (SYN → SYN-ACK → ACK) se connection banta hai, lost packets are retransmitted. UDP me ye guarantee no, but fast hai.

**Why it matters:** Har connection banane me handshake ka cost hai (1 round trip). Isliye **keep-alive** aur **connection pooling** itni badi optimization hai.

**Where it is used:** DB connection pool · HTTP keep-alive · gRPC (HTTP/2 but persistent connection) · WebSocket.
**AI me role:** Streaming responses ke liye connection open rehna chahiye — idle timeout invalid set kiya to stream beech me tut jayegi. Long-running inference me proxy timeouts badhane padte hain.
**Salesforce me role:** Callout ke liye har baar naya TLS connection banta hai — isliye 100 chhote callouts ki jagah 1 bulk callout better hai. Ye **integration design ka core rule** hai.

#### 4. TLS / HTTPS

**What it is:** Encryption in transit. A certificate verifies the server's identity, then data is encrypted using symmetric cryptography. **mTLS** me client bhi certificate deta hai.

**Why it matters:** Without HTTPS, passwords, tokens, and personal data can travel in plaintext. Aaj HTTPS optional no, mandatory hai (browsers bhi block karte hain).

**Where it is used:** Har public endpoint · TLS termination LB but · Certificate auto-renew (Let's Encrypt/ACM) · Expired cert = poora system down (bahut common outage).
**AI me role:** API keys HTTPS ke bina bhejna = key chori. Aur keys client-side (browser/mobile) me kabhi mat rakho — hamesha apne backend se proxy karo.
**Salesforce me role:** Salesforce sirf HTTPS accept karta hai. Callout ke liye target ka certificate valid hona chahiye (self-signed reject). Two-way SSL ke liye Certificate & Key Management me cert upload karke Named Credential me attach karte ho.

#### 5. HTTP Methods

**What it is:** GET (read, safe) · POST (create) · PUT (replace the full resource) · PATCH (buttial update) · DELETE (delete) · OPTIONS (CORS preflight) · HEAD (headers only).

**Idempotency:** GET, PUT, DELETE idempotent hain (run it 10 times, the resulting state is the same). POST no — isliye double-click but duplicate order ban jata hai. Fix: idempotency key.

**Where it is used:** REST API design · Retry logic (safe hai ya no ye method batata hai) · Caching (GET cacheable, POST no).
**AI me role:** LLM APIs mostly POST hain (bada prompt body me). Retry karte waqt dhyan rakho — POST retry = double cost + duplicate side-effects agar tool calls involved hain.
**Salesforce me role:** `@HttpGet`, `@HttpPost`, `@HttpPatch`, `@HttpDelete` annotations Apex REST me. Composite API, Bulk API 2.0, sObject Rows API — sab in methods but bane hain. `PATCH` upsert with External Id = integration ka favourite pattern.

#### 6. Headers

**What it is:** Metadata for the request/response. Common: `Authorization`, `Content-Type`, `Accept`, `User-Agent`, `Cache-Control`, `X-Request-Id`, `ETag`.

**Why it matters:** Authentication, caching, content negotiation, and tracing can all be driven by headers. `X-Request-Id` pass karna distributed debugging ki jaan hai.

**AI me role:** `Authorization: Bearer sk-...`, `OpenAI-Organization`, aur streaming ke liye `Accept: text/event-stream`. Rate limit info bhi response headers me aati hai (`x-ratelimit-remaining`) — usse throttle karo.
**Salesforce me role:** `Authorization: Bearer <session-id>`, `Sforce-Query-Options: batchSize=200`, `Sforce-Limit-Info` response header jo batata hai aapne kitne API calls kharch kiye — daily API limit monitor karne ke liye.

#### 7. Cookies & Sessions

**What it is:** A cookie is a small value stored by the browser jo har request me apne aap jati hai. A session is user state stored server-side, jiska ID cookie me hota hai.

**Security flags (important):** `HttpOnly` (JS padh na sake → XSS protection) · `Secure` (sirf HTTPS) · `SameSite=Lax/Strict` (CSRF protection).

**Where it is used:** Login state, shopping cart, A/B test bucket, analytics.
**AI me role:** Chat app me conversation/session ID track karna — taki server valid history load kare. Ye "AI memory" ka backend implementation hai.
**Salesforce me role:** Session ID hi API auth token hai. Session Settings me timeout, IP lock, "Lock sessions to the domain" configure hota hai. Experience Cloud guest user sessions alag treat hote hain.

#### 8. Status Codes

**What it is:** A three-digit verdict returned in the response. 2xx = ho gaya · 3xx = redirect · 4xx = *client* error · 5xx = *server* error.

**Why it matters:** Client ka retry logic isi but depend karta hai — 4xx retry karna bekar hai (wahi galti dobara), 5xx aur 429 retry-worthy hain. Monitoring alerts bhi 5xx rate but lagti hain.

**AI me role:** `429` (rate limit → backoff), `400 context_length_exceeded` (prompt chhota karo ya summarize), `503 overloaded` (retry ya fallback model). Ek robust LLM client me ye teeno handle hone chahiye.
**Salesforce me role:** `401` = session expired (refresh token), `403 REQUEST_LIMIT_EXCEEDED` = daily API limit khatam, `400 MALFORMED_QUERY`, `500 UNABLE_TO_LOCK_ROW` — last wala **retry-worthy** hai kyunki wo temporary lock contention hai.

#### 9. HTTP/1.1 → HTTP/2 → HTTP/3

**What it is:** **1.1** — ek connection but ek-ek request (head-of-line blocking). **2** — multiplexing: ek connection but kai requests saath, header compression, server push. **3** — QUIC (UDP but), connection migration (WiFi se 4G but switch karo, connection no tutta), faster handshake.

**Why it matters:** HTTP/2 aane ke baad "file bundling" jaisi purani optimizations kam matter karti hain. Mobile users ke liye HTTP/3 real difference banata hai.

**AI me role:** gRPC HTTP/2 but chalta hai — model serving (Triton, TorchServe) me isi se low latency aur bidirectional streaming milti hai.
**Salesforce me role:** Lightning pages me bahut sare butallel resource requests hoti hain — HTTP/2 se page load fast hota hai. CDN but static resources HTTP/2-3 se serve hote hain.

| CodeMatlabKab use karo |                     |                               |
| ---------------------- | ------------------- | ----------------------------- |
| 200                    | OK                  | Sab theek                     |
| 201                    | Created             | POST se naya resource bana    |
| 400                    | Bad Request         | Client ne invalid data bheja    |
| 401                    | Unauthorized        | Login hi no hai             |
| 403                    | Forbidden           | Login hai but permission no |
| 404                    | Not Found           | Resource exist no karta     |
| 429                    | Too Many Requests   | Rate limit lag gaya           |
| 500                    | Server Error        | Aapke code me exception       |
| 503                    | Service Unavailable | Server down / overloaded      |

## 05. API Engineering — Core

**Hinglish:** API = your backend's **menu card**. The client only needs to know what it can order — how the kitchen works internally is not its concern.

```
flowchart LR
    R["Incoming Request"] --> V["1. Validation
is the data valid?"]
    V -->|"invalid"| E400["400 Bad Request"]
    V -->|"valid"| A["2. Auth check
is this user allowed?"]
    A -->|"no"| E401["401 / 403"]
    A -->|"yes"| RL["3. Rate Limit
bahut requests to no?"]
    RL -->|"limit exceeded"| E429["429 Too Many Requests"]
    RL -->|"within limit"| BL["4. Business Logic"]
    BL --> DB["5. Database"]
    DB --> RES["6. Response - paginated JSON"]
    BL -->|"exception"| E500["500 + logged error"]
  
```

### Topics — detail me

#### 1. REST + Resource Modeling

**What it is:** Design the API around **resources** (nouns), and express actions through HTTP methods. URL me verb no hona chahiye.

**Example:** `GET /users/5/orders?status=paid` ✅   vs   `GET /getUserOrdersByStatus?id=5` ❌

**Why it matters:** Predictable API = frontend team ko documentation kam padhni padti hai, aur caching/tooling automatically kaam karti hai.

**Where it is used:** Har public API, mobile backend, microservice boundaries.
**AI me role:** Aapke AI features bhi REST endpoints hi honge: `POST /chat/completions`, `POST /documents/ingest`, `GET /conversations/:id`. Achha resource model AI agent ke liye bhi zaroori hai — agent ko tools REST endpoints ke roop me hi diye jate hain.
**Salesforce me role:** SF ka REST API poora resource-modeled hai: `/services/data/v60.0/sobjects/Account/001xx`. Apna Apex REST banate waqt bhi yahi convention follow karo: `@RestResource(urlMapping='/orders/*')`.

#### 2. CRUD Operations

**What it is:** Create / Read / Update / Delete — har application ka 80% kaam. Map: POST / GET / PUT-PATCH / DELETE.

**Why it matters:** Ye aapki pehli poori API hogi. Par yahan **soft delete** ka concept seekho — asli data delete mat karo, `deleted_at` set karo (audit + recovery).

**AI me role:** RAG pipeline me documents ka CRUD chahiye — document update hua to uske purane chunks vector DB se delete karke naye insert karne padte hain, warna AI purana answer dega. Ye sabse common RAG bug hai.
**Salesforce me role:** CRUD + **FLS** (Field Level Security) + Sharing = SF ka security model. Apex me `WITH USER_MODE` / `Security.stripInaccessible()` use karke CRUD/FLS enforce karna security review ka mandatory requirement hai.

#### 3. Request Validation

**What it is:** Client se aaya data server but verify karna — required fields, type, format, range, allowed values.

**Why it matters:** **Client but bharosa kabhi mat karo.** Frontend validation sirf UX ke liye hai; attacker Postman se direct API hit karega. Ye OWASP ki #1 defence hai.

**Where it is used:** Zod/Joi (Node), Pydantic (Python), Bean Validation (Java) — schema define karo, middleware me enforce karo.
**AI me role:** **Do taraf se zaroori.** (1) User input validate karo — prompt injection filter, max length. (2) **LLM ka output bhi validate karo** — Pydantic/Zod schema se butse karo, fail ho to retry. LLM confidently invalid JSON deta hai.
**Salesforce me role:** Validation Rules (declarative), `addError()` in triggers, Required fields, Duplicate Rules. Apex REST me manually validate karna padta hai kyunki external caller kuch bhi bhej sakta hai.

#### 4. Error Handling (API level)

**What it is:** Har error ek consistent shape me: `{ "error": { "code": "INSUFFICIENT_FUNDS", "message": "...", "requestId": "abc" } }`

**Why it matters:** Client ek hi butser likh sake. Aur **stack trace kabhi expose mat karo** — wo attacker ko aapka framework, version aur file paths bata deta hai.

**AI me role:** AI errors alag category hain — `MODEL_OVERLOADED`, `CONTENT_FILTERED`, `CONTEXT_TOO_LONG`, `HALLUCINATION_DETECTED`. In but UI ka behaviour alag hona chahiye (retry vs rephrase vs fallback model).
**Salesforce me role:** SF errors structured aate hain (`errorCode` + `message` + `fields`). Integration me in codes but branch karo — `DUPLICATE_VALUE` but upsert karo, `UNABLE_TO_LOCK_ROW` but retry karo.

#### 5. Pagination, Filtering & Sorting

**What it is:** Bade result sets ko tukdo me dena. **Offset-based** (`?page=3&limit=20`) simple but deep pages but slow. **Cursor-based** (`?after=eyJpZCI6MTAwfQ`) hamesha fast aur consistent.

**Why it matters:** Bina pagination ke ek din table 10 lakh rows ki ho jayegi aur aapki API timeout karne lagegi. Ye "kal theek tha aaj down hai" ka classic reason hai.

**Where it is used:** Har list endpoint. Default limit set karo (e.g. 20) aur max cap (e.g. 100).
**AI me role:** RAG me **top-k** hi pagination hai — saare documents LLM ko no bhej sakte (context limit + cost). Chunking + ranking + top-k = smart pagination. Chat history bhi paginate/summarize karni padti hai.
**Salesforce me role:** SOQL `LIMIT`/`OFFSET` (max offset 2000!), `queryMore()` with query locator, Bulk API for large volumes. `OFFSET` ki limit hi wajah hai ki SF me cursor-style pagination (`WHERE Id > :lastId ORDER BY Id`) recommended hai.

#### 6. API Versioning

**What it is:** `/v1/orders` → `/v2/orders`. Purane clients tootne no chahiye when you breaking change karte ho.

**Rule:** Adding a field is generally safe. Removing/renaming a field or changing its type is a breaking change and may require a new version.

**Where it is used:** Public APIs, mobile apps (purana app version months tak chalta rehta hai), buttner integrations.
**AI me role:** **Prompt versioning** bhi utna hi zaroori hai. Prompt badla = output badal gaya = downstream butsing toot gayi. Prompts ko code ki tarah version control me rakho + evals chalao. Model version pin karo (`gpt-4o-2024-08-06`), warna vendor silently model badal dega.
**Salesforce me role:** SF ka versioning gold standard hai — API v20 se v60+ tak sab support hain, aur behaviour version-specific rehta hai. Apex class ka apna API version hota hai. Isliye SF integrations 10 saal purani bhi chalti rehti hain.

#### 7. Rate Limiting

**What it is:** How many requests a client can make (per user / per IP / per API key). Limit exceeded = `429` + `Retry-After`.

**Why it matters:** Abuse rokta hai, cost control karta hai, aur ek buggy client ko poore system ko girane se bachata hai (noisy neighbour problem).

**Where it is used:** Login endpoint (brute force), public APIs, expensive endpoints (report generation).
**AI me role:** **Sabse zaroori yahan hai** — kyunki har LLM call me paisa lagta hai. Bina rate limit ke ek script aapka $5000 ka bill bana degi. Do level chahiye: (1) per-user request limit, (2) per-user **token/cost budget**. Aur upstream vendor ka rate limit bhi handle karo.
**Salesforce me role:** Daily API request limits (edition + license based), Concurrent Apex limit (10 long-running), Bulk API batch limits. `Sforce-Limit-Info` header se track karo. Integration design me "kitne API calls kharch honge" ek architecture decision hai.

#### 8. Webhooks

**What it is:** Ulta API — aap poll no karte, event hone but **wo** aapko HTTP POST karta hai. Example: payment success, GitHub push, Stripe refund.

**Must-have security:** signature verification (HMAC), timestamp checks (replay attacks), idempotency (the same event may arrive twice), aur return 200 quickly and move the work to a queue.

**Where it is used:** Payment gateways, CI/CD, third-butty integrations, real-time sync.
**AI me role:** Long-running AI jobs (video analysis, fine-tuning, batch inference) ke liye webhook hi valid pattern hai — job submit karo, kaam hone but vendor aapko call karega. Polling waste hai.
**Salesforce me role:** SF me webhook **Outbound Message** (declarative, SOAP) ya **Platform Event + external subscriber** ya simply Apex trigger → `@future` callout ke roop me aata hai. Ulta direction me: external system → SF ke liye Apex REST endpoint banao ya Platform Event publish karao.

#### 9. OpenAPI / Swagger

**What it is:** A machine-readable API specification (YAML/JSON). Isse auto-generate hota hai: interactive docs, client SDKs, mock servers, aur contract tests.

**Why it matters:** Frontend team ko poochna no padta "is field ka type kya hai". Spec = single source of truth.

**AI me role:** **Bahut bada.** OpenAI/Anthropic tool-calling me aap functions ka JSON Schema dete ho — wo basically OpenAPI hi hai. Agent ko OpenAPI spec do aur wo khud aapke API call karna seekh jata hai (ye Custom GPTs / MCP servers ka base hai).
**Salesforce me role:** **External Services** feature seedha OpenAPI spec leta hai aur usse Flow-callable actions auto-generate kar deta hai — bina code likhe integration. **Agentforce** me bhi actions ka schema define karna padta hai taki agent samajh sake kab kaunsa action call karna hai.

**Cursor vs Offset pagination:** Offset (`LIMIT 20 OFFSET 100000`) can become very slow on large datasets. Cursor (`WHERE id > last_id LIMIT 20`) remains efficient for deep pagination.

## 06. Databases — Core

**Hinglish:** Data is the real product. Code dobara likha ja sakta hai, kharab data wapas no aata. Isliye DB backend ka sabse important butt hai.

```
flowchart TD
    D["Choose a database"] --> Q{"Data structured hai aur
relations important hain?"}
    Q -->|"Yes"| SQL["SQL - PostgreSQL / MySQL"]
    Q -->|"No, flexible schema"| NO["NoSQL"]
    NO --> M["MongoDB - documents"]
    NO --> RD["Redis - cache, key-value, super fast"]
    NO --> DY["DynamoDB - managed, huge scale"]
    SQL --> T["Tables, Relationships, Joins"]
    T --> I["Indexes - speed"]
    I --> TR["Transactions - ACID"]
    TR --> C["Constraints - data valid rahe"]
    C --> QO["Query Optimization - EXPLAIN"]
  
```

### SQL side — in detail

#### 1. Tables & Relationships

**What it is:** Data is stored in rows/columns. **One-to-many** (one User can have many Orders — child me foreign key). **Many-to-many** (Student ↔ Course — with a junction table in between). **One-to-one** (User ↔ UserProfile).

**Normalization:** Data duplicate mat karo — customer ka naam har order row me mat likho, `customer_id` rakho. **Denormalization** tab karo jab read performance chahiye (deliberate duplication).

**Why it matters:** A poor data model creates pain across every feature. Schema badalna production me sabse mehnga kaam hai.
**AI me role:** Chat app ka schema: `conversations` → `messages` (one-to-many) → `message_sources` (RAG citations). Document → chunks → embeddings bhi relational hierarchy hai.
**Salesforce me role:** **Lookup** = loose one-to-many, **Master-Detail** = tight one-to-many (child butent ke bina no reh sakta, sharing inherit karta hai, roll-up summary milti hai), **Junction Object** = many-to-many (2 master-detail fields). Ye teen relationships SF data modelling ki poori neev hain.

#### 2. Joins

**What it is:** INNER (dono me match ho) · LEFT (left ka sab + match) · RIGHT · FULL OUTER · SELF JOIN (manager-employee).

**Why it matters:** A JOIN is generally preferable to issuing many separate queries, especially when it avoids N+1 patterns. Ye N+1 problem ka asli ilaaj hai.

**Where it is used:** Report queries, dashboards, list views with related data.
**AI me role:** **Text-to-SQL** AI ka popular use case hai — but LLM joins me hi sabse zyada galti karta hai. Isliye schema description + example queries prompt me dena padta hai. Aur generated SQL ko **read-only user** se hi chalao (SQL injection ka AI version).
**Salesforce me role:** SOQL me classic JOIN no hai! Uski jagah **butent-child traversal** hai: `SELECT Name, Account.Industry FROM Contact` (child→butent, 5 level tak) aur **subquery**: `SELECT Name, (SELECT LastName FROM Contacts) FROM Account` (butent→child, 1 level). Aur **semi-join**: `WHERE AccountId IN (SELECT Id FROM Account WHERE ...)`.

#### 3. Indexes

**What it is:** Like the index of a book. B-Tree structure jo `WHERE`, `JOIN`, `ORDER BY` ko O(log n) bana deta hai.

**Cost:** Every index consumes disk space aur **har INSERT/UPDATE ko slow** karta hai (index bhi update hota hai). Isliye 15 index lagane se app slow ho jayegi.

**Where it is used:** Foreign keys, frequently filtered columns, unique constraints. `EXPLAIN ANALYZE` se prove karo — guess mat karo.
**AI me role:** Vector DB me index alag type ke hote hain — **HNSW** (graph-based, fast + accurate, memory heavy) aur **IVF** (clustering-based, memory efficient). Ye ANN indexes hain: 100% accurate no but 100x fast. Trade-off tuning (`ef_search`, `nprobe`) RAG performance ki key hai.
**Salesforce me role:** SF khud indexes manage karta hai. Standard indexed: `Id`, `Name`, `OwnerId`, `CreatedDate`, `SystemModstamp`, Master-Detail/Lookup fields, **External Id** aur **Unique** fields. **Custom index** Salesforce Support se maangna padta hai. **Non-selective query** (bade object but index na lagna) = `Non-selective query against large object type` error. Isliye filter hamesha indexed field but rakho, aur `!=` / `NOT` / leading-wildcard `LIKE '%x'` se bacho — ye index kill kar dete hain.

#### 4. Transactions (ACID)

**What it is:** A group of operations treated as one atomic unit. `BEGIN ... COMMIT`. Beech me kuch fail = poora `ROLLBACK`.

**Isolation levels:** Read Uncommitted → Read Committed (default) → Repeatable Read → Serializable. Jitna strict, utna safe but utna slow (aur lock contention zyada).

**Where it is used:** Money transfer, inventory decrement, order + payment + stock ek saath.
**AI me role:** Agent jab multiple tools call karke DB me changes karta hai, wahan transaction boundary sochni padti hai — agent beech me fail hua to adhoora state no rehna chahiye. Isliye **saga pattern** / compensating actions use hote hain.
**Salesforce me role:** Poora Apex transaction hi ek DB transaction hai — unhandled exception = **sab kuch rollback**. `Database.setSavepoint()` se manual savepoint bana sakte ho. `Database.insert(records, false)` = buttial success allow (kuch fail hone but baaki save ho jayein). Ye SF integration me bahut important pattern hai.

#### 5. Constraints

**What it is:** NOT NULL · UNIQUE · PRIMARY KEY · FOREIGN KEY · CHECK · DEFAULT. DB khud invalid data reject kare.

**Why it matters:** Application code can contain bugs, 3 alag services same table me likh sakti hain — but constraint hamesha lagega. **Data integrity ki last line of defence.**

**AI me role:** Vector DB me `UNIQUE(document_id, chunk_index)` rakhna — warna re-ingestion but duplicate chunks ban jate hain aur AI same content 3 baar retrieve karke context waste karta hai.
**Salesforce me role:** Required field, Unique field, External Id, Validation Rules, Lookup filters, Master-Detail cascade delete — sab constraints hi hain. Fark: SF me ye **declarative** hain, aur Data Loader se bhi bypass no hote (validation rules to bypass ho sakte hain agar user permission ho).

#### 6. Query Optimization

**What it is:** `EXPLAIN ANALYZE` chalao aur read the query plan. **Seq Scan** on big table = index missing. **Nested Loop** on large sets = problem.

**Common fixes:** Index add karo · `SELECT *` band karo (sirf zaroori columns) · `N+1` ko JOIN se replace karo · Function on indexed column mat lagao (`WHERE LOWER(email)=...` index kill karta hai — functional index banao).

**AI me role:** RAG me slow retrieval = slow answer. Metadata filter (`WHERE tenant_id = ...`) ko vector search se pehle lagao (pre-filtering), warna 10 lakh vectors scan honge.
**Salesforce me role:** **Query Plan Tool** (Dev Console me enable karo) SOQL ka cost dikhata hai — cost < 1 achha hai. Selectivity threshold: standard index 30% (max 1 million), custom index 10% (max 333k). Bade orgs me **Skinny Table** aur **Divisions** bhi optimization tools hain.

### NoSQL side — in detail

#### 7. MongoDB (Document DB)

**What it is:** JSON-like documents. Flexible schema — har document alag fields rakh sakta hai. Nested data ek hi document me (no join needed).

**Kab use karo:** Content management, product catalog (har category ke alag attributes), event/log data, rapid prototyping.

**Kab NA karo:** Complex relations, multi-document transactions heavy, reporting/analytics.
**AI me role:** Chat history store karne ke liye achha (har message ka structure thoda alag — text, tool call, image). MongoDB Atlas me built-in **vector search** bhi hai, to ek hi DB me document + embedding rakh sakte ho.
**Salesforce me role:** Analogy — SF ka **Custom Metadata** aur **JSON in Long Text field** flexible schema jaisa kaam karte hain. Aur **Salesforce Data Cloud** internally NoSQL-style scale but chalta hai. External data ke liye Salesforce Connect (OData) se NoSQL source ko External Object bana sakte ho.

#### 8. Redis (Key-Value / In-Memory)

**What it is:** A data store that operates primarily in memory. Sub-millisecond. Sirf key-value no — Lists, Sets, Sorted Sets, Hashes, Streams, Pub/Sub, TTL sab built-in.

**Top use cases:** Cache · Session store · Rate limit counters · Leaderboards (sorted set) · Distributed locks · Job queues · Real-time pub-sub.

**AI me role:** **Semantic cache** — milta-julta question pehle poocha gaya to LLM call bachao (bada cost saving). Conversation memory store. Rate limit + token budget counters. **Redis Vector Search** se embeddings bhi store ho jate hain.
**Salesforce me role:** SF ka apna "Redis" = **Platform Cache** (Org Cache + Session Cache). Governor limits bachane ke liye baar-baar use hone wala data (config, exchange rates, expensive query results) cache me daalte ho. Heroku app ke saath Redis add-on bhi common pattern hai.

#### 9. DynamoDB & Wide-Column (Cassandra)

**What it is:** Massive scale, predictable single-digit ms latency. Par **access patterns need to be designed in advance** — buttition key + sort key. Ad-hoc query no kar sakte.

**Kab use karo:** IoT/time-series, activity feeds, session store at huge scale, write-heavy workloads jahan query pattern fixed hai.

**Why it matters:** Ye "query-first design" sikhata hai — pehle sochо kaunsi query chalegi, phir table design karo. SQL me ulta hota hai.
**AI me role:** AI usage logs, token consumption tracking, feedback events — huge write volume, simple read pattern. Perfect fit.
**Salesforce me role:** **Big Objects** exactly yahi cheez hain — billions of records, but sirf **index (composite key)** but query kar sakte ho, ad-hoc SOQL no. Use case: audit history, archived data, long-term event logs. Query via `Async SOQL`.

**Analogy:** SQL = an Excel sheet with strict rules. MongoDB = a folder of forms where each form can have a different structure. Redis = desk but rakha sticky note — turant milta hai but permanent no.

**Default advice:** If you are unsure, start with **PostgreSQL**. It is capable enough for a very large range of applications and also handles JSON well.

---

## 🚀 Learning Philosophy

> **Learn → Build → Debug → Scale → Explain**

Do not stop at tutorials. For every major topic, implement something, understand its failure modes, and connect the concept to a real production scenario.

⭐ If this roadmap is useful, consider starring the repository.
