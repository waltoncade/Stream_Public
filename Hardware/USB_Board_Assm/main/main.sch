EESchema Schematic File Version 4
LIBS:main-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 9
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 650  1200 0    50   ~ 0
Inputs:\n- 4x USB Control\n- 4x Light Strip Control\nOutputs:\n- 1x USB Hub\n- 12V and 5V\nKey Features:\n- 12V to 5V DC converter
$Comp
L power:+12V #PWR0104
U 1 1 5F3B88F4
P 2800 1950
F 0 "#PWR0104" H 2800 1800 50  0001 C CNN
F 1 "+12V" H 2815 2123 50  0000 C CNN
F 2 "" H 2800 1950 50  0001 C CNN
F 3 "" H 2800 1950 50  0001 C CNN
	1    2800 1950
	1    0    0    -1  
$EndComp
$Comp
L main-rescue:PJ-037A-SamacSys_Parts J101
U 1 1 5F3B4267
P 2800 2050
F 0 "J101" H 3200 1700 50  0000 C CNN
F 1 "PJ-037A" H 3200 1800 50  0000 C CNN
F 2 "PJ037A" H 3450 2150 50  0001 L CNN
F 3 "https://www.mouser.com/datasheet/2/670/pj-037a-1312287.pdf" H 3450 2050 50  0001 L CNN
F 4 "DC Power Connectors Power Jacks" H 3450 1950 50  0001 L CNN "Description"
F 5 "11" H 3450 1850 50  0001 L CNN "Height"
F 6 "CUI Devices" H 3450 1750 50  0001 L CNN "Manufacturer_Name"
F 7 "PJ-037A" H 3450 1650 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "PJ-037A" H 3450 1550 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/pj-037a/cui-devices" H 3450 1450 50  0001 L CNN "Arrow Price/Stock"
F 10 "490-PJ-037A" H 3450 1350 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.co.uk/ProductDetail/CUI-Devices/PJ-037A?qs=WyjlAZoYn53bdNRXfildEA%3D%3D" H 3450 1250 50  0001 L CNN "Mouser Price/Stock"
	1    2800 2050
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5F3B9773
P 2800 2050
F 0 "#PWR0105" H 2800 1800 50  0001 C CNN
F 1 "GND" H 2805 1877 50  0000 C CNN
F 2 "" H 2800 2050 50  0001 C CNN
F 3 "" H 2800 2050 50  0001 C CNN
	1    2800 2050
	1    0    0    -1  
$EndComp
Text Label 4550 2250 2    50   ~ 0
USB1
Text Label 5450 2250 0    50   ~ 0
USB2
Text Label 4550 2350 2    50   ~ 0
USB3
Text Label 5450 2350 0    50   ~ 0
USB4
Text Label 4550 2450 2    50   ~ 0
L1G
Text Label 5450 2450 0    50   ~ 0
L1R
Text Label 4550 2550 2    50   ~ 0
L2G
Text Label 5450 2550 0    50   ~ 0
L2R
Text Label 4550 2650 2    50   ~ 0
L3G
Text Label 5450 2650 0    50   ~ 0
L3R
Text Label 4550 2750 2    50   ~ 0
L4G
Text Label 5450 2750 0    50   ~ 0
L4R
Text Label 9050 2400 2    50   ~ 0
L1G
Text Label 9050 2550 2    50   ~ 0
L1R
Text Label 9050 3100 2    50   ~ 0
L2G
Text Label 9050 3250 2    50   ~ 0
L2R
Text Label 9050 3800 2    50   ~ 0
L3G
Text Label 9050 3950 2    50   ~ 0
L3R
Text Label 9050 4550 2    50   ~ 0
L4G
Text Label 9050 4700 2    50   ~ 0
L4R
Text Label 6900 1850 2    50   ~ 0
USB1
$Sheet
S 9400 2300 1000 350 
U 5F3900B0
F0 "Light_1" 50
F1 "Light_Logic.sch" 50
F2 "LG" I L 9400 2400 50 
F3 "LR" I L 9400 2550 50 
$EndSheet
Wire Wire Line
	9400 2400 9050 2400
Wire Wire Line
	9400 2550 9050 2550
Wire Wire Line
	6900 1850 7250 1850
