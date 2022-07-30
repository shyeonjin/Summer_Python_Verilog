`timescale 1ns/1ps

module Johnson_Counter(
  clk,
  rst,
  Q
);

  input clk,rst;
  output [3:0]Q;

D_FF D1(Q[1],Q[0],clk,rst);
D_FF D2(Q[2],Q[1],clk,rst);
D_FF D3(Q[3],Q[2],clk,rst);
D_FF D4(~Q[0],Q[3],clk,rst);
endmodule


module D_FF(
  D,
  Q,
  clk,  
  rst);
  input D,clk,rst;
  output reg Q;
  always @ (posedge clk, negedge rst)
  begin 
    if (!rst)
    begin
      Q<=1'b0;
    end
    else 
    Q<=D;
  end 
endmodule



