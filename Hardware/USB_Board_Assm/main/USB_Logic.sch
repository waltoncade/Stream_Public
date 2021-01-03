EESchema Schematic File Version 4
LIBS:main-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 7 9
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
L main-rescue:USB-A1HSW6-SamacSys_Parts J901
U 1 1 5F39B5A0
P 6500 2850
AR Path="/5F39AC8F/5F39B5A0" Ref="J901"  Part="1" 
AR Path="/5F39FEA5/5F39B5A0" Ref="J?"  Part="1" 
AR Path="/5F3A09F1/5F39B5A0" Ref="J?"  Part="1" 
AR Path="/5F3A0E43/5F39B5A0" Ref="J?"  Part="1" 
AR Path="/5F877533/5F39B5A0" Ref="J801"  Part="1" 
AR Path="/5F8776AE/5F39B5A0" Ref="J701"  Part="1" 
AR Path="/5F877849/5F39B5A0" Ref="J601"  Part="1" 
F 0 "J701" H 6900 3115 50  0000 C CNN
F 1 "USB-A1HSW6" H 6900 3024 50  0000 C CNN
F 2 "USBA1HSW6" H 7150 2950 50  0001 L CNN
F 3 "http://www.on-shore.com/wp-content/uploads/2015/09/usb-a1hsxx.pdf" H 7150 2850 50  0001 L CNN
F 4 "USB - A Receptacle Connector 4 Position Through Hole, Right Angle" H 7150 2750 50  0001 L CNN "Description"
F 5 "7" H 7150 2650 50  0001 L CNN "Height"
F 6 "On-Shore Technology, Inc" H 7150 2550 50  0001 L CNN "Manufacturer_Name"
F 7 "USB-A1HSW6" H 7150 2450 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "USB-A1HSW6" H 7150 2350 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/usb-a1hsw6/on-shore-technology" H 7150 2250 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 7150 2150 50  0001 L CNN "Mouser Part Number"
F 11 "" H 7150 2050 50  0001 L CNN "Mouser Price/Stock"
	1    6500 2850
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR0903
U 1 1 5F39B5A6
P 6500 2950
AR Path="/5F39AC8F/5F39B5A6" Ref="#PWR0903"  Part="1" 
AR Path="/5F39FEA5/5F39B5A6" Ref="#PWR?"  Part="1" 
AR Path="/5F3A09F1/5F39B5A6" Ref="#PWR?"  Part="1" 
AR Path="/5F3A0E43/5F39B5A6" Ref="#PWR?"  Part="1" 
AR Path="/5F877533/5F39B5A6" Ref="#PWR0803"  Part="1" 
AR Path="/5F8776AE/5F39B5A6" Ref="#PWR0703"  Part="1" 
AR Path="/5F877849/5F39B5A6" Ref="#PWR0603"  Part="1" 
F 0 "#PWR0703" H 6500 2700 50  0001 C CNN
F 1 "GND" H 6505 2777 50  0000 C CNN
F 2 "" H 6500 2950 50  0001 C CNN
F 3 "" H 6500 2950 50  0001 C CNN
	1    6500 2950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5700 3150 5400 3150
$Comp
L power:+5V #PWR0902
U 1 1 5F39B5BC
P 5700 2850
AR Path="/5F39AC8F/5F39B5BC" Ref="#PWR0902"  Part="1" 
AR Path="/5F39FEA5/5F39B5BC" Ref="#PWR?"  Part="1" 
AR Path="/5F3A09F1/5F39B5BC" Ref="#PWR?"  Part="1" 
AR Path="/5F3A0E43/5F39B5BC" Ref="#PWR?"  Part="1" 
AR Path="/5F877533/5F39B5BC" Ref="#PWR0802"  Part="1" 
AR Path="/5F8776AE/5F39B5BC" Ref="#PWR0702"  Part="1" 
AR Path="/5F877849/5F39B5BC" Ref="#PWR0602"  Part="1" 
F 0 "#PWR0702" H 5700 2700 50  0001 C CNN
F 1 "+5V" H 5715 3023 50  0000 C CNN
F 2 "" H 5700 2850 50  0001 C CNN
F 3 "" H 5700 2850 50  0001 C CNN
	1    5700 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0901
