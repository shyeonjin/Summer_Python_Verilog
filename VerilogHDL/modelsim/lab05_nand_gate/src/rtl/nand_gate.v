`timescale 1ns/1ps

module nand_gate (
    first,,second,
    out
);

  input first,second;
  output out;

  assign out = ~(first&&second);

endmodule