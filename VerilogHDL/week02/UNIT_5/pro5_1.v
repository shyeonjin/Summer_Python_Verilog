// 게이트 형태
// 예제 5-1 And/Or 게이트 파생
wire OUT,IN1,IN2;

// 기본적인 게이트 파생
and a1(OUT,IN1,IN2);
nand na1(OUT,IN1,IN2);
or or1(OUT,IN1,IN2);
nor nor1(OUT,IN1,IN2);
xor x1(OUT,IN1,IN2);
xnor nx1(OUT,IN1,IN2);

// 두 개 이상의 입력: 3개의 입력을 가진 nand 게이트
nand na1_3inp(OUT,IN1,IN2,IN3);

// 인스턴스 이름이 없는 게이트 파생
and (OUT,IN1,IN2);


// BUf/Not 게이트
// 예제 5-2 BUf/Not 게이트 파생
// 기본적인 게이트의 파생
buf b1(OUT1,IN);
not n1(OUT1,IN);

// 두 개 이상의 출력
buf b1_2out(OUT1,OUT2,IN);

// 인스턴스 이름이 없는 게이트 파생
not (OUT1,IN);


// 예제 5-3 Bufif/Notif 게이트 파생
// bufif의 파생
bufif1 b1(out,in,ctr1);
bufif0 b0(out,in,ctr1);

// notif의 파생
notif1 n1(out,in,ctr1);
notif0 n0(out,in,ctr1);

// 인스턴스의 배열
// 예제 5-4 프리미티브 인스턴스의 간단한 배열
wire [7:0] OUT,IN1,IN2;

// 기본 게이트 파생
nand n_gate[7:0](OUT,IN1,IN2);

// 위의 것은 아래의 8개를 파생하는 것과 같다.

nand n_gate0(OUT[0],IN1[0],IN2[0]);
nand n_gate1(OUT[1],IN1[1],IN2[1]);
nand n_gate2(OUT[2],IN1[2],IN2[2]);
nand n_gate3(OUT[3],IN1[3],IN2[3]);
nand n_gate4(OUT[4],IN1[4],IN2[4]);
nand n_gate5(OUT[5],IN1[5],IN2[5]);
nand n_gate6(OUT[6],IN1[6],IN2[6]);
nand n_gate7(OUT[7],IN1[7],IN2[7]);



// 예제 5-5 멀티플렉서의 Verilog 기술
// 4:1 멀티플렉서 모듈. 포트리스트는 I/O 다이어그램에서 직관적으로 알 수 있다.
module mux4_to_1(out,i0,i1,i2,i3,s1,s0);

output out;
input i0,i1,i2,i3;
input s1,s0;

// 내부 wire 선언
wire s1n,s0n;
wire y0,y1,y2,y3;

// 게이트 파생.s1n, s0n 신호를 생성
not (s1n,s1);
not (s0n,s0);

// 3input AND 게이트 파생
and (y0,i0,s1n,s0n);
and (y1,i1,s1n,s0);
and (y2,i2,s1,s0n);
and (y3,i3,s1,s0);

// 4개 입력을 갖는 OR 게이트 파생
or (out,y0,y1,y2,y3);

endmodule


// 예제 5-6 멀티플렉서 스티뮬러스
// 스티뮬러스 모듈을 정의 (포트가 없다.)
module stimulus;

// 입력으로 연결되는 변수들을 정의.
reg IN0,IN1,IN2,IN3;
reg S1,S0;

// 출력 wire 선언
wire OUTPUT;

// 멀티플렉서의 파생.
mux4_to_1 mymux(OUTPUT,IN0,IN1,IN2,IN3,S1,S0);

// 입력 스티뮬러스 생성, 스티뮬러스 모듈 정의 (포트없음).
initial
begin
    // 입력 라인을 셋
    IN0=1;IN1=0;IN2=1;IN3=0;
    #1 $display("IN0 = %b,IN1 = %b,IN2 = %b,IN3 = %b\n",IN0,IN1,IN2,IN3);

    // IN0를 선택
    s1=0;s0=0;
    #1 $display("S1 = %b,S0 = %b, OUTPUT = %b",S1,S0,OUTPUT);

    // IN1를 선택
    s1=0;s0=1;
    #1 $display("S1 = %b,S0 = %b, OUTPUT = %b",S1,S0,OUTPUT);
    
    // IN2를 선택
    s1=1;s0=0;
    #1 $display("S1 = %b,S0 = %b, OUTPUT = %b",S1,S0,OUTPUT);
    
    // IN3를 선택
    s1=1;s0=1;
    #1 $display("S1 = %b,S0 = %b, OUTPUT = %b",S1,S0,OUTPUT);
end

endmodule



// 예제 5-7 1비트 전가산기의 Verilog 기술

// 1-비트 전가산기의 정의 
module fulladd(sum,c_out,a,b,c_in);

// I/O 포트 선언
output sum,c_out;
input a,b,c_in;

// 내부 넷
wire s1,c1,c2;

// 프리미티브 논리 게이트의 파생
xor (s1,a,b);
and (c1,a,b);

xor(sum,s1,c_in)
and(c2,s1,c_in)

xor(c_out,c2,c1);
endmodule



// 예제 5-8 4-비트 전가산기의 Verilog 기술
// 4-비트 전가산기 정의
module fulladd4(sum,c_out,a,b,c_in);

output[3:0]sum;
output c_out;
input[3:0]a,b;
input c_in;

// 내부 넷
wire c1,c2,c3;

// 4개의 1-비트 전가산기의 파생
fulladd fa0(sum[0],c1,a[0],b[0],c_in);
fulladd fa1(sum[1],c2,a[1],b[1],c1);
fulladd fa2(sum[2],c3,a[2],b[2],c2);
fulladd fa3(sum[3],c_out,a[3],b[3],c3);

endmodule


// 예제 5-9 4-비트 전가산기 스티뮬러스
// 스티뮬러스 블로의 정의 (최상위 모듈)
module stimulus;

// 변수를 선언 
reg[3:0]A,B;
reg C_IN;
wire[3:0] SUM;
wire C_OUT;

// FA_1이라는 4-비트 전가산기를 파생
fulladd4 FA1_4(SUM,C_OUT,A,B,C,C_IN);

// 신호값을 출력
initial
begin
    $monitor($time,"A=%b, B=%b,C_IN=%b,---C_OUT=%b,SUM=%b\n",A,B,C_IN,C_OUT,SUM);
end
// 스티뮬러스 입력
initial
begin
    A=4'd0; B=4'd0; C_IN=1'b0;
    
    #5 A=4'd3; B=4'd4; 
    #5 A=4'd2; B=4'd5; 
    #5 A=4'd9; B=4'd9; 
    #5 A=4'd10; B=4'd15; 
    #5 A=4'd10; B=4'd5; C_IN=1'b1;
end
endmodule
