# 🔁 Flip-Flops: The Memory of Digital Circuits

Flip-flops are **basic sequential logic circuits** used to store binary data (`0` or `1`). Acting as 1-bit memory elements, they are essential building blocks for many digital systems.

---

## 🔧 What Flip-Flops Do

Flip-flops switch ("flip" or "flop") between two **stable states** — set or reset — based on input signals and clock timing.  
They **store a bit of data** until a signal instructs them to change it.

---

## 🧠 Common Uses of Flip-Flops

Flip-flops are used in a variety of digital applications:

- **🗂 Data Storage:** Each flip-flop stores 1 bit (e.g., in RAM, registers).
- **⏱ Counters:** Found in digital clocks, timers, frequency dividers.
- **➡️ Shift Registers:** Move data sequentially (e.g., serial-to-parallel conversion).
- **⚙️ State Machines:** Control logic in systems like vending machines, traffic lights.
- **🔄 Synchronization:** Used for signal synchronization between different clock domains.

---

## 🔧 Types of Flip-Flops

| Type         | Description                                |
|--------------|--------------------------------------------|
| **SR**       | Set-Reset flip-flop                        |
| **D**        | Data or Delay flip-flop                    |
| **JK**       | Jack-Kilby flip-flop                       |
| **T**        | Toggle flip-flop                           |

---

## 🔄 SR Flip-Flop (Set-Reset Flip-Flop)

An **SR Flip-Flop** is the simplest type, with:

- **Inputs:**  
  - `S` (Set)  
  - `R` (Reset)

- **Outputs:**  
  - `Q` (normal output)  
  - `Q̅` (inverted output)

It **stores 1 bit of data** based on the combination of S and R inputs.

### 🧪 SR Flip-Flop Truth Table

| S | R | Q (Next State) | Description        |
|---|---|----------------|--------------------|
| 0 | 0 | No change      | Hold previous state|
| 0 | 1 | 0              | Reset              |
| 1 | 0 | 1              | Set                |
| 1 | 1 | Invalid ❌      | Not allowed        |

> ⚠️ **Warning:** When **S = 1** and **R = 1**, it's an **invalid condition**. Both outputs `Q` and `Q̅` go to `0`, violating the rule that they must be complements of each other.

---

## 🧠 Quick Summary

- **Set (S = 1):** Makes `Q = 1`
- **Reset (R = 1):** Makes `Q = 0`
- **S = 0, R = 0:** Holds previous state
- **S = 1, R = 1:** ❌ Invalid state — avoid using!

📷 [SR Flip-Flop Circuit Diagram](location)

---

## 🧠  D Flip-Flop

This document provides a concise overview of **D Flip-Flops** and **JK Flip-Flops**, two fundamental building blocks in digital electronics.

---

## 🔷 D Flip-Flop (Data or Delay Flip-Flop)

A **D Flip-Flop** captures the value on its **D (Data)** input at the moment of a **clock edge** (usually the rising edge), and holds that value until the next clock edge.

### 📥 Inputs & Outputs
- `D` → Data input  
- `CLK` → Clock input  
- `Q` → Output (follows D on clock)  
- `Q̅` (optional) → Inverted output

### 📋 Truth Table

| CLK (Edge) | D | Q (Next State) |
|------------|---|----------------|
| ↑ Rising   | 0 | 0              |
| ↑ Rising   | 1 | 1              |
| No edge    | X | No change      |

✅ On the **rising edge** of CLK, Q becomes whatever D is.  

## ⚙️ Applications

### D Flip-Flop:
- Data storage
- Latching circuits
- Shift registers
- Pipeline stages

### 🧪 Summary
- Clean operation, no invalid states.
- Used in:
  - Registers
  - Counters
  - Memory elements
  - Pipelines
- One of the **most fundamental storage elements** in digital circuits.

---

## 🔶 JK Flip-Flop

The **JK Flip-Flop** is a clocked flip-flop that:
- Combines features of the **SR** and **T flip-flops**
- Eliminates the **invalid state** of SR flip-flops
- Can **toggle**, **set**, **reset**, or **hold** its output

📛 Named after its inventors: **Jack Kilby** (co-inventor of the integrated circuit).

### 🔌 Inputs & Outputs
- `J` = Set input  
- `K` = Reset input  
- `CLK` = Clock input (edge-triggered)  
- `Q` = Output  
- `Q̅` = Inverted output

### 📊 Truth Table

| J | K | CLK ↑ | Q (Next State) | Action      |
|---|---|--------|----------------|-------------|
| 0 | 0 | Rising | Q              | No change   |
| 0 | 1 | Rising | 0              | Reset       |
| 1 | 0 | Rising | 1              | Set         |
| 1 | 1 | Rising | ~Q             | Toggle      |

✅ Only changes on **rising edge** of CLK.  
✅ When **J = K = 1**, the flip-flop toggles its output — unlike the SR flip-flop which would be invalid.

