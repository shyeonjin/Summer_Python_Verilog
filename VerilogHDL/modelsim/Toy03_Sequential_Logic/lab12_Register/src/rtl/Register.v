`timescale 1ns/1ps

module register(XQ,Ld,OQ,Rd,Y);
input [3:0]XQ;
input Ld,Rd;
output reg [3:0]Y,OQ;

always @(posedge Ld, negedge Rd)
begin
    if (Rd)
    begin
        OQ<=4'h0; 
    end 
    else OQ<=XQ;
end

always @ (Rd)
    if (Rd == 1'b1)
        Y <= OQ;
    else
        Y <= 4'h0;

endmodule