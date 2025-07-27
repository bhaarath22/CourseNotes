--DESIGN CODE Structural Modelling

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY NOT_GATE IS
    PORT (
        A : IN std_logic;
        Y : OUT std_logic
    );
END NOT_GATE;

ARCHITECTURE behavior OF NOT_GATE IS
BEGIN
    Y <= NOT A;
END behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
ENTITY AND_GATE IS
    PORT (
        A, B, C : IN std_logic;
        Y       : OUT std_logic  ); END AND_GATE;



ARCHITECTURE behavior OF AND_GATE IS
BEGIN
    Y <= A AND B AND C;
END behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY DEMUX1to4 IS
    PORT (
        I  : IN std_logic;
        S  : IN std_logic_vector(1 DOWNTO 0);  
        Y0, Y1, Y2, Y3 : OUT std_logic 
    );
END DEMUX1to4;

ARCHITECTURE structural OF DEMUX1to4 IS

    COMPONENT NOT_GATE
        PORT (
            A : IN std_logic;
            Y : OUT std_logic
        );
    END COMPONENT;

    COMPONENT AND_GATE
        PORT (
            A, B, C : IN std_logic;
            Y       : OUT std_logic
        );
    END COMPONENT;

    SIGNAL S0_not, S1_not : std_logic;  

BEGIN
   
    NOT1: NOT_GATE PORT MAP (A => S(0), Y => S0_not);
    NOT2: NOT_GATE PORT MAP (A => S(1), Y => S1_not);
    
    AND1: AND_GATE PORT MAP (A => I, B => S1_not, C => S0_not, Y => Y0);  
    AND2: AND_GATE PORT MAP (A => I, B => S1_not, C => S(0), Y => Y1);    
    AND3: AND_GATE PORT MAP (A => I, B => S(1), C => S0_not, Y => Y2);   
    AND4: AND_GATE PORT MAP (A => I, B => S(1), C => S(0), Y => Y3);      
END structural;

--Test bench Code

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY DEMUX_TB IS
END DEMUX_TB;

ARCHITECTURE behavior OF DEMUX_TB IS
    SIGNAL I  : std_logic; 
    SIGNAL S  : std_logic_vector(1 DOWNTO 0);  
    SIGNAL Y0, Y1, Y2, Y3 : std_logic;

    COMPONENT DEMUX1to4
        PORT (
            I  : IN std_logic;
            S  : IN std_logic_vector(1 DOWNTO 0);
            Y0, Y1, Y2, Y3 : OUT std_logic
        );
    END COMPONENT;

BEGIN
    
    UUT: DEMUX1to4 PORT MAP (I => I, S => S, Y0 => Y0, Y1 => Y1, Y2 => Y2, Y3 => Y3);

    PROCESS
    BEGIN
        I <= '1'; S <= "00"; WAIT FOR 10 ns;
        I <= '1'; S <= "01"; WAIT FOR 10 ns;
        I <= '1'; S <= "10"; WAIT FOR 10 ns;
        I <= '1'; S <= "11"; WAIT FOR 10 ns;

        I <= '0'; S <= "00"; WAIT FOR 10 ns;
        I <= '0'; S <= "01"; WAIT FOR 10 ns;
        I <= '0'; S <= "10"; WAIT FOR 10 ns;
        I <= '0'; S <= "11"; WAIT FOR 10 ns;

        WAIT;
    END PROCESS;
END behavior;
