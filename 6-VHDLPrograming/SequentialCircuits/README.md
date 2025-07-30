# 🔌 Digital Circuits: Combinational & Sequential

## 🔄 Combinational Circuits

### A **Combinational Circuit** is a digital circuit where the output depends only on the **current inputs** — no memory or feedback involved.

### 🔑 Key Features
- ❌ No memory
- ❌ No feedback paths
- ❌ Clock not required
- ➡️ Output = f(Input)

### 🟢 Examples
- Half Adder / Full Adder
- Multiplexer (MUX)
- Decoder / Encoder
- Logic Gates (AND, OR, XOR, etc.)


## 🔁 Sequential Circuits

### A **Sequential Circuit** is a type of digital circuit where the output depends on both the **current inputs** and **past inputs** — it has **memory**.

### 🔑 Key Features
- ✅ Has memory (stores previous states using flip-flops/latches)
- 🔁 Feedback exists for state storage
- 🕒 Usually requires a clock (synchronous) or feedback (asynchronous)
- ➡️ Output = f(Input + History)

### 🟡 Examples
- Flip-Flops (SR, D, JK, T)
- Registers
- Counters
- Finite State Machines (FSMs)

---
---

## 🔁 Sequential vs 🔄 Combinational Circuits

| Feature              | 🔄 Combinational Circuits         | 🔁 Sequential Circuits                |
|----------------------|----------------------------------|--------------------------------------|
| **Output depends on** | Only present inputs              | Present inputs + Past state          |
| **Memory**            | ❌ No                            | ✅ Yes (Flip-Flops/Latches)           |
| **Feedback path**     | ❌ No                            | ✅ Yes                                |
| **Clock**             | ❌ Not required                  | ✅ Usually required                   |
| **Examples**          | Adders, MUX, DEMUX, Encoders     | Counters, Registers, FSMs            |
| **Timing**            | Instantaneous (gate delay only) | State changes on clock/events        |
| **Complexity**        | Simpler                         | More complex (state handling)        |
| **VHDL Style**        | Dataflow/Structural              | Behavioral/Structural (with storage) |

---

## 🧠 Key Concept

> If the circuit **remembers** anything — it's **Sequential**.  
> If it **just calculates output** based on input instantly — it's **Combinational**.

---  
