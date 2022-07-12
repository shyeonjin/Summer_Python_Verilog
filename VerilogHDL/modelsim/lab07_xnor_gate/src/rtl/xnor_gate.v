`timescale 1ns/1ps

module xnor_gate (
    first,
    second,
    out
);

  input first,second;
  output out;

  assign out = ((first+second)%2!=1)?1'b1:1'b0;


endmodule