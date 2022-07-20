`timescale 1ns/1ps

module half_Subtractor(
  first,
  second,
  B,
  D
);

  input first,second;
  output B,D;

  assign {B,D} = first+(~second+1);

endmodule