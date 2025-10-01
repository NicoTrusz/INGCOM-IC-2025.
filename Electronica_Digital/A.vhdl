library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity FuncLog_Nbits is
  generic (
    N : integer := 4
  );
  port (
    A  : in  signed(N-1 downto 0);
    B  : in  signed(N-1 downto 0);
    OP : in  std_logic;
    R  : out signed(N-1 downto 0)
  );
end entity;

architecture Behavioral of FuncLog_Nbits is
begin
  
R <= A and B when OP ='0' else 
  A or B;

end architecture;