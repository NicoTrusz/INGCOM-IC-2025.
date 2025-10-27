---------------------------------
----- Electrónica Digital -------
----- Taller 4 - Grupo 1 --------
-------- ALU_Reg_Nbits ----------
---------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU_Reg_Nbits is
    generic (
        N : integer := 4
    );
    port (
        clk : in STD_LOGIC;
        w : in STD_LOGIC_VECTOR(1 downto 0);
        en_out : in STD_LOGIC;
        a : in signed(N-1 downto 0);
        b : in signed(N-1 downto 0);
        flags : out std_logic_vector(3 downto 0);
        result : out signed(N-1 downto 0)
    );
end ALU_Reg_Nbits;

architecture Behavioral of ALU_Reg_Nbits is
    component ALU_Nbits is
        generic (
            N : integer := 4
        );
        port (
            nro1, nro2 : in signed(N-1 downto 0);
            selec : in std_logic_vector(1 downto 0);
            resul : out signed(N-1 downto 0);
            flags : out std_logic_vector(3 downto 0)
        );
    end component;

    signal reg_a, reg_b, reg_result : signed(N-1 downto 0);
    signal flags_int : std_logic_vector(3 downto 0);
begin
    ALU_unit: ALU_Nbits
        port map (
            nro1 => reg_a,
            nro2 => reg_b,
            selec => "00", -- Definimos la operación como suma
            resul => reg_result,
            flags => flags_int
        );

    process (clk)
    begin
        if rising_edge(clk) then
            if w = "11" then
                reg_a <= "0111"; -- Primer operando (7 en binario)
                reg_b <= "1111"; -- Segundo operando (-1 en binario)
            end if;
        end if;
    end process;

    process
    begin
        wait for 10 ns;
        assert reg_result = "0110" report "Resultado incorrecto" severity error; -- Resultado esperado: 6 en binario
        wait;
    end process;
end Behavioral;

-----------------------------------------
-----------------------------------------
-----------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU_Reg_Nbits_Testbench is
end ALU_Reg_Nbits_Testbench;

architecture Behavioral of ALU_Reg_Nbits_Testbench is
    component ALU_Reg_Nbits is
        generic (
            N : integer := 4
        );
        port (
            clk : in STD_LOGIC;
            w : in STD_LOGIC_VECTOR(1 downto 0);
            en_out : in STD_LOGIC;
            a : in signed(3 downto 0);
            b : in signed(3 downto 0);
            flags : out std_logic_vector(3 downto 0);
            result : out signed(3 downto 0)
        );
    end component;

    signal clk : STD_LOGIC := '0';
    signal w : STD_LOGIC_VECTOR(1 downto 0) := "11"; -- Habilitamos la escritura para ambos registros
    signal en_out : STD_LOGIC := '0';
    signal a : signed(3 downto 0);
    signal b : signed(3 downto 0);
    signal flags : std_logic_vector(3 downto 0);
    signal result : signed(3 downto 0);

begin
    DUT: ALU_Reg_Nbits
        port map (
            clk => clk,
            w => w,
            en_out => en_out,
            a => a,
            b => b,
            flags => flags,
            result => result
        );

    clk_process: process
    begin
        while now < 60 ns loop
            clk <= not clk;
            wait for 10 ns;
        end loop;
        wait;
    end process;

    stimulus_process: process
    begin
        wait for 100 ns; -- Esperamos un tiempo para estabilizar la señal
        assert result = "0110" report "Resultado incorrecto" severity error; -- Resultado esperado: 6 en binario
        wait;
    end process;

end Behavioral;