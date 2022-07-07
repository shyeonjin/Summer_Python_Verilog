// 시스템 태스크와 컴파일러 지시어

// 시스템 테스크


// 예제 3-3 $display 태스크

// 따옴표 안의 문자열을 출력.
$display("Hello Verilog world");

// 현재 시뮬레이션 시간 230을 출력.
$display($time)

// 41-비트 virtual address의 값 1fe0000001c 그리고 시간 200을 출력
reg[0:40] virtual_addr;
$display ("At time %d virtual address is %h",$time,virtual_addr)

// port_id 값 5를 2진수로 출력
reg[4:0] port_id; $display("ID of the port is %b",port_id);


// x 문자를 출력
// 4-비트 bus의 값 10xx(신호충돌)을 2진수로 출력
reg [3:0] bus;$display("Bus value is %b",bus);


// 최상위 top 모듈에서 파생된 인스턴스 p1의 계층 이름을 출력.
// 인자가 필요하지 않다. 유용한 특징이다.
$display("This string is displayed from %m level if hierarchy");


// 예제 3-4 특수문자
// 특수 문자 개행과 %의 출력
$display("This is a \n multiline string with a %% sign");

// 모니터링 태스크
// Verilog에서는 $monitor태스크로 신호의 값이 변할 때 마다 그 신호를 출력할 수 있다.


// 예제 3-5 Monitor문
// 시간과 클럭 그리고 리셋 신호의 값을 모니터링.
// 클럭운 먀 5단위 시간마다 바뀌고, 리셋은 10 단위 시간에 0이 된다.
initial
begin 
    $monitor($time,"Value of signals clock= %b reset=%b",clock,reset);
end
monitor 문의 출력의 일부분:

// 시뮬레이션의 중단과 종료 태스크
// 시뮬레이션을 하는 동안 중단을 하기 위해서 $stop를 제공한다.

// 예제 3-6 stop과 finish 태스크

// 단위 시간 100에 시뮬레이션을 중단하고 결과를 조사.
// 단위 시간 1000에 시뮬레이션을 끝냄.
initial 
begin 
    clock=0;
    reset=1;
    #100 $stop;
    #900 $finish;
end


// 컴파일러 지시어

// 예제 3-7 define 지시어
// 기본 워드 크기를 텍스트 메크로로 정의.
// 코드 내에서 'WORD_SIZE로 사용
'define WORD_SIZE 32

// 별명을 정의. 'S가 나타날 때마다 $stop로 대치
'define S $stop;

// 자주 사용되는 텍스트 문자열을 정의
'define WORD_REG reg [31:0]

// 예제 3-8 include 지시어
// main 파일인 design.v 파일에서 header.v 파일을 포함.
'include header.value
...
...
< design.v 내용 >
...
...