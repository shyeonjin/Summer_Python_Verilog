`timescale 1ns/1ps
module MUX_always(
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

always @(A,B,C,D,Sel)
begin
    if (Sel==2'h0)
    begin
        OUT=A;
    end
    else if(Sel==2'h1)
    begin
        OUT=B;
    end
    else if(Sel==2'h2)
    begin
        OUT=C;
    end
    else 
    begin
        OUT=D;
    end
end

endmodule
