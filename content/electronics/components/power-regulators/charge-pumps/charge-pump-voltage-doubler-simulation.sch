EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L rectifier_schlib:VSOURCE V2
U 1 1 57336052
P 4200 4450
F 0 "V2" H 3900 4500 50  0000 L CNN
F 1 "PULSE(0 5 0 10n 10n 5u 10u)" H 2800 4400 50  0000 L CNN
F 2 "" H 4200 4450 50  0000 C CNN
F 3 "" H 4200 4450 50  0000 C CNN
F 4 "Value" H 4200 4450 60  0001 C CNN "Fieldname"
F 5 "V" H 4200 4450 60  0001 C CNN "Spice_Primitive"
F 6 "1 2" H 3900 4650 60  0001 C CNN "Spice_Node_Sequence"
	1    4200 4450
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:GND #PWR01
U 1 1 573360D3
P 4200 4750
F 0 "#PWR01" H 4200 4500 50  0001 C CNN
F 1 "GND" H 4205 4577 50  0000 C CNN
F 2 "" H 4200 4750 50  0000 C CNN
F 3 "" H 4200 4750 50  0000 C CNN
	1    4200 4750
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:D D1
U 1 1 573361B8
P 4500 3650
F 0 "D1" H 4500 3435 50  0000 C CNN
F 1 "1N4148" H 4500 3526 50  0000 C CNN
F 2 "" H 4500 3650 50  0000 C CNN
F 3 "" H 4500 3650 50  0000 C CNN
F 4 "Value" H 4500 3650 60  0001 C CNN "Fieldname"
F 5 "D" H 4500 3650 60  0001 C CNN "Spice_Primitive"
F 6 "2 1" H 4500 3650 60  0001 C CNN "Spice_Node_Sequence"
	1    4500 3650
	-1   0    0    1   
$EndComp
$Comp
L rectifier_schlib:C C1
U 1 1 5733628F
P 5350 3950
F 0 "C1" H 5465 3996 50  0000 L CNN
F 1 "100n" H 5465 3905 50  0000 L CNN
F 2 "" H 5388 3800 50  0000 C CNN
F 3 "" H 5350 3950 50  0000 C CNN
F 4 "Value" H 5350 3950 60  0001 C CNN "Fieldname"
F 5 "C" H 5350 3950 60  0001 C CNN "Spice_Primitive"
F 6 "1 2" H 5350 3950 60  0001 C CNN "SpiceMapping"
	1    5350 3950
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:R R2
U 1 1 573362F7
P 5700 3950
F 0 "R2" H 5630 3904 50  0000 R CNN
F 1 "100k" H 5630 3995 50  0000 R CNN
F 2 "" V 5630 3950 50  0000 C CNN
F 3 "" H 5700 3950 50  0000 C CNN
F 4 "Value" H 5700 3950 60  0001 C CNN "Fieldname"
F 5 "1 2" H 5700 3950 60  0001 C CNN "SpiceMapping"
F 6 "R" V 5700 3950 60  0001 C CNN "Spice_Primitive"
	1    5700 3950
	-1   0    0    1   
$EndComp
Text Notes 4500 4950 0    60   ~ 0
.tran 1u 100u\n
Wire Wire Line
	5200 3650 5350 3650
Wire Wire Line
	5700 3650 5700 3800
Wire Wire Line
	5350 3800 5350 3650
Connection ~ 5350 3650
Wire Wire Line
	5350 4250 5350 4100
Wire Wire Line
	5700 4250 5700 4100
Wire Wire Line
	4200 3650 4350 3650
Text Label 4750 4250 2    60   ~ 0
pwm_in
Text Label 5700 3650 0    60   ~ 0
rect_out
Wire Wire Line
	5350 3650 5700 3650
Wire Wire Line
	5350 4250 5700 4250
$Comp
L rectifier_schlib:VSOURCE V1
U 1 1 5FD5E984
P 4200 3850
F 0 "V1" H 3900 3900 50  0000 L CNN
F 1 "DC 5" H 3850 3800 50  0000 L CNN
F 2 "" H 4200 3850 50  0000 C CNN
F 3 "" H 4200 3850 50  0000 C CNN
F 4 "Value" H 4200 3850 60  0001 C CNN "Fieldname"
F 5 "V" H 4200 3850 60  0001 C CNN "Spice_Primitive"
F 6 "1 2" H 3900 4050 60  0001 C CNN "Spice_Node_Sequence"
	1    4200 3850
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:C C2
U 1 1 5FD681FD
P 4800 3900
F 0 "C2" H 4915 3946 50  0000 L CNN
F 1 "100n" H 4915 3855 50  0000 L CNN
F 2 "" H 4838 3750 50  0000 C CNN
F 3 "" H 4800 3900 50  0000 C CNN
F 4 "Value" H 4800 3900 60  0001 C CNN "Fieldname"
F 5 "C" H 4800 3900 60  0001 C CNN "Spice_Primitive"
F 6 "1 2" H 4800 3900 60  0001 C CNN "SpiceMapping"
	1    4800 3900
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:D D?
U 1 1 5FD68D10
P 5050 3650
F 0 "D?" H 5050 3435 50  0000 C CNN
F 1 "1N4148" H 5050 3526 50  0000 C CNN
F 2 "" H 5050 3650 50  0000 C CNN
F 3 "" H 5050 3650 50  0000 C CNN
F 4 "Value" H 5050 3650 60  0001 C CNN "Fieldname"
F 5 "D" H 5050 3650 60  0001 C CNN "Spice_Primitive"
F 6 "2 1" H 5050 3650 60  0001 C CNN "Spice_Node_Sequence"
	1    5050 3650
	-1   0    0    1   
$EndComp
Wire Wire Line
	4650 3650 4800 3650
Wire Wire Line
	4800 3750 4800 3650
Connection ~ 4800 3650
Wire Wire Line
	4800 3650 4900 3650
Wire Wire Line
	4800 4050 4800 4250
Wire Wire Line
	4800 4250 4200 4250
Wire Wire Line
	4200 4650 4200 4750
$Comp
L rectifier_schlib:GND #PWR?
U 1 1 5FD69C41
P 4200 4050
F 0 "#PWR?" H 4200 3800 50  0001 C CNN
F 1 "GND" H 4205 3877 50  0000 C CNN
F 2 "" H 4200 4050 50  0000 C CNN
F 3 "" H 4200 4050 50  0000 C CNN
	1    4200 4050
	1    0    0    -1  
$EndComp
$Comp
L rectifier_schlib:GND #PWR?
U 1 1 5FD6A33F
P 5700 4250
F 0 "#PWR?" H 5700 4000 50  0001 C CNN
F 1 "GND" H 5705 4077 50  0000 C CNN
F 2 "" H 5700 4250 50  0000 C CNN
F 3 "" H 5700 4250 50  0000 C CNN
	1    5700 4250
	1    0    0    -1  
$EndComp
Connection ~ 5700 4250
$EndSCHEMATC
