`timescale 1ns/1ps

module testbench();

    reg a,b,c;
    wire out;

    xor_three_input_gate xtig (
      .first(a),
      .second(b),
      .third(c),
      .out(out)
    );

    initial
    begin
        a=1'b0;b=1'b0;c=1'b0;
        #10 a=1'b0; b=1'b0; c=1'b1;
        #10 a=1'b0; b=1'b1; c=1'b0;
        #10 a=1'b0; b=1'b1; c=1'b1;
        #10 a=1'b1; b=1'b0; c=1'b0;
        #10 a=1'b1; b=1'b0; c=1'b1;
        #10 a=1'b1; b=1'b1; c=1'b0;
        #10 a=1'b1; b=1'b1; c=1'b1;
        #10;
    end


endmodule