`timescale 1ns/1ps


module moore_machine(
    din,
    dout,
    clk,
    rst);
   input din,clk,rst;
   output reg dout;
   reg [1:0]n_state,c_state;

   parameter S_0 =2'h0;
   parameter S_1 =2'h1;
   parameter S_2 =2'h2;
   parameter S_3 =2'h3;

   always @ (posedge clk, negedge rst)
   begin
    if (!rst)
    begin 
        c_state<=S_0;
    end

    else
    begin 
        c_state <= n_state;
    end
   end

   always @ (c_state ,din)
   begin
    case (c_state)
    S_0:begin
    n_state=(din==1'b1)?c_state:S_1;
    dout=1'b0;
    end
   
    S_1:begin
    n_state=(din==1'b1)?S_2:c_state;
    dout=1'b0;
    end
   
    S_2:begin
    n_state=(din==1'b1)?S_3:S_1;
    dout=1'b0;
    end
    
    S_3:begin
    n_state=(din==1'b1)?S_0:S_1;
    dout=1'b1;
    end

    default : begin
	n_state = S_0;
	dout= 1'b0;
    end

   endcase
   

   end
endmodule 