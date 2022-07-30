`timescale 1ns/1ps

module testbench();

    reg D,clk,rst;
    wire Q,Qbar;

    D_FF DFF (
      .D(D),
      .clk(clk),
      .rst(rst),
      .Q(Q),
      .Qbar(Qbar)
    );
    initial begin
        clk = 1'b0;
        forever begin
            #5 clk = ~clk;
        end
    end

    initial
    begin
        D=1'b0; rst=1'b0;
        #3 rst=1'b1;
        #10 D=1'b1;
        #10 D=1'b0;
        #10 $stop;
    end



endmodule