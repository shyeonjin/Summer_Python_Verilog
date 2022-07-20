`timescale 1ns/1ps

module testbench();

    reg [1:0]A,B;

    digital_Comparartor dC (
      .A(A),
      .B(B)
    );

    initial
    begin
        A=2'b00;B=2'b00;
        #10 A=2'b00; B=2'b01;
        #10 A=2'b00; B=2'b10;
        #10 A=2'b00; B=2'b11;
        #10 A=2'b01; B=2'b00;
        #10 A=2'b01; B=2'b01;
        #10 A=2'b01; B=2'b10;
        #10 A=2'b01; B=2'b11;
        #10 A=2'b10; B=2'b00;
        #10 A=2'b10; B=2'b01;
        #10 A=2'b10; B=2'b10;
        #10 A=2'b10; B=2'b11;
        #10 A=2'b11; B=2'b00;
        #10 A=2'b11; B=2'b01;
        #10 A=2'b11; B=2'b10;
        #10 A=2'b11; B=2'b11;
        #10;
    end

endmodule