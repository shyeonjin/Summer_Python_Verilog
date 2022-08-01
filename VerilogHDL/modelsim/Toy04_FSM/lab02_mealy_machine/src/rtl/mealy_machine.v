`timescale 1ns/1ps

module mealy_machine(
    din,
    dout,
    clk,
    rst);
    input clk,rst,din;
    output reg dout;

    reg [2:0]c_state,n_state;

    parameter S_0 =3'h0;
    parameter S_1 =3'h1;
    parameter S_2 =3'h2;
    parameter S_3 =3'h3;
    parameter S_4 =3'h4;

    always @ (posedge clk, negedge rst)
    begin
        if (!rst)
        begin 
            c_state<=S_0;
        end

        else 
        begin
            c_state<=n_state;
        end
    end

    always @ (c_state,din)
    begin
        case (c_state)
        S_0:begin
            n_state=(din==1'b1)?S_3:S_1;
            dout=1'b0;
        end
        S_1:begin
            n_state=(din==1'b1)?S_2:S_4;
            dout=1'b0;
        end
        S_2:begin
            n_state=S_0;
            dout=(din==1'b1)?1'b1:1'b0;
        end
        S_3:begin
            n_state=S_4;
            dout=1'b0;
        end
        S_4:begin 
            n_state=S_0;
            dout=1'b0;
        end
        default : begin
	        n_state = S_0;
	        dout= 1'b0;
        end
        endcase
    end

endmodule