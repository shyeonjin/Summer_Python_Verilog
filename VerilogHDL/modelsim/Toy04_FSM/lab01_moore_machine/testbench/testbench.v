`timescale 1ns/1ps

module testbench;

reg clk,rst,din;

always #5 clk = ~clk;
moore_machine moma(
	.clk(clk),
	.rst(rst),
	.din(din),
	.dout(dout)
);

initial begin
    clk = 1'b0; din = 1'b0;rst = 1'b0;
	#7 rst = 1'b1;
    #5 din = 1'b1;
    #20 din = 1'b0;
    #20 din = 1'b1;
    #10 din = 1'b0;
    #30 din = 1'b1;
    #10 din = 1'b0;
    #40 din = 1'b1;
	#(10)   $stop;
end


endmodule