Text Label 6900 2050 2    50   ~ 0
D1-
Text Label 6900 2250 2    50   ~ 0
D1+
Wire Wire Line
	6900 2050 7250 2050
Wire Wire Line
	6900 2250 7250 2250
Text Label 6900 2800 2    50   ~ 0
USB2
Text Label 6900 3000 2    50   ~ 0
D2-
Text Label 6900 3200 2    50   ~ 0
D2+
Text Label 6900 3800 2    50   ~ 0
USB3
Text Label 6900 4000 2    50   ~ 0
D3-
Text Label 6900 4200 2    50   ~ 0
D3+
Text Label 6900 4800 2    50   ~ 0
USB4
Text Label 6900 5000 2    50   ~ 0
D4-
Text Label 6900 5200 2    50   ~ 0
D4+
Text Label 2900 5950 2    50   ~ 0
D1+
Text Label 2900 5850 2    50   ~ 0
D1-
Text Label 2900 5750 2    50   ~ 0
D2+
Text Label 2900 5650 2    50   ~ 0
D2-
Text Label 2900 5550 2    50   ~ 0
D3+
Text Label 2900 5450 2    50   ~ 0
D3-
Text Label 2900 5350 2    50   ~ 0
D4+
Text Label 2900 5250 2    50   ~ 0
D4-
$Comp
L power:+5V #PWR0113
U 1 1 5F3AADA1
P 4550 3050
F 0 "#PWR0113" H 4550 2900 50  0001 C CNN
F 1 "+5V" V 4565 3178 50  0000 L CNN
F 2 "" H 4550 3050 50  0001 C CNN
F 3 "" H 4550 3050 50  0001 C CNN
	1    4550 3050
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0114
U 1 1 5F3AB605
P 4550 3150
F 0 "#PWR0114" H 4550 3000 50  0001 C CNN
F 1 "+5V" V 4565 3278 50  0000 L CNN
F 2 "" H 4550 3150 50  0001 C CNN
F 3 "" H 4550 3150 50  0001 C CNN
	1    4550 3150
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0119
U 1 1 5F3ABB05
P 5450 3050
F 0 "#PWR0119" H 5450 2800 50  0001 C CNN
F 1 "GND" V 5455 2922 50  0000 R CNN
F 2 "" H 5450 3050 50  0001 C CNN
F 3 "" H 5450 3050 50  0001 C CNN
	1    5450 3050
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 5F3AC00F
P 5450 3150
F 0 "#PWR0120" H 5450 2900 50  0001 C CNN
F 1 "GND" V 5455 3022 50  0000 R CNN
F 2 "" H 5450 3150 50  0001 C CNN
F 3 "" H 5450 3150 50  0001 C CNN
	1    5450 3150
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0106
U 1 1 5F3B02B6
P 2800 4950
F 0 "#PWR0106" H 2800 4700 50  0001 C CNN
F 1 "GND" V 2805 4822 50  0000 R CNN
F 2 "" H 2800 4950 50  0001 C CNN
F 3 "" H 2800 4950 50  0001 C CNN
	1    2800 4950
	0    1    1    0   
$EndComp
$Comp
L main-rescue:USB-A1HSW6-SamacSys_Parts J?
U 1 1 5F866FC9
P 2850 2900
AR Path="/5F39AC8F/5F866FC9" Ref="J?"  Part="1" 
AR Path="/5F39FEA5/5F866FC9" Ref="J?"  Part="1" 
AR Path="/5F3A09F1/5F866FC9" Ref="J?"  Part="1" 
AR Path="/5F3A0E43/5F866FC9" Ref="J?"  Part="1" 
AR Path="/5F866FC9" Ref="J102"  Part="1" 
F 0 "J102" H 3250 3165 50  0000 C CNN
F 1 "USB-A1HSW6" H 3250 3074 50  0000 C CNN
F 2 "USBA1HSW6" H 3500 3000 50  0001 L CNN
F 3 "http://www.on-shore.com/wp-content/uploads/2015/09/usb-a1hsxx.pdf" H 3500 2900 50  0001 L CNN
F 4 "USB - A Receptacle Connector 4 Position Through Hole, Right Angle" H 3500 2800 50  0001 L CNN "Description"
F 5 "7" H 3500 2700 50  0001 L CNN "Height"
F 6 "On-Shore Technology, Inc" H 3500 2600 50  0001 L CNN "Manufacturer_Name"
F 7 "USB-A1HSW6" H 3500 2500 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "USB-A1HSW6" H 3500 2400 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/usb-a1hsw6/on-shore-technology" H 3500 2300 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 3500 2200 50  0001 L CNN "Mouser Part Number"
F 11 "" H 3500 2100 50  0001 L CNN "Mouser Price/Stock"
	1    2850 2900
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0101
U 1 1 5F8760B9
P 2050 2900
F 0 "#PWR0101" H 2050 2750 50  0001 C CNN
F 1 "+5V" H 2065 3073 50  0000 C CNN
F 2 "" H 2050 2900 50  0001 C CNN
F 3 "" H 2050 2900 50  0001 C CNN
	1    2050 2900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5F876F1E
