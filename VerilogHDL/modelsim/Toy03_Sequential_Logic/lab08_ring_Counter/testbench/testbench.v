`timescale 1ns/1ps

module testbench();

    reg clk,rst;
    wire [3:0]Q;

    ring_Counter rc (
      clk,
      rst,
      Q
    );
    always #5 clk=~clk;
    
    initial
    begin
        clk=1'b0;rst=1'b0;
        #10 rst=1'b1;
        #200 $stop;
    end



endmodule