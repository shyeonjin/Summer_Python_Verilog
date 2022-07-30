`timescale 1ns/1ps

module testbench();

  reg D;
  D_Latch DL(
    .D(D)
  );

  initial 
  begin
    D=1'b0;
    # 10 D=1'b1;
    # 10;
    
  end

endmodule