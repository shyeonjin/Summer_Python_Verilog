// 모듈
// 예제 4-1 SR 래치의 구성요소
// 모듈의 이름과 포트 리스트
// SR 래치 모듈
module SR_latch(Q,Qbar,Sbar,Rbar);

// 포트 선언
output Q,Qbar;
input Sbar,Rbar;

// 하위 모듈을 파생
// 이 경우 Veriolg 프리미티브인 nand 게이트가 파생
// wire가 꼬인 형태로 연결되어 있는 것을 주목하자.
nand n1(Q,Sbar,Qbar);
nand n2(Qbar,Rbar,Q);

endmodule

// 스티뮬러스 블록
module Top;

wire q, qbar;
reg set,reset;

// 하위 모듈의 파생
// 이 경우 SR래치를 파생
// SR 래치에 invert된 set과 reset 신호를 공급

SR_latch m1(q,qbar,~set,~reset);

initial 
begin
    $monitor($time,"set=%b, reset=%b,q=%b",set,reset,q);
    set=0;
    reset=0;
    #5 reset=1;
    #5 reset=0;
    #5 set=1;

end
endmodule


// 위에 정의된 SR래치는 변수 선언, 데이터 플로우문 또는 행위적 블록은 존재하지 않는다.
// 스티뮬러스 블록은 모둘이름, wire, reg, 변수 선언, 하위 모듈의 파생 행위적 블록,
// 그리고 endmodule 문을 포함하지만 포트 리스트, 포트 선언, 데이터플로우 구문은 포함하지 않는다.
// 그러므로 module, 모듈이름 그리고 endmodule을 제외한 모든 성분은 선택적이고 설계시 필요에 따라 혼용할 수 있다.