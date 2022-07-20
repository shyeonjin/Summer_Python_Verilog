`timescale 1ns/1ps

module Equality_Comparator(
  A,
  B,
  OUT
);
  input [1:0]A,B;
  output OUT;

  assign OUT = (A==B);

endmodule