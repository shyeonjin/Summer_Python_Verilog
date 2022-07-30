`timescale 1ns/1ps

module testbench();

    reg clk,rst;
    wire Q;

    Johnson_Counter JSC (
      .clk(clk),
      .rst(rst),
      .Q(Q)
     );
    always #5 clk=~clk;

    initial
    begin
        clk=1'b0; rst=1'b0;
        #7 rst=1'b1;
        #300 $stop;
    end



endmodule