`timescale 1ps/1ps

module testbench();
    reg clk, rst, S, R;
    wire Q, Qbar;
    SR_FF srff(.S(S),.R(R),.Q(Q),.CLK(clk),.rst(rst),.Qbar(Qbar));
    initial begin
        clk = 1'b0;
        forever
        begin
            #5 clk = ~clk;
        end
    end
    initial begin
        rst = 1'b0; S = 1'b0; R = 1'b0;
        #7  rst = 1'b1; S = 1'b1; R = 1'b0;
        #10 S = 1'b1; R = 1'b0;
        #10 S = 1'b0; R = 1'b0;
        #10 S = 1'b0; R = 1'b1;
        #10 S = 1'b0; R = 1'b1;
        #10 S = 1'b0; R = 1'b0;
        #10 $stop;
    end
endmodule