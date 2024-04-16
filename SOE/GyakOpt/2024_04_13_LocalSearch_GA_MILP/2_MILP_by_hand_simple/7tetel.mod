var B0 binary;
var B1 binary;
var B2 binary;
var B3 binary;
var B4 binary;
var B5 binary;
var B6 binary;

var K0 binary;
var K1 binary;
var K2 binary;
var K3 binary;
var K4 binary;
var K5 binary;
var K6 binary;

var A0 binary;
var A1 binary;
var A2 binary;
var A3 binary;
var A4 binary;
var A5 binary;
var A6 binary;

var MS >= 0;

s.t. T0: B0 + K0 + A0 = 1;
s.t. T1: B1 + K1 + A1 = 1;
s.t. T2: B2 + K2 + A2 = 1;
s.t. T3: B3 + K3 + A3 = 1;
s.t. T4: B4 + K4 + A4 = 1;
s.t. T5: B5 + K5 + A5 = 1;
s.t. T6: B6 + K6 + A6 = 1;


s.t. Benedek:
    B0 * 6 + B1 * 2 + B2 * 9 + B3 * 7 + B4 * 4 + B5 * 2 + B6 * 4 <= MS;
s.t. Kakas: 
    K0 * 7 + K1 * 2 + K2 * 3 + K3 * 9 + K4 * 3 + K5 * 10 + K6 * 7 <= MS;
s.t. Andras:
    A0 * 3 + A1 * 9 + A2 * 4 + A3 * 4 + A4 * 6 + A5 * 4 + A6 * 9 <= MS;

minimize Makespan : MS;