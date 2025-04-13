library ieee;
use ieee.std_logic_1164.all;

entity mux is
    port (
        a   : in  std_logic_vector(31 downto 0);
        b   : in  std_logic_vector(31 downto 0);
        sel : in  std_logic;
        y   : out std_logic_vector(31 downto 0)
    );
end entity;

architecture rtl of mux is
begin
    y <= a when sel = '0' else b;
end architecture;
