`timescale 1ns/1ps

module Encoder_vector(
    IN,
    out  
);

  input [7:0] IN;
  output reg [2:0] out;

  always @(IN)
  begin
    if (IN[7]==1'b1)
    begin
     out=3'b000; 
    end

    else if (IN[6]==1'b1)
    begin
     out=3'b001; 
    end

    else if (IN[5]==1'b1)
    begin
     out=3'b010; 
    end

    else if (IN[4]==1'b1)
    begin
     out=3'b011; 
    end

    else if (IN[3]==1'b1)
    begin
     out=3'b100; 
    end

    else if (IN[2]==1'b1)
    begin
     out=3'b101; 
    end

    else if (IN[1]==1'b1)
    begin
     out=3'b110; 
    end

    else if (IN[0]==1'b1)
    begin
     out=3'b111; 
    end

    else
    begin
      out=3'bxxx;
    end 

  end

endmodule