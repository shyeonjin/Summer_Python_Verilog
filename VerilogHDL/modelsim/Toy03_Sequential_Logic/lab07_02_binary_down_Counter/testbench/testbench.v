`timescale 1ns/1ps

module testbench();

    reg clk,rst;
    wire Q;

    binary_down_Counter bdco (
      clk,
      rst,
      Q
    );
    always #5 clk=~clk;

    initial
    begin
        clk=1'b0;rst=1'b0;
        #4 rst=1'b1;
        #100 $stop;
    end



endmodule