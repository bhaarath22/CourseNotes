# 🔁 Digital Counters Overview

## 📌 What is a Counter?

A counter is a type of sequential logic circuit that counts events, typically in the form of clock pulses. It stores and updates a binary value with each clock cycle.

---

## 🧠 Types of Counters

| Type            | Description                                               |
|-----------------|-----------------------------------------------------------|
| Asynchronous    | Flip-flops are triggered one after another (ripple effect)|
| Synchronous     | All flip-flops are triggered simultaneously               |
| Up Counter      | Counts upward (e.g., 0 → 1 → 2 → …)                        |
| Down Counter    | Counts downward (e.g., 7 → 6 → 5 → …)                      |
| Up/Down Counter | Can count in both directions, based on control input      |
| Modulo-n        | Resets after reaching a defined count (e.g., Mod-10)      |

---

## 🧩 Counter Types Explained

### 🔸 Asynchronous (Ripple) Counter

- Clock input is applied only to the first flip-flop.
- Subsequent flip-flops are triggered by the output of the previous one.
- Simple but suffers from propagation delay.
- Example: 4-bit ripple counter → counts from 0000 to 1111.

### 🔸 Synchronous Counter

- All flip-flops receive the same clock signal.
- Faster and more accurate than asynchronous counters.
- Ideal for high-speed digital systems.

### 🔸 Up Counter

- Increments value on each rising edge of the clock.
- Example: Counts 0, 1, 2, 3, ..., wraps around after max.

### 🔸 Down Counter

- Decrements value on each clock pulse.
- Example: Counts ..., 3, 2, 1, 0 → wraps to max value.

### 🔸 Up/Down Counter

- Direction determined by control signal.
- '1' = Count up, '0' = Count down.

### 🔸 Modulo-n Counter

- Counts from 0 to (n−1), then resets.
- Example: Mod-10 (Decade) Counter → 0 to 9.

---

## 🔧 Key Components

- 🧱 Flip-Flops: Usually T or JK flip-flops
- ⏱ Clock Input: Triggers state change
- 🔄 Reset Input: Sets counter to initial value (typically 0)
- ✅ Enable Input: Allows counting when active

---

## 📐 Common Applications

- ⏰ Digital clocks
- 📡 Frequency counters
- 📈 Event counters
- ⏲ Digital timers
- 💾 Memory addressing (in CPUs)
- ⏩ Shift registers

---

## 🔍 How Counters Work

### ✅ 4-Bit Up Counter

- CLK: Clock input
- RST: Asynchronous reset
- COUNT: 4-bit output
- Counts: 0000 → 1111 (0 → 15), then wraps to 0000

### 🔻 4-Bit Down Counter

- Starts at 1111 (15)
- Decrements on each rising clock edge
- RST = '1' resets to 15
- 0000 → wraps around to 1111

### 🔁 4-Bit Up/Down Counter

- CLK: Clock input
- RST: Asynchronous reset
- UP_DOWN: Direction control ('1' = up, '0' = down)
- COUNT: 4-bit output (adjusts based on direction)
