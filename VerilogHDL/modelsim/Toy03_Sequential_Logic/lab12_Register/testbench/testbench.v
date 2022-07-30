module testbench();
reg [3:0]XQ;
reg Ld,Rd;
wire [3:0]OQ,Y;

register rg(XQ,Ld,OQ,Rd,Y);

initial begin
    Ld = 1'b0; Rd = 1'b0; XQ =4'h0;
    #5 XQ = 4'b0101;
    #10 Ld = 1'b1;
    #5 XQ = 4'b1100;
    #15 Rd = 1'b1; 
    #40 $stop;
end
endmodule 