library ieee;
use ieee.std_logic_1164.all;

entity alu_control_tb is
end entity;

architecture rtl of alu_control_tb is
    signal alu_op      : std_logic_vector(1 downto 0);
    signal funct3      : std_logic_vector(2 downto 0);
    signal funct7      : std_logic_vector(6 downto 0);
    signal alu_control : std_logic_vector(3 downto 0);
begin
    uut: entity work.alu_control
        port map (
            alu_op      => alu_op,
            funct3      => funct3,
            funct7      => funct7,
            alu_control => alu_control
        );
end architecture;
