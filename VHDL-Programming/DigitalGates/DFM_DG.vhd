-- Design Code
library IEEE;
use IEEE.std_logic_1164.all;

entity DigitalGatesDF is
    port (
        a, b : in std_logic;
        and_out, or_out, not_out, nand_out, nor_out, xor_out, xnor_out : out std_logic
    );
end DigitalGatesDF;

architecture DGDF of DigitalGatesDF is
begin
    and_out  <= a and b;
    or_out   <= a or b;
    not_out  <= not a;
    nand_out <= a nand b;
    nor_out  <= a nor b;
    xor_out  <= a xor b;
    xnor_out <= a xnor b;
end DGDF;


-- Test Bench Code
library IEEE;
use IEEE.std_logic_1164.all;

entity TBDG is
end TBDG;

architecture tb of TBDG is
    component DigitalGatesDF
        port (
            a, b : in std_logic;
            and_out, or_out, not_out, nand_out, nor_out, xor_out, xnor_out : out std_logic
        );
    end component;

    signal a, b : std_logic;
    signal and_out, or_out, not_out, nand_out, nor_out, xor_out, xnor_out : std_logic;

begin
    
    uut: DigitalGatesDF
        port map(
            a => a, b => b,
            and_out => and_out, or_out => or_out, not_out => not_out,
            nand_out => nand_out, nor_out => nor_out, xor_out => xor_out,
            xnor_out => xnor_out
        );

   
    process
    begin
        a <= '0'; b <= '0'; wait for 10 ns;
        a <= '1'; b <= '0'; wait for 10 ns;
        a <= '0'; b <= '1'; wait for 10 ns;
        a <= '1'; b <= '1'; wait for 10 ns;
        wait; 
    end process;

end tb;
