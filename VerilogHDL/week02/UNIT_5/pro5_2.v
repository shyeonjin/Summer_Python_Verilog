// 게이트 지연
// 상승, 하강, 턴-오프 지연

// 예제 5-10 지연 명세의 형태
// 모든 변화에 대한 지연
and #(delay_time) a1(out,i1,i2);

// 상승과 하강 지연 명세
and #(rise_val,fall_val) a2(out,i1,i2);

// 상승, 하강 그리고 턴-오프 지연 명세
bufif0 #(rise_val,fall_val,turnoff_val) b1(out,in,control);


and #(5) a1(out,i1,i2);
and #(4,6) a2(out,i1,i2);
bufif0 #(3,4,5) b1(out,in,control);


// 예제 5-11 최소, 최대 그리고 전형적 지연값
// 1개의 지연값
// 만약 +mindelays이면, 지연=4
// 만약 +typdelays이면, 지연=5
// 만약 +maxdelays이면, 지연=6
and #(4:5:6) a1(out,i1,i2);

// 2개의 지연값

// 만약 +mindelays이면, 상승=3, 하강 5, 턴-오프= min(3,5)
// 만약 +typdelays이면, 상승=4, 하강 6, 턴-오프= min(4,6)
// 만약 +maxdelays이면, 상승=5, 하강 7, 턴-오프= min(5,7)
and #(3:4:5,5:6:7) a2(out,i1,i2);

// 3개의 지연값
// 만약 +mindelays이면, 상승=2, 하강 3, 턴-오프= 4
// 만약 +typdelays이면, 상승=3, 하강 4, 턴-오프= 5
// 만약 +maxdelays이면, 상승=4, 하강 5, 턴-오프= 6
and #(2:3:4,3:4:5,4:5:6) a3(out,i1,i2);


// 지연 예제
// 예제 5-12 지연을 감안한 모듈 D의 Verilog 기술
// D라는 간단한 조합회로 모듈 정의
module D(out,a,b,c);

// I/O 포트 선언
output out;
input a,b,c;

// 내부 넷
wire a;

// 회로를 설계하기 위한 프리미티브 게이트의 파생
and #(5) a1(e,a,b);
or #(5) o1(out ,e,c);
endmodule

// 예제 5-13 지연을 감안한 모듈 D 스티뮬러스
module stimulus;

// 변수선언
reg A,B,C;
wire OUT;

// 모듈 D파생
D d1(OUT,A,B,C);

initial
begin
    A=1'b0; B=1'b0; C=1'b0;
    #10 A=1'b1; B=1'b1; C=1'b1;
    #10 A=1'b1; B=1'b0; C=1'b0;
    #20 $finish;
end
endmodule