--DESIGN CODE STRUCTURAL MODELLING

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY NOT_Gate IS
    PORT (
        A : IN  std_logic;
        Y : OUT std_logic
    );
END NOT_Gate;

ARCHITECTURE dataflow OF NOT_Gate IS
BEGIN
    Y <= NOT A;
END dataflow;


LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY AND_Gate IS
    PORT (
        A, B, C : IN  std_logic;
        Y       : OUT std_logic
    );
END AND_Gate;

ARCHITECTURE dataflow OF AND_Gate IS
BEGIN
    Y <= A AND B AND C;
END dataflow;

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Decoder2to4 IS
    PORT (
        A  : IN  std_logic_vector(1 DOWNTO 0);
        EN : IN  std_logic;  
        Y  : OUT std_logic_vector(3 DOWNTO 0) 
    );
END Decoder2to4;

ARCHITECTURE structural OF Decoder2to4 IS
    
    COMPONENT NOT_Gate
        PORT (
            A  : IN  std_logic;
            Y  : OUT std_logic
        );
    END COMPONENT;

  
    COMPONENT AND_Gate
        PORT (
            A, B, C : IN  std_logic;
            Y       : OUT std_logic
        );
    END COMPONENT;

    SIGNAL A0_not, A1_not : std_logic;

BEGIN
   
    NOT1: NOT_Gate PORT MAP (A => A(0), Y => A0_not);
    NOT2: NOT_Gate PORT MAP (A => A(1), Y => A1_not);

    AND0: AND_Gate PORT MAP (A => EN, B => A1_not, C => A0_not, Y => Y(0));
    AND1: AND_Gate PORT MAP (A => EN, B => A1_not, C => A(0),  Y => Y(1));
    AND2: AND_Gate PORT MAP (A => EN, B => A(1),  C => A0_not, Y => Y(2));
    AND3: AND_Gate PORT MAP (A => EN, B => A(1),  C => A(0),  Y => Y(3));

END structural;








--TEST BENCH CODE
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY Decoder2to4_TB IS
END Decoder2to4_TB;

ARCHITECTURE behavior OF Decoder2to4_TB IS
    COMPONENT Decoder2to4
        PORT (
            A  : IN  std_logic_vector(1 DOWNTO 0);
            EN : IN  std_logic;
            Y  : OUT std_logic_vector(3 DOWNTO 0)
        );
    END COMPONENT;

    SIGNAL A  : std_logic_vector(1 DOWNTO 0);
    SIGNAL EN : std_logic;
    SIGNAL Y  : std_logic_vector(3 DOWNTO 0);

BEGIN
   
    UUT: Decoder2to4 PORT MAP (A => A, EN => EN, Y => Y);

    PROCESS
    BEGIN
        EN <= '1';
        
        A <= "00"; WAIT FOR 10 ns;
        A <= "01"; WAIT FOR 10 ns;
        A <= "10"; WAIT FOR 10 ns; 
        A <= "11"; WAIT FOR 10 ns; 

        EN <= '0'; 
        A <= "00"; WAIT FOR 10 ns; 
        A <= "01"; WAIT FOR 10 ns;
        A <= "10"; WAIT FOR 10 ns; 
        A <= "11"; WAIT FOR 10 ns;

        WAIT;
    END PROCESS;

END behavior;
