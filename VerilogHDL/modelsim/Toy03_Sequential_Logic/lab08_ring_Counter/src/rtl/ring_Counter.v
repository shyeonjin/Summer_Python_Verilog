`timescale 1ns/1ps

module ring_Counter(
  clk,
  rst,
  Q
);

  input clk,rst;
  output [3:0]Q;
  D_FF D1(Q[0],clk,rst,Q[1]);
  D_FF D2(Q[1],clk,rst,Q[2]);
  D_FF D3(Q[2],clk,rst,Q[3]);
  S_D_FF D4(Q[3],clk,rst,Q[0]);
endmodule


module D_FF(
  D,
  clk,
  rst,
  Q
);
input D,clk,rst;
output reg Q;

always @ (posedge clk,negedge rst)
begin 
  if (!rst)
  begin
    Q<=1'b0;
  end
  else
  Q<=D;
 
end
endmodule


module S_D_FF(
  D,
  clk,
  rst,
  Q
);
input D,clk,rst;
output reg Q;

always @ (posedge clk,negedge rst)
begin 
  if (!rst)
  begin
    Q<=1'b1;
  end
  else
  Q<=D;
end
endmodule