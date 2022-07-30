`timescale 1ns/1ps

module T_FF(
  T,
  clk,
  rst,
  Q,
  Qbar
);

  input T,clk,rst;
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
      if (T==1'b1)
      begin
        Q<=~Q;
        Qbar<=~Qbar; 
      end
      else if(T==1'b0)
      begin
        Q<=Q;
        Qbar<=Qbar; 
      end

    end
  end

endmodule