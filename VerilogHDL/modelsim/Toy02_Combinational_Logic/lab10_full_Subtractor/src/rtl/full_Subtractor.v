`timescale 1ns/1ps

module full_Subtractor(a, b, B_IN, B_OUT,out);
    input a, b, B_IN;
    
    wire BORROW1, BORROW2;
    wire out2;

    output B_OUT, out;
    
    half_Subtractor hS1(a, b, BORROW1, out2);
    half_Subtractor hS2(out2, B_IN, BORROW2, out);

    assign B_OUT = BORROW1|BORROW2;
endmodule

module half_Subtractor(
  first,
  second,
  B,
  D
);

  input first,second;
  output B,D;

  assign {B,D} = first+(~second+1);

endmodule