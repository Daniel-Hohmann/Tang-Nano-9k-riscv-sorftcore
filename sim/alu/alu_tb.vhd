library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity alu_tb is
    port (
        x         : out std_logic_vector(31 downto 0); -- Eingabe x
        y         : out std_logic_vector(31 downto 0); -- Eingabe y
        s         : out std_logic_vector(3 downto 0);  -- Steuerungssignal für die ALU-Operation
        result    : in std_logic_vector(31 downto 0);  -- Ergebnis der ALU-Operation (Eingang für Testbench)
        zero_flag : in std_logic                       -- Zero-Flag (Eingang für Testbench)
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

    -- Interne Signale für Testbench
    signal x_sig         : std_logic_vector(31 downto 0) := (others => '0'); -- Initialisiere mit '0'
    signal y_sig         : std_logic_vector(31 downto 0) := (others => '0'); -- Initialisiere mit '0'
    signal s_sig         : std_logic_vector(3 downto 0) := (others => '0');  -- Initialisiere mit '0'
    signal result_sig    : std_logic_vector(31 downto 0);
    signal zero_flag_sig : std_logic;

begin

    -- Ports mit internen Signalen verbinden
    x <= x_sig;
    y <= y_sig;
    s <= s_sig;

    result_sig <= result;       -- Ergebnis der ALU an Testbench zurückgeben
    zero_flag_sig <= zero_flag; -- Zero-Flag der ALU an Testbench zurückgeben

    -- ALU-Instanz mit Verbindungen
    dut: alu
        port map (
            x         => x_sig,
            y         => y_sig,
            s         => s_sig,
            result    => result_sig,
            zero_flag => zero_flag_sig
        );

end architecture tb;

