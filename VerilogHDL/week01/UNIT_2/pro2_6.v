// 예제

// 설계 블록
// 예제 2-3 리플 캐리 카운터 Top 블록
module ripple_carry_counter(q,clk,reset);

output [3:0] q;
input clk,reset;

T_FF tff0(p[0],clk,reset);
T_FF tff1(q[1],q[0],reset);
T_FF tff2(q[2],q[1],reset);
T_FF tff3(q[3],q[2],reset);

endmodule

// 예제 2-4 플립플롭 T_FF


module T_FF(q,clk,reset);

output q;
input clk,reset;
wire d;

D_FF dff0(q,d,clk,reset);
not n1(d,q);

endmodule


// 예제 2-5 플립플롭 D_F

module D_FF(q,d,clk,reset);

output q;
input d, clk, reset;
reg q;


always @(posedge reset or negedge clk)
if (reset)
    q<=1'b0;
else
    q<=d;

endmodule

// 스티뮬러스 블록

// 예제 2-6 스티뮬러스 블록
module stimulus;

reg clk;
reg reset;
wire [3:0] q;

ripple_carry_counter r1 (q,clk, reset);

initial
    clk=1'b0;
always  
    #5 clk=~clk;


initial
begin
    reset=1'b1;
    #15 reset = 1'b0;
    #180 reset = 1'b1;
    #10 reset = 1'b0;
    #20 $finish;
end
    
initial 
    $monitor($time,"Out q=%d",q);
endmodule