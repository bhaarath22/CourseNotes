--Design  Behavioral Modelling

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY PriorityEncoder4to2 IS
    PORT (
        D : IN  std_logic_vector(3 DOWNTO 0);
        Y : OUT std_logic_vector(1 DOWNTO 0)
    );
END PriorityEncoder4to2;

ARCHITECTURE behavioral OF PriorityEncoder4to2 IS
BEGIN
    PROCESS (D)
    BEGIN
        IF D(3) = '1' THEN
            Y <= "11";  
        ELSIF D(2) = '1' THEN
            Y <= "10";  
        ELSIF D(1) = '1' THEN
            Y <= "01";  
        ELSIF D(0) = '1' THEN
            Y <= "00";  
        ELSE
            Y <= "00";  
        END IF;
    END PROCESS;
END behavioral;

--Test Bench code
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY PriorityEncoder4to2_TB IS
END PriorityEncoder4to2_TB;

ARCHITECTURE behavior OF PriorityEncoder4to2_TB IS

    COMPONENT PriorityEncoder4to2
        PORT (
            D : IN  std_logic_vector(3 DOWNTO 0);
            Y : OUT std_logic_vector(1 DOWNTO 0)
        );
    END COMPONENT;

    SIGNAL D : std_logic_vector(3 DOWNTO 0);
    SIGNAL Y : std_logic_vector(1 DOWNTO 0);

BEGIN

    UUT: PriorityEncoder4to2 PORT MAP (D => D, Y => Y);

    PROCESS
    BEGIN
        D <= "0001"; WAIT FOR 10 ns; 
        D <= "0010"; WAIT FOR 10 ns; 
        D <= "0100"; WAIT FOR 10 ns; 
        D <= "1000"; WAIT FOR 10 ns; 
        D <= "0000"; WAIT FOR 10 ns; 

        WAIT;
    END PROCESS;

END behavior;
