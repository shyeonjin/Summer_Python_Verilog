`timescale 1ns/1ps
module MUX_assign(
    A,
    B,
    C,
    D,
    Sel,
    OUT
);

input [3:0]A,B,C,D;
input [1:0]Sel;
output reg [3:0]OUT;

assign OUT= (Sel==2'h0)? A:
            (Sel==2'h1)? B:
            (Sel==2'h2)? C:
                         D;
endmodule
