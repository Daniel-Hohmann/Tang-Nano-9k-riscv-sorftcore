library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity register_file is
    port (
        clk              : in  std_logic;  -- Clock
        reset            : in  std_logic;  -- Reset
        reg_write        : in  std_logic;  -- Enable Write
        reg_read1        : in  std_logic_vector(4 downto 0); -- Address for Register 1
        reg_read2        : in  std_logic_vector(4 downto 0); -- Address for Register 2
        reg_write_addr   : in  std_logic_vector(4 downto 0); -- Write Address
        reg_write_data   : in  std_logic_vector(31 downto 0); -- Write Data
        reg_data1        : out std_logic_vector(31 downto 0);  -- Data Output Register 1
        reg_data2        : out std_logic_vector(31 downto 0)   -- Data Output Register 2
    );
end entity register_file;

architecture rtl of register_file is
    type reg_array is array (0 to 31) of std_logic_vector(31 downto 0);
    signal registers : reg_array := (others => (others => '0')); -- Register array initialized to 0
begin
    -- Register Read Operations
    process(clk, reset)
    begin
        if reset = '1' then
            registers <= (others => (others => '0')); -- Reset all registers to 0
        elsif rising_edge(clk) then
            if reg_write = '1' then
                registers(to_integer(unsigned(reg_write_addr))) <= reg_write_data;  -- Write data to specified register
            end if;
        end if;
    end process;

    -- Register Read Data Outputs
    reg_data1 <= registers(to_integer(unsigned(reg_read1))); -- Read data from register 1
    reg_data2 <= registers(to_integer(unsigned(reg_read2))); -- Read data from register 2
end architecture rtl;

