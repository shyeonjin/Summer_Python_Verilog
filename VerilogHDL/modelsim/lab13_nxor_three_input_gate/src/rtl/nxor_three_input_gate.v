`timescale 1ns/1ps

module nxor_three_input_gate (
    first,second,third,
    out
);

  input first,second,third;
  output out;

  assign out = ((first+second+third)%2!=1)?1'b1:1'b0;

endmodule