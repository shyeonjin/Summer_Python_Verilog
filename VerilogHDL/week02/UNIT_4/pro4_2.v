// 포트
// 포트는 모듈이 외부 환경과 소통할 수 있는 인터페이스이다.
// 포트를 통해서만 모듈과 외부환경이 상호 작용 할 수 있다.
// 외부 환경에서는 모듈의 내부를 볼 수 없다. 
// 이것은 설계자에게 매우 강력한 유연성을 제공한다.

// 예제 4-2 포트 리스트
module  fulladd4(sum,c_out,a,b,c_in);    // 포트 리스트를 가진다.
endmodule
module Top;                              // 포트 리스트가 없다. 시뮬레이션시 최상위 모듈이다.
endmodule

// 포드 선언
// input = 입력 포트, output = 출력 포트, inout = 양반향 포트

// 예제 4-3 포트 선언
module fulladd4(sum,c_out,a,b,c_in);

// 포트 선언 시작 부분
    output[3:0] sum;
    output c_count;
    
    input[3:0] a,b;
    input c_in;
// 포트 선언 끝 부분
...
< 모듈 내용>
...
endmodule


// Verilog에서 모든 포트 선언은 wire로 선언된다. 그러므로 만약 모든 포트를 wire로 할 생각이면
// 충분히 output, input 또는 inout으로 선언할 수 있다.
// input 또는 inout는 일반적으로 wire로 선언된다.
// 그런데 만약 output 포트가 값을 유지해야 한다면, 반드시 reg로 선언되어야 한다.


// 예제 4-4 DFF에 대한 Port 선언
module DFF(1,d,clk,reset);
output q;
reg q;
input d,clk,reset;
...
...
endmodule

// reg 변수는 값을 저장하는데, 입력 포트는 값을 저장하지 않고 
// 단순히 그것에 연결된 외부 신호에 의해 변환값을 그대로 전달만 하면 되기 때문에
// input과 inout현의 포트는 reg로 선언될 수 없다.

// 예제 4-5 ANSO C 형식의 포트 선언 구문
module fulladd4(output reg [3:0]sum, output reg c_out,
                input[3:0]a,b,
                input c_in);
...
< 모듈 내용>
...
endmodule


// 포트 연결 규칙(Port Connection Rules)

// 입력(input)
// 내부적으로 입력 포트는 반드시 넷형이다. 외부적으로 입력 포트는 reg 또는 넷 변수와 연결될 수 있다.

// 출력(output)
// 내부적으로 출력 포트는 reg 또는 넷형이다. 외부적으로 출력 포트는 반드시 넷과 연결되어야 한다.

// inout
// 내부적으로 입출력포트는 반드시 넷형이다. 외부적으로 입출력 포트는 반드시 넷과 연결되어야 한다.

// 크기 맞춤(Width matching)
// 모듈 포트 사이에 연결할 때, Verilog는 내부와 외부 항목이 서로 다른 크기를 가지는 연결을 허용한다.
// 그러나 크기를 맞추지 않는 것은 좋지 않다.

// 연결되지 않는 포트(Unconnected ports)
// Verilog는 포트를 연결하지 않은 채 내버려 둘 수 있다.


// 예제 4-6 올바르지 않은 포트 연결
module Top;

// 연결 변수의 선언.
reg [3:0]A,B;
reg C_IN;
wire [3:0] SUM;
wire C_OUT;

    // fa0라는 fulladd를 파생
    fulladd4 fa0(SUM,C_OUT,A,B,C_IN);
    // fulladd4 모듈에서 출력 포트 sum이 Top모듈 에서 레지스터 변수 SUM에
    // 연결되어 있기에 불법적인 연결이다.

endmodule


// 외부신호에 포트 연결하기
// 위치에 의한 포트 연결


// 예제 4-7 순서 리스트에 의한 연결

module Top;

// 연결 변수의 선언.
reg [3:0]A,B;
reg C_IN;
wire [3:0] SUM;
wire C_OUT;

    // fa0라는 fulladd를 파생
    fulladd4 fa0(SUM,C_OUT,A,B,C_IN);
    // fulladd4 모듈에서 출력 포트 sum이 Top모듈 에서 레지스터 변수 SUM에
    // 연결되어 있기에 불법적인 연결이다.

endmodule

module fulladd4(sum,c_out,a,b,c_in);
output [3:0] sum;
output c_cout;
input [3:0] a,b;
input c_in;
    ...
    < 모듈 내용 >
    ...
endmodule

// 이름에 의한 포트 연결
// 모듈 fa_byname의 파생과 이름에 의한 신호 연결
fulladd4 fa_byname(.c_out(C_OUT),.sum(SUM),b(B),.c_in(C_IN),a(A),);