U 1 1 5F39B67B
P 4850 4150
AR Path="/5F39AC8F/5F39B67B" Ref="#PWR0901"  Part="1" 
AR Path="/5F39FEA5/5F39B67B" Ref="#PWR?"  Part="1" 
AR Path="/5F3A09F1/5F39B67B" Ref="#PWR?"  Part="1" 
AR Path="/5F3A0E43/5F39B67B" Ref="#PWR?"  Part="1" 
AR Path="/5F877533/5F39B67B" Ref="#PWR0801"  Part="1" 
AR Path="/5F8776AE/5F39B67B" Ref="#PWR0701"  Part="1" 
AR Path="/5F877849/5F39B67B" Ref="#PWR0601"  Part="1" 
F 0 "#PWR0701" H 4850 3900 50  0001 C CNN
F 1 "GND" H 4855 3977 50  0000 C CNN
F 2 "" H 4850 4150 50  0001 C CNN
F 3 "" H 4850 4150 50  0001 C CNN
	1    4850 4150
	1    0    0    -1  
$EndComp
Text HLabel 3150 3950 0    50   Input ~ 0
Control
Text HLabel 5700 2950 0    50   Output ~ 0
D-
Text HLabel 5700 3050 0    50   Output ~ 0
D+
$Comp
L main-rescue:RK73B2ATTD221J-SamacSys_Parts R901
U 1 1 5F872CB1
P 3350 3950
AR Path="/5F39AC8F/5F872CB1" Ref="R901"  Part="1" 
AR Path="/5F877533/5F872CB1" Ref="R801"  Part="1" 
AR Path="/5F8776AE/5F872CB1" Ref="R701"  Part="1" 
AR Path="/5F877849/5F872CB1" Ref="R601"  Part="1" 
F 0 "R701" H 3700 4175 50  0000 C CNN
F 1 "RK73B2ATTD221J" H 3700 4084 50  0000 C CNN
F 2 "RESC2012X60N" H 3900 4000 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/RK73B2ATTD221J.pdf" H 3900 3900 50  0001 L CNN
F 4 "KOA Thick Film Surface Mount Resistor 0805 Case 220 +/-5% 0.25W +/-200ppm/C" H 3900 3800 50  0001 L CNN "Description"
F 5 "0.6" H 3900 3700 50  0001 L CNN "Height"
F 6 "KOA Speer" H 3900 3600 50  0001 L CNN "Manufacturer_Name"
F 7 "RK73B2ATTD221J" H 3900 3500 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "RK73B2ATTD221J" H 3900 3400 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/rk73b2attd221j/koa-speer-electronics" H 3900 3300 50  0001 L CNN "Arrow Price/Stock"
F 10 "660-RK73B2ATTD221J" H 3900 3200 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=660-RK73B2ATTD221J" H 3900 3100 50  0001 L CNN "Mouser Price/Stock"
	1    3350 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 3950 3150 3950
$Comp
L main-rescue:VFHR1112H-3BY2A-TR-SamacSys_Parts LED801
U 1 1 5F8C9D71
P 6300 3900
AR Path="/5F877533/5F8C9D71" Ref="LED801"  Part="1" 
AR Path="/5F39AC8F/5F8C9D71" Ref="LED901"  Part="1" 
AR Path="/5F877849/5F8C9D71" Ref="LED601"  Part="1" 
AR Path="/5F8776AE/5F8C9D71" Ref="LED701"  Part="1" 
F 0 "LED701" H 6600 4267 50  0000 C CNN
F 1 "VFHR1112H-3BY2A-TR" H 6600 4176 50  0000 C CNN
F 2 "LEDC2012X90N" H 6800 4050 50  0001 L BNN
F 3 "https://componentsearchengine.com/Datasheets/1/VFHR1112H-3BY2A-TR.pdf" H 6800 3950 50  0001 L BNN
F 4 "Standard LEDs - SMD Surface Mount LED" H 6800 3850 50  0001 L BNN "Description"
F 5 "0.9" H 6800 3750 50  0001 L BNN "Height"
F 6 "Stanley Electric" H 6800 3650 50  0001 L BNN "Manufacturer_Name"
F 7 "VFHR1112H-3BY2A-TR" H 6800 3550 50  0001 L BNN "Manufacturer_Part_Number"
F 8 "VFHR1112H-3BY2A-TR" H 6800 3450 50  0001 L BNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/vfhr1112h-3by2a-tr/stanley-electric" H 6800 3350 50  0001 L BNN "Arrow Price/Stock"
F 10 "327-VFHR1112H3BY2ATR" H 6800 3250 50  0001 L BNN "Mouser Part Number"
F 11 "https://www.mouser.co.uk/ProductDetail/Stanley-Electric/VFHR1112H-3BY2A-TR?qs=byeeYqUIh0P97ifiMYV8SQ%3D%3D" H 6800 3150 50  0001 L BNN "Mouser Price/Stock"
	1    6300 3900
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0804
U 1 1 5F8CC0BF
P 6900 3900
AR Path="/5F877533/5F8CC0BF" Ref="#PWR0804"  Part="1" 
AR Path="/5F39AC8F/5F8CC0BF" Ref="#PWR0904"  Part="1" 
AR Path="/5F877849/5F8CC0BF" Ref="#PWR0604"  Part="1" 
AR Path="/5F8776AE/5F8CC0BF" Ref="#PWR0704"  Part="1" 
F 0 "#PWR0704" H 6900 3750 50  0001 C CNN
F 1 "+5V" V 6915 4028 50  0000 L CNN
F 2 "" H 6900 3900 50  0001 C CNN
F 3 "" H 6900 3900 50  0001 C CNN
	1    6900 3900
	0    1    1    0   
