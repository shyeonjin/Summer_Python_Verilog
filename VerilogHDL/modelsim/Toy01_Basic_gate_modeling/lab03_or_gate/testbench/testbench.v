`timescale 1ns/1ps

module testbench();

    reg a,b;
    wire out;

    or_gate og(
      .a(a),
      .b(b),
      .out(out)
    );

    initial
    begin
        a=1'b0;b=1'b0;
        #10 a=1'b1;b=1'b0;
        #10 a=1'b0;b=1'b1;
        #10 a=1'b1;b=1'b1;
        #10 ;
    end
endmodule