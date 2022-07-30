`timescale 1ns/1ps

module JK_FF(
  J,
  K,
  clk,
  rst,
  Q,
  Qbar
);

  input J,K,clk,rst;
  output reg Q,Qbar;

  always @ (posedge clk or negedge rst)
  begin 
    if (!rst)
    begin 
      Q<=1'b0;
      Qbar<=1'b1;
    end
    else 
    begin 
      if (J==0 && K==0)
      begin 
        Q<=Q;
        Qbar<=Qbar;     
      end
      else if (J==1'b1 && K==1'b0)
      begin 
        Q<=1'b1;
        Qbar<=1'b0;
      end
      else if (J==1'b0 && K==1'b1)
      begin
        Q<=1'b0;
        Qbar<=1'b1;
      end
      else 
      begin 
        Q<=~Q;
        Qbar<=~Qbar;
      end
    end
    
    
  end
endmodule