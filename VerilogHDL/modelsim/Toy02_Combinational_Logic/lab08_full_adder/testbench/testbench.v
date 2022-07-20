`timescale 1ps/1ps

module testbench();
    reg a, b, c;
    wire carry, out;

    full_adder fa(a, b, c, carry, out);

    initial begin
        a = 1'b0; b = 1'b0; c = 1'b0;
        #10 a = 1'b0; b = 1'b0; c = 1'b1;
        #10 a = 1'b0; b = 1'b1; c = 1'b0;
        #10 a = 1'b0; b = 1'b1; c = 1'b1;
        #10 a = 1'b1; b = 1'b0; c = 1'b0;
        #10 a = 1'b1; b = 1'b0; c = 1'b1;
        #10 a = 1'b1; b = 1'b1; c = 1'b0;
        #10 a = 1'b1; b = 1'b1; c = 1'b1;
        #10 $stop;
    end
endmodule