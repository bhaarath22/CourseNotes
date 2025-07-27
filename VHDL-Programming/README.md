# **VHDL (Very High-Speed Integrated Circuit Hardware Description Language)**

VHDL is a powerful hardware description language used to model digital systems at various levels of abstraction, from algorithmic to gate level. It combines sequential, concurrent, net-list, timing specifications, and waveform generation capabilities.

## **Table of Contents**
- [Entity and Architecture](#entity-and-architecture)
- [Modeling Styles in VHDL](#modeling-styles-in-vhdl)
  - [Data Flow Modeling](#1-data-flow-modeling)
  - [Behavioral Modeling](#2-behavioral-modeling)
  - [Structural Modeling](#3-structural-modeling)
- [Sequential and Concurrent Statements](#sequential-and-concurrent-statements)
  - [Sequential Statements](#sequential-statements)
  - [Concurrent Statements](#concurrent-statements)
- [Data Objects in VHDL](#data-objects-in-vhdl)
- [Data Types in VHDL](#data-types-in-vhdl)

---

## **Entity and Architecture**

- **Entity**: Defines the external interface of a design, specifying its inputs, outputs, and optional generics, acting as a blueprint for the module's interaction with its environment.
- **Architecture**: Defines the internal workings and functionality of a design entity, describing its behavior, structure, or both.

---

## **Modeling Styles in VHDL**
### **1. Data Flow Modeling**
- Describes the flow of data through the design using **concurrent signal assignment** statements.
- Does not explicitly specify structure, making it useful for high-level descriptions.
- Example:
  ```vhdl
  output <= input1 AND input2;
  ```

### **2. Behavioral Modeling**
- Uses **sequential statements** inside `processes`, `functions`, or `procedures`.
- Resembles traditional programming, making it useful for algorithmic descriptions.
- Example:
  ```vhdl
  process(clk)
  begin
      if rising_edge(clk) then
          output <= input1 XOR input2;
      end if;
  end process;
  ```

### **3. Structural Modeling**
- Describes a design in terms of interconnected components, similar to a block diagram.
- Example:
  ```vhdl
  U1: AND_GATE port map (A, B, Y);
  ```

---

## **Sequential and Concurrent Statements**

### **Sequential Statements**
- Execute one after another inside a `process`, `function`, or `procedure`.
- Common sequential statements:

  - **Variable Assignment (`:=`)**
    ```vhdl
    process
        variable temp : integer;
    begin
        temp := 5; -- Immediate assignment
    end process;
    ```
  
  - **Signal Assignment (`<=`)**
    ```vhdl
    process
    begin
        A <= '1'; -- Scheduled assignment
    end process;
    ```
  
  - **Conditional Statements**
    ```vhdl
    if A = '1' then
        B <= '0';
    else
        B <= '1';
    end if;
    ```

  - **Loops (For, While, Loop)**
    ```vhdl
    for i in 0 to 7 loop
        array(i) := '0';
    end loop;
    ```
  
  - **Wait Statement**
    ```vhdl
    wait until clk'event and clk = '1';
    ```

### **Concurrent Statements**
- Execute simultaneously outside processes, mainly in architecture.
- Common concurrent statements:
  - **Signal Assignment**:
    ```vhdl
    B <= A and C;
    ```
  - **Conditional Signal Assignment (`when-else`)**:
    ```vhdl
    output <= "00" when sel = "00" else
              "01" when sel = "01" else
              "10";
    ```
  - **Selected Signal Assignment (`with-select`)**:
    ```vhdl
    with sel select
        output <= "00" when "00",
                  "01" when "01",
                  "10" when others;
    ```

---

## **Data Objects in VHDL**
A **data object** is a storage element that holds a value. VHDL provides four types of data objects:

- **Constant**: Holds a fixed value that cannot change during simulation. Example:
  ```vhdl
  constant PI : real := 3.14;
  ```

- **Variable**: Stores temporary data and can be updated within a process, function, or procedure. Example:
  ```vhdl
  variable count : integer := 0;
  ```

- **Signal**: Represents a hardware connection and can be assigned values concurrently. Example:
  ```vhdl
  signal clk : std_logic := '0';
  ```

- **File**: Used to read and write data to external files. Example:
  ```vhdl
  file my_file : text;
  ```

---

## **Data Types in VHDL**
VHDL supports various **data types**, categorized as follows:

### **1. Scalar Types (Single Value)**
- **Bit Types**:
  ```vhdl
  signal my_bit : bit := '1';
  signal my_vector : bit_vector(3 downto 0) := "1101";
  ```
- **Std_Logic Types** (More flexible than `bit`):
  ```vhdl
  signal my_signal : std_logic := '0';
  signal my_bus : std_logic_vector(7 downto 0) := "00001111";
  ```
- **Integer and Real Types**:
  ```vhdl
  signal count : integer := 10;
  signal voltage : real := 3.3;
  ```
- **Boolean Type**:
  ```vhdl
  variable flag : boolean := true;
  ```

### **2. Composite Types (Multiple Values)**
- **Arrays**:
  ```vhdl
  type data_array is array (0 to 3) of integer;
  signal my_array : data_array := (1, 2, 3, 4);
  ```
- **Records**:
  ```vhdl
  type person is record
      name : string(1 to 10);
      age : integer;
  end record;
  
  signal student : person := ("John Doe", 25);
  ```

### **3. Access (Pointer) Types**
- Used for dynamic memory allocation (not synthesizable).
  ```vhdl
  type ptr is access integer;
  variable my_ptr : ptr;
  ```

### **4. File Types**
- Used for reading/writing external data.
  ```vhdl
  file my_file : text;
  ```

---



