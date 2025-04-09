library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.alu_pkg.all; -- getting the ALU Constants from alu_pkg.vhd

entity alu is
    port (
        -- inputs
        x           : in std_logic_vector(31 downto 0);
        y           : in std_logic_vector(31 downto 0);
        s           : in std_logic_vector(3 downto 0);
        -- outputs
        result      : out std_logic_vector(31 downto 0);
        zero_flag   : out std_logic
    );
end entity alu;

architecture rtl of alu is 
    signal x_s, y_s : signed(31 downto 0); -- for refrenzes and calculations
    signal res : signed(31 downto 0) := to_signed(0, 32);
begin
    -- convert the inputs to signed for Calculation
    x_s <= signed(x);
    y_s <= signed(y);

    process (x_s, y_s, s)
    begin
        case s is
            when ALU_OP_ADD =>
                res <= x_s + y_s;

            when ALU_OP_SUB =>
                res <= x_s - y_s;

            when ALU_OP_AND =>
                res <= x_s and y_s;

            when ALU_OP_OR =>
                res <= x_s or y_s;

            when ALU_OP_XOR =>
                res <= x_s xor y_s;

            when ALU_OP_SLL =>
                res <= shift_left(x_s, to_integer(unsigned(y(4 downto 0))));  -- nur untere 5 Bit
            
            when ALU_OP_SRL =>
                if x_s < 0 then
                    -- If x is negative, we calculate the amount and apply shift_right to unsigned.
                    res <= signed(shift_right(unsigned(-x_s), to_integer(unsigned(y(4 downto 0)))));
                else
                    -- If x is positive, apply shift_right directly to unsigned.
                    res <= signed(shift_right(unsigned(x_s), to_integer(unsigned(y(4 downto 0)))));
                end if;

            when ALU_OP_SLT =>
                if x_s < y_s then
                    res <= (others => '0');
                    res(0) <= '1';
                else
                    res <= (others => '0');
                end if;
            
            when others =>
                res <= (others => '0');
        end case;
   end process;
    result <= std_logic_vector(res);
    zero_flag <= '1' when res = 0 else '0';
end architecture;
