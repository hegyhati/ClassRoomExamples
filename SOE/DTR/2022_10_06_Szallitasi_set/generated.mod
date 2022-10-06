var from_A_to_D >= 0;
var from_A_to_E >= 0;
var from_A_to_F >= 0;
var from_A_to_G >= 0;
var from_B_to_D >= 0;
var from_B_to_E >= 0;
var from_B_to_F >= 0;
var from_B_to_G >= 0;
var from_C_to_D >= 0;
var from_C_to_E >= 0;
var from_C_to_F >= 0;
var from_C_to_G >= 0;

s.t. A_capacity_constraint:
	 + from_A_to_D + from_A_to_E + from_A_to_F + from_A_to_G <= 50 ;
s.t. B_capacity_constraint:
	 + from_B_to_D + from_B_to_E + from_B_to_F + from_B_to_G <= 150 ;
s.t. C_capacity_constraint:
	 + from_C_to_D + from_C_to_E + from_C_to_F + from_C_to_G <= 250 ;

s.t. D_demand_constraint:
	from_A_to_D + from_B_to_D + from_C_to_D >= 75 ;
s.t. E_demand_constraint:
	from_A_to_E + from_B_to_E + from_C_to_E >= 125 ;
s.t. F_demand_constraint:
	from_A_to_F + from_B_to_F + from_C_to_F >= 130 ;
s.t. G_demand_constraint:
	from_A_to_G + from_B_to_G + from_C_to_G >= 120 ;

minimize Cost:
 + 129 * from_A_to_D + 37 * from_A_to_E + 116 * from_A_to_F + 108 * from_A_to_G + 40 * from_B_to_D + 47 * from_B_to_E + 127 * from_B_to_F + 117 * from_B_to_G + 110 * from_C_to_D + 126 * from_C_to_E + 83 * from_C_to_F + 94 * from_C_to_G;
