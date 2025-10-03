-- Code your testbench here
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity TB_ALU_Nbits is
end entity;

architecture sim of TB_ALU_Nbits is
  constant N : integer := 4;

  type caso_t is record
    A_bin : std_logic_vector(N-1 downto 0);
    B_bin : std_logic_vector(N-1 downto 0);
    OP    : std_logic_vector(1 downto 0);
  end record;

  type tabla_t is array (natural range <>) of caso_t;

  constant casos : tabla_t := (
    (A_bin => "1111", B_bin => "0001", OP => "00"),
    (A_bin => "0101", B_bin => "0101", OP => "00"),
    (A_bin => "0101", B_bin => "0101", OP => "01"),
    (A_bin => "1000", B_bin => "0111", OP => "00"),
    (A_bin => "1000", B_bin => "0111", OP => "01"),
    (A_bin => "0110", B_bin => "1010", OP => "00"),
    (A_bin => "0110", B_bin => "1010", OP => "01"),
    (A_bin => "1101", B_bin => "1100", OP => "10"),
    (A_bin => "1101", B_bin => "1101", OP => "11")
  );

  signal nro1  : signed(N-1 downto 0);
  signal nro2  : signed(N-1 downto 0);
  signal selec : std_logic_vector(1 downto 0);
  signal resul : signed(N-1 downto 0);
  signal flags : std_logic_vector(3 downto 0);

begin

  UUT: entity work.ALU_Nbits
    generic map (N => N)
    port map (
      nro1  => nro1,
      nro2  => nro2,
      selec => selec,
      resul => resul,
      flags => flags
    );

  TestbenchProcess: process
  begin
    for i in casos'range loop
      nro1  <= signed(casos(i).A_bin);
      nro2  <= signed(casos(i).B_bin);
      selec <= casos(i).OP;
      wait for 10 ns;

      report "Caso " & integer'image(i);
      report ": A=" & to_hstring(casos(i).A_bin); 
      report " B=" & to_hstring(casos(i).B_bin);
      report " OP=" & to_hstring(casos(i).OP); 
      report "flags = " & to_hstring(flags);
	  report "resul = " & to_hstring(std_logic_vector(resul));

    end loop;
    wait;
  end process;

end architecture;