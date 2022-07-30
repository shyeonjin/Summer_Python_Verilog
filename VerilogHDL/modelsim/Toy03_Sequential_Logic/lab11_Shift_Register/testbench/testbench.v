`timescale 1ns/1ps

module testbench();
  reg clk,rst,SL,SR;
  wire Q;  
  Shift_Register SHR(SL,SR,Q,clk,rst);
    always #5 clk = ~clk;
    initial begin
        rst = 1'b0; SR = 1'b0; SL = 1'b0; clk = 1'b0;
        #3 rst = 1'b1;
        #7 SR =1'b1; SL = 1'b0;
        #30 SR = 1'b0; SL = 1'b1;
        #60 $stop;
    end
endmodule