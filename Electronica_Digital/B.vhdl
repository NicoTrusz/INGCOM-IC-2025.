library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity SumArit_Nbits is
  generic ( N : integer := 8 );
  port (
    A     : in  signed(N-1 downto 0);
    B     : in  signed(N-1 downto 0);
    OP    : in  std_logic;
    R     : out signed(N-1 downto 0);
    zcvn  : out std_logic_vector(3 downto 0)
  );
end entity;

architecture Behavioral of SumArit_Nbits is
  signal B_mod   : signed(N-1 downto 0);
  signal result  : signed(N downto 0); -- 1 bit extra para detectar carry
begin

  -- Operación: suma o resta
  B_mod <= B when OP = '0' else -B;
  result <= resize(A, N+1) + resize(B_mod, N+1);
  R <= result(N-1 downto 0);

  -- Flags
  zcvn(3) <= '1' when result(N-1 downto 0) = 0 else '0'; -- Zero
  zcvn(2) <= result(N);                                   -- Carry/Borrow
  zcvn(1) <= '1' when (A(N-1) = B_mod(N-1)) and (R(N-1) /= A(N-1)) else '0'; -- Overflow
  zcvn(0) <= '1' when R(N-1) = '1' else '0';                                 -- Negativo

end architecture;