P 2850 3000
F 0 "#PWR0107" H 2850 2750 50  0001 C CNN
F 1 "GND" H 2855 2827 50  0000 C CNN
F 2 "" H 2850 3000 50  0001 C CNN
F 3 "" H 2850 3000 50  0001 C CNN
	1    2850 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 2800 6900 2800
Wire Wire Line
	6900 3000 7250 3000
Wire Wire Line
	7250 3200 6900 3200
Wire Wire Line
	6900 3800 7250 3800
Wire Wire Line
	7250 4000 6900 4000
Wire Wire Line
	6900 4200 7250 4200
Wire Wire Line
	7250 4800 6900 4800
Wire Wire Line
	6900 5000 7250 5000
Wire Wire Line
	7250 5200 6900 5200
$Comp
L power:GND #PWR0102
U 1 1 5F87BB41
P 2050 3200
F 0 "#PWR0102" H 2050 2950 50  0001 C CNN
F 1 "GND" H 2055 3027 50  0000 C CNN
F 2 "" H 2050 3200 50  0001 C CNN
F 3 "" H 2050 3200 50  0001 C CNN
	1    2050 3200
	1    0    0    -1  
$EndComp
$Comp
L main-rescue:TST-110-01-G-D-SamacSys_Parts J103
U 1 1 5F87C7F3
P 4550 2250
F 0 "J103" H 5000 2515 50  0000 C CNN
F 1 "TST-110-01-G-D" H 5000 2424 50  0000 C CNN
F 2 "TST-110-XX-Y-D" H 5300 2350 50  0001 L CNN
F 3 "http://suddendocs.samtec.com/prints/tst-1xx-xx-x-x-xx-xx-mkt.pdf" H 5300 2250 50  0001 L CNN
F 4 "20 Position, Shrouded PCB Headers, 0.100&quot; pitch" H 5300 2150 50  0001 L CNN "Description"
F 5 "" H 5300 2050 50  0001 L CNN "Height"
F 6 "SAMTEC" H 5300 1950 50  0001 L CNN "Manufacturer_Name"
F 7 "TST-110-01-G-D" H 5300 1850 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "TST-110-01-G-D" H 5300 1750 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/tst-110-01-g-d/samtec" H 5300 1650 50  0001 L CNN "Arrow Price/Stock"
F 10 "200-TST11001GD" H 5300 1550 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.co.uk/ProductDetail/Samtec/TST-110-01-G-D?qs=rU5fayqh%252BE1iIX99OHEFCg%3D%3D" H 5300 1450 50  0001 L CNN "Mouser Price/Stock"
	1    4550 2250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 5F885C92
P 5450 2950
F 0 "#PWR0118" H 5450 2700 50  0001 C CNN
F 1 "GND" V 5455 2822 50  0000 R CNN
F 2 "" H 5450 2950 50  0001 C CNN
F 3 "" H 5450 2950 50  0001 C CNN
	1    5450 2950
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0117
U 1 1 5F8861DF
P 5450 2850
F 0 "#PWR0117" H 5450 2600 50  0001 C CNN
F 1 "GND" V 5455 2722 50  0000 R CNN
F 2 "" H 5450 2850 50  0001 C CNN
F 3 "" H 5450 2850 50  0001 C CNN
	1    5450 2850
	0    -1   -1   0   
