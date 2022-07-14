`timescale 1ns/1ps

module nor_gate (
    first,
    second,
    out
);

  input first,second;
  output out;

  assign out = ~(first||second);

endmodule