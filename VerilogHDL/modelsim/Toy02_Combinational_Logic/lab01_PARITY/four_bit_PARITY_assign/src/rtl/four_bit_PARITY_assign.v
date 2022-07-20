`timescale 1ns/1ps

module four_bit_PARITY_assign(
    IN,
    odd_out,
    even_out  
);

  input [3:0] IN;
  output wire odd_out,even_out;

  assign odd_out=(IN<4'b1010)?((^IN%2==0)?1'b1:1'b0):(1'bx);
  assign even_out=(IN<4'b1010)?((^IN%2==1)?1'b1:1'b0):(1'bx);
endmodule