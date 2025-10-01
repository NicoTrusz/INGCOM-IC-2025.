library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity FuncLog_Nbits_tb is
end entity;

architecture Test of FuncLog_Nbits_tb is
  constant N : integer := 4;

  signal A, B : signed(N-1 downto 0);
  signal OP   : std_logic;
  signal R    : signed(N-1 downto 0);

begin
  UUT: entity work.FuncLog_Nbits
    generic map (N => N)
    port map (
      A  => A,
      B  => B,
      OP => OP,
      R  => R
    );

  test_proc: process
  begin
    -- Caso 1: A=1111, B=0001, OP=0 → AND
    A  <= to_signed(15, N);
    B  <= to_signed(1, N);
    OP <= "0";
    wait for 10 ns;

    -- Caso 2: A=0101, B=0101, OP=0 → AND
    A  <= to_signed(5, N);
    B  <= to_signed(5, N);
    OP <= "0";
    wait for 10 ns;

    -- Caso 3: A=0101, B=0101, OP=1 → OR
    A  <= to_signed(5, N);
    B  <= to_signed(5, N);
    OP <= "1";
    wait for 10 ns;

    -- Caso 4: A=1000, B=0111, OP=0 → AND
    A  <= to_signed(8, N);
    B  <= to_signed(7, N);
    OP <= "0";
    wait for 10 ns;

    -- Caso 5: A=1000, B=0111, OP=1 → OR
    A  <= to_signed(8, N);
    B  <= to_signed(7, N);
    OP <= "1";
    wait for 10 ns;

    -- Caso 6: A=0110, B=1010, OP=0 → AND
    A  <= to_signed(6, N);
    B  <= to_signed(10, N);
    OP <= "0";
    wait for 10 ns;

    -- Caso 7: A=0110, B=1010, OP=1 → OR
    A  <= to_signed(6, N);
    B  <= to_signed(10, N);
    OP <= "1";
    wait for 10 ns;

    wait;
  end process;
end architecture;

--ejemplo de assert con and
--assert (resul_4="1110") and (flags_test="0001") report "Fallo caso 8"