library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package alu_pkg is 

    -- ALU Operations as Constant's
    constant ALU_OP_ADD : std_logic_vector(3 downto 0) := "0000";
    constant ALU_OP_SUB : std_logic_vector(3 downto 0) := "0001";
    constant ALU_OP_AND : std_logic_vector(3 downto 0) := "0010";
    constant ALU_OP_OR : std_logic_vector(3 downto 0) := "0011";
    constant ALU_OP_XOR : std_logic_vector(3 downto 0) := "0100";
    constant ALU_OP_SLL : std_logic_vector(3 downto 0) := "0101"; -- Shift Left Logical
    constant ALU_OP_SRL : std_logic_vector(3 downto 0) := "0110"; -- Shift Right Logical
    constant ALU_OP_SLT : std_logic_vector(3 downto 0) := "0111"; -- Set Less Than

end package;