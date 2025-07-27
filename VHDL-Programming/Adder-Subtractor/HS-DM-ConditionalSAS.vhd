library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity halfsubtractor is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           Diff : out STD_LOGIC;
           Borrow : out STD_LOGIC);
end halfsubtractor;

architecture dataflow of halfsubtractor is
begin
    Diff <= '1' when (A /= B) else '0';
    Borrow <= '1' when (A = '0' and B = '1') else '0';
end dataflow;

-- Testbench
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tbhalfsubtractor is
end tbhalfsubtractor;

architecture test of tbhalfsubtractor is
    signal A, B, Diff, Borrow : STD_LOGIC;
    
    component halfsubtractor
        Port ( A : in STD_LOGIC;
               B : in STD_LOGIC;
               Diff : out STD_LOGIC;
               Borrow : out STD_LOGIC);
    end component;
    
begin
    uut: halfsubtractor port map (A => A, B => B, Diff => Diff, Borrow => Borrow);
    
    process
    begin
        A <= '0'; B <= '0'; wait for 10 ns;
        A <= '0'; B <= '1'; wait for 10 ns;
        A <= '1'; B <= '0'; wait for 10 ns;
        A <= '1'; B <= '1'; wait for 10 ns;
        wait;
    end process;
    
end test;
