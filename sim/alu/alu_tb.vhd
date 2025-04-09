library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_tb is
    port (
        x         : in std_logic_vector(31 downto 0);
        y         : in std_logic_vector(31 downto 0);
        s         : in std_logic_vector(3 downto 0);
        result    : out std_logic_vector(31 downto 0);
        zero_flag : out std_logic
    );
end entity alu_tb;

architecture tb of alu_tb is

    component alu
        port (
            x         : in std_logic_vector(31 downto 0);
            y         : in std_logic_vector(31 downto 0);
            s         : in std_logic_vector(3 downto 0);
            result    : out std_logic_vector(31 downto 0);
            zero_flag : out std_logic
        );
    end component;

begin

    dut: alu
        port map (
            x         => x,
            y         => y,
            s         => s,
            result    => result,
            zero_flag => zero_flag
        );

end architecture tb;