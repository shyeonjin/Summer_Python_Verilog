`timescale 1ns/1ps

module Encoder_I(
    IN0,IN1,IN2,IN3,IN4,IN5,IN6,IN7,
    out  
);

  input IN0,IN1,IN2,IN3,IN4,IN5,IN6,IN7;
  output reg [2:0] out;

  always @(IN0,IN1,IN2,IN3,IN4,IN5,IN6,IN7)
  begin
    if (IN0==1'b1)
    begin
     out=3'b000; 
    end

    else if (IN1==1'b1)
    begin
     out=3'b001; 
    end

    else if (IN2==1'b1)
    begin
     out=3'b010; 
    end

    else if (IN3==1'b1)
    begin
     out=3'b011; 
    end

    else if (IN4==1'b1)
    begin
     out=3'b100; 
    end

    else if (IN5==1'b1)
    begin
     out=3'b101; 
    end

    else if (IN6==1'b1)
    begin
     out=3'b110; 
    end

    else if (IN7==1'b1)
    begin
     out=3'b111; 
    end

    else
    begin
      out=3'bxxx;
    end 

  end

endmodule