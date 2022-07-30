`timescale 1ns/1ps

module D_FF(
  D,
  clk,
  rst,
  Q,
  Qbar
);

  input D,clk,rst;
  output reg Q,Qbar;

  always @(posedge clk or negedge rst)
  begin
    if (!rst)
    begin
      Q<=1'b0;
      Qbar<=1'b1;
    end
    else 
    begin
      if (D==1'b1)
      begin
        Q<=1'b1;
        Qbar<=1'b0; 
      end
      else if(D==1'b0)
      begin
        Q<=1'b0;
        Qbar<=1'b1; 
      end

    end
  end

endmodule