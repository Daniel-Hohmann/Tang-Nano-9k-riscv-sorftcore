library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comparator is
    port (
        a  : in  std_logic_vector(31 downto 0);
        b  : in  std_logic_vector(31 downto 0);
        eq : out std_logic;
        ne : out std_logic;
        lt : out std_logic;
        ge : out std_logic
    );
end entity;

architecture rtl of comparator is
    signal a_s, b_s : signed(31 downto 0);
begin
    a_s <= signed(a);
    b_s <= signed(b);

    eq <= '1' when a_s = b_s else '0';
    ne <= '1' when a_s /= b_s else '0';
    lt <= '1' when a_s < b_s else '0';
    ge <= '1' when a_s >= b_s else '0';
end architecture;
