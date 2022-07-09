`timescale 1ns/1ps

module nor_three_input_gate (
    first,second,third,
    out
);

  input first,second,third;
  output out;

  assign out = ~(first||second||third);

endmodule