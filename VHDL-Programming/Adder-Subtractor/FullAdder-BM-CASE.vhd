library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fullAdder is
    Port ( A : in STD_LOGIC;
           B : in STD_LOGIC;
           Cin : in STD_LOGIC;
           Sum : out STD_LOGIC;
           Cout : out STD_LOGIC);
end fullAdder;

architecture Behavioral of fullAdder is
begin
    process(A, B, Cin)
    variable input_vector : STD_LOGIC_VECTOR(2 downto 0);
    begin
        input_vector := A & B & Cin;
        case input_vector is
            when "000" => Sum <= '0'; Cout <= '0';
            when "001" => Sum <= '1'; Cout <= '0';
            when "010" => Sum <= '1'; Cout <= '0';
            when "011" => Sum <= '0'; Cout <= '1';
            when "100" => Sum <= '1'; Cout <= '0';
            when "101" => Sum <= '0'; Cout <= '1';
            when "110" => Sum <= '0'; Cout <= '1';
            when "111" => Sum <= '1'; Cout <= '1';
            when others => Sum <= '0'; Cout <= '0';
        end case;
    end process;
end Behavioral;


-- test bench code
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tbfullAdder is
end tbfullAdder;

architecture testbench of tbfullAdder is
    signal A, B, Cin, Sum, Cout : STD_LOGIC;
    component fullAdder
        Port ( A : in STD_LOGIC;
               B : in STD_LOGIC;
               Cin : in STD_LOGIC;
               Sum : out STD_LOGIC;
               Cout : out STD_LOGIC);
    end component;

begin
    UUT: fullAdder port map (A => A, B => B, Cin => Cin, Sum => Sum, Cout => Cout);

    process
    begin
        A <= '0'; B <= '0'; Cin <= '0'; wait for 10 ns;
        A <= '0'; B <= '0'; Cin <= '1'; wait for 10 ns;
        A <= '0'; B <= '1'; Cin <= '0'; wait for 10 ns;
        A <= '0'; B <= '1'; Cin <= '1'; wait for 10 ns;
        A <= '1'; B <= '0'; Cin <= '0'; wait for 10 ns;
        A <= '1'; B <= '0'; Cin <= '1'; wait for 10 ns;
        A <= '1'; B <= '1'; Cin <= '0'; wait for 10 ns;
        A <= '1'; B <= '1'; Cin <= '1'; wait for 10 ns;
        wait;
    end process;
end testbench;
