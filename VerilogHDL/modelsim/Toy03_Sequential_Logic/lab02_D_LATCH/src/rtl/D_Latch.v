`timescale 1ns/1ps

module D_Latch(
  D,
  Q,
  Qbar
);
input D;
output Q,Qbar;

assign Q=(D==1'b0)?1'b0:1'b1;
assign Qbar=(D==1'b0)?1'b1:1'b0;

endmodule