$EndComp
$Comp
L main-rescue:RK73B2ATTD221J-SamacSys_Parts R902
U 1 1 5F8CD192
P 5400 3900
AR Path="/5F39AC8F/5F8CD192" Ref="R902"  Part="1" 
AR Path="/5F877533/5F8CD192" Ref="R802"  Part="1" 
AR Path="/5F8776AE/5F8CD192" Ref="R702"  Part="1" 
AR Path="/5F877849/5F8CD192" Ref="R602"  Part="1" 
F 0 "R702" H 5750 4125 50  0000 C CNN
F 1 "RK73B2ATTD151J" H 5750 4034 50  0000 C CNN
F 2 "RESC2012X60N" H 5950 3950 50  0001 L CNN
F 3 "http://www.koaspeer.com/pdfs/RK73B.pdf" H 5950 3850 50  0001 L CNN
F 4 "KOA Thick Film Surface Mount Resistor 0805 Case 220 +/-5% 0.25W +/-200ppm/C" H 5950 3750 50  0001 L CNN "Description"
F 5 "0.6" H 5950 3650 50  0001 L CNN "Height"
F 6 "KOA Speer" H 5950 3550 50  0001 L CNN "Manufacturer_Name"
F 7 "RK73B2ATTD151J" H 5950 3450 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "" H 5950 3350 50  0001 L CNN "Arrow Part Number"
F 9 "" H 5950 3250 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 5950 3150 50  0001 L CNN "Mouser Part Number"
F 11 "" H 5950 3050 50  0001 L CNN "Mouser Price/Stock"
	1    5400 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 3900 6100 3900
$Comp
L main-rescue:AO3414-SamacSys_Parts Q701
U 1 1 5F8DA6F8
P 4550 3950
AR Path="/5F8776AE/5F8DA6F8" Ref="Q701"  Part="1" 
AR Path="/5F39AC8F/5F8DA6F8" Ref="Q901"  Part="1" 
AR Path="/5F877533/5F8DA6F8" Ref="Q801"  Part="1" 
AR Path="/5F877849/5F8DA6F8" Ref="Q601"  Part="1" 
F 0 "Q701" H 4980 4096 50  0000 L CNN
F 1 "AO3414" H 4980 4005 50  0000 L CNN
F 2 "SOT95P280X125-3N" H 5000 3900 50  0001 L CNN
F 3 "https://static6.arrow.com/aropdfconversion/67ac6f06d2170690d71560ead25e52fb73b77ec0/ao3414.pdf" H 5000 3800 50  0001 L CNN
F 4 "Trans MOSFET N-CH 20V 3A 3-Pin SOT-23" H 5000 3700 50  0001 L CNN "Description"
F 5 "1.25" H 5000 3600 50  0001 L CNN "Height"
F 6 "Alpha & Omega Semiconductors" H 5000 3500 50  0001 L CNN "Manufacturer_Name"
F 7 "AO3414" H 5000 3400 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "AO3414" H 5000 3300 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/ao3414/alpha-and-omega-semiconductor" H 5000 3200 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 5000 3100 50  0001 L CNN "Mouser Part Number"
F 11 "" H 5000 3000 50  0001 L CNN "Mouser Price/Stock"
	1    4550 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 3150 5400 3550
Wire Wire Line
	4850 3550 5400 3550
Connection ~ 5400 3550
Wire Wire Line
	5400 3550 5400 3900
Wire Wire Line
	4050 3950 4550 3950
$EndSCHEMATC
