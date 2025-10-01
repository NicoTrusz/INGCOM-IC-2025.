library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_SumArit_Nbits is
end entity;

architecture Test of tb_SumArit_Nbits is
  constant N : integer := 4;

  signal A, B     : signed(N-1 downto 0);
  signal OP       : std_logic;
  signal R        : signed(N-1 downto 0);
  signal zcvn     : std_logic_vector(3 downto 0);

begin
  DUT: entity work.SumArit_Nbits
    generic map (N => N)
    port map (
      A    => A,
      B    => B,
      OP   => OP,
      R    => R,
      zcvn => zcvn
    );

  stim_proc: process
  begin
    -- Caso 1: 0101 + 0101 = 1010, sin overflow
    A <= to_signed(5, N); B <= to_signed(5, N); OP <= '0';
    wait for 10 ns;
    assert R = to_signed(10, N) report "Error en suma 5+5" severity error;
    assert zcvn = "0010" report "Flags incorrectos en suma 5+5" severity error;

    -- Caso 2: 0111 + 0001 = 1000, con overflow
    A <= to_signed(7, N); B <= to_signed(1, N); OP <= '0';
    wait for 10 ns;
    assert R = to_signed(-8, N) report "Error en suma 7+1" severity error;
    assert zcvn = "0011" report "Flags incorrectos en suma 7+1" severity error;

    -- Caso 3: 0110 - 1010 = 0110 + 0110 = 1100, sin overflow
    A <= to_signed(6, N); B <= to_signed(-6, N); OP <= '1';
    wait for 10 ns;
    assert R = to_signed(12, N) report "Error en resta 6-(-6)" severity error;
    assert zcvn = "0010" report "Flags incorrectos en resta 6-(-6)" severity error;

    -- Caso 4: 1111 - 0001 = 1110, sin overflow
    A <= to_signed(-1, N); B <= to_signed(1, N); OP <= '1';
    wait for 10 ns;
    assert R = to_signed(-2, N) report "Error en resta -1-1" severity error;
    assert zcvn = "0001" report "Flags incorrectos en resta -1-1" severity error;

    -- Caso 5: 0100 - 0100 = 0000, flag Z = 1
    A <= to_signed(4, N); B <= to_signed(4, N); OP <= '1';
    wait for 10 ns;
    assert R = to_signed(0, N) report "Error en resta 4-4" severity error;
    assert zcvn = "1000" report "Flags incorrectos en resta 4-4" severity error;

    wait;
  end process;

end architecture;
