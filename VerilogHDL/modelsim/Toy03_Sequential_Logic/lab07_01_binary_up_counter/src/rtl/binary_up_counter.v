`timescale 1ps/1ps

module binary_up_Counter(
    clk,
    rst,
    Q,
);

input clk,rst;
output [2:0]Q;
wire t0,t1,t2;
T_FF T1(1'b1,clk,rst,Q[0],t0);
T_FF T2(Q[0],clk,rst,Q[1],t1);
T_FF T3(Q[0] && Q[1],clk,rst,Q[2],t2);

endmodule

module T_FF(
    T,
    clk,
    rst,
    Q,
    Qbar
);
input T,clk,rst;
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
