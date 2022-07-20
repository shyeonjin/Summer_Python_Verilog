`timescale 1ns/1ps

module half_adder(
  first,
  second,
  C_OUT,
  out
);

  input first,second;
  output C_OUT,out;

  assign {C_OUT,out} = first+second;

endmodule