library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_control is
    port (
        alu_op      : in std_logic_vector(1 downto 0);
        funct3      : in std_logic_vector(2 downto 0);
        funct7      : in std_logic_vector(6 downto 0);
        alu_control : out std_logic_vector(3 downto 0)
    );
end entity;
architecture rtl of alu_control is
begin
    process(alu_op, funct3, funct7)
    begin
        case alu_op is
            when "10" =>  -- R-Typ Instruktionen
                case funct3 is
                    when "000" =>
                        if funct7 = "0000000" then
                            alu_control <= "0000";  -- ADD
                        elsif funct7 = "0100000" then
                            alu_control <= "0001";  -- SUB
                        else
                            alu_control <= (others => '0');
                        end if;
                    when "111" =>
                        alu_control <= "0010";  -- AND
                    when "110" =>
                        alu_control <= "0011";  -- OR
                    when "100" =>
                        alu_control <= "0100";  -- XOR
                    when "001" =>
                        alu_control <= "0101";  -- SLL
                    when others =>
                        alu_control <= (others => '0');
                end case;

            when "00" =>  -- Load/Store (ADD für Adressberechnung)
                alu_control <= "0000";  -- ADD

            when "01" =>  -- Branch (SUB für Vergleich)
                alu_control <= "0001";  -- SUB

            when others =>
                alu_control <= (others => '0');
        end case;
    end process;
end architecture;
