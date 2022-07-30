`timescale 1ns/1ps

module testbench();

    reg T,clk,rst;
    wire Q,Qbar;

    T_FF TFF (
      .T(T),
      .clk(clk),
      .rst(rst),
      .Q(Q),
      .Qbar(Qbar)
    );

    always #5 clk=~clk; 
    
    

    initial
    begin
        T=1'b0; rst=1'b0;clk=1'b0;
        #3 rst=1'b1;
        #7 T=1'b1;
        #20 T=1'b0;
        #20 T=1'b1;
        #20 T=1'b0;
        #60 $stop;
    end



endmodule