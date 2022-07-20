`timescale 1ns/1ps

module four_bit_PARITY_always(
    IN,
    odd_out,
    even_out  
);

  input [3:0] IN;
  output reg odd_out,even_out;

  always @(IN) 
  begin
    if (IN<4'b1010)
      begin
        
        if (^IN%2==0)
        begin
          odd_out=1'b1;
          even_out=1'b0;
        end

        else 
        begin
          odd_out=1'b0;
          even_out=1'b1;
        end
      end
    else
      begin
        odd_out=1'bx;
        even_out=1'bx;
      end

      
  end




endmodule