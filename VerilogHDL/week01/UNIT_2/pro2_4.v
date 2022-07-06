// 인스턴스
// 모듈은 실제 객체를 만들 수 있는 템플릿을 제고안다.
// 모듈이 불러졌을 때, Verilog는 템플릿으로부터 고유한 객체를 생성한다.
// 각 객체는 이름, 변수, 파라미터, 그리고 입출력 인터페이스를 가지고 있다.
// 모듈 템플릿으로부터 객체를 생성하는 것을 파생(instantiation)이라고 하고, 객체를 인스턴스라고 한다.

// 예제 2-1: 모듈 파생

// 리플 캐리 카운터라는 최상위 블록을 정의한다.
// 이건은 4개의 T-플립플롭을 파생한다.

module ripple_carry_counter(q,clk,reset)

output [3:0] q;
input clk,reset;

T_FF tff0(q[0],clk,reset);
T_FF tff1(q[1],q[0],reset);
T_FF tff2(q[2],q[1],reset);
T_FF tff3(q[3],q[2],reset);

endmodule

module T_FF(q,clk,reset);

output q;
input clk,reset;
wire d;

D_FF dff0(q,d,clk,reset);
not n1(d,q);

endmodule


// 모듈안에 다른 모듈이 존재할 수 없다.
// 예
module ripple_carry_counter(q,clk,reset);

output [3:0] q;
input clk,reset;

    module T_FF(q,clock,reset);
    ...
    < 모듈 T_FF의 내용>
    ...
    endmodule


endmodule