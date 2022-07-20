`timescale 1ns/1ps

module digital_Comparartor(
  A,
  B,
  E,
  G,
  L
);

  input [1:0]A,B;
  output E,G,L;

  assign G = (A>B);
  assign E = (A==B);
  assign L = (A<B);

endmodule