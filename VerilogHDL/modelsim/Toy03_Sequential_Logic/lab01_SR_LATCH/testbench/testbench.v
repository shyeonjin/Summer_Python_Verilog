`timescale 1ps/1ps

module testbench();
   reg S,R;
   SR_LATCH SL(
        .S(S),
        .R(R)
        );



    initial begin
        S=1'b0; R=1'b0;
        #10 S = 1'b0; R = 1'b1;
        #10 S = 1'b1; R = 1'b0;
        #10 S = 1'b1; R = 1'b1;
        #10 ;
    end
endmodule