$EndComp
$Comp
L power:+12V #PWR0111
U 1 1 5F886839
P 4550 2850
F 0 "#PWR0111" H 4550 2700 50  0001 C CNN
F 1 "+12V" V 4565 3023 50  0000 C CNN
F 2 "" H 4550 2850 50  0001 C CNN
F 3 "" H 4550 2850 50  0001 C CNN
	1    4550 2850
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0112
U 1 1 5F8878B2
P 4550 2950
F 0 "#PWR0112" H 4550 2800 50  0001 C CNN
F 1 "+5V" V 4565 3078 50  0000 L CNN
F 2 "" H 4550 2950 50  0001 C CNN
F 3 "" H 4550 2950 50  0001 C CNN
	1    4550 2950
	0    -1   -1   0   
$EndComp
$Sheet
S 9400 3000 1000 350 
U 5F895509
F0 "Light_2" 50
F1 "Light_Logic.sch" 50
F2 "LG" I L 9400 3100 50 
F3 "LR" I L 9400 3250 50 
$EndSheet
Wire Wire Line
	9400 3100 9050 3100
Wire Wire Line
	9400 3250 9050 3250
$Sheet
S 9400 3700 1000 350 
U 5F89571F
F0 "Light_3" 50
F1 "Light_Logic.sch" 50
F2 "LG" I L 9400 3800 50 
F3 "LR" I L 9400 3950 50 
$EndSheet
Wire Wire Line
	9400 3800 9050 3800
Wire Wire Line
	9400 3950 9050 3950
$Sheet
S 9400 4450 1000 350 
U 5F8959AC
F0 "Light_4" 50
F1 "Light_Logic.sch" 50
F2 "LG" I L 9400 4550 50 
F3 "LR" I L 9400 4700 50 
$EndSheet
Wire Wire Line
	9400 4550 9050 4550
Wire Wire Line
	9400 4700 9050 4700
$Sheet
S 7250 4650 1000 650 
U 5F877849
F0 "USB_4" 50
F1 "USB_Logic.sch" 50
F2 "Control" I L 7250 4800 50 
F3 "D-" O L 7250 5000 50 
F4 "D+" O L 7250 5200 50 
$EndSheet
$Sheet
S 7250 3650 1000 650 
U 5F8776AE
F0 "USB_3" 50
F1 "USB_Logic.sch" 50
F2 "Control" I L 7250 3800 50 
F3 "D-" O L 7250 4000 50 
F4 "D+" O L 7250 4200 50 
$EndSheet
$Sheet
S 7250 2650 1000 650 
U 5F877533
F0 "USB_2" 50
F1 "USB_Logic.sch" 50
F2 "Control" I L 7250 2800 50 
F3 "D-" O L 7250 3000 50 
F4 "D+" O L 7250 3200 50 
$EndSheet
$Sheet
S 7250 1700 1000 650 
U 5F39AC8F
F0 "USB_1" 50
F1 "USB_Logic.sch" 50
F2 "Control" I L 7250 1850 50 
F3 "D-" O L 7250 2050 50 
F4 "D+" O L 7250 2250 50 
$EndSheet
Wire Wire Line
	2500 5050 2900 5050
Wire Wire Line
	2500 5150 2900 5150
$Comp
L main-rescue:ECS-120-20-4-SamacSys_Parts Y101
U 1 1 5F89D192
P 2500 5150
F 0 "Y101" H 2792 4785 50  0000 C CNN
F 1 "ECS-120-20-4" H 2792 4876 50  0000 C CNN
F 2 "HC-49USX" H 3150 5250 50  0001 L CNN
F 3 "https://ecsxtal.com/store/pdf/hc_49us.pdf" H 3150 5150 50  0001 L CNN
F 4 "Crystals 12MHz 20pF HC-49US" H 3150 5050 50  0001 L CNN "Description"
F 5 "" H 3150 4950 50  0001 L CNN "Height"
F 6 "ECS" H 3150 4850 50  0001 L CNN "Manufacturer_Name"
F 7 "ECS-120-20-4" H 3150 4750 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "" H 3150 4650 50  0001 L CNN "Arrow Part Number"
F 9 "" H 3150 4550 50  0001 L CNN "Arrow Price/Stock"
F 10 "520-HCU1200-20" H 3150 4450 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=520-HCU1200-20" H 3150 4350 50  0001 L CNN "Mouser Price/Stock"
	1    2500 5150
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 5F8A3860
P 1450 6050
F 0 "#PWR0103" H 1450 5800 50  0001 C CNN
F 1 "GND" H 1455 5877 50  0000 C CNN
F 2 "" H 1450 6050 50  0001 C CNN
F 3 "" H 1450 6050 50  0001 C CNN
	1    1450 6050
	0    1    1    0   
