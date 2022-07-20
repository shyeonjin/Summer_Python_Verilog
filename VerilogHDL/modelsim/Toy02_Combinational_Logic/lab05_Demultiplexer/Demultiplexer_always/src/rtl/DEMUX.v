`timescale 1ns/1ps

module DEMUX(
    A,B,C,D,
    IN,
    Sel
);

  input [7:0] IN;
  input [1:0] Sel;
  output reg [7:0]A,B,C,D;

  always @(IN,Sel)
  begin
    if(Sel==2'h0)
    begin
      A=IN ;
    end
    else
    begin
      A=8'h00;
    end
  end

  always @(IN,Sel)
  begin
    if(Sel==2'h1)
    begin
      B=IN ;
    end
    else
    begin
      B=8'h00;
    end
  end

  always @(IN,Sel)
  begin
    if(Sel==2'h2)
    begin
      C=IN ;
    end
    else
    begin
      C=8'h00;
    end
  end

  always @(IN,Sel)
  begin
    if(Sel==2'h3)
    begin
      D=IN ;
    end
    else
    begin
      D=8'h00;
    end
  end
  

endmodule