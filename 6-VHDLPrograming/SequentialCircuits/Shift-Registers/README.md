# 🔄 What is a Shift Register?

A shift register is a sequential logic circuit made up of flip-flops used to store and shift binary data. It’s mainly used for data storage, data movement, or data manipulation in digital circuits.  
Each flip-flop in a shift register holds a single bit, and data moves through them either left or right (depending on the type) with each clock pulse.

---

## 🧠 Types of Shift Registers

### 1. Serial In – Serial Out (SISO)
- Data enters and exits one bit at a time.
- Used for data buffering.
  
Only one bit enters and exits per clock cycle.  
Example: Input = 1011 (from MSB to LSB)

| Clock | Input | Q1 | Q2 | Q3 | Q4 | Output |
|-------|-------|----|----|----|----|--------|
| 0     | -     | 0  | 0  | 0  | 0  | -      |
| 1     | 1     | 1  | 0  | 0  | 0  | -      |
| 2     | 0     | 0  | 1  | 0  | 0  | -      |
| 3     | 1     | 1  | 0  | 1  | 0  | -      |
| 4     | 1     | 1  | 1  | 0  | 1  | 1      |

➡️ Final output is the last bit that exits Q4 after all shifts.

---

### 2. Serial In – Parallel Out (SIPO)
- Data enters serially, but all bits are available at once in parallel.
- Used when converting serial data to parallel.

  Data is entered serially but observed all at once after each clock.  
Example: Input = 1100 (MSB to LSB)

| Clock | Input | Q1 | Q2 | Q3 | Q4 |
|-------|-------|----|----|----|----|
| 0     | -     | 0  | 0  | 0  | 0  |
| 1     | 1     | 1  | 0  | 0  | 0  |
| 2     | 1     | 1  | 1  | 0  | 0  |
| 3     | 0     | 0  | 1  | 1  | 0  |
| 4     | 0     | 0  | 0  | 1  | 1  |

➡️ Parallel output = 0011 at this point.

---

### 3. Parallel In – Serial Out (PISO)
- All bits are loaded at once; then shift out serially.
- Used to transmit parallel data serially, e.g., in microcontrollers.

 All 4 bits are loaded at once, and then shifted out one bit per clock.  
Example: Load = 1010 (Q1=1, Q2=0, Q3=1, Q4=0)

| Clock | Load | Q1 | Q2 | Q3 | Q4 | Output |
|-------|------|----|----|----|----|--------|
| 0     | Yes  | 1  | 0  | 1  | 0  | -      |
| 1     | No   | 0  | 1  | 0  | 1  | 1      |
| 2     | No   | 1  | 0  | 1  | 0  | 0      |
| 3     | No   | 0  | 1  | 0  | 0  | 1      |
| 4     | No   | 1  | 0  | 0  | 0  | 0      |

➡️ Output: 1 → 0 → 1 → 0 (same as input)

---

### 4. Parallel In – Parallel Out (PIPO)
- Loads and outputs all bits at once.
- Works like a latch or register in CPUs.

All bits are loaded and output together in one clock cycle.  
Example: Load = 1101

| Clock | Load | Q1 | Q2 | Q3 | Q4 |
|-------|------|----|----|----|----|
| 0     | Yes  | 1  | 1  | 0  | 1  |

➡️ Output: 1101 immediately after load signal.

---

### 5. Bidirectional Shift Register
- Can shift both left and right.
- Adds flexibility for arithmetic operations.

Data can shift either left or right depending on a control input.  
Initial state: 1001  
Direction: Right

| Clock | Direction | Q1 | Q2 | Q3 | Q4 |
|-------|-----------|----|----|----|----|
| 0     | -         | 1  | 0  | 0  | 1  |
| 1     | Right     | 0  | 1  | 0  | 0  |
| 2     | Right     | 0  | 0  | 1  | 0  |
| 3     | Left      | 0  | 1  | 0  | 1  |

➡️ Supports shifting either direction with a control signal.

---

### 6. Universal Shift Register
- Combines all features: serial/parallel input and output, bi-directional shift.
- Versatile, but more complex.

All-in-one: serial/parallel in/out, left/right shift.

Example:
- Load parallel data: 1010
- Shift left → becomes 0100
- Insert 1 serially → becomes 1001

| Operation         | Q1 | Q2 | Q3 | Q4 |
|-------------------|----|----|----|----|
| Load 1010         | 1  | 0  | 1  | 0  |
| Shift Left        | 0  | 1  | 0  | 0  |
| Serial In = 1     | 1  | 0  | 0  | 1  |

---

## ⚙️ Applications

- Data storage  
- Data transfer (e.g., UART, SPI)  
- LED sequencing (like running lights)  
- Arithmetic operations (like multiplication/division by 2)  
- Digital signal processing  

---
## 🔧 Real World Chips

- 74HC595: Popular 8-bit SIPO  
- 74LS164: Serial in, parallel out  
- CD4015: Dual 4-bit shift register  
