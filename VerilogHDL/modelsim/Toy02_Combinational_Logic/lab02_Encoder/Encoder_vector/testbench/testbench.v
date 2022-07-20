`timescale 1ns/1ps

module testbench();

    reg [7:0]IN;

    Encoder_vector ENV (
      .IN(IN)
      );

    initial
    begin
        IN = 8'b0000_0001;
        #10 IN = 8'b0000_0010;
        #10 IN = 8'b0000_0100;
        #10 IN = 8'b0000_1000;
        #10 IN = 8'b0001_0000;
        #10 IN = 8'b0010_0000;
        #10 IN = 8'b0100_0000;
        #10 IN = 8'b1000_0000;
        #10 ;

    end

endmodule