`timescale 1ns/1ps

module DEMUX(
    A,B,C,D,
    IN,
    Sel
);

  input [7:0] IN;
  input [1:0] Sel;
  output reg [7:0]A,B,C,D;

  assign A=(Sel==2'h0)?IN:8'h00;
  assign B=(Sel==2'h1)?IN:8'h00;
  assign C=(Sel==2'h2)?IN:8'h00;
  assign D=(Sel==2'h3)?IN:8'h00;
  

endmodule