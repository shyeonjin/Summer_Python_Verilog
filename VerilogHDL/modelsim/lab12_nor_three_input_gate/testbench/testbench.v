`timescale 1ns/1ps

module testbench();

    reg a,b,c;
    wire out;

    nor_three_input_gate ntig (
      .first(a),
      .second(b),
      .third(c),
      .out(out)
    );

    initials
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