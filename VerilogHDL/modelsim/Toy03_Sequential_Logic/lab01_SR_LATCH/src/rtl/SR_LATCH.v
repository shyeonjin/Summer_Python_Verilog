`timescale 1ns/1ps

module SR_LATCH(
    S,
    R,
    Q,
    Qbar
);
input S,R;
output reg Q,Qbar;

always @(S,R) 
begin
    if (S==1'b0&&R==1'b0)
    begin
        Q=1'bx; Qbar=1'bx; 
    end
    else if(S==1'b0&&R==1'b1)
    begin
        Q=1'b0; Qbar=1'b1; 
    end
    else if(S==1'b1&&R==1'b0)
    begin
        Q=1'b1; Qbar=1'b0; 
    end
    else 
    begin
        Q=1'b0; Qbar=1'b0; 
    end
end
    
endmodule