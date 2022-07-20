`timescale 1ns/1ps

module testbench();

    reg IN0,IN1,IN2,IN3,IN4,IN5,IN6,IN7;

    Encoder_I ENI (
      .IN0(IN0),.IN1(IN1),.IN2(IN2),.IN3(IN3),.IN4(IN4),.IN5(IN5),.IN6(IN6),.IN7(IN7)
      );

    initial
    begin
        IN0=1'b1; IN1=1'b0; IN2=1'b0; IN3=1'b0; IN4=1'b0; IN5=1'b0; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b1; IN2=1'b0; IN3=1'b0; IN4=1'b0; IN5=1'b0; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b1; IN3=1'b0; IN4=1'b0; IN5=1'b0; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b0; IN3=1'b1; IN4=1'b0; IN5=1'b0; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b0; IN3=1'b0; IN4=1'b1; IN5=1'b0; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b0; IN3=1'b0; IN4=1'b0; IN5=1'b1; IN6=1'b0; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b0; IN3=1'b0; IN4=1'b0; IN5=1'b0; IN6=1'b1; IN7=1'b0;
        #10 IN0=1'b0; IN1=1'b0; IN2=1'b0; IN3=1'b0; IN4=1'b0; IN5=1'b0; IN6=1'b0; IN7=1'b1;
        #10 ;

    end

endmodule