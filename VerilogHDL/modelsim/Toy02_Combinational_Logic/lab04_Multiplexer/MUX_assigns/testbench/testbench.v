`timescale 1ns/1ps

module testbench();

    reg [3:0]A,B,C,D;
    reg [1:0]Sel;
    wire [3:0]out;

    MUX_assign Mas (
      .A(A),
      .B(B),
      .C(C),
      .D(D),
      .Sel(Sel),
      .OUT(out)
    );
    
    initial
    begin
        A=4'h5; B=4'h6; C=4'h7; D=4'h8;
        Sel = 2'h0;
        #10; Sel = 2'h1;
        #10; Sel = 2'h2;
        #10; Sel = 2'h3;
        #10; $stop;
    end

endmodule