### 🔄 Summary
- `J = 1, K = 0` → **Set**
- `J = 0, K = 1` → **Reset**
- `J = K = 1` → **Toggle**
- `J = K = 0` → **No change**

---

## ⚙️ Applications

### JK Flip-Flop:
- Counters (especially synchronous ones)
- Toggle-based control logic
- Frequency dividers
- Sequential circuits with toggling behavior

---

## 🧠 Why Use JK Flip-Flop?

- It is a **universal flip-flop**:
  - Can mimic SR, D, and T flip-flops depending on the inputs
- Ideal for:
  - **Toggle-based circuits**
  - **Binary counters**
 
---  

# 🔄 T Flip-Flop 

## 🧠 Overview

A T Flip-Flop (Toggle Flip-Flop) is a simple yet powerful digital circuit element. It toggles its output state based on the input provided to it. Every time the clock edge triggers, the T Flip-Flop will change its state depending on the value of the toggle input (T).

### 🔶  Description:
- **T = 0**: The output remains in its previous state (no change).
- **T = 1**: The output toggles (inverts) its state.

This makes T Flip-Flops ideal for tasks such as counting and frequency division, where we need a simple binary state toggle.

##  🔶 Truth Table

| T  | CLK ↑ | Q (Next State) | Description           |
|----|-------|----------------|-----------------------|
| 0  | Rising| Q (no change)   | Hold (no change)      |
| 1  | Rising| ~Q (toggle)     | Toggle (invert output)|

### Notes:
- **T**: Toggle input.
- **CLK**: Clock input (edge-triggered).
- **Q**: Output.
- **Q̅**: Optional inverted output.

## 🔶  Inputs and Outputs

- **T (Toggle Input)**: This input controls whether the output should be toggled.
- **CLK (Clock Input)**: The clock signal triggers the change in state of the flip-flop.
- **Q (Output)**: The output that holds the current state of the flip-flop.
- **Q̅ (Optional Inverted Output)**: The inverted output, usually representing the opposite state of Q.

## ⚙️ Applications

T Flip-Flops have various uses in digital systems:
- **Binary Counters**: Used to create binary counters by chaining multiple T Flip-Flops.
- **Frequency Dividers**: They can divide the frequency of a clock signal by 2, making them useful in frequency division tasks.
- **Toggle Switches**: Ideal for implementing toggling mechanisms.
- **Pulse Train Generation**: Used for generating pulse trains in circuits.

## 🧠 Summary

- **T = 1**: The output toggles (inverts).
- **T = 0**: The output remains unchanged (holds the previous state).

T Flip-Flops are clean, simple, and perfect for counting and toggling tasks, making them a key component in digital circuit design.

---

# Digital Flip-Flops Overview

## 1. SR Flip-Flop
- **Inputs**: S (Set), R (Reset)
- **Expression**: 
  - \( Q_{n+1} = S + Q_n \cdot \overline{R} \)
- **✅ Means**:
  - If **S = 1**, Q is set to 1.
  - If **R = 1**, Q is reset to 0.
  - If both **S = 0** and **R = 0**, Q holds the previous value.
  - **Invalid when**: **S = R = 1**.

---

## 2. D Flip-Flop
- **Input**: D (Data)
- **Expression**: 
  - \( Q_{n+1} = D \)
- **✅ Clean and simple**:
  - Q just copies D at the clock edge.

---

## 3. JK Flip-Flop
- **Inputs**: J, K
- **Expression**: 
  - \( Q_{n+1} = J \cdot \overline{Q_n} + \overline{K} \cdot Q_n \)
- **✅ This covers**:
  - **Set** when **J = 1** and **K = 0**.
  - **Reset** when **J = 0** and **K = 1**.
  - **Toggle** when **J = K = 1**.
  - **Hold** when **J = K = 0**.

---

## 4. T Flip-Flop
- **Input**: T (Toggle)
- **Expression**: 
  - \( Q_{n+1} = T \oplus Q_n \)
- **✅ XOR means**:
  - If **T = 0**, Q holds (**Q ⊕ 0 = Q**).
  - If **T = 1**, Q toggles (**Q ⊕ 1 = \overline{Q}**).

---

## 🧠 Summary Table

## 🧠 Summary Table

## 🧠 Summary Table

| Flip-Flop | Inputs | Boolean Expression                         | Description             |
|-----------|--------|--------------------------------------------|-------------------------|
| **SR**    | S, R   | Q(n+1) = S + Q(n)·R'                       | Set / Reset             |
| **D**     | D      | Q(n+1) = D                                 | Direct Load             |
| **JK**    | J, K   | Q(n+1) = J·Q'(n) + K'·Q(n)                 | Set / Reset / Toggle    |
| **T**     | T      | Q(n+1) = T ⊕ Q(n)                          | Toggle / Hold           |
