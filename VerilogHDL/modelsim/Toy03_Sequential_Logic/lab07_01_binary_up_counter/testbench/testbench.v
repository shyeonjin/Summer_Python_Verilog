`timescale 1ps/1ps

module testbench();
    reg clk, rst;
    wire [2:0]Q;
    binary_up_Counter binuc(clk, rst, Q);
    always #5 clk = ~clk;
    initial begin
        clk = 1'b0; rst = 1'b0;
        #7 rst = 1'b1;
        #200 $stop;
    end
endmodule