$EndComp
$Comp
L main-rescue:GRM21BC81D106KE51L-SamacSys_Parts C102
U 1 1 5F8A5334
P 2900 4650
F 0 "C102" V 3104 4778 50  0000 L CNN
F 1 "GRM21BC81D106KE51L" V 3195 4778 50  0000 L CNN
F 2 "CAPC2012X145N" H 3250 4700 50  0001 L CNN
F 3 "http://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/mlcc/c02e.pdf" H 3250 4600 50  0001 L CNN
F 4 "Multilayer Ceramic Capacitors MLCC - SMD/SMT 0805 10uF 20volts *Derate Voltage/Temp" H 3250 4500 50  0001 L CNN "Description"
F 5 "1.45" H 3250 4400 50  0001 L CNN "Height"
F 6 "Murata Electronics" H 3250 4300 50  0001 L CNN "Manufacturer_Name"
F 7 "GRM21BC81D106KE51L" H 3250 4200 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "GRM21BC81D106KE51L" H 3250 4100 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/grm21bc81d106ke51l/murata-manufacturing" H 3250 4000 50  0001 L CNN "Arrow Price/Stock"
F 10 "81-GRM21BC81D106KE1L" H 3250 3900 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=81-GRM21BC81D106KE1L" H 3250 3800 50  0001 L CNN "Mouser Price/Stock"
	1    2900 4650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2900 4650 2900 4950
Wire Wire Line
	2800 4950 2900 4950
$Comp
L power:+5V #PWR0108
U 1 1 5F8A6D6B
P 2900 4150
F 0 "#PWR0108" H 2900 4000 50  0001 C CNN
F 1 "+5V" H 2915 4323 50  0000 C CNN
F 2 "" H 2900 4150 50  0001 C CNN
F 3 "" H 2900 4150 50  0001 C CNN
	1    2900 4150
	1    0    0    -1  
$EndComp
$Comp
L main-rescue:RK73H2ATTD2701F-SamacSys_Parts R101
U 1 1 5F8A7EAF
P 2900 6250
F 0 "R101" V 3204 6338 50  0000 L CNN
F 1 "RK73H2ATTD2701F" V 3295 6338 50  0000 L CNN
F 2 "RESC2012X60N" H 3450 6300 50  0001 L CNN
F 3 "http://www.koaspeer.com/catimages/Products/RK73H/RK73H.pdf" H 3450 6200 50  0001 L CNN
F 4 "Resistor Thick Film 2.7K 1% SMD 0805" H 3450 6100 50  0001 L CNN "Description"
F 5 "0.6" H 3450 6000 50  0001 L CNN "Height"
F 6 "KOA Speer" H 3450 5900 50  0001 L CNN "Manufacturer_Name"
F 7 "RK73H2ATTD2701F" H 3450 5800 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "RK73H2ATTD2701F" H 3450 5700 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/rk73h2attd2701f/koa-speer-electronics" H 3450 5600 50  0001 L CNN "Arrow Price/Stock"
F 10 "660-RK73H2ATTD2701F" H 3450 5500 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=660-RK73H2ATTD2701F" H 3450 5400 50  0001 L CNN "Mouser Price/Stock"
	1    2900 6250
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0109
U 1 1 5F8AA5A7
P 2900 6950
F 0 "#PWR0109" H 2900 6700 50  0001 C CNN
F 1 "GND" H 2905 6777 50  0000 C CNN
F 2 "" H 2900 6950 50  0001 C CNN
F 3 "" H 2900 6950 50  0001 C CNN
	1    2900 6950
	1    0    0    -1  
$EndComp
Text Label 2050 3100 2    50   ~ 0
D0+
Text Label 2050 3000 2    50   ~ 0
DO-
Text Label 4200 6150 0    50   ~ 0
D0+
Text Label 4200 6250 0    50   ~ 0
DO-
Text Label 2500 6050 0    50   ~ 0
VD18
Text Label 4200 4950 0    50   ~ 0
VD18
Text Label 4200 5650 0    50   ~ 0
VD33
Text Label 2600 6150 0    50   ~ 0
VD33
Wire Wire Line
	2600 6150 2900 6150
