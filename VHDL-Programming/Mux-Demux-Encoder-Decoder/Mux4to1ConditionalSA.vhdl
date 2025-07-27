--Design Code Data Flow Modeling
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY MUX4to1 IS
    PORT (
        A, B, C, D : IN std_logic; 
        S          : IN std_logic_vector(1 DOWNTO 0); 
        Y          : OUT std_logic);
END MUX4to1;
ARCHITECTURE dataflow OF MUX4to1 IS
BEGIN
    
    Y <= A WHEN S = "00" ELSE  
         B WHEN S = "01" ELSE 
         C WHEN S = "10" ELSE 
         D;                    
END dataflow;


--Test Bench Code
LIBRARY ieee;
﻿﻿USE ieee.std_logic_1164.ALL;

ENTITY TB_MUX4to1 IS
END TB_MUX4to1;

ARCHITECTURE behavior OF TB_MUX4to1 IS
    SIGNAL A, B, C, D, Y : std_logic;
    SIGNAL S : std_logic_vector(1 DOWNTO 0);
    COMPONENT MUX4to1
        PORT (
            A, B, C, D : IN std_logic;
            S          : IN std_logic_vector(1 DOWNTO 0);
            Y          : OUT std_logic
        );
    END COMPONENT;

BEGIN
    UUT: MUX4to1 PORT MAP (A => A, B => B, C => C, D => D, S => S, Y => Y);
    PROCESS
    BEGIN
        A <= '0'; B <= '1'; C <= '0'; D <= '1'; 
        S <= "00";
        WAIT FOR 10 ns;
        S <= "01";
        WAIT FOR 10 ns;
        S <= "10";
        WAIT FOR 10 ns;
        S <= "11";
        WAIT FOR 10 ns;

        WAIT;
    END PROCESS;
END behavior;
