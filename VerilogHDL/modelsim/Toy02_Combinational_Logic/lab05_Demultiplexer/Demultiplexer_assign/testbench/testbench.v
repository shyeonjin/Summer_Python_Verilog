`timescale 1ns/1ps

module testbench();

    reg [7:0] IN;
    reg [1:0] Sel;

    DEMUX D (
      .IN(IN),
      .Sel(Sel)
    );

    initial
    begin
        IN = 8'h01;
        #5 IN = 8'h23;
        #15 IN = 8'h45;
        #10 IN = 8'h67;
        #10;
    end

    initial
    begin
        Sel = 2'h0;
        #10 Sel = 2'h1;
        #5 Sel = 2'h2;
        #10 Sel = 2'h3;
        #10;
    end

endmodule