$Comp
L power:+5V #PWR0121
U 1 1 5F8B0B60
P 5800 6050
F 0 "#PWR0121" H 5800 5900 50  0001 C CNN
F 1 "+5V" H 5815 6223 50  0000 C CNN
F 2 "" H 5800 6050 50  0001 C CNN
F 3 "" H 5800 6050 50  0001 C CNN
	1    5800 6050
	0    1    1    0   
$EndComp
$Comp
L main-rescue:RK73H2ATTD2701F-SamacSys_Parts R103
U 1 1 5F8B21C4
P 5650 6050
F 0 "R103" V 5954 6138 50  0000 L CNN
F 1 "RK73H2ATTD2701F" V 6045 6138 50  0000 L CNN
F 2 "RESC2012X60N" H 6200 6100 50  0001 L CNN
F 3 "http://www.koaspeer.com/catimages/Products/RK73H/RK73H.pdf" H 6200 6000 50  0001 L CNN
F 4 "Resistor Thick Film 2.7K 1% SMD 0805" H 6200 5900 50  0001 L CNN "Description"
F 5 "0.6" H 6200 5800 50  0001 L CNN "Height"
F 6 "KOA Speer" H 6200 5700 50  0001 L CNN "Manufacturer_Name"
F 7 "RK73H2ATTD2701F" H 6200 5600 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "RK73H2ATTD2701F" H 6200 5500 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/rk73h2attd2701f/koa-speer-electronics" H 6200 5400 50  0001 L CNN "Arrow Price/Stock"
F 10 "660-RK73H2ATTD2701F" H 6200 5300 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=660-RK73H2ATTD2701F" H 6200 5200 50  0001 L CNN "Mouser Price/Stock"
	1    5650 6050
	-1   0    0    1   
$EndComp
Wire Wire Line
	5800 6050 5650 6050
Wire Wire Line
	4200 6050 4700 6050
Connection ~ 2900 4950
$Comp
L main-rescue:FE1.1S-SamacSys_Parts IC101
U 1 1 5F3CE5E6
P 2900 4950
F 0 "IC101" H 3550 5215 50  0000 C CNN
F 1 "FE1.1S" H 3550 5124 50  0000 C CNN
F 2 "SOP64P600X175-28N" H 4050 5050 50  0001 L CNN
F 3 "https://cdn-shop.adafruit.com/product-files/2991/FE1.1s+Data+Sheet+(Rev.+1.0).pdf" H 4050 4950 50  0001 L CNN
F 4 "USB 2.0 HIGH SPEED 4-PORT HUB CONTROLLER" H 4050 4850 50  0001 L CNN "Description"
F 5 "1.75" H 4050 4750 50  0001 L CNN "Height"
F 6 "JFD IC" H 4050 4650 50  0001 L CNN "Manufacturer_Name"
F 7 "FE1.1S" H 4050 4550 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "FE1.1S" H 4050 4450 50  0001 L CNN "Arrow Part Number"
F 9 "" H 4050 4350 50  0001 L CNN "Arrow Price/Stock"
F 10 "" H 4050 4250 50  0001 L CNN "Mouser Part Number"
F 11 "" H 4050 4150 50  0001 L CNN "Mouser Price/Stock"
	1    2900 4950
	1    0    0    -1  
$EndComp
Connection ~ 4700 6050
Wire Wire Line
	4700 6050 4950 6050
$Comp
L main-rescue:RK73H2ATTD2701F-SamacSys_Parts R102
U 1 1 5F8BDD19
P 4900 5150
F 0 "R102" V 5204 5238 50  0000 L CNN
F 1 "RK73H2ATTD2701F" V 5295 5238 50  0000 L CNN
F 2 "RESC2012X60N" H 5450 5200 50  0001 L CNN
F 3 "http://www.koaspeer.com/catimages/Products/RK73H/RK73H.pdf" H 5450 5100 50  0001 L CNN
F 4 "Resistor Thick Film 2.7K 1% SMD 0805" H 5450 5000 50  0001 L CNN "Description"
F 5 "0.6" H 5450 4900 50  0001 L CNN "Height"
F 6 "KOA Speer" H 5450 4800 50  0001 L CNN "Manufacturer_Name"
F 7 "RK73H2ATTD2701F" H 5450 4700 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "RK73H2ATTD2701F" H 5450 4600 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/rk73h2attd2701f/koa-speer-electronics" H 5450 4500 50  0001 L CNN "Arrow Price/Stock"
F 10 "660-RK73H2ATTD2701F" H 5450 4400 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=660-RK73H2ATTD2701F" H 5450 4300 50  0001 L CNN "Mouser Price/Stock"
	1    4900 5150
	0    1    1    0   
