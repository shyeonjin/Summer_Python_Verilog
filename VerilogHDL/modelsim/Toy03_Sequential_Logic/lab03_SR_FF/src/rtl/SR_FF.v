`timescale 1ns/1ps

module SR_FF(
  S,
  R,
  Q,
  CLK,
  rst,
  Qbar
);

  input S,R,CLK,rst;
  output reg Q,Qbar;

  
  always @(posedge CLK,negedge rst)
  begin
        if (!rst)
        begin
            Q <= 1'b0;
            Qbar <= 1'b1;
        end
        else
        begin 
            if (S == 1'b1)
            begin
                Q <= 1'b1;
                Qbar <= 1'b0;
            end
            else if (R == 1'b1)
            begin
                Q <= 1'b0;
                Qbar <= 1'b1;
            end
        end
    end
endmodule