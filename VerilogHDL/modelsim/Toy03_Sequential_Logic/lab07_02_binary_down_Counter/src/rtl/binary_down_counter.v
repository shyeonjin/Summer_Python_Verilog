`timescale 1ns/1ps

module binary_down_Counter(
  clk,
  rst,
  Q
);
input clk,rst;
output [2:0]Q;
wire t1,t2,t3;
T_FF T1(1'b1,clk,rst,Q[0],t1);
T_FF T2(1'b1,Q[0],rst,Q[1],t2);
T_FF T3(1'b1,Q[1],rst,Q[2],t3);


endmodule


module T_FF(T,clk,rst,Q,Qbar);
input clk,rst,T;
output reg Q,Qbar;
always @(posedge clk , negedge rst)
begin
    if (!rst)
    begin
        Q<=1'b0;
        Qbar<=1'b1;
    end
    else 
    begin 
        if (T==1'b1)
        begin
            Q<=~Q;
            Qbar<=~Qbar; 
        end
    end

end
endmodule