$EndComp
$Comp
L power:+5V #PWR0116
U 1 1 5F8BE43A
P 4900 5150
F 0 "#PWR0116" H 4900 5000 50  0001 C CNN
F 1 "+5V" H 4915 5323 50  0000 C CNN
F 2 "" H 4900 5150 50  0001 C CNN
F 3 "" H 4900 5150 50  0001 C CNN
	1    4900 5150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0110
U 1 1 5F8C1F45
P 4200 5750
F 0 "#PWR0110" H 4200 5600 50  0001 C CNN
F 1 "+5V" V 4215 5878 50  0000 L CNN
F 2 "" H 4200 5750 50  0001 C CNN
F 3 "" H 4200 5750 50  0001 C CNN
	1    4200 5750
	0    1    1    0   
$EndComp
Connection ~ 4900 5850
Wire Wire Line
	4900 5850 4200 5850
$Comp
L main-rescue:PJ-031DH-SamacSys_Parts J104
U 1 1 5F8C45EA
P 6050 5850
F 0 "J104" H 6450 6115 50  0000 C CNN
F 1 "PJ-031DH" H 6450 6024 50  0000 C CNN
F 2 "PJ031DH" H 6700 5950 50  0001 L CNN
F 3 "https://www.cui.com/product/resource/pj-031dh.pdf" H 6700 5850 50  0001 L CNN
F 4 "DC Power Connectors Power Jacks" H 6700 5750 50  0001 L CNN "Description"
F 5 "7" H 6700 5650 50  0001 L CNN "Height"
F 6 "CUI Devices" H 6700 5550 50  0001 L CNN "Manufacturer_Name"
F 7 "PJ-031DH" H 6700 5450 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "PJ-031DH" H 6700 5350 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/pj-031dh/cui-devices" H 6700 5250 50  0001 L CNN "Arrow Price/Stock"
F 10 "490-PJ-031DH" H 6700 5150 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.co.uk/ProductDetail/CUI-Devices/PJ-031DH?qs=WyjlAZoYn52nDKNxzxC0%2FA%3D%3D" H 6700 5050 50  0001 L CNN "Mouser Price/Stock"
	1    6050 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 5850 6050 5850
$Comp
L power:GND #PWR0122
U 1 1 5F8C7F71
P 6850 5850
F 0 "#PWR0122" H 6850 5600 50  0001 C CNN
F 1 "GND" V 6855 5722 50  0000 R CNN
F 2 "" H 6850 5850 50  0001 C CNN
F 3 "" H 6850 5850 50  0001 C CNN
	1    6850 5850
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0123
U 1 1 5F8C86E3
P 6850 5950
F 0 "#PWR0123" H 6850 5800 50  0001 C CNN
F 1 "+5V" H 6865 6123 50  0000 C CNN
F 2 "" H 6850 5950 50  0001 C CNN
F 3 "" H 6850 5950 50  0001 C CNN
	1    6850 5950
	-1   0    0    1   
$EndComp
Text Label 4200 5950 0    50   ~ 0
VD33
$Comp
L main-rescue:TL2201EEYA-SamacSys_Parts S101
U 1 1 5F8D0634
P 5900 7350
F 0 "S101" H 6500 7615 50  0000 C CNN
F 1 "TL2201EEYA" H 6500 7524 50  0000 C CNN
F 2 "TL2201EEYA" H 6950 7450 50  0001 L CNN
F 3 "https://www.e-switch.com/system/asset/product_line/data_sheet/61/TL2201.pdf" H 6950 7350 50  0001 L CNN
F 4 "Tactile Switches DPDT .1A 30V" H 6950 7250 50  0001 L CNN "Description"
F 5 "14" H 6950 7150 50  0001 L CNN "Height"
F 6 "E-Switch" H 6950 7050 50  0001 L CNN "Manufacturer_Name"
F 7 "TL2201EEYA" H 6950 6950 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "" H 6950 6850 50  0001 L CNN "Arrow Part Number"
F 9 "" H 6950 6750 50  0001 L CNN "Arrow Price/Stock"
F 10 "612-TL2201EEYA" H 6950 6650 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.co.uk/ProductDetail/E-Switch/TL2201EEYA?qs=YXf4ACKMM4x3Bw8ZH9o%2FjQ%3D%3D" H 6950 6550 50  0001 L CNN "Mouser Price/Stock"
	1    5900 7350
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0115
U 1 1 5F8D5253
P 4700 7250
F 0 "#PWR0115" H 4700 7000 50  0001 C CNN
F 1 "GND" V 4705 7122 50  0000 R CNN
F 2 "" H 4700 7250 50  0001 C CNN
F 3 "" H 4700 7250 50  0001 C CNN
	1    4700 7250
	0    1    1    0   
