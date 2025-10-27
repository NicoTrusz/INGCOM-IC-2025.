---------------------------------
----- Electrónica Digital -------
----- Taller 4 - Grupo 1 --------
---------- Reg_Nbits ------------
---------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity Reg_Nbits is
    generic (N : integer := 4);
    port (
        clk : in std_logic;
        w_i : in std_logic;
        en_out_i : in std_logic;
        D : in std_logic_vector(N-1 downto 0);
        Q : out std_logic_vector(N-1 downto 0)
    );
end entity Reg_Nbits;

architecture Behavioral of Reg_Nbits is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if w_i = '1' then
                Q <= D;
            end if;
        end if;
    end process;

    Q <= (others => 'Z') when en_out_i = '0' else Q;
end architecture Behavioral;

------------------------------------
-------------TESTBENCH--------------
------------------------------------
library ieee;
use ieee.std_logic_1164.all;

entity tb_Reg_Nbits is
end entity tb_Reg_Nbits;

architecture Behavioral of tb_Reg_Nbits is
    constant N : integer := 4;
    signal clk : std_logic := '0';
    signal w_i : std_logic := '0';
    signal en_out_i : std_logic := '0';
    signal D : std_logic_vector(N-1 downto 0) := (others => '0');
    signal Q : std_logic_vector(N-1 downto 0);
begin
    uut: entity work.Reg_Nbits(Behavioral)
        generic map (N => N)
        port map (
            clk => clk,
            w_i => w_i,
            en_out_i => en_out_i,
            D => D,
            Q => Q
        );

    tb: process
    begin
        -- Test case: Escribir un valor y ver que se almacene correctamente
        w_i <= '1'; -- Habilitar escritura
        D <= "1010"; -- Escribir valor
        wait for 10 ns; -- Esperar un ciclo

        assert Q = "1010" report "Test failed: Q should be 1010" severity error;

        -- Test case: Reset y revisar que se mantenga el valor
        D <= (others => '0'); -- Reset
        wait for 10 ns; -- Esperar un ciclo

        assert Q = "1010" report "Test failed: Q should still be 1010" severity error;

        wait;
    end process tb;

    clk <= not clk after 5 ns; -- Generador de señal de clock
end architecture Behavioral;