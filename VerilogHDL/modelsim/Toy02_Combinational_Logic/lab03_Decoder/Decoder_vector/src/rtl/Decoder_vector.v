`timescale 1ns/1ps

module Decoder_vector(
    IN,
    out
);

  input [2:0] IN;
  output reg [7:0] out;

  
  always @(IN)
  begin
      if (IN == 3'b000)
          out = 8'b1000_0000;
      else if (IN == 3'b001)
          out = 8'b0100_0000;
      else if (IN == 3'b010)
          out = 8'b0010_0000;
      else if (IN == 3'b011)
          out = 8'b0001_0000;
      else if (IN == 3'b100)
          out = 8'b0000_1000;
      else if (IN == 3'b101)
          out = 8'b0000_0100;
      else if (IN == 3'b110)
          out = 8'b0000_0010;
      else if (IN == 3'b111)
          out = 8'b0000_0001;
      else
          out = 8'bxxxx_xxxx;
  end

endmodule