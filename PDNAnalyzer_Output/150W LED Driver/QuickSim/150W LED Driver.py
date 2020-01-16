designFile = "Y:/Altium Projects/150WLEDDriver_LT3756-2/PDNAnalyzer_Output/150W LED Driver/odb.tgz"

powerNets = ["48V", "SW", "ISP", "ISN"]

groundNets = ["GND", "SENSE", "LED_GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "3"), ("J1", "1"), ("J1", "2") ],
"ground_pins": [ ("J1", "6"), ("J1", "5"), ("J1", "4"), ("J1", "pdna_pin_M_1"), ("J1", "pdna_pin_M_2") ],
"voltage": 48,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J2", "3"), ("J2", "1"), ("J2", "2") ],
"ground_pins": [ ("J2", "6"), ("J2", "5"), ("J2", "4") ],
"current": 1.8,
"Rpin": 0.166666666666667,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("D1", "1") ],
"ground_pins": [ ("R11", "2") ],
"voltage": 90,
"Rpin": 0,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("L1", "1") ],
"ground_pins": [ ("R11", "1") ],
"current": 0.0001,
"Rpin": 100000,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("D1", "1") ],
"ground_pins": [ ("R11", "2") ],
"resistance": 1E-09,
"Rpin": 500000,
}
]


voltage_regulators = [
{
"id": "5",
"type": "linear",

"in": [ ("D1", "1") ],
"out": [ ("D1", "2") ],
"ref": [],

"v2": -0.8,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "6",
"type": "linear",

"in": [ ("R3", "2") ],
"out": [ ("R3", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.028,
}
,
{
"id": "7",
"type": "linear",

"in": [ ("R11", "2") ],
"out": [ ("R11", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.01,
}
,
{
"id": "8",
"type": "linear",

"in": [ ("IC4", "1"), ("IC4", "2"), ("IC4", "3") ],
"out": [ ("IC4", "5"), ("IC4", "6"), ("IC4", "7"), ("IC4", "8") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0102857142857143,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.6E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 0.0002},
        {'name': 'LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.001065},
        {'name': 'LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 0.0002},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.6E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