$EndComp
Wire Wire Line
	4700 6050 4700 7150
$Comp
L main-rescue:GRM21BC81D106KE51L-SamacSys_Parts C104
U 1 1 5F98914C
P 2600 6650
F 0 "C104" V 2804 6778 50  0000 L CNN
F 1 "GRM21BC81D106KE51L" V 2895 6778 50  0000 L CNN
F 2 "CAPC2012X145N" H 2950 6700 50  0001 L CNN
F 3 "http://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/mlcc/c02e.pdf" H 2950 6600 50  0001 L CNN
F 4 "Multilayer Ceramic Capacitors MLCC - SMD/SMT 0805 10uF 20volts *Derate Voltage/Temp" H 2950 6500 50  0001 L CNN "Description"
F 5 "1.45" H 2950 6400 50  0001 L CNN "Height"
F 6 "Murata Electronics" H 2950 6300 50  0001 L CNN "Manufacturer_Name"
F 7 "GRM21BC81D106KE51L" H 2950 6200 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "GRM21BC81D106KE51L" H 2950 6100 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/grm21bc81d106ke51l/murata-manufacturing" H 2950 6000 50  0001 L CNN "Arrow Price/Stock"
F 10 "81-GRM21BC81D106KE1L" H 2950 5900 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=81-GRM21BC81D106KE1L" H 2950 5800 50  0001 L CNN "Mouser Price/Stock"
	1    2600 6650
	0    -1   -1   0   
$EndComp
$Comp
L main-rescue:GRM21BC81D106KE51L-SamacSys_Parts C101
U 1 1 5F8A02F4
P 1450 6050
F 0 "C101" V 1654 6178 50  0000 L CNN
F 1 "GRM21BC81D106KE51L" V 1745 6178 50  0000 L CNN
F 2 "CAPC2012X145N" H 1800 6100 50  0001 L CNN
F 3 "http://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/mlcc/c02e.pdf" H 1800 6000 50  0001 L CNN
F 4 "Multilayer Ceramic Capacitors MLCC - SMD/SMT 0805 10uF 20volts *Derate Voltage/Temp" H 1800 5900 50  0001 L CNN "Description"
F 5 "1.45" H 1800 5800 50  0001 L CNN "Height"
F 6 "Murata Electronics" H 1800 5700 50  0001 L CNN "Manufacturer_Name"
F 7 "GRM21BC81D106KE51L" H 1800 5600 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "GRM21BC81D106KE51L" H 1800 5500 50  0001 L CNN "Arrow Part Number"
F 9 "https://www.arrow.com/en/products/grm21bc81d106ke51l/murata-manufacturing" H 1800 5400 50  0001 L CNN "Arrow Price/Stock"
F 10 "81-GRM21BC81D106KE1L" H 1800 5300 50  0001 L CNN "Mouser Part Number"
F 11 "https://www.mouser.com/Search/Refine.aspx?Keyword=81-GRM21BC81D106KE1L" H 1800 5200 50  0001 L CNN "Mouser Price/Stock"
	1    1450 6050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0124
U 1 1 5F98F3AA
P 2600 6650
F 0 "#PWR0124" H 2600 6400 50  0001 C CNN
F 1 "GND" H 2605 6477 50  0000 C CNN
F 2 "" H 2600 6650 50  0001 C CNN
F 3 "" H 2600 6650 50  0001 C CNN
	1    2600 6650
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 6050 2900 6050
$EndSCHEMATC
