`timescale 1ns/1ps

module testbench();

    reg J,K,clk,rst;
    wire Q,Qbar;

    JK_FF JK (
      .J(J),
      .K(K),
      .clk(clk),
      .rst(rst),
      .Q(Q),
      .Qbar(Qbar)
    );

    initial
    begin
      clk=1'b0;
      forever
      begin
        #5 clk=~clk;
      end
    end

    initial
    begin
        J=1'b0; K=1'b0;rst=1'b0;
        #7 rst=1'b1;
        #10 J=1'b0; K=1'b0;
        #10 J=1'b1; K=1'b0;
        #10 J=1'b0; K=1'b1;
        #10 J=1'b1; K=1'b1;
        #30 $stop;
    end



endmodule