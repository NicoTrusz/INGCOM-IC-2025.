-------------------------
--      ALU_Nbits        
--       Grupo 2         
--     integrantes       
--    Nicolás Trusz      
--    Tania Sanchesz     
-------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU_Nbits is
  generic ( N : integer := 4 );
  port (
    nro1  : in  signed(N-1 downto 0);
    nro2  : in  signed(N-1 downto 0);
    selec : in  std_logic_vector(1 downto 0);
    resul : out signed(N-1 downto 0);
    flags : out std_logic_vector(3 downto 0)
  );
end entity;

architecture RTL of ALU_Nbits is
  signal R_arit    : signed(N-1 downto 0);
  signal R_log     : signed(N-1 downto 0);
  signal zcvn_arit : std_logic_vector(3 downto 0);

  function ALUlogic(R: signed) return std_logic_vector is
    variable result : std_logic_vector(3 downto 0);
  begin
    result(3) := '1' when R = to_signed(0, R'length) else '0';  -- Z
    result(2) := '0';                                           -- C
    result(1) := '0';                                           -- V
    result(0) := R(R'length - 1);                               -- N
    return result;
  end function;

begin
 -- Unidad Aritmetica
  U_ARIT: entity work.SumArit_Nbits
    generic map (N => N)
    port map (
      A    => nro1,
      B    => nro2,
      OP   => selec(0),
      R    => R_arit,
      zcvn => zcvn_arit
    );
-- Unidad Logica
  U_LOG: entity work.FuncLog_Nbits
    generic map (N => N)
    port map (
      A => nro1,
      B => nro2,
      OP => selec(0),
      R => R_log
    );
-- Multiplexor
  with selec select
    resul <= R_arit when "00",
             R_arit when "01",
             R_log  when "10",
             R_log  when "11",
             (others => '0') when others;
-- llamada Flag bandera
  flags <= zcvn_arit when selec(1) = '0' else ALUlogic(R_log);

end architecture;



-----------------------------
-----------------------------
------------------------------
------------ALU MATI---------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU_Nbits is
	generic (N:integer := 4);
    port (
        nro1, nro2 : in signed(N-1 downto 0);
        selec : in std_logic_vector(1 downto 0);
        resul : out signed(N-1 downto 0);
        flags : out std_logic_vector(3 downto 0)
    );
end ALU_Nbits;

architecture Behavioral of ALU_Nbits is
signal signal_SumArit: signed(3 downto 0);
signal signal_FuncLog: signed(3 downto 0);

begin
	with selec(1) select
	resul <=  signal_SumArit when '0',
 		  signal_FuncLog when others;
                       
             
    FuncLog_unit : entity work.FuncLog_Nbits(Behavioral)
    	port map (A => nro1, B => nro2, r => signal_FuncLog, OP => selec(0));
    
    SumArit_unit : entity work.SumArit_Nbits(Behavioral)
    	port map (A => nro1, B => nro2, OP => selec(0), r => signal_SumArit, zcvn => flags);
        
end Behavioral;   