--DESIGN CODE DATA FLOW Modelling

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Encoder4to2 IS
    PORT (
        D : IN  std_logic_vector(3 DOWNTO 0);
        Y : OUT std_logic_vector(1 DOWNTO 0)
    );
END Encoder4to2;

ARCHITECTURE dataflow OF Encoder4to2 IS
BEGIN
    Y(1) <= D(3) OR D(2);
    Y(0) <= D(3) OR (NOT D(2) AND D(1));
END dataflow;

--TEST BENC CODE
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Encoder4to2_TB IS
END Encoder4to2_TB;

ARCHITECTURE behavior OF Encoder4to2_TB IS

    COMPONENT Encoder4to2
        PORT (
            D : IN  std_logic_vector(3 DOWNTO 0);
            Y : OUT std_logic_vector(1 DOWNTO 0)
        );
    END COMPONENT;

    SIGNAL D : std_logic_vector(3 DOWNTO 0);
    SIGNAL Y : std_logic_vector(1 DOWNTO 0);

BEGIN

    UUT: Encoder4to2 PORT MAP (D => D, Y => Y);

    PROCESS
    BEGIN
        D <= "0001"; WAIT FOR 10 ns;
        D <= "0010"; WAIT FOR 10 ns;
        D <= "0100"; WAIT FOR 10 ns;
        D <= "1000"; WAIT FOR 10 ns;
        D <= "1100"; WAIT FOR 10 ns;
        D <= "1010"; WAIT FOR 10 ns;
        D <= "0110"; WAIT FOR 10 ns;
        D <= "1111"; WAIT FOR 10 ns;

        WAIT;
    END PROCESS;

END behavior;
