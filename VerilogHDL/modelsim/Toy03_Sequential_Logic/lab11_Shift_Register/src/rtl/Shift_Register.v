`timescale 1ns/1ps


module Shift_Register(
  SL,
  SR,
  Q,
  clk,
  rst
);
input SL,SR,clk,rst;
output [3:0]Q;

reg [3:0] D_Q;

always @ ( SL,SR,posedge clk,Q)
begin
  if (SL==1'b1 && SR==1'b0)
  begin
    D_Q[0]=1'b0;
    D_Q[1]=Q[0];
    D_Q[2]=Q[1];
    D_Q[3]=Q[2];
  end

  else if(SL==1'b0 && SR==1'b1)
  begin
    D_Q[0]=Q[1];
    D_Q[1]=Q[2];
    D_Q[2]=Q[3];
    D_Q[3]=1'b0;
  end
  else
    D_Q <= Q;
end


R_D_FF RDFF1(D_Q[0],Q[0],rst,clk);
R_D_FF RDFF2(D_Q[1],Q[1],rst,clk);
R_D_FF RDFF3(D_Q[3],Q[3],rst,clk);
D_FF DFF1(D_Q[2],Q[2],rst,clk);

endmodule


module D_FF(
  D,
  Q,
  rst,
  clk
);
input clk,rst,D;
output reg Q;
 
always @ (posedge clk, negedge rst)
begin
  if(!rst)
  begin
    Q<=1'b0;
  end
  else Q<=D;
end
endmodule

module R_D_FF(
  D,
  Q,
  rst,
  clk
);
input clk,rst,D;
output reg Q;
always @ (posedge clk, negedge rst)
begin
  if(!rst)
  begin
    Q<=1'b1;
  end
  else Q<=D;
end
endmodule