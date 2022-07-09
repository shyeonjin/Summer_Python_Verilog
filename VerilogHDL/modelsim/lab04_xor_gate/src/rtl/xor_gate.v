`timescale 1ns/1ps

module xor_gate (
    a,b,
    out
);

  input a,b;
  output out;

  assign out = ((a+b)%2==1)? 1'b1:1'b0;
endmodule