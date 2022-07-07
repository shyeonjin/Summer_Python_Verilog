// 데이터 형

// 논리값 집합
// 0 = 논리적 0, 거짓 상태
// 1 = 논리적 1, 참 상태
// x = 알 수 없는 논리 값
// z = 하이 임피던스, 플로팅 상태


// 넷(Nets)
// 넷은 키워드가 아니라 wire, wand, wor, tri, triand, trior,trireg 등의 집합으로 나타낸다.
wire a;     // 위의 회로에서 넷 a를 정의
wire b,c;   // 위의 회로에서 넷 b,c를 정의
wire d=1'b0 // 냇 d는 논리값 0으로 선언


// 레지스터
// 레지스터는 데이터를 저장할 수 있다.
// 레지스터는 다른 논리값이 들어오기 전까지는 그 값을 유지할 수 있다.


// 예제 3-1: 레지스터의 예제
reg reset;
initial begin
    reset=1'b1
    #100 reset=1'b0;
end

// 예제 3-2: 부호 있는 레지스터의 선언
reg signed [63:0] m;
integer i;

// 벡터
wire a;
wire [7:0] bus;
wire [31:0] busA,busB,busC;
reg clock;
reg [0:40] virtural_addr;

// 벡터 부분 선택
busA[7]  //7번 비트
bus[2:0] //3개의 하위비트

virtual_addr[0:1] // 2개의 상위 비트

// 가변 벡터 부분 선택
reg [255:0] data1;  // 리틀-엔디언 표기법
reg [0:255] data2;  // 빅- 엔디언 표기법
reg [7:0] byte;

// 가변 부분 선택을 사용, 각각은 부분들을 선택할 수 있다.
byte=data1[31-:8]; // starting bit =31, width =8 =>data[31:24]
byte=data1[24+:8]; // starting bit =24, width =8 =>data[31:24]
byte=data1[31-:8]; // starting bit =31, width =8 =>data[24:31]
byte=data1[24+:8]; // starting bit =24, width =8 =>data[24:31]

for (j=0;j<=31;j=j+1)
    byte=data1[(j*8)+:8];

// 벡터부분 초기화
data1[(byteNim*8)+:8]=8'b0;


// 정수, 실수, 시간 레지스터 데이터형
// 정수
integer counter;    //counter로 사용되는 범용 변수.
initial
counter=-1;         //counter에 음수 1을 저장

// 실수
real delta;         // delta라는 실수를 정의.
initial
begin
    delta=4e10;     // delta에 과학적 표기법으로 대입.
    delra=2.13;     // delta에 2.13을 대입.
end
integer i;          // 정수 i를 정의
initial 
    i=delta;    // i는 2값을 가진다

// 시간
time save_sim_time;  // 시간 변수 save_sim_time을 정의.
initial 
    save_sim_time=$time;   // 현재 시뮬레이션 시간을 저장.

// 배열
integer count[0:7];         // 8 count 변수의 배열.
reg bool[31:0];             // 32 1-비트 boolean 레지스터 변수의 배열.
time clk_point[1:100];      // 100 time chk_point 변수의 배열.
reg [4:0] port_id[0:7];     // 8 port_id의 배열; 각 port_id는 5-비트의 폭을 가진다.
integer matrix[4:0][0:255]; // 정수형 이차원 배열.
reg[63:0] array_4d[15:0][7:0][7:0][225:0];    // 사차원 배열.
wire[7:0] w_array2[5:0];    // 8-비트 벡터 와이어 배열 선언.
wire w_array1[7:0][5:0];    // 싱글 비트 와이어의 배열 선언.


count[5]=0;         
chk_point[100]=0;
port_id[3]=0;

matrix[1][0]=33559;
array_4d[0][0][0][15:0]=0;


port_id=0; 
matrix[1]=0;



// 메모리

reg mem1bit[0:1023];
reg[7:0] membyte[0:1023];
membyte[511]


// 파라미터
parameter port_id = 5;              // 상수 port_id 정의
parameter cache_line_width=256;     // 캐쉬 줄의 폭을 정의한 상수
parameter signed [15:0] WIDTH;      // 파라미터 WIDTH에 대한 부호와 범위 고정


localparam  state1 = 4'b0001,
            state2 = 4'b0010,
            state3 = 4'b0100,
            state4 = 4'b1000;


// 문자열

reg [8*18:1] string_value;
initial
    string_value ="Hello Verilog World";