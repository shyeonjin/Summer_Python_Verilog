`timescale 1ns/1ps

module full_adder(a, b, C_IN, C_OUT,out);
    input a, b, C_IN;
    
    wire carry1, carry2;
    wire out2;

    output C_OUT, out;
    
    half_adder ha1(a, b, carry1, out2);
    half_adder ha2(out2, C_IN, carry2, out);

    assign C_OUT = carry1|carry2;
endmodule

module half_adder(
  first,
  second,
  C_OUT,
  out
);

  input first,second;
  output out,C_OUT;

  assign {C_OUT,out} = first+second;

endmodule