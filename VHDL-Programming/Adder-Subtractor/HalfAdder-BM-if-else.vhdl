-- desing
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Half_Adder is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        Sum : out STD_LOGIC;
        Carry : out STD_LOGIC
    );
end Half_Adder;

architecture Behavioral of Half_Adder is
begin
    process(A, B)
    begin
        if (A = '0' and B = '0') then
            Sum <= '0';
            Carry <= '0';
        elsif (A = '0' and B = '1') then
            Sum <= '1';
            Carry <= '0';
        elsif (A = '1' and B = '0') then
            Sum <= '1';
            Carry <= '0';
        else
            Sum <= '0';
            Carry <= '1';
        end if;
    end process;
end Behavioral;

--Testbench
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Half_Adder_tb is
end Half_Adder_tb;

architecture testbench of Half_Adder_tb is
    signal A, B, Sum, Carry : STD_LOGIC;
    component Half_Adder
        Port (
            A : in STD_LOGIC;
            B : in STD_LOGIC;
            Sum : out STD_LOGIC;
            Carry : out STD_LOGIC
        );
    end component;
begin
    uut: Half_Adder port map (A, B, Sum, Carry);
    process
    begin
        A <= '0'; B <= '0';
        wait for 10 ns;
        A <= '0'; B <= '1';
        wait for 10 ns;
        A <= '1'; B <= '0';
        wait for 10 ns;
        A <= '1'; B <= '1';
        wait for 10 ns;
        wait;
    end process;
end testbench;



