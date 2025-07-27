library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fullsubtractor is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           Bin : in STD_LOGIC;
           Diff : out STD_LOGIC;
           Bout : out STD_LOGIC);
end fullsubtractor;

architecture dataflow of fullsubtractor is
    signal input_vector : STD_LOGIC_VECTOR(2 downto 0);
begin
    input_vector <= A & B & Bin;
    
    Diff <= A xor B xor Bin;
    
    with input_vector select
        Bout <= '1' when "001",  
                 '1' when "010",  
                 '1' when "011",  
                 '1' when "110",  
                 '1' when "111",  
                 '0' when others;
end dataflow;

-- Testbench
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tbfullsubtractor is
end tbfullsubtractor;

architecture test of tbfullsubtractor is
    signal A, B, Bin, Diff, Bout : STD_LOGIC;
    
    component fullsubtractor
        Port ( A : in STD_LOGIC;
               B : in STD_LOGIC;
               Bin : in STD_LOGIC;
               Diff : out STD_LOGIC;
               Bout : out STD_LOGIC);
    end component;
    
begin
    uut: fullsubtractor port map (A => A, B => B, Bin => Bin, Diff => Diff, Bout => Bout);
    
    process
    begin
        A <= '0'; B <= '0'; Bin <= '0'; wait for 10 ns;
        A <= '0'; B <= '0'; Bin <= '1'; wait for 10 ns;
        A <= '0'; B <= '1'; Bin <= '0'; wait for 10 ns;
        A <= '0'; B <= '1'; Bin <= '1'; wait for 10 ns;
        A <= '1'; B <= '0'; Bin <= '0'; wait for 10 ns;
        A <= '1'; B <= '0'; Bin <= '1'; wait for 10 ns;
        A <= '1'; B <= '1'; Bin <= '0'; wait for 10 ns;
        A <= '1'; B <= '1'; Bin <= '1'; wait for 10 ns;
        wait;
    end process;
    
end test;
