#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "N#N",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50341,-0.000166173,3.03798e-08,1.44597e-09,-9.50262e-13,486.598,3.08249], Tmin=(10,'K'), Tmax=(806.389,'K')),
            NASAPolynomial(coeffs=[3.10804,0.000789777,1.22084e-07,-1.7575e-10,3.17808e-14,583.047,5.1075], Tmin=(806.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.04703,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
N       0.54338000    0.00000000    0.00000000
N      -0.54338000    0.00000000   -0.00000000
""",
)

entry(
    index = 1,
    label = "[Ar]",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,-15.5058,4.36578], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,-15.5058,4.36578], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-0.128901,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
Ar      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 2,
    label = "[He]",
    molecule = 
"""
1 He u0 p1 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,-1490.85,0.91429], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,-1490.85,0.91429], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-12.3956,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
He      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 3,
    label = "[Ne]",
    molecule = 
"""
1 Ne u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,1.99051e-15,-1.1909e-17,2.10806e-20,-1.11018e-23,-1494.5,3.32691], Tmin=(10,'K'), Tmax=(794.005,'K')),
            NASAPolynomial(coeffs=[2.5,1.52667e-14,-1.58445e-17,6.63089e-21,-9.62112e-25,-1494.5,3.32691], Tmin=(794.005,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-12.4259,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
Ne      0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 4,
    label = "CCCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67726,0.0329734,-7.66352e-05,2.29266e-07,-2.01652e-10,-15797.7,8.70019], Tmin=(10,'K'), Tmax=(466.223,'K')),
            NASAPolynomial(coeffs=[-2.34366,0.0513638,-2.87731e-05,7.78097e-09,-8.19317e-13,-14874.7,37.0306], Tmin=(466.223,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-131.35,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.73902700   -0.64359800    0.46624200
C      -0.68326100   -0.68559000   -0.08914700
C       1.46906600    0.66071600    0.16496900
C      -1.59565100    0.38479900    0.49969900
H       0.70452800   -0.80081400    1.54782200
H       1.30735700   -1.47820100    0.05113200
H      -0.64524500   -0.57464700   -1.17632600
H      -1.11182200   -1.67059900    0.10570000
H       1.47000300    0.86351000   -0.90776900
H       0.99762200    1.50799300    0.66235500
H       2.50548900    0.61938300    0.49829500
H      -1.60741400    0.32476200    1.58971700
H      -1.26631900    1.38692100    0.22616000
H      -2.61999200    0.26817700    0.14739700
""",
)

entry(
    index = 5,
    label = "[O][O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.507,-0.000405639,1.23211e-06,1.57398e-09,-2.02187e-12,-1252.36,4.69557], Tmin=(10,'K'), Tmax=(633.958,'K')),
            NASAPolynomial(coeffs=[2.87704,0.00206503,-1.05483e-06,2.36422e-10,-1.85713e-14,-1142.26,7.68604], Tmin=(633.958,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.4099,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.59493100    0.00000000    0.00000000
O      -0.59493100    0.00000000   -0.00000000
""",
)

entry(
    index = 6,
    label = "[CH]",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4963,0.000296825,-2.04497e-06,4.10405e-09,-2.08599e-12,71249.8,1.3278], Tmin=(10,'K'), Tmax=(780.671,'K')),
            NASAPolynomial(coeffs=[3.18599,0.000482328,2.97153e-07,-2.0052e-10,3.04729e-14,71341,3.02213], Tmin=(780.671,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (592.404,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.55850200    0.00000000    0.00000000
H      -0.55850200    0.00000000    0.00000000
""",
)

entry(
    index = 7,
    label = "[C]#C",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99091,0.000660445,1.20685e-05,-3.3536e-08,2.89139e-11,66931.3,-3.28472], Tmin=(10,'K'), Tmax=(401.945,'K')),
            NASAPolynomial(coeffs=[4.08024,0.00187029,-2.79063e-07,-6.53672e-11,1.5865e-14,66907.2,-3.84518], Tmin=(401.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (556.499,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.04550000    0.00035300   -0.00000000
C       1.14939700   -0.01485300   -0.00000000
H      -1.10389700    0.01450000   -0.00000000
""",
)

entry(
    index = 8,
    label = "[O]",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,4.66012e-16,-1.89077e-18,2.26862e-21,-8.121e-25,29269.9,4.09089], Tmin=(10,'K'), Tmax=(1259.07,'K')),
            NASAPolynomial(coeffs=[2.5,1.42187e-14,-1.19788e-17,4.27646e-21,-5.48837e-25,29269.9,4.09089], Tmin=(1259.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (243.363,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 9,
    label = "[C-]#[O+]",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50434,-0.00021832,2.80835e-07,1.45394e-09,-1.10233e-12,-13834.9,3.81713], Tmin=(10,'K'), Tmax=(774.826,'K')),
            NASAPolynomial(coeffs=[2.99717,0.00122365,-2.33553e-07,-6.27583e-11,1.92007e-14,-13721,6.3624], Tmin=(774.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-115.028,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.88202400   -0.94554200   -0.00000000
O      -2.00259200   -0.99890200    0.00000000
""",
)

entry(
    index = 10,
    label = "O=C=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53583,-0.0034783,3.85159e-05,-6.92159e-08,4.07543e-11,-48329,5.37924], Tmin=(10,'K'), Tmax=(533.72,'K')),
            NASAPolynomial(coeffs=[2.75533,0.00713059,-4.67605e-06,1.44281e-09,-1.69191e-13,-48313.5,8.0196], Tmin=(533.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-401.833,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -4.42441600   -0.26409900   -0.00000000
O      -2.11404500   -0.30570100    0.00000000
C      -3.26923100   -0.28490000    0.00000000
""",
)

entry(
    index = 11,
    label = "O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00475,-0.000240961,9.44101e-07,1.29411e-09,-1.12294e-12,-28364.7,-0.115922], Tmin=(10,'K'), Tmax=(774.235,'K')),
            NASAPolynomial(coeffs=[3.50585,0.00114691,5.60031e-07,-3.59745e-10,5.18994e-14,-28251.8,2.39357], Tmin=(774.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-235.836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -0.00189400    0.39032300   -0.00000000
H      -0.75864300   -0.19854300    0.00000000
H       0.76053700   -0.19178000   -0.00000000
""",
)

entry(
    index = 12,
    label = "C=O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03195,-0.00195093,9.19803e-06,2.64309e-09,-7.92557e-12,-13508.1,3.46229], Tmin=(10,'K'), Tmax=(594.338,'K')),
            NASAPolynomial(coeffs=[1.44721,0.00944813,-4.43648e-06,9.60406e-10,-7.68487e-14,-13095,15.4783], Tmin=(594.338,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.302,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.15593100   -0.07496700    0.26242600
C      -0.00747900    0.00051000   -0.00170100
H      -0.64601500   -0.89623700   -0.08090900
H      -0.50243700    0.97059400   -0.17981600
""",
)

entry(
    index = 13,
    label = "C",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04165,-0.00250165,1.15323e-05,3.46785e-09,-9.37972e-12,-9325.36,-0.432512], Tmin=(10,'K'), Tmax=(613.446,'K')),
            NASAPolynomial(coeffs=[0.692699,0.0117204,-4.62328e-06,7.8949e-10,-4.15329e-14,-8771.19,15.2556], Tmin=(613.446,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.5204,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.00005200    0.00005000    0.00002700
H      -0.67324700    0.84929600   -0.08463900
H      -0.39246700   -0.83245800   -0.57855800
H       0.08511400   -0.29218800    1.04358400
H       0.98054800    0.27530000   -0.38041400
""",
)

entry(
    index = 14,
    label = "C=C",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10242,-0.00693486,5.16363e-05,-6.17065e-08,2.43248e-11,6017.46,3.21985], Tmin=(10,'K'), Tmax=(759.068,'K')),
            NASAPolynomial(coeffs=[0.490981,0.0180919,-9.66792e-06,2.54144e-09,-2.62689e-13,6392.99,18.5096], Tmin=(759.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (50.0538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.62796400    0.03314200    0.20283300
C       0.62774700   -0.03482500   -0.20319900
H      -1.25810100   -0.84558200    0.24644200
H      -1.07542300    0.97013500    0.50765100
H       1.25791400    0.84383500   -0.24683200
H       1.07511500   -0.97185700   -0.50799900
""",
)

entry(
    index = 15,
    label = "C=CC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.988,0.000428016,6.73098e-05,-1.03955e-07,5.24921e-11,1781.35,6.97167], Tmin=(10,'K'), Tmax=(510.301,'K')),
            NASAPolynomial(coeffs=[0.400004,0.0285526,-1.53608e-05,4.04726e-09,-4.19123e-13,2147.54,21.8678], Tmin=(510.301,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (14.7994,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -1.13076500    0.03315800   -0.34423700
C       0.27021400    0.27432400    0.12086900
C       1.35214100   -0.23723900   -0.44439700
H      -1.14827900   -0.62175300   -1.21420200
H      -1.62026000    0.97208300   -0.60882200
H      -1.72964100   -0.42484300    0.44495200
H       0.38521100    0.91896400    0.98682800
H       1.28038800   -0.88508300   -1.31014400
H       2.34298200   -0.02857000   -0.06494800
""",
)

entry(
    index = 16,
    label = "[H][H]",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49863,8.11482e-05,-2.56237e-07,1.33921e-11,3.05429e-13,-444.289,-4.29111], Tmin=(10,'K'), Tmax=(610.663,'K')),
            NASAPolynomial(coeffs=[3.68702,-0.000782839,9.57106e-07,-3.18961e-10,3.52672e-14,-474.197,-5.16356], Tmin=(610.663,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.69451,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
H       0.36951500    0.00000000    0.00000000
H      -0.36951500    0.00000000   -0.00000000
""",
)

entry(
    index = 17,
    label = "[H]",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,4.66012e-16,-1.89077e-18,2.26862e-21,-8.121e-25,25472.6,-0.461279], Tmin=(10,'K'), Tmax=(1259.07,'K')),
            NASAPolynomial(coeffs=[2.5,1.42187e-14,-1.19788e-17,4.27646e-21,-5.48837e-25,25472.6,-0.461279], Tmin=(1259.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.791,'kJ/mol'),
        Cp0 = (20.7862,'J/(mol*K)'),
        CpInf = (20.7862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
H       0.00000000    0.00000000    0.00000000
""",
)

entry(
    index = 18,
    label = "[OH]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49686,0.000184716,-1.0034e-06,1.58134e-09,-6.16053e-13,4291.54,1.47257], Tmin=(10,'K'), Tmax=(982.369,'K')),
            NASAPolynomial(coeffs=[3.45024,-0.000290465,7.37563e-07,-2.89212e-10,3.53397e-14,4332.79,1.85996], Tmin=(982.369,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.6809,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.48557500    0.00000000    0.00000000
H      -0.48557500    0.00000000    0.00000000
""",
)

entry(
    index = 19,
    label = "[O]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02904,-0.00171365,1.0211e-05,-1.02433e-08,3.35616e-12,844.521,4.6613], Tmin=(10,'K'), Tmax=(934.081,'K')),
            NASAPolynomial(coeffs=[3.02687,0.00428372,-2.15915e-06,5.40523e-10,-5.33029e-14,957.327,9.02952], Tmin=(934.081,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (7.02952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -0.16361700    0.43849000    0.00000000
O       0.99492000   -0.17053000   -0.00000000
H      -0.83130300   -0.26796000    0.00000000
""",
)

entry(
    index = 20,
    label = "OO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97323,0.00193869,8.28015e-06,-1.20169e-08,5.28835e-12,-16098.4,5.27749], Tmin=(10,'K'), Tmax=(595.509,'K')),
            NASAPolynomial(coeffs=[3.29912,0.0064666,-3.12495e-06,7.50908e-10,-7.16822e-14,-16018.1,8.18025], Tmin=(595.509,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.855,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (78.9875,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.58310700    0.41066200    0.25838500
O       0.58275100   -0.40583300    0.26677300
H      -1.18757900   -0.12904100   -0.26237900
H       1.18803500    0.12421100   -0.26288000
""",
)

entry(
    index = 21,
    label = "[CH3]",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98354,0.0010436,1.03006e-05,-1.78403e-08,1.09943e-11,16909.8,0.220215], Tmin=(10,'K'), Tmax=(399.298,'K')),
            NASAPolynomial(coeffs=[3.70613,0.00382257,-1.38965e-07,-4.10135e-10,8.12236e-14,16932,1.30387], Tmin=(399.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.00001300   -0.00015100   -0.00125300
H       1.05127700   -0.23197600    0.00320900
H      -0.72687200   -0.79416600    0.00243700
H      -0.32451900    1.02629200   -0.00429300
""",
)

entry(
    index = 22,
    label = "[CH]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01388,-0.000821442,4.65285e-06,-5.21986e-11,-2.50853e-12,4550.39,4.13326], Tmin=(10,'K'), Tmax=(627.689,'K')),
            NASAPolynomial(coeffs=[2.73916,0.00465882,-2.12733e-06,4.40717e-10,-3.30289e-14,4762.49,10.1042], Tmin=(627.689,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.8393,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.02367400   -0.15576300    0.00000000
C      -0.02592800    0.35746100    0.00000000
H      -0.99764600   -0.20169800    0.00000000
""",
)

entry(
    index = 23,
    label = "C[C]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90233,0.0118928,-5.00318e-05,1.62361e-07,-1.53593e-10,-2162.26,7.44133], Tmin=(10,'K'), Tmax=(414.297,'K')),
            NASAPolynomial(coeffs=[1.72231,0.0167745,-9.17522e-06,2.43072e-09,-2.51053e-13,-1842.89,17.7121], Tmin=(414.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-17.9828,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.93052600   -0.10668200   -0.26504600
C      -0.46686200   -0.00057500    0.02393400
C       0.98807100    0.25566800    0.33326200
H      -0.56961300   -0.59947800   -0.88104700
H      -0.91415200   -0.50792300    0.87662300
H      -0.96787000    0.95909000   -0.08782500
""",
)

entry(
    index = 24,
    label = "[CH2]C=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01542,-0.00146118,5.46414e-05,-8.84545e-08,4.62878e-11,693.809,7.14304], Tmin=(10,'K'), Tmax=(565.73,'K')),
            NASAPolynomial(coeffs=[1.73332,0.019089,-1.15513e-05,3.34163e-09,-3.72943e-13,881.374,16.2285], Tmin=(565.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.76497,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -1.33024500   -1.05685600    0.01148800
C       0.72441500    0.03782500    0.03346200
C      -0.69981200   -0.00987500   -0.02774000
H       1.25533300    0.97714600   -0.00396900
H       1.27424700   -0.88788700    0.11883400
H      -1.22666300    0.95410700   -0.11384500
""",
)

entry(
    index = 25,
    label = "[CH]=C",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07386,-0.00582397,5.07139e-05,-7.32809e-08,3.53703e-11,34777.5,4.92419], Tmin=(10,'K'), Tmax=(617.23,'K')),
            NASAPolynomial(coeffs=[1.86052,0.0133027,-7.39172e-06,2.03331e-09,-2.19695e-13,34959.6,13.7963], Tmin=(617.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.163,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.47147200   -0.09029300    0.03034400
C       0.77665200   -0.44086600    0.14724800
H      -0.75758600    0.90224100   -0.30157900
H      -1.28372800   -0.77803200    0.26063300
H       1.31875800   -1.32454200    0.44268500
""",
)

entry(
    index = 26,
    label = "[CH2]",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00375,-0.000188169,3.18523e-06,-2.18177e-09,4.47807e-13,44983.1,0.593704], Tmin=(10,'K'), Tmax=(902.691,'K')),
            NASAPolynomial(coeffs=[3.26056,0.00260503,-6.25286e-07,1.87444e-11,8.33077e-15,45137.6,4.21596], Tmin=(902.691,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (374.012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.00104400    0.27927000   -0.00000000
H      -0.99029700   -0.14329200    0.00000000
H       0.99134100   -0.13597800   -0.00000000
""",
)

entry(
    index = 27,
    label = "C=C=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98054,0.00114814,3.64397e-05,-6.59762e-08,3.75005e-11,-7904.56,4.88186], Tmin=(10,'K'), Tmax=(543.533,'K')),
            NASAPolynomial(coeffs=[2.87578,0.0133165,-8.28586e-06,2.55052e-09,-3.05679e-13,-7844.11,8.98944], Tmin=(543.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.73,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.91073200   -0.20257900    0.26473100
C      -0.53751300   -0.01528400    0.08354000
C       0.76230600   -0.11466400    0.17971600
H      -1.05095700    0.73078100    0.66601500
H      -1.06732700   -0.68164900   -0.57581000
""",
)

entry(
    index = 28,
    label = "C#C",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98976,0.000591719,1.99003e-05,-3.43769e-08,1.88371e-11,26533,-4.58873], Tmin=(10,'K'), Tmax=(560.242,'K')),
            NASAPolynomial(coeffs=[3.32741,0.00747952,-4.32102e-06,1.32336e-09,-1.62768e-13,26573.3,-2.07935], Tmin=(560.242,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.59436700    0.24784800    0.00549400
C       0.59436100    0.13708800   -0.00582700
H      -1.65253800    0.34662900    0.01583400
H       1.65254400    0.03863500   -0.01560100
""",
)

entry(
    index = 29,
    label = "CO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00442,-0.000357626,2.35236e-05,-2.49173e-08,8.42075e-12,-24817.9,5.26274], Tmin=(10,'K'), Tmax=(777.273,'K')),
            NASAPolynomial(coeffs=[0.873142,0.0157561,-7.57234e-06,1.75296e-09,-1.57175e-13,-24331.1,19.5805], Tmin=(777.273,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.345,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.92542800   -0.46582700   -0.33949800
C      -0.35721900    0.03231700   -0.02049900
H      -0.62969800   -0.16333400    1.02012000
H      -0.44311300    1.10541000   -0.21140900
H      -1.06789700   -0.48497400   -0.66110300
H       1.57249900   -0.02359300    0.21229000
""",
)

entry(
    index = 30,
    label = "C[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02031,-0.00142488,2.83071e-05,-3.6052e-08,1.50505e-11,628.69,5.39135], Tmin=(10,'K'), Tmax=(621.134,'K')),
            NASAPolynomial(coeffs=[1.75285,0.0131771,-6.95537e-06,1.79518e-09,-1.8247e-13,910.37,15.2507], Tmin=(621.134,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.23073,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.30581700   -0.14086000   -0.15466700
C      -0.04575600   -0.02967800    0.01379100
H      -0.36364600   -0.21849800    1.04431900
H      -0.28159500    1.02504800   -0.20493800
H      -0.61481900   -0.63601300   -0.69840600
""",
)

entry(
    index = 31,
    label = "CC",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04575,-0.00286736,4.27217e-05,-4.19669e-08,1.19031e-11,-10638.6,5.50143], Tmin=(10,'K'), Tmax=(620.573,'K')),
            NASAPolynomial(coeffs=[-1.33196,0.0260504,-1.32896e-05,3.28675e-09,-3.17765e-13,-9860.57,29.7713], Tmin=(620.573,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.4409,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.76153700    0.00738800   -0.01521000
C       0.76161600   -0.00726200    0.01524100
H      -1.17735400   -0.09939900    0.98626900
H      -1.13895500    0.94075000   -0.43194900
H      -1.15197100   -0.80793900   -0.62354200
H       1.15180200    0.80696000    0.62464400
H       1.17730700    0.10070100   -0.98615700
H       1.13899300   -0.94119800    0.43070400
""",
)

entry(
    index = 32,
    label = "C[CH2]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9852,0.000673363,3.63677e-05,-4.86867e-08,2.1101e-11,13481.9,5.70833], Tmin=(10,'K'), Tmax=(596.85,'K')),
            NASAPolynomial(coeffs=[1.28119,0.0187943,-9.17152e-06,2.17688e-09,-2.02928e-13,13804.7,17.3582], Tmin=(596.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (112.087,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.62062400    0.01459100    0.02556100
C       0.85733800   -0.04835600   -0.09598800
H      -1.06294500    0.62511600   -0.76192100
H      -0.93315000    0.45838000    0.97957700
H      -1.07009800   -0.97764800   -0.01875000
H       1.41842800    0.80168000   -0.45195800
H       1.41105200   -0.87386300    0.32357900
""",
)

entry(
    index = 33,
    label = "CC=O",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97357,0.00141204,4.01916e-05,-5.93294e-08,2.8355e-11,-20664,7.2786], Tmin=(10,'K'), Tmax=(539.573,'K')),
            NASAPolynomial(coeffs=[1.55144,0.0193679,-9.72523e-06,2.34499e-09,-2.20532e-13,-20402.6,17.4696], Tmin=(539.573,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.824,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.56330700   -0.83998100   -0.42496400
C      -0.64867400   -0.02966500   -0.01745300
C       0.84960000    0.01878100    0.01245200
H      -0.98800600   -0.94740700   -0.48947300
H      -1.03447400    0.03696400    1.00134300
H      -1.02942300    0.83794600   -0.55916900
H       1.28767000    0.92336200    0.47736300
""",
)

entry(
    index = 34,
    label = "[O]C=O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01066,-0.000901006,2.72047e-05,-4.12318e-08,2.00038e-11,-15486.2,7.03964], Tmin=(10,'K'), Tmax=(620.697,'K')),
            NASAPolynomial(coeffs=[2.71527,0.0101917,-6.23566e-06,1.80959e-09,-2.01682e-13,-15378.3,12.2454], Tmin=(620.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-128.76,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.21637300   -0.20722700    0.18914900
O      -0.92792100   -0.84745700   -0.02725100
C      -0.07334900   -0.01874700   -0.00776600
H      -0.21510400    1.07353000   -0.15413200
""",
)

entry(
    index = 35,
    label = "O=CO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07069,-0.00484746,4.88711e-05,-6.33749e-08,2.6185e-11,-46709.6,6.51997], Tmin=(10,'K'), Tmax=(756.969,'K')),
            NASAPolynomial(coeffs=[1.30878,0.0176137,-1.12258e-05,3.28153e-09,-3.63318e-13,-46516.9,17.5869], Tmin=(756.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-388.352,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.78898000   -0.28233000    0.46542300
O      -0.54817300    0.64115400   -1.08177300
C      -0.39384200    0.09373600   -0.03345100
H      -1.19705900   -0.17453400    0.66091600
H       1.46922600   -0.02863500   -0.17491500
""",
)

entry(
    index = 36,
    label = "CO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.979,0.00109806,3.17755e-05,-4.57282e-08,2.1167e-11,-29.7951,8.30032], Tmin=(10,'K'), Tmax=(559.08,'K')),
            NASAPolynomial(coeffs=[1.89225,0.0160284,-8.28346e-06,2.04102e-09,-1.94255e-13,203.53,17.1542], Tmin=(559.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-0.258552,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.91405100    0.54257000   -0.05705700
O       1.76387300   -0.41024000    0.17461900
C      -0.43134600    0.04772000   -0.03240200
H      -0.63514000   -0.37113800    0.95014600
H      -1.06981300    0.90320600   -0.23299000
H      -0.54172500   -0.71221800   -0.80221700
""",
)

entry(
    index = 37,
    label = "COO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90491,0.00955094,9.83522e-06,-1.56075e-08,5.69312e-12,-16328.7,8.41571], Tmin=(10,'K'), Tmax=(963.586,'K')),
            NASAPolynomial(coeffs=[3.2509,0.0168796,-8.75529e-06,2.2236e-09,-2.22308e-13,-16416.9,10.4352], Tmin=(963.586,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.764,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.49857000   -0.59226200   -0.43479500
O       1.51399900    0.31999500   -0.03593700
C      -0.73237000    0.01932600   -0.12647700
H      -1.49298000   -0.67138100   -0.48714200
H      -0.82727500    0.97698900   -0.63939500
H      -0.84242400    0.16445500    0.95033800
H       1.91815100   -0.15428000    0.69999500
""",
)

entry(
    index = 38,
    label = "CCO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77138,0.0241105,-5.60691e-05,1.51984e-07,-1.36768e-10,-4607.98,10.6111], Tmin=(10,'K'), Tmax=(427.119,'K')),
            NASAPolynomial(coeffs=[1.65255,0.0283745,-1.63321e-05,4.56454e-09,-4.96595e-13,-4284.87,20.6943], Tmin=(427.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.3191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.57595700    0.40439200   -0.20672000
O       1.19049600    1.60510800    0.09855200
C       0.51676000   -0.55465200    0.00814400
C       0.26986200   -0.74965600    1.48536300
H       0.87568500   -1.46020800   -0.47684700
H      -0.36408900   -0.18054200   -0.51094700
H      -0.03224300    0.19283000    1.93727900
H      -0.52444500   -1.47989100    1.63373800
H       1.17043000   -1.10896700    1.98063600
""",
)

entry(
    index = 39,
    label = "CCOO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79246,0.017638,2.10324e-05,-4.32962e-08,2.11039e-11,-20630.8,11.0683], Tmin=(10,'K'), Tmax=(674.006,'K')),
            NASAPolynomial(coeffs=[2.44608,0.0302535,-1.73369e-05,4.83655e-09,-5.25774e-13,-20554.3,16.2533], Tmin=(674.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-171.558,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.02727100   -0.74530800   -0.50949400
O       2.37990900   -0.65884000   -0.07442100
C       0.24487400    0.00751900    0.40027400
C       0.55370200    1.48846600    0.34584700
H      -0.77769200   -0.19793000    0.07980700
H       0.37947000   -0.39070500    1.41000600
H       1.58672000    1.66901300    0.63501400
H      -0.09900900    2.03456300    1.02668300
H       0.40234000    1.86804900   -0.66366900
H       2.53782100   -1.56232700    0.22266500
""",
)

entry(
    index = 40,
    label = "CC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76412,0.0255937,-9.07299e-05,2.35231e-07,-1.99757e-10,-3684.3,22.8122], Tmin=(10,'K'), Tmax=(430.403,'K')),
            NASAPolynomial(coeffs=[1.71314,0.0239915,-1.31331e-05,3.49491e-09,-3.63404e-13,-3316.36,33.2013], Tmin=(430.403,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.6384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -1.36656900    0.76258200   -0.86044200
C       0.78959900   -0.01757900   -0.04272900
C      -0.72412600   -0.00848300    0.07011300
H       1.18111000    0.99226000    0.06939500
H       1.09172600   -0.39619200   -1.01792300
H       1.23257500   -0.64921400    0.72733800
H      -1.05812700    0.34008900    1.06081500
H      -1.14618900   -1.02356300   -0.00666600
""",
)

entry(
    index = 41,
    label = "C1CO1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15855,-0.0108124,7.99509e-05,-9.96082e-08,4.04643e-11,-8554.94,5.89444], Tmin=(10,'K'), Tmax=(762.181,'K')),
            NASAPolynomial(coeffs=[-0.342485,0.0250171,-1.4588e-05,4.09758e-09,-4.44604e-13,-8223.4,24.0609], Tmin=(762.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-71.097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.01782400   -0.28444300    1.12639500
C       0.72980900    0.05448100   -0.04659900
C      -0.73137400   -0.03155000   -0.04586100
H       1.20332100    1.02870300   -0.03482800
H       1.30852600   -0.74971400   -0.48460800
H      -1.31565200    0.88065500   -0.03163600
H      -1.21245400   -0.89823300   -0.48286200
""",
)

entry(
    index = 42,
    label = "[O]OCC=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,D} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76422,0.0206091,1.71683e-05,-6.83789e-08,5.08687e-11,-11918.3,11.7249], Tmin=(10,'K'), Tmax=(497.627,'K')),
            NASAPolynomial(coeffs=[4.20682,0.0242788,-1.5679e-05,4.81222e-09,-5.63903e-13,-12051.8,8.99932], Tmin=(497.627,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-99.1153,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.85424100    0.97439000   -0.21052400
O      -0.83889900   -2.34909100    1.01698900
O      -2.07361300    0.98461100   -0.66485500
C      -0.34510300   -0.36082800   -0.18261700
C      -1.15082100   -1.22276000    0.77084200
H      -0.39237900   -0.78197800   -1.18655900
H       0.68930900   -0.29403700    0.14831200
H      -2.03862500   -0.73529900    1.21143000
""",
)

entry(
    index = 43,
    label = "[CH2]C(C)=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 C u1 p0 c0 {3,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91451,0.0111883,3.18379e-05,-4.85239e-08,1.98978e-11,-5305.31,9.3428], Tmin=(10,'K'), Tmax=(830.415,'K')),
            NASAPolynomial(coeffs=[2.76679,0.0269798,-1.52252e-05,4.14177e-09,-4.38031e-13,-5468.56,12.5359], Tmin=(830.415,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.0982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.61784700   -1.37967000    0.53200700
C      -1.10871000    0.15011700   -0.09999000
C       0.17687700   -0.24055900    0.59286400
C       0.87729200    0.77598800    1.33544800
H      -1.83174800    0.52260400    0.62667800
H      -1.51820700   -0.71382700   -0.61437400
H      -0.92385900    0.95150300   -0.81636400
H       0.50572200    1.78789100    1.40219200
H       1.79603100    0.50783100    1.83406000
""",
)

entry(
    index = 44,
    label = "CC(=O)C[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {4,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82805,0.0227001,6.87088e-06,-1.97186e-08,7.65329e-12,-17310.7,11.0348], Tmin=(10,'K'), Tmax=(1034.39,'K')),
            NASAPolynomial(coeffs=[5.60448,0.0264024,-1.38284e-05,3.50266e-09,-3.47047e-13,-18243.8,-0.329437], Tmin=(1034.39,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.97041000    1.85192800   -0.72709900
O       0.92850100   -0.42704200    0.42949100
C      -1.32543900    0.13195600   -0.12887600
C       0.63057200    1.72403000   -0.57536500
C       0.16048200    0.36745700   -0.03056000
H      -1.59943100   -0.73322900    0.46695400
H      -1.59126700   -0.04789700   -1.17219300
H      -1.88075800    1.01171300    0.19964500
H       0.06650000    2.00218600   -1.47767500
H       0.34208600    2.47029200    0.18854200
""",
)

entry(
    index = 45,
    label = "CC(=O)CO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,D}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51532,0.0481957,-9.68486e-05,1.74269e-07,-1.3142e-10,-19172.4,12.665], Tmin=(10,'K'), Tmax=(409.266,'K')),
            NASAPolynomial(coeffs=[4.00079,0.0356821,-2.25115e-05,6.79776e-09,-7.87799e-13,-19147.1,11.5515], Tmin=(409.266,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-159.419,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (245.277,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -2.10174800    0.02466600    0.36125100
O      -0.12404400   -2.92639300    0.11062200
O      -2.81423400   -0.02691300   -0.72569700
C      -0.88825700   -0.71938200    0.21733400
C      -2.47092200   -2.76176700    0.52600600
C      -1.09167500   -2.23196000    0.26808700
H      -0.25339900   -0.42113600    1.05004300
H      -0.41757300   -0.45203200   -0.72667800
H      -2.89103600   -2.29939900    1.42012400
H      -3.12648400   -2.49285600   -0.30329100
H      -2.42197200   -3.84044100    0.63495100
""",
)

entry(
    index = 46,
    label = "CC(=O)COO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {5,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6683,0.0316183,3.59669e-06,-2.40526e-08,1.08876e-11,-36958.5,11.6502], Tmin=(10,'K'), Tmax=(907.434,'K')),
            NASAPolynomial(coeffs=[5.00766,0.0357393,-1.97866e-05,5.30102e-09,-5.53533e-13,-37614.3,3.04443], Tmin=(907.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-307.304,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.09421200   -0.07761300   -0.98193200
O      -2.45026800    0.03305900   -1.38768800
O      -2.30393500    0.76056100    1.28058300
C      -1.06064800   -0.91174700    0.13781000
C      -1.54847100   -1.03541700    2.65422100
C      -1.70448500   -0.28252500    1.36140200
H      -0.00428200   -1.10470100    0.34058600
H      -1.55000100   -1.87057900   -0.06757900
H      -2.17899900   -0.59134800    3.41831500
H      -1.80190300   -2.08719800    2.51788200
H      -0.50506100   -0.99205000    2.97189500
H      -2.76005000    0.72827000   -0.78685400
""",
)

entry(
    index = 47,
    label = "C=CC=O",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9642,0.00221783,8.00044e-05,-1.52171e-07,9.19249e-11,-8584.49,7.88101], Tmin=(10,'K'), Tmax=(495.941,'K')),
            NASAPolynomial(coeffs=[1.53419,0.0282086,-1.79377e-05,5.47386e-09,-6.42219e-13,-8422.06,17.1078], Tmin=(495.941,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-71.3865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -2.29403700   -0.34836600   -0.10557000
C      -0.07701200    0.26428400    0.45655200
C       1.19439100    0.21512800    0.08232400
C      -1.12390800   -0.35294600   -0.37906000
H      -0.40406100    0.74647300    1.36909600
H       1.47853700   -0.27856100   -0.84032200
H       1.98760100    0.65663700    0.66920000
H      -0.75405600   -0.83607200   -1.30466200
""",
)

entry(
    index = 48,
    label = "[CH2]CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88385,0.0110015,2.99411e-05,-4.18762e-08,1.61786e-11,10928.1,9.91048], Tmin=(10,'K'), Tmax=(833.309,'K')),
            NASAPolynomial(coeffs=[1.25996,0.030058,-1.59925e-05,4.17678e-09,-4.29222e-13,11141.1,20.7447], Tmin=(833.309,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (90.8592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.14491400    0.58979200    0.05836500
C      -1.10278900   -0.27221200   -0.11114300
C       1.39797600   -0.14908300   -0.24321100
H       0.06127400    1.46987900   -0.59463500
H       0.18747400    0.99141700    1.07433600
H      -1.16924600   -0.65225100   -1.13129000
H      -2.00987000    0.29355800    0.09736000
H      -1.07231100   -1.12920200    0.56171400
H       2.35619600    0.21733000    0.09213100
H       1.38824800   -0.97333000   -0.94203800
""",
)

entry(
    index = 49,
    label = "C[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7086,0.0341932,-0.000166476,4.66916e-07,-4.09798e-10,9212.78,10.4194], Tmin=(10,'K'), Tmax=(419.932,'K')),
            NASAPolynomial(coeffs=[-0.220195,0.031945,-1.67397e-05,4.23381e-09,-4.16893e-13,9892.53,30.1294], Tmin=(419.932,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.5894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -1.28478300   -0.12590500   -0.08531600
C       1.28742900   -0.02562700   -0.12531600
C      -0.01259200    0.47821300    0.38926700
H      -1.30215300   -0.19825800   -1.17635500
H      -1.41460300   -1.14960900    0.29171800
H      -2.15412200    0.44764700    0.23225300
H       1.50857500   -1.03522300    0.24721300
H       2.11877500    0.61483400    0.16491400
H       1.27617900   -0.09886400   -1.21636800
H      -0.02270500    1.09279200    1.27799000
""",
)

entry(
    index = 50,
    label = "[CH2]C=C",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10403,-0.0104648,0.000138439,-2.6123e-07,1.64704e-10,19676,6.73579], Tmin=(10,'K'), Tmax=(477.858,'K')),
            NASAPolynomial(coeffs=[0.917896,0.0275705,-1.66293e-05,4.88021e-09,-5.55389e-13,19850.8,18.3966], Tmin=(477.858,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.591,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.00652800    0.14291800    0.52026500
C      -1.21459300    0.31052600   -0.12032800
C       1.17113300   -0.18471500   -0.11426600
H       0.01873600    0.27821300    1.59613200
H      -2.11103400    0.56743800    0.42252500
H      -1.29406800    0.18726600   -1.19195300
H       1.19939900   -0.32955100   -1.18574600
H       2.09311600   -0.30639000    0.43294900
""",
)

entry(
    index = 51,
    label = "CCCO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4359,0.0622312,-0.000267238,6.82555e-07,-5.92121e-10,-7433.21,11.5324], Tmin=(10,'K'), Tmax=(399.456,'K')),
            NASAPolynomial(coeffs=[1.35261,0.0401807,-2.32969e-05,6.50303e-09,-7.03425e-13,-6924.41,23.9567], Tmin=(399.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -2.17456800    0.08390700    0.40276200
O      -2.31670300    1.15564500   -0.31504200
C       0.23156600    0.31750100    0.72431600
C      -0.88890700   -0.53542100    0.16880400
C       0.12381400    0.51801700    2.23038200
H       0.21512900    1.27635600    0.20535500
H       1.17433100   -0.16941400    0.46819700
H      -0.79739800   -0.68783000   -0.90538600
H      -0.96322600   -1.49551300    0.67867000
H       0.15765000   -0.43761000    2.75531500
H       0.94095300    1.13428300    2.60099500
H      -0.81318000    1.00982600    2.48859300
""",
)

entry(
    index = 52,
    label = "CC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83228,0.0164754,0.000144653,-6.00515e-07,8.34649e-10,-9538.13,11.7837], Tmin=(10,'K'), Tmax=(181.374,'K')),
            NASAPolynomial(coeffs=[2.92847,0.0364081,-2.01974e-05,5.42236e-09,-5.6569e-13,-9505.34,14.6011], Tmin=(181.374,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.26,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.55500600   -1.49313800   -0.18668700
O      -1.71055000   -1.66924500   -0.74660000
C      -0.06020000   -0.13694900   -0.38201000
C       1.38672400   -0.16857500    0.05309800
C      -0.91852700    0.82069900    0.41470100
H      -0.15210600    0.05833500   -1.45068600
H       1.95300200   -0.89420300   -0.52765200
H       1.83225200    0.81520000   -0.08605600
H       1.45627900   -0.43250600    1.10827600
H      -0.58293000    1.84350600    0.24739300
H      -1.95879200    0.73759700    0.10780500
H      -0.84061200    0.59811300    1.47915300
""",
)

entry(
    index = 53,
    label = "[CH2]CCOO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u1 p0 c0 {3,S} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32329,0.0647133,-0.000168613,2.88236e-07,-1.88608e-10,725.655,11.6273], Tmin=(10,'K'), Tmax=(471.994,'K')),
            NASAPolynomial(coeffs=[5.05867,0.033915,-1.95963e-05,5.52681e-09,-6.07865e-13,741.08,6.45682], Tmin=(471.994,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (6.01191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.48377800    0.16427900    0.58968900
O       0.27139300   -1.23956100    0.62990700
C       1.49117700   -0.09744500   -1.62795700
C       0.42832400    0.56880000   -0.76487500
C       2.83342300   -0.08720300   -0.99142800
H       1.50824700    0.41971800   -2.59637000
H       1.18731500   -1.12263800   -1.85507600
H      -0.57026300    0.38415800   -1.16683200
H       0.59485100    1.64597600   -0.70612900
H       3.04669600    0.58069800   -0.17025500
H       3.65095800   -0.64132700   -1.42606600
H       1.17785500   -1.56820900    0.70307700
""",
)

entry(
    index = 54,
    label = "C=CC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57821,0.0467741,-0.000208068,5.34189e-07,-4.65203e-10,9315.36,9.92781], Tmin=(10,'K'), Tmax=(396.907,'K')),
            NASAPolynomial(coeffs=[2.08809,0.0289813,-1.68274e-05,4.69825e-09,-5.07976e-13,9692.08,18.9955], Tmin=(396.907,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.4343,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -1.29754500    0.92164800   -1.22939700
C      -1.10982700   -0.02952100   -0.27088700
C       0.31573700   -0.34604000    0.08350700
C       1.35656000    0.24278500   -0.47834100
H      -1.64708600   -0.93740300   -0.59575300
H      -1.67708200    0.28700200    0.62164100
H       0.45238200   -1.10522100    0.84665700
H       1.21670800    0.99935500   -1.23916500
H       2.36795000   -0.01274500   -0.19596500
""",
)

entry(
    index = 55,
    label = "[CH2]OC=C",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95032,0.00302414,9.14131e-05,-1.73949e-07,1.03992e-10,7955.58,9.39795], Tmin=(10,'K'), Tmax=(518.761,'K')),
            NASAPolynomial(coeffs=[1.58443,0.0313215,-1.94824e-05,5.92665e-09,-6.9898e-13,8065.75,17.9552], Tmin=(518.761,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (66.1292,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.42864900    0.24471800   -1.21834500
C       0.42322500   -0.51227100   -0.47478900
C       0.09528300   -1.47552100    0.37318200
C      -1.75030200    0.21097000   -0.92819100
H       1.44622800   -0.22894000   -0.67690700
H      -0.92461900   -1.78576600    0.54144600
H       0.88211100   -1.99191700    0.89970300
H      -2.34714700    0.78905400   -1.61300500
H      -2.03249500    0.08635400    0.10820400
""",
)

entry(
    index = 56,
    label = "[CH2]CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81815,0.0250165,9.99244e-06,-2.01823e-08,6.75582e-12,8160.37,10.886], Tmin=(10,'K'), Tmax=(1166.97,'K')),
            NASAPolynomial(coeffs=[5.59092,0.0316932,-1.49821e-05,3.44977e-09,-3.13056e-13,6878.24,-1.66099], Tmin=(1166.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (67.8636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
C      -0.39875100    0.91040200    0.22121400
C       1.01031100    0.42533100    0.57122200
C      -1.28228900   -0.20974000   -0.31387000
C       1.77292700   -0.04236200   -0.61592800
H      -0.85799300    1.35225800    1.10709300
H      -0.32258100    1.70847200   -0.52186800
H       1.55172200    1.24459700    1.06445100
H       0.94620600   -0.37575200    1.31265200
H      -1.38301000   -1.00589300    0.42578400
H      -0.85001200   -0.64918500   -1.21358200
H      -2.28109400    0.15019600   -0.55829300
H       1.69960000    0.49893400   -1.54906300
H       2.53323900   -0.80363100   -0.53530000
""",
)

entry(
    index = 57,
    label = "C[CH]CC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51376,0.0546433,-0.000240913,6.36843e-07,-5.48602e-10,6605.9,11.9271], Tmin=(10,'K'), Tmax=(416.871,'K')),
            NASAPolynomial(coeffs=[-0.444772,0.0434336,-2.35692e-05,6.18876e-09,-6.33371e-13,7363.38,32.6879], Tmin=(416.871,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.9082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.61193900    0.10621400   -0.41049700
C       1.92076800    0.54505600    0.23643600
C      -1.41583100   -1.45556700   -0.06870700
C      -0.04255100   -1.02466300    0.30069100
H       0.79999000   -0.16971100   -1.45887600
H      -0.08318900    0.95174700   -0.46171500
H       2.63350800   -0.28017200    0.25794200
H       1.75204400    0.86545800    1.26468300
H       2.37876300    1.37057600   -0.30672500
H      -1.83054500   -2.16088200    0.64969600
H      -2.09186600   -0.59886400   -0.13634100
H      -1.43836400   -1.94285100   -1.05295400
H       0.57523600   -1.68117700    0.89997700
""",
)

entry(
    index = 58,
    label = "CCCCO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09115,0.101215,-0.000481815,1.23097e-06,-1.07274e-09,-10159.5,12.6752], Tmin=(10,'K'), Tmax=(390.975,'K')),
            NASAPolynomial(coeffs=[1.00136,0.0531952,-3.13281e-05,8.81724e-09,-9.57861e-13,-9465.67,27.5781], Tmin=(390.975,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-84.5124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.68124700    0.61572300    1.50167900
O       1.96022100    1.85468300    1.23566900
C       0.34297000    0.22720600   -0.49997600
C      -0.96055500   -0.01040300    0.25319300
C       1.57072400   -0.16823700    0.29103400
C      -2.17551600    0.40137200   -0.56736400
H      -1.03430000   -1.06751100    0.52149300
H      -0.93991900    0.54780200    1.19068700
H       0.43625900    1.28040900   -0.77238000
H       0.34613600   -0.34426000   -1.43179900
H       1.51413700   -1.19608400    0.64806900
H       2.49048300   -0.01794300   -0.27178600
H      -3.10214800    0.22853400   -0.02198000
H      -2.22489200   -0.16169600   -1.50053800
H      -2.12886200    1.46094500   -0.82150400
""",
)

entry(
    index = 59,
    label = "CCC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48331,0.0505611,-8.64428e-05,1.81345e-07,-1.47096e-10,-12046.7,12.7658], Tmin=(10,'K'), Tmax=(448.926,'K')),
            NASAPolynomial(coeffs=[1.28944,0.052002,-3.07571e-05,8.80563e-09,-9.78106e-13,-11667.3,23.625], Tmin=(448.926,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-100.177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (340.893,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.41962800    1.49101600    0.23024000
O      -1.14522800    2.10058900    1.11419400
C      -0.47909500    0.04323100    0.38087900
C       0.64063400   -0.49327900   -0.48894300
C      -1.86311200   -0.43376800   -0.00056700
C       0.77292100   -2.00817700   -0.39185200
H      -0.28090300   -0.15405000    1.43618800
H       0.45139700   -0.19366400   -1.52207500
H       1.57176800   -0.01479300   -0.18250900
H      -0.10358200   -2.51293900   -0.79622400
H       0.89465800   -2.32464700    0.64520800
H       1.64083300   -2.35443600   -0.94979100
H      -2.04136200   -0.26797200   -1.06376100
H      -1.96722500   -1.49670000    0.21084800
H      -2.61034400    0.10702900    0.57624000
""",
)

entry(
    index = 60,
    label = "CCC(C)OO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34424,0.059856,-0.000105946,1.88395e-07,-1.31539e-10,-27909,12.7236], Tmin=(10,'K'), Tmax=(499.539,'K')),
            NASAPolynomial(coeffs=[1.27548,0.0560124,-3.31209e-05,9.41879e-09,-1.03747e-12,-27447.7,23.8171], Tmin=(499.539,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-232.075,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.44479300    1.27633800   -0.07246600
O      -1.70842500    1.73855600    0.38745200
C      -0.38191300   -0.13150600    0.14400300
C       1.05500500   -0.49752400   -0.19428700
C      -1.41191700   -0.85490800   -0.70148600
C       1.34993100   -1.97747600    0.01649800
H      -0.56914300   -0.32231700    1.20743800
H       1.24394000   -0.21710300   -1.23286200
H       1.71634000    0.10945600    0.42552500
H       0.78819300   -2.60018100   -0.67858900
H       1.09063300   -2.28810200    1.02999800
H       2.40800000   -2.18445000   -0.13490500
H      -1.17239400   -0.74010900   -1.75971500
H      -2.40085200   -0.44121300   -0.51826500
H      -1.43385100   -1.91670400   -0.45902200
H      -1.45221200    2.22819700    1.17744100
""",
)

entry(
    index = 61,
    label = "C=CCC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.909,0.0164279,2.95713e-05,-4.03757e-08,1.40387e-11,-803.239,8.65619], Tmin=(10,'K'), Tmax=(1008.7,'K')),
            NASAPolynomial(coeffs=[2.93208,0.0341777,-1.74582e-05,4.34441e-09,-4.24868e-13,-1312.07,9.87858], Tmin=(1008.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.64227,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.42028600    0.09135700   -0.56273700
C      -1.62860000    0.17668000    0.35634600
C       0.77261200   -0.60522600    0.02261900
C       0.85044300   -1.13242900    1.23503500
H      -0.69489400   -0.41930900   -1.49039600
H      -0.11498700    1.09629300   -0.86873900
H      -1.97519100   -0.81728200    0.64028500
H      -2.45169800    0.69265000   -0.13535800
H      -1.38756800    0.72037100    1.27013100
H       1.63904100   -0.66956700   -0.62867900
H       1.75438600   -1.61815300    1.57586400
H       0.02095200   -1.09998000    1.92957200
""",
)

entry(
    index = 62,
    label = "CC=CC",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74162,0.0194759,2.15482e-05,-3.61523e-08,1.48009e-11,-2328.31,7.76867], Tmin=(10,'K'), Tmax=(676.221,'K')),
            NASAPolynomial(coeffs=[0.531474,0.0384647,-2.0573e-05,5.37385e-09,-5.51437e-13,-1894.15,21.9998], Tmin=(676.221,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.3975,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       1.94243500   -0.08739800    0.11888300
C      -1.94246000    0.08739800   -0.24141900
C       0.54926100   -0.06353200   -0.42636000
C      -0.54926800    0.06352000    0.30381800
H       1.94053100    0.01309900    1.20352500
H       2.44877800   -1.01984000   -0.13748800
H       2.54180000    0.72367000   -0.29886100
H      -2.44870400    1.01995400    0.01473900
H      -2.54189000   -0.72350200    0.17653400
H      -1.94057100   -0.01335300   -1.32603200
H       0.44796000   -0.15869700   -1.50456600
H      -0.44797200    0.15868100    1.38202700
""",
)

entry(
    index = 63,
    label = "C=C[CH]C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97046,0.0147281,2.77691e-05,-3.67159e-08,1.23588e-11,15491.3,8.77521], Tmin=(10,'K'), Tmax=(1057.81,'K')),
            NASAPolynomial(coeffs=[3.93402,0.0298684,-1.4974e-05,3.62961e-09,-3.44998e-13,14659.6,4.98564], Tmin=(1057.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (128.855,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -1.69828300    0.09931500   -0.13745600
C      -0.71273900   -0.86728600    0.42866700
C      -0.58498800   -1.11248200    1.78878100
C      -1.33345000   -0.50965200    2.76731600
H      -1.63735300    0.14489200   -1.22190600
H      -1.53258000    1.10724800    0.25324400
H      -2.72171700   -0.17596000    0.13248600
H      -0.06751500   -1.40203500   -0.25418700
H       0.16333600   -1.83485100    2.09460200
H      -2.09528100    0.21918300    2.52799400
H      -1.18471100   -0.74491400    3.81012200
""",
)

entry(
    index = 64,
    label = "[CH2]CC=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70897,0.0309881,-7.64554e-05,2.10759e-07,-1.90311e-10,23673.9,10.7618], Tmin=(10,'K'), Tmax=(425.598,'K')),
            NASAPolynomial(coeffs=[0.837676,0.0366051,-2.09387e-05,5.823e-09,-6.30843e-13,24111.8,24.4349], Tmin=(425.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (196.828,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.50863600   -0.52516200    0.14226000
C      -0.63165900    0.41030400   -0.14195300
C       1.62239000    0.14578100    0.86939500
C      -1.86411800    0.25636600    0.31502900
H       0.88550600   -0.93989500   -0.79688900
H       0.12633600   -1.37842200    0.71895400
H      -0.39042200    1.27584800   -0.75160100
H       2.64197000   -0.18887100    0.75740800
H       1.40257700    0.87415600    1.63546900
H      -2.13195600   -0.59331700    0.93207800
H      -2.64600000    0.96833000    0.08891100
""",
)

entry(
    index = 65,
    label = "[CH]=CCC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u1 p0 c0 {3,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70722,0.023137,9.79992e-06,-2.94755e-08,1.52789e-11,28012.7,9.23649], Tmin=(10,'K'), Tmax=(543.981,'K')),
            NASAPolynomial(coeffs=[2.3243,0.0333057,-1.82397e-05,4.88774e-09,-5.13454e-13,28163.2,15.0663], Tmin=(543.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.868,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (249.434,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.37063800    0.64422100   -0.60532300
C      -1.01553900    0.03344100    0.62929600
C       1.10214200    0.35594200   -0.72059900
C       1.80252000   -0.34419400    0.12963200
H      -0.86465800    0.28082500   -1.51031400
H      -0.51048600    1.72845100   -0.60885900
H      -0.90068000   -1.05045900    0.62610300
H      -2.07826400    0.26717300    0.67174500
H      -0.54298000    0.41108300    1.53604900
H       1.60676000    0.77553600   -1.59323700
H       2.82820500   -0.65740100    0.23020700
""",
)

entry(
    index = 66,
    label = "C=CC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95515,0.00257608,9.64292e-05,-1.65667e-07,8.9071e-11,12750.9,6.89984], Tmin=(10,'K'), Tmax=(559.83,'K')),
            NASAPolynomial(coeffs=[-0.07371,0.0399812,-2.68864e-05,8.68161e-09,-1.06737e-12,13066.9,22.7933], Tmin=(559.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (105.997,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (228.648,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.66646300    0.45048300    0.02506700
C      -0.59841500   -0.06799000    0.53041300
C       1.84531000   -0.11346900    0.26687800
C      -1.77723600    0.49625600    0.28895100
H       0.61143800    1.34984200   -0.58022200
H      -0.54346000   -0.96734200    1.13570500
H       1.92199000   -1.01107000    0.86839600
H       2.76392000    0.29972000   -0.12478400
H      -1.85380000    1.39391100   -0.31253600
H      -2.69587400    0.08344600    0.68096200
""",
)

entry(
    index = 67,
    label = "C=CC(C)[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82136,0.015488,6.39206e-05,-1.13943e-07,5.85142e-11,5779.57,11.1079], Tmin=(10,'K'), Tmax=(610.789,'K')),
            NASAPolynomial(coeffs=[0.972749,0.0429957,-2.53741e-05,7.24953e-09,-8.0325e-13,5962.43,22.0947], Tmin=(610.789,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.0301,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.25794000   -0.63101500    1.57933000
C       0.58339300   -0.55062600    0.24703400
C       1.36005900    0.77977700    0.12379600
C      -0.63839300   -0.53894200   -0.62792400
C      -0.81342300   -1.36238600   -1.64710800
H       1.25725300   -1.36667800   -0.04545600
H       0.70937800    1.61120300    0.38831800
H       1.68671200    0.88984000   -0.90838500
H       2.22385400    0.77327900    0.78467900
H      -1.38627100    0.20263700   -0.36572400
H      -1.69661300   -1.31889400   -2.26927700
H      -0.07168000   -2.11308600   -1.89373300
""",
)

entry(
    index = 68,
    label = "CC1CCO1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98226,0.000704346,0.000121641,-1.92337e-07,9.85427e-11,-16499.2,10.6387], Tmin=(10,'K'), Tmax=(505.171,'K')),
            NASAPolynomial(coeffs=[-2.49597,0.0520026,-3.06877e-05,8.69989e-09,-9.525e-13,-15844.7,37.4683], Tmin=(505.171,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.198,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.66552800   -1.18368900    0.05168900
C       0.29012200   -0.26272500   -0.51103800
C      -0.56858800    0.94039200   -0.08742000
C      -1.61208000   -0.12653500    0.26530400
C       1.65947700   -0.41616500    0.09650100
H       0.33412400   -0.38760200   -1.59739900
H      -0.16619100    1.46408900    0.77724800
H      -0.83485000    1.65410500   -0.86126200
H      -1.99829900   -0.12504500    1.28422800
H      -2.44567500   -0.18876900   -0.43778000
H       1.60548400   -0.28626600    1.17742500
H       2.05822400   -1.40842700   -0.11342800
H       2.34377900    0.32673700   -0.31556700
""",
)

entry(
    index = 69,
    label = "CCC(C)[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77213,0.0223159,4.2453e-05,-6.64207e-08,2.68046e-11,-10475,11.0709], Tmin=(10,'K'), Tmax=(837.296,'K')),
            NASAPolynomial(coeffs=[1.27423,0.0474307,-2.61541e-05,7.00737e-09,-7.33491e-13,-10518.7,19.9191], Tmin=(837.296,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.0965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.33419700    0.56665200   -0.12543000
C      -0.79517900   -0.51164600   -0.48191400
C       0.70099100   -0.64996000   -0.18787200
C      -1.51304800    0.35006100    0.54489700
C       1.41796500   -1.61565400   -1.12702300
H      -1.23334500   -1.51082900   -0.52243600
H      -0.89865100   -0.08109300   -1.48093300
H       0.81054600   -1.02189500    0.85049800
H      -1.04628900    1.33161900    0.60771400
H      -2.56213600    0.48395400    0.28567800
H      -1.46821200   -0.10698200    1.53483000
H       2.47364600   -1.67650800   -0.87125400
H       0.97710400   -2.61016400   -1.06863500
H       1.32952300   -1.26168600   -2.15442000
""",
)

entry(
    index = 70,
    label = "C[CH]CCOO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
6  C u1 p0 c0 {3,S} {5,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79655,0.126708,-0.000551521,1.21368e-06,-9.39739e-10,-3500.63,27.6431], Tmin=(10,'K'), Tmax=(420.138,'K')),
            NASAPolynomial(coeffs=[4.54298,0.0445958,-2.45587e-05,6.51648e-09,-6.72623e-13,-3069.42,27.6103], Tmin=(420.138,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.1364,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.21653800    1.26187200   -0.84634000
O       1.35546000    0.62088800   -2.10517100
C       0.36407100   -0.85554800    0.06273700
C       1.37904200    0.28116000    0.16093700
C      -1.58944800    0.74704200    0.62621000
C      -1.03165900   -0.38290500   -0.16467900
H       0.43438500   -1.42441900    1.00166400
H       0.66387400   -1.54142600   -0.72907200
H       2.39697300   -0.11406700    0.13418700
H       1.24813200    0.85070600    1.08268000
H      -1.01787100    1.66456000    0.46348000
H      -1.54826200    0.53918200    1.70356300
H      -2.62779800    0.94532800    0.36964800
H      -1.70774500   -1.03276700   -0.70229700
H       0.43060400    0.46524100   -2.34192300
""",
)

entry(
    index = 71,
    label = "[CH2]CCCOO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74263,0.135906,-0.000638822,1.49311e-06,-1.22111e-09,-2092.94,42.1396], Tmin=(10,'K'), Tmax=(399.845,'K')),
            NASAPolynomial(coeffs=[4.13046,0.0474852,-2.74925e-05,7.61108e-09,-8.14322e-13,-1608.09,44.1672], Tmin=(399.845,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-17.4451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.89544900   -0.59952200    1.01300800
O       3.12428200    0.01667900    1.38648000
C       0.89434300    1.60407500    0.65835300
C       0.02306100    1.47870800    1.91057400
C       1.26406600    0.25279900    0.07284300
C      -1.29914400    0.85618700    1.63935700
H       0.36357400    2.17187900   -0.11054500
H       1.80681100    2.15108200    0.89342700
H      -0.11220600    2.48254800    2.33433900
H       0.56281800    0.90219300    2.66281700
H       1.90341400    0.36564400   -0.80726100
H       0.36994300   -0.30890600   -0.20578600
H      -1.78597900    0.22662400    2.36749500
H      -1.87287800    1.15890600    0.77399000
H       3.76283300   -0.58950700    0.99383300
""",
)

entry(
    index = 72,
    label = "[CH2]CC(C)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u0 p2 c0 {1,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u1 p0 c0 {4,S} {13,S} {14,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35215,0.0668595,-0.000170628,3.81772e-07,-3.22684e-10,-3764.6,13.276], Tmin=(10,'K'), Tmax=(399.801,'K')),
            NASAPolynomial(coeffs=[2.47796,0.0528697,-3.28371e-05,9.76369e-09,-1.11653e-12,-3512.99,18.9645], Tmin=(399.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-31.317,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.84092400    1.42729800    0.09168200
O      -1.66089800    1.84422100   -0.99211100
C      -0.13896900    0.25649600   -0.31607800
C       0.93433900    0.06566000    0.74865600
C      -1.07147000   -0.93372400   -0.42799900
C       1.92242800    1.17338000    0.79108200
H       0.33173600    0.46822900   -1.28031100
H       0.42024700   -0.04274300    1.71526900
H       1.43089700   -0.88982700    0.56567500
H      -0.52295600   -1.81707900   -0.75415900
H      -1.85711700   -0.73790900   -1.15561500
H      -1.52694700   -1.14533000    0.54063200
H       1.60785200    2.18061900    0.56689700
H       2.90605100    1.01712100    1.20517900
H      -2.54364400    1.67313400   -0.64427200
""",
)

entry(
    index = 73,
    label = "CC(CCOO)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {7,S}
2  O u0 p2 c0 {4,S} {5,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94224,0.101451,-0.000281174,5.29504e-07,-3.77291e-10,-21756.7,14.81], Tmin=(10,'K'), Tmax=(448.807,'K')),
            NASAPolynomial(coeffs=[4.02637,0.0602115,-3.78098e-05,1.12428e-08,-1.28064e-12,-21536,13.9912], Tmin=(448.807,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       5.36067200    2.94855900    3.26187000
O       1.40465300    3.38523500    2.07176700
O       6.03129800    3.94499900    4.01875600
O       0.43893700    4.10280700    1.58942900
C       2.38079400    3.03256000    1.04898100
C       3.58692100    2.50572500    1.79756300
C       4.24284400    3.56861200    2.65733300
C       1.76270500    2.02328200    0.10744800
H       2.61088400    3.96299900    0.52713300
H       4.31062000    2.13225300    1.07193300
H       3.28120000    1.66143300    2.41869200
H       3.55630600    3.93748500    3.42333500
H       4.57785800    4.41347100    2.04989700
H       2.46223100    1.78800300   -0.69348300
H       1.52296700    1.10506300    0.64368700
H       0.85290300    2.42986300   -0.32875100
H       5.82025000    3.67863400    4.92164600
""",
)

entry(
    index = 74,
    label = "CC(CCO[O])OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68696,0.0564188,-2.84028e-05,5.07047e-09,8.46734e-14,-21079.8,13.44], Tmin=(10,'K'), Tmax=(1589.32,'K')),
            NASAPolynomial(coeffs=[23.9284,0.0182704,-4.47434e-06,9.87743e-11,6.99249e-14,-29129.8,-98.6749], Tmin=(1589.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-175.304,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.29763900   -0.65900900    0.84239200
O       0.97378300   -0.17608700    2.50674900
O      -2.24059100   -1.62783800    0.39917000
O       1.01866200    1.00182900    3.04498400
C      -0.62840100   -0.16161200   -0.30807000
C       0.54740000    0.63817400    0.22918300
C       1.46517100   -0.14619100    1.14863400
C      -1.54676600    0.67650600   -1.17603600
H      -0.25650300   -1.02283100   -0.87374600
H       0.19488700    1.52027900    0.76721700
H       1.12512700    0.99412300   -0.62492300
H       1.53366800   -1.19521300    0.86429500
H       2.45902100    0.29598100    1.18963000
H      -2.38824500    0.08188100   -1.52510800
H      -1.92235000    1.52780000   -0.60697300
H      -1.00981400    1.05098600   -2.04742900
H      -3.06922800   -1.23391600    0.69512600
""",
)

entry(
    index = 75,
    label = "CC(C[CH]OO)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {17,S}
4  O u0 p2 c0 {2,S} {16,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
8  C u1 p0 c0 {2,S} {6,S} {15,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80378,0.0267535,0.00078883,-6.28623e-06,1.57871e-08,-16782.7,10.4328], Tmin=(10,'K'), Tmax=(134.617,'K')),
            NASAPolynomial(coeffs=[3.99567,0.0609929,-3.77433e-05,1.12647e-08,-1.29588e-12,-16824.1,8.54764], Tmin=(134.617,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       3.20350400    1.50117400   -1.19070800
O      -0.05811000    0.60058700    1.44992600
O       3.22247500    2.81657500   -1.73742900
O       1.07408000    0.00778700    2.08154400
C       1.89119700    1.23487000   -0.70871900
C       1.54693800    2.18692400    0.44567700
C       0.86027800    1.24192400   -1.82189400
C       0.23502500    1.88099700    1.07183500
H       2.00085800    0.22506600   -0.30812800
H       1.52073600    3.20843100    0.06781200
H       2.35695300    2.12208600    1.17394400
H      -0.08215800    0.83352800   -1.45914400
H       1.20136200    0.62489100   -2.65300700
H       0.68207100    2.25582900   -2.17978800
H      -0.68061700    2.37807200    0.78353100
H       0.90206500    0.20701600    3.01128700
H       3.28636000    2.62966600   -2.68095100
""",
)

entry(
    index = 76,
    label = "C[C](CCOO)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {8,S}
3  O u0 p2 c0 {1,S} {16,S}
4  O u0 p2 c0 {2,S} {17,S}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
7  C u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
8  C u1 p0 c0 {2,S} {5,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71886,0.0235573,0.000232091,-6.70931e-07,5.92601e-10,-47113.7,13.2447], Tmin=(10,'K'), Tmax=(363.724,'K')),
            NASAPolynomial(coeffs=[1.99223,0.06639,-4.28854e-05,1.33062e-08,-1.58101e-12,-47145.8,17.6602], Tmin=(363.724,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-391.698,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       5.29685000   -1.21765300    1.31520700
O       4.72159200    0.15195400   -1.03041100
O       4.46453900    1.10087600   -0.00454000
O       2.47436200    0.18759400   -1.58782100
C       3.20096300   -1.39174600    0.07036400
C       4.39318600   -2.06707500    0.72671800
C       3.86817600   -1.52626500   -2.38429800
C       3.54548800   -0.62409400   -1.21299500
H       2.44146600   -2.13343200   -0.17987100
H       2.75166700   -0.70159600    0.78604300
H       4.06626400   -2.74886200    1.52936800
H       4.94854600   -2.71917700    0.03638200
H       4.14596500   -0.90819000   -3.23461600
H       2.98303000   -2.10544800   -2.63858000
H       4.69013000   -2.19968300   -2.15018600
H       4.84792600    0.64272500    0.76152300
H       2.43183300    0.90942100   -0.94950900
""",
)

entry(
    index = 77,
    label = "CC(CC=O)OO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,D} {5,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.04084,0.095005,-0.000261679,4.76782e-07,-3.37654e-10,-38329.4,26.6921], Tmin=(10,'K'), Tmax=(425.144,'K')),
            NASAPolynomial(coeffs=[5.99651,0.0482811,-3.00903e-05,8.97882e-09,-1.03037e-12,-38409.8,16.9712], Tmin=(425.144,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-318.712,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (336.736,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.30090800   -1.21214800    0.37504600
O      -2.55825500   -0.77036700    0.86964000
O       1.02603900    2.11783200    1.49603900
C      -0.35940800   -0.15915300    0.55956500
C      -0.15426600    0.10579600    2.04143300
C       0.90000000   -0.63081800   -0.13699200
C       0.62275600    1.35555100    2.33288300
H      -0.74074100    0.74561900    0.07908400
H      -1.12279700    0.19989600    2.54074700
H       0.35129600   -0.73930800    2.51972700
H       0.70550100   -0.81566300   -1.19161100
H       1.25580900   -1.55504300    0.31894500
H       1.66929300    0.13319100   -0.04793400
H       0.80659400    1.55834600    3.40479300
H      -3.04144200   -0.61303300    0.04990900
""",
)

entry(
    index = 78,
    label = "CC(=O)CCOO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {15,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {7,S} {12,S} {13,S} {14,S}
7  C u0 p0 c0 {3,D} {4,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63348,0.039267,6.31653e-06,-2.93686e-08,1.22574e-11,-40680.6,12.3171], Tmin=(10,'K'), Tmax=(983.158,'K')),
            NASAPolynomial(coeffs=[5.95164,0.0444409,-2.38607e-05,6.20428e-09,-6.3041e-13,-41842.3,-2.41714], Tmin=(983.158,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-338.232,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.47575900    0.78201500   -0.65076000
O       1.80987500    0.85440800   -2.02890100
O       4.19107400   -0.27345400   -0.88689600
C       2.21137200   -1.55410700   -0.67138000
C       1.09616500   -0.54410700   -0.36811800
C       3.98068700   -1.39130100    1.19901600
C       3.53882600   -1.01254200   -0.18666200
H       1.96977900   -2.50243800   -0.19129800
H       2.27835900   -1.70368700   -1.74679000
H       0.85881200   -0.52394600    0.69683800
H       0.19749600   -0.81272900   -0.92747100
H       4.17117900   -2.46536500    1.23742800
H       4.87747500   -0.84385700    1.47165400
H       3.17936500   -1.18315000    1.91048100
H       2.77074200    0.70650400   -1.99284400
""",
)

entry(
    index = 79,
    label = "C[C]C",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u2 p0 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70254,0.0356682,-0.000198109,5.55015e-07,-4.90557e-10,34859.5,7.54064], Tmin=(10,'K'), Tmax=(410.396,'K')),
            NASAPolynomial(coeffs=[0.0959731,0.0281489,-1.46622e-05,3.66061e-09,-3.54019e-13,35514.8,26.1062], Tmin=(410.396,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.824,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -1.33697600   -0.00479100   -0.38823900
C       1.33695200    0.08304400   -0.18738700
C      -0.00004400    0.58490000   -0.52601800
H      -2.10729700    0.67536800   -0.75381000
H      -1.43072000   -0.93945000   -0.95568000
H      -1.57494000   -0.23550300    0.65794500
H       1.43067000   -0.13675200    0.88372100
H       2.10711300    0.81386400   -0.43721500
H       1.57514100   -0.84068100   -0.72991700
""",
)

entry(
    index = 80,
    label = "[CH2]C[O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9794,0.00131992,6.09229e-05,-1.16165e-07,7.27118e-11,21650.3,10.3099], Tmin=(10,'K'), Tmax=(409.834,'K')),
            NASAPolynomial(coeffs=[1.91624,0.0214568,-1.27798e-05,3.72774e-09,-4.24185e-13,21819.5,18.423], Tmin=(409.834,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (180.006,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.22371200   -0.80189000   -0.79529300
C      -0.58594000    0.12487800   -0.00565400
C       0.88886300   -0.03439400    0.00821000
H      -0.89384900    1.14922000   -0.25117200
H      -1.02092500   -0.07030400    1.00033200
H       1.54139300    0.82345900   -0.01262000
H       1.30890300   -1.02754100    0.03430300
""",
)

entry(
    index = 81,
    label = "[CH2]C[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u1 p0 c0 {1,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59694,0.039833,-7.72303e-05,1.67106e-07,-1.32921e-10,30858,10.7663], Tmin=(10,'K'), Tmax=(458.939,'K')),
            NASAPolynomial(coeffs=[1.53269,0.0405451,-2.30817e-05,6.4098e-09,-6.94955e-13,31229.4,21.1], Tmin=(458.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (256.558,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
C      -0.80124300    0.53758300   -0.00366700
C       1.36638400    0.07124100   -1.32369200
C       0.11026000   -0.41488700   -0.69754800
C      -1.89232600   -0.12728100    0.75383000
H      -0.19744000    1.17757500    0.66360500
H      -1.23502000    1.25117600   -0.72308800
H       1.16736100    0.67532100   -2.21915700
H       1.92357400    0.71481600   -0.63743400
H       2.01550700   -0.74890500   -1.62566700
H      -0.27567300   -1.39087400   -0.95980700
H      -1.73438300   -1.10912500    1.17516900
H      -2.78130800    0.41436900    1.03762100
""",
)

entry(
    index = 82,
    label = "[CH2]CC(C)[O]",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  C u1 p0 c0 {3,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63073,0.0353089,-8.83237e-06,-7.44317e-09,3.76585e-12,13912.2,12.1599], Tmin=(10,'K'), Tmax=(1105.2,'K')),
            NASAPolynomial(coeffs=[6.64683,0.0327539,-1.67125e-05,4.15531e-09,-4.06151e-13,12734.9,-5.00296], Tmin=(1105.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.654,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.27078100   -1.32461500   -1.09315400
C       0.52273100   -0.67947200   -0.14262800
C      -0.86132500   -0.27622600   -0.67172100
C       1.28381900    0.47800400    0.49646400
C      -1.62489800   -1.42831700   -1.20752300
H       0.37514800   -1.47200100    0.61675800
H      -0.69585200    0.48457300   -1.44894400
H      -1.41520200    0.22558500    0.12487000
H       0.71925700    0.89920100    1.32748000
H       2.25154600    0.13701300    0.85773700
H       1.44554000    1.26350400   -0.24205700
H      -1.09772400   -2.22623300   -1.70781600
H      -2.70140800   -1.40101800   -1.26653000
""",
)

entry(
    index = 83,
    label = "C[C]CC",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u2 p0 c0 {1,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60648,0.0448639,-0.0001956,5.39688e-07,-4.77795e-10,32467,11.8744], Tmin=(10,'K'), Tmax=(412.458,'K')),
            NASAPolynomial(coeffs=[-0.370244,0.0403055,-2.21905e-05,5.90925e-09,-6.12897e-13,33161.8,31.9846], Tmin=(412.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.93,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (270.22,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
C      -0.58693500    0.23397100   -0.16548700
C      -2.01608600   -0.32922100   -0.16576300
C       0.44345800   -1.17270700    1.87530000
C       0.37728000   -0.65391300    0.50265500
H      -0.26594200    0.41104900   -1.19457000
H      -0.59016600    1.21817700    0.32382500
H      -2.37103000   -0.47984900    0.85381200
H      -2.70375500    0.35239800   -0.66575200
H      -2.04730100   -1.28998900   -0.67867300
H      -0.41453600   -1.81237100    2.11717300
H       1.34347700   -1.77008300    2.02640300
H       0.46231500   -0.36087600    2.61379900
""",
)

entry(
    index = 84,
    label = "CC(CC[O])OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {16,S}
3  O u1 p2 c0 {7,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58278,0.0484442,-1.45419e-05,-6.86349e-09,3.76687e-12,-20470.2,12.9209], Tmin=(10,'K'), Tmax=(1211.85,'K')),
            NASAPolynomial(coeffs=[10.5606,0.0385931,-1.86635e-05,4.37903e-09,-4.03939e-13,-23129.3,-26.0773], Tmin=(1211.85,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-170.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.53736700    0.58507800   -1.15591600
O       1.19026000    1.82514200   -1.76310600
O      -2.72151100    0.45545100   -1.95419600
C       0.58465200    0.30698700   -0.13059900
C      -0.74672500   -0.15599000   -0.70076800
C       1.23790800   -0.77110500    0.71415500
C      -1.48102200    0.86930300   -1.55894700
H       0.44949400    1.22081200    0.45679800
H      -1.39948200   -0.42128100    0.13425200
H      -0.58559300   -1.06285800   -1.28689200
H       0.57478800   -1.05832400    1.52840200
H       1.43679100   -1.65193000    0.10380800
H       2.17822600   -0.41699800    1.13168400
H      -1.53453800    1.85560500   -1.07574400
H      -0.93306800    1.05606200   -2.49782400
H       1.94175300    2.37352000   -1.50994500
""",
)

entry(
    index = 85,
    label = "CC(CCOO)OO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {7,S}
3  O u0 p2 c0 {2,S} {17,S}
4  O u0 p2 c0 {1,S} {18,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
8  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15041,0.0852713,-0.000199447,4.04193e-07,-3.15678e-10,-37753.8,13.6305], Tmin=(10,'K'), Tmax=(425.11,'K')),
            NASAPolynomial(coeffs=[2.51572,0.0655979,-3.95399e-05,1.15148e-08,-1.29723e-12,-37468.1,18.8751], Tmin=(425.11,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-313.925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.18173300    3.47200700    2.83606600
O      -2.20634800    3.38748500   -0.54362300
O      -3.51178600    3.94422800   -0.46859600
O       0.56323700    3.11246100    4.15740000
C       0.24483200    2.29858100    2.02924000
C      -0.32514400    2.71799100    0.68485500
C      -1.76014900    3.19696600    0.78581400
C       1.66633100    1.78399600    1.92112600
H      -0.39866300    1.53828800    2.48667800
H       0.29769400    3.50623400    0.25897500
H      -0.27784500    1.86091500    0.01106800
H      -1.82924400    4.13659700    1.33392600
H      -2.38762900    2.45034500    1.28540500
H       2.29896600    2.53847500    1.45324700
H       1.69382100    0.87816900    1.31574300
H       2.06299300    1.55672900    2.90770800
H      -4.04893600    3.21876700   -0.80770200
H      -0.26850500    3.23071100    4.63045800
""",
)

entry(
    index = 86,
    label = "CC(=O)CC[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
6  C u0 p0 c0 {2,D} {3,S} {5,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54079,0.0493192,-0.00013417,3.62149e-07,-3.39038e-10,-22689.7,12.7063], Tmin=(10,'K'), Tmax=(391.489,'K')),
            NASAPolynomial(coeffs=[0.919252,0.0491255,-3.00574e-05,8.82525e-09,-9.98606e-13,-22277.7,25.5357], Tmin=(391.489,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-188.669,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -2.57593100    0.49618900   -1.34570000
O       0.37999800   -1.47927000    0.67545000
C      -0.74212300    0.56619900    0.23740800
C      -1.75055500   -0.24979200   -0.55683900
C       1.20077600    0.38117600    1.90977600
C       0.29226500   -0.30147900    0.92016800
H      -0.22060100    1.25675800   -0.43134700
H      -1.24412900    1.18878900    0.98139800
H      -1.21652400   -0.92991400   -1.24325800
H      -2.32789800   -0.92645600    0.08708500
H       1.62913000    1.28427500    1.47392200
H       0.61671200    0.68968100    2.77873600
H       1.98710500   -0.29931700    2.22216700
""",
)

entry(
    index = 87,
    label = "[CH2]C(=O)COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {11,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {6,S}
6  C u1 p0 c0 {5,S} {9,S} {10,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84863,0.0110266,0.00015254,-3.93026e-07,3.06755e-10,-15052.9,12.029], Tmin=(10,'K'), Tmax=(423.409,'K')),
            NASAPolynomial(coeffs=[3.07037,0.0398988,-2.59832e-05,8.10086e-09,-9.64807e-13,-15179.9,12.8368], Tmin=(423.409,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-125.162,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.78991200   -0.87468900    0.22169300
O       2.58269800    0.12003300   -0.40902800
O       1.91324900    1.05000800    2.10572100
C       0.59224800   -0.26976500    0.60775900
C       0.79030500    0.74926300    1.72115900
C      -0.38463600    1.34518400    2.29002400
H      -0.05018800   -1.07975400    0.96073200
H       0.10274700    0.21437800   -0.24454900
H      -1.37390700    1.08458400    1.94297500
H      -0.26759700    2.06693600    3.08340000
H       2.98643600    0.54239000    0.36510500
""",
)

entry(
    index = 88,
    label = "O=C1COC1",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5 C u0 p0 c0 {2,D} {3,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00967,-0.00136012,9.80532e-05,-1.6006e-07,8.28495e-11,-23648.1,8.61763], Tmin=(10,'K'), Tmax=(593.847,'K')),
            NASAPolynomial(coeffs=[0.318226,0.0347934,-2.17819e-05,6.48071e-09,-7.37807e-13,-23408.7,22.827], Tmin=(593.847,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-196.633,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -0.01146200   -1.10407500    0.53118400
O       0.01922100    1.84045000   -0.88641000
C       0.93848600   -0.43616700   -0.31310500
C      -0.94326800   -0.01114900    0.52860200
C       0.00802900    0.77138700   -0.37155300
H       1.89572800   -0.25970600    0.18070400
H       1.09371600   -0.94695800   -1.26508800
H      -1.09880800    0.41695000    1.52043100
H      -1.90154200   -0.27083200    0.07523500
""",
)

entry(
    index = 89,
    label = "C=C([O])C[O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u1 p2 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {5,D}
5 C u0 p0 c0 {4,D} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90523,0.00581043,0.000110935,-2.32081e-07,1.45784e-10,2661.77,12.0241], Tmin=(10,'K'), Tmax=(530.235,'K')),
            NASAPolynomial(coeffs=[3.02966,0.032624,-2.20868e-05,7.04525e-09,-8.5091e-13,2470.55,13.0139], Tmin=(530.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.0991,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -2.01740000   -0.87462800   -0.21806000
O       1.19671900    0.53027600    0.30600600
C      -1.06584500    0.09198000   -0.25335400
C       0.23514800   -0.20204000    0.49566300
C       0.27208000   -1.31318500    1.39378100
H      -1.52000000    0.97172500    0.24110300
H      -0.83729700    0.43117200   -1.27217100
H       1.19134800   -1.50712700    1.92450900
H      -0.58989700   -1.94522800    1.53538100
""",
)

entry(
    index = 90,
    label = "[O]OCC(=O)COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {1,S} {13,S}
4  O u0 p2 c0 {8,D}
5  O u1 p2 c0 {2,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
8  C u0 p0 c0 {4,D} {6,S} {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57536,0.0484923,-2.93527e-05,6.53024e-09,6.94693e-14,-28120.9,13.8967], Tmin=(10,'K'), Tmax=(1245.89,'K')),
            NASAPolynomial(coeffs=[12.5585,0.0275976,-1.37632e-05,3.30753e-09,-3.11063e-13,-30976.1,-33.8918], Tmin=(1245.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-233.815,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.53639000    1.48019600   -0.68917700
O      -2.92585700   -0.06607200    2.94521000
O      -2.44600500    2.40043800   -0.55202800
O      -3.29402700   -1.33486700    0.59431400
O      -2.22798600   -1.28105800    3.17430800
C      -2.13282400    0.18205900   -0.77420500
C      -2.38536400    0.51682000    1.79922300
C      -2.68151100   -0.30141300    0.55906800
H      -1.30188100    0.65742000    1.88525500
H      -2.84575200    1.50257100    1.70658300
H      -1.34044200   -0.49201500   -1.09661900
H      -2.93335400    0.20085500   -1.51103800
H      -2.76777600   -1.90098000    2.66207300
""",
)

entry(
    index = 91,
    label = "[O]C[O]",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04334,-0.00399707,4.67212e-05,-2.42647e-08,-5.65106e-11,13614.2,7.10606], Tmin=(10,'K'), Tmax=(310.496,'K')),
            NASAPolynomial(coeffs=[1.64294,0.0175171,-1.17574e-05,3.69573e-09,-4.39949e-13,13808.6,16.6095], Tmin=(310.496,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -1.03010200    0.78561700   -0.04540400
O       1.06722400    0.73496700   -0.02087900
C      -0.00015000   -0.02428600    0.00190700
H      -0.02788700   -0.71148300    0.90028300
H      -0.00908400   -0.78481500   -0.83590600
""",
)

entry(
    index = 92,
    label = "C1=CCC1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17563,-0.0132268,0.000135303,-1.92063e-07,8.85227e-11,18645.7,7.18563], Tmin=(10,'K'), Tmax=(672.937,'K')),
            NASAPolynomial(coeffs=[-1.5104,0.0393305,-2.36638e-05,6.84724e-09,-7.63429e-13,18986.3,29.2093], Tmin=(672.937,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.048,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.96915000   -0.10148900   -0.01287900
C       0.17861400    0.95201800   -0.11106400
C       1.11482700   -0.22350400    0.05607000
C       0.13570300   -1.12122200    0.13980400
H      -1.62408100    0.01853500    0.84994000
H      -1.57978400   -0.19503200   -0.91098000
H       0.19232900    1.68694200    0.69381300
H       0.23883800    1.47197100   -1.06703300
H       2.19346100   -0.29343200    0.09253700
H       0.11934200   -2.19488700    0.26979000
""",
)

entry(
    index = 93,
    label = "[CH2]C=C[CH2]",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87149,0.00774875,0.000119787,-2.57578e-07,1.62155e-10,40100.3,10.0897], Tmin=(10,'K'), Tmax=(551.008,'K')),
            NASAPolynomial(coeffs=[4.77648,0.0300819,-1.96923e-05,6.37502e-09,-7.96143e-13,39561.8,2.28157], Tmin=(551.008,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (333.366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.63466500   -0.64159400   -0.34320500
C      -0.73772600   -0.48889300   -0.47895500
C       1.48919800    0.28141400    0.39490800
C      -1.46858100    0.54291700    0.05905700
H       1.10119400   -1.50138200   -0.81548900
H      -1.26378600   -1.24331200   -1.05293800
H       1.72751900    0.11166600    1.43641500
H       1.98996300    1.10044600   -0.10385600
H      -2.53655300    0.60592400   -0.08238100
H      -0.98836300    1.31908500    0.63940200
""",
)

entry(
    index = 94,
    label = "[CH]1CC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17799,-0.0138517,0.00012061,-1.77069e-07,8.51895e-11,32124,7.28793], Tmin=(10,'K'), Tmax=(648.039,'K')),
            NASAPolynomial(coeffs=[-0.0184581,0.028915,-1.74165e-05,5.08188e-09,-5.72186e-13,32313.8,22.9807], Tmin=(648.039,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (267.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.76251600   -0.27189700    0.00625200
C      -0.75741000   -0.27150700    0.08931300
C      -0.02839800    0.83824800   -0.52461400
H       1.20859300   -0.97039100   -0.69080700
H       1.33504300   -0.12233000    0.91320400
H      -1.27719400   -0.96974100   -0.55496200
H      -1.22761000   -0.12157700    1.05326200
H      -0.01544000    1.88899400   -0.29174700
""",
)

entry(
    index = 95,
    label = "C=CCO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {4,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54948,0.049964,-0.000213872,5.58309e-07,-4.95658e-10,9062.42,11.7124], Tmin=(10,'K'), Tmax=(391.154,'K')),
            NASAPolynomial(coeffs=[1.85949,0.033299,-1.97849e-05,5.63978e-09,-6.20965e-13,9454.33,21.599], Tmin=(391.154,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.3293,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.83836600    1.64873800   -0.40087300
O       1.61445300    1.63785700   -1.44013200
C       0.75751900    0.33377300    0.20042600
C      -0.05038800   -0.58449700   -0.65399200
C      -1.10508100   -1.24718800   -0.21089100
H       1.78267400   -0.01636600    0.32007700
H       0.29629100    0.49525300    1.17248500
H       0.29151000   -0.68907200   -1.67715700
H      -1.45038600   -1.14048500    0.81045500
H      -1.65664300   -1.92329900   -0.84918700
""",
)

entry(
    index = 96,
    label = "C1OO1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10373,-0.00690484,4.96019e-05,-6.05597e-08,2.3963e-11,-790.354,5.80202], Tmin=(10,'K'), Tmax=(789.979,'K')),
            NASAPolynomial(coeffs=[1.25686,0.0158658,-9.50025e-06,2.70604e-09,-2.95525e-13,-601.286,17.2152], Tmin=(789.979,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.54796,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.92368300    0.06408200    0.73354000
O       0.93087200   -0.09132300   -0.72213300
C      -0.24070500    0.00368900   -0.00156500
H      -0.79308200    0.93349300   -0.10326500
H      -0.82076900   -0.90984100    0.09342400
""",
)

entry(
    index = 97,
    label = "C=CC(C)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59857,0.0367883,-1.13806e-05,-5.83752e-09,3.43949e-12,4262.16,13.9164], Tmin=(10,'K'), Tmax=(1082.05,'K')),
            NASAPolynomial(coeffs=[6.59984,0.0333717,-1.72882e-05,4.36013e-09,-4.31766e-13,3163.16,-2.87666], Tmin=(1082.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.85624300    1.47422600   -0.18163700
O      -1.82839200    1.82179400    0.60112900
C      -0.31105600    0.17081000    0.18849200
C      -1.34956800   -0.89303100   -0.10719300
C       0.94018300    0.00726700   -0.61012300
C       2.12386900   -0.22950800   -0.07122200
H      -0.09202500    0.22469800    1.25490800
H      -0.97360000   -1.86628800    0.20362300
H      -2.26787400   -0.67349500    0.43336300
H      -1.56141900   -0.92473100   -1.17596300
H       0.82146300    0.06583800   -1.68724100
H       3.00366500   -0.37967600   -0.68119900
H       2.25128000   -0.28552000    1.00309500
""",
)

entry(
    index = 98,
    label = "CC=CCO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32421,0.0725128,-0.000286531,6.86e-07,-5.71573e-10,4519.17,12.9456], Tmin=(10,'K'), Tmax=(407.329,'K')),
            NASAPolynomial(coeffs=[2.07079,0.0431673,-2.50729e-05,7.02303e-09,-7.62955e-13,4966.84,22.1087], Tmin=(407.329,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.5528,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.99953600    0.28505300   -0.78167600
O      -3.16405700    0.08892600   -0.24562900
C      -1.22466900   -0.94124400   -0.80610400
C       1.04490900   -1.78398000    2.23161800
C      -0.74878100   -1.29103400    0.56169700
C       0.53178400   -1.41444700    0.87819700
H      -1.87698500   -1.70625000   -1.22660600
H      -0.39781100   -0.73530700   -1.48285600
H       0.22861200   -1.92575300    2.93752500
H       1.70670000   -1.00705300    2.61755100
H       1.62844500   -2.70497800    2.18704100
H       1.27763400   -1.24180100    0.10659900
H      -1.52301300   -1.44951600    1.30511000
""",
)

entry(
    index = 99,
    label = "[CH2]C1CC1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96439,0.00218728,0.00010973,-1.96293e-07,1.13815e-10,23623.1,8.67285], Tmin=(10,'K'), Tmax=(445.479,'K')),
            NASAPolynomial(coeffs=[-0.559935,0.0428048,-2.7013e-05,8.31006e-09,-9.87455e-13,24026.3,26.8425], Tmin=(445.479,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (196.401,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.23366600    0.01692300    0.53957900
C       0.69119200    0.88852400   -0.29042000
C       1.01811600   -0.55162100   -0.10363900
C      -1.54144800   -0.34716500    0.02147600
H      -0.17426800    0.16895800    1.60784600
H       0.31719600    1.20446500   -1.25323300
H       1.28559800    1.62254200    0.23292200
H       1.83827200   -0.81205700    0.54867600
H       0.86753200   -1.21983600   -0.93881200
H      -2.39263600   -0.45583800    0.67288100
H      -1.67588900   -0.51499500   -1.03727600
""",
)

entry(
    index = 100,
    label = "C=CCCO[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {12,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32534,0.0732976,-0.000299728,7.40957e-07,-6.34729e-10,5510.89,13.1135], Tmin=(10,'K'), Tmax=(397.75,'K')),
            NASAPolynomial(coeffs=[1.88411,0.0442784,-2.61942e-05,7.44683e-09,-8.18667e-13,5969.74,23.0647], Tmin=(397.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (45.7952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.06551300   -0.89471200    0.07053000
O       0.24538900   -1.68810200    1.04935400
C      -2.45884400   -1.35172500    0.06464500
C      -1.36984400   -0.31155600    0.26445800
C      -3.80723700   -0.76212700    0.34176700
C      -4.75945100   -0.60819800   -0.56429800
H      -2.41290900   -1.73639200   -0.95468100
H      -2.25512000   -2.17719900    0.74992100
H      -1.39430600    0.11052300    1.26877300
H      -1.43072300    0.48429000   -0.47537000
H      -3.98585600   -0.43513800    1.36196200
H      -4.61507300   -0.92449400   -1.59051900
H      -5.71544800   -0.17055000   -0.31227800
""",
)

entry(
    index = 101,
    label = "[C]1CCC1",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u2 p0 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10649,-0.0078691,0.000112815,-1.57604e-07,7.05805e-11,52797.6,8.63846], Tmin=(10,'K'), Tmax=(690.069,'K')),
            NASAPolynomial(coeffs=[-1.42083,0.0396069,-2.39378e-05,6.92848e-09,-7.70769e-13,53192.9,30.591], Tmin=(690.069,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (438.996,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.00313900    0.70818800   -0.17115800
C       1.13003600   -0.33394400    0.09207200
C      -1.12691200   -0.34878800    0.07305800
C       0.00580900   -1.29001900    0.31211200
H       0.00269000    1.10504600   -1.18259700
H      -0.01449900    1.52337600    0.54709000
H       1.75915000   -0.12113200    0.95826100
H       1.77618900   -0.53765500   -0.76369300
H      -1.75573500   -0.56077000   -0.79354700
H      -1.77338900   -0.14430200    0.92840300
""",
)

entry(
    index = 102,
    label = "[CH2]C(CCO)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {6,S} {15,S}
3  O u0 p2 c0 {1,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
7  C u1 p0 c0 {4,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.93817,0.103398,-0.000312217,5.94231e-07,-4.23699e-10,-20930.9,13.6086], Tmin=(10,'K'), Tmax=(442.59,'K')),
            NASAPolynomial(coeffs=[4.97373,0.0529612,-3.26923e-05,9.6233e-09,-1.08917e-12,-20797.3,8.99251], Tmin=(442.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-174.056,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.54576300   -1.93091600    3.07356500
O       4.05638600   -0.33500800    0.96714000
O       1.42913600   -3.05252500    3.13416500
C       0.56168200   -1.45302800    1.72504400
C       1.75724100   -0.56174900    1.41995100
C       3.11155200   -1.23388100    1.52423500
C      -0.72364200   -0.73388000    1.55295400
H       0.59084900   -2.34442900    1.08203800
H       1.72930200    0.31152100    2.07449100
H       1.65059200   -0.20067100    0.39406200
H       3.10072800   -2.18524400    0.98218800
H       3.35476600   -1.44927700    2.56786400
H      -1.63087500   -1.17073300    1.93851700
H      -0.76413100    0.20002000    1.01575400
H       4.93388000   -0.71218500    1.05244900
H       1.95278000   -2.82807800    3.91129400
""",
)

entry(
    index = 103,
    label = "OCCC1CO1",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {6,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48394,0.0571891,-0.000198089,5.60065e-07,-5.32502e-10,-35188,25.6426], Tmin=(10,'K'), Tmax=(382.257,'K')),
            NASAPolynomial(coeffs=[0.19041,0.0533545,-3.27561e-05,9.61718e-09,-1.08651e-12,-34656.4,42.0247], Tmin=(382.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-292.593,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -3.50786500   -2.12962600   -1.88196400
O      -2.43434000    1.07767700   -0.21852400
C      -2.92268600   -0.89572600   -2.27575200
C      -1.58550100   -0.59557200   -1.66182300
C      -3.10128700   -1.98700000   -3.23319700
C      -1.73301300   -0.15550900   -0.21824700
H      -3.62261200   -0.06807400   -2.30293700
H      -1.08840000    0.19671400   -2.22530600
H      -0.96352500   -1.49123900   -1.70624100
H      -0.74673400   -0.04104600    0.24122500
H      -2.28532700   -0.92143500    0.33486800
H      -2.23960300   -2.58024000   -3.51904000
H      -3.90729200   -1.94576500   -3.95585300
H      -2.67488600    1.30325800    0.68168900
""",
)

entry(
    index = 104,
    label = "[CH2]C1CO1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 C u1 p0 c0 {2,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97338,0.00169779,9.25772e-05,-1.72873e-07,1.04919e-10,9863,9.24064], Tmin=(10,'K'), Tmax=(425.001,'K')),
            NASAPolynomial(coeffs=[0.527513,0.0341383,-2.19502e-05,6.82698e-09,-8.16278e-13,10155.8,22.9155], Tmin=(425.001,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (81.9998,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.88328100   -0.87687500    0.64885200
C      -0.16671400    0.08494200    0.48276800
C       1.18598400    0.28126100   -0.08957700
C      -1.28923400   -0.31137400   -0.34460400
H      -0.39294200    0.64005200    1.38589700
H       1.32360500    0.13282900   -1.15480200
H       1.86313100    0.98066800    0.38809500
H      -1.12572800   -0.99211100   -1.16583800
H      -2.28148200    0.06060800   -0.15069100
""",
)

entry(
    index = 105,
    label = "[CH]1CCOOC1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {5,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
6  C u1 p0 c0 {3,S} {5,S} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95188,0.00290996,0.000139143,-2.45879e-07,1.40004e-10,5420.68,11.2021], Tmin=(10,'K'), Tmax=(454.824,'K')),
            NASAPolynomial(coeffs=[-2.08839,0.0560477,-3.61561e-05,1.11459e-08,-1.31568e-12,5969.97,35.5823], Tmin=(454.824,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (45.0515,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.01842100   -1.53758200    0.57654600
O       1.11165500   -1.28423700   -0.29654600
C      -0.93583200    0.63211000    0.12603000
C      -1.10887400   -0.88066200    0.02291500
C       1.52922200    0.05432700   -0.06403100
C       0.42574700    1.01273800   -0.34030500
H      -1.06846300    0.92135600    1.17792900
H      -1.71187800    1.14586900   -0.44306300
H      -1.23064000   -1.19716600   -1.01509600
H      -1.95452900   -1.23414100    0.61150000
H       1.88857900    0.13101400    0.97229800
H       2.37793700    0.20066300   -0.73265200
H       0.65865500    2.03571000   -0.59572500
""",
)

entry(
    index = 106,
    label = "[O]C=CCC[O]",
    molecule = 
"""
multiplicity 3
1  O u1 p2 c0 {4,S}
2  O u1 p2 c0 {6,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45532,0.0545308,-0.000125833,2.47104e-07,-1.90796e-10,-537.057,12.7075], Tmin=(10,'K'), Tmax=(419.697,'K')),
            NASAPolynomial(coeffs=[3.50289,0.0401468,-2.46366e-05,7.27264e-09,-8.27917e-13,-418.36,13.9809], Tmin=(419.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.47889,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -2.61149700   -0.27733300    0.53205900
O       1.06986900    1.51174400    1.27045400
C      -0.37282600   -0.22522500   -0.45358500
C      -1.69640100    0.48695300   -0.12553300
C       0.32311300   -0.64180500    0.78750400
C       1.01889400    0.32658200    1.57783300
H       0.25360000    0.48412400   -0.99836900
H      -0.58235400   -1.08143000   -1.09259700
H      -2.15881200    0.89468800   -1.03689500
H      -1.50067700    1.36799500    0.50892900
H       0.26384000   -1.66123100    1.14165900
H       1.51296000   -0.03361300    2.49310400
""",
)

entry(
    index = 107,
    label = "O=CC1CCO1",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {2,D} {3,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1266,0.0177468,3.29758e-05,-4.38468e-08,1.4542e-11,-24711.4,10.6906], Tmin=(10,'K'), Tmax=(1111.03,'K')),
            NASAPolynomial(coeffs=[7.35075,0.0293779,-1.4102e-05,3.22809e-09,-2.86821e-13,-26862.2,-11.6583], Tmin=(1111.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.339,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.04092800    0.78955600   -1.09723400
O       2.42376100   -1.31935800    0.35904800
C       0.37734900   -0.43048600   -0.48201200
C      -0.72254100   -0.31704400    0.59617700
C      -1.18543900    0.88965300   -0.23167200
C       1.78173800   -0.35385700    0.05746600
H       0.28488200   -1.29383600   -1.14351600
H      -1.40266500   -1.15908900    0.66333000
H      -0.34715700   -0.06810900    1.58585100
H      -1.21933100    1.84879000    0.28352500
H      -2.11407200    0.73671200   -0.78268700
H       2.16430300    0.67717000    0.19172500
""",
)

entry(
    index = 108,
    label = "C1=COOCC1",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {6,S}
3  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07581,-0.00697521,0.000165167,-2.70611e-07,1.41465e-10,-3936.98,10.618], Tmin=(10,'K'), Tmax=(599.244,'K')),
            NASAPolynomial(coeffs=[-1.00351,0.0491209,-3.0798e-05,9.20107e-09,-1.0525e-12,-3726.67,29.1972], Tmin=(599.244,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.7475,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.16791900   -1.53155200    0.64266300
O       1.47319100   -1.05138100    0.35573300
C      -0.92495400    0.49451700   -0.04507100
C      -0.74743000   -0.99210700   -0.30131800
C       0.44058000    1.08831400    0.12772100
C       1.50108100    0.31037100    0.27980000
H      -1.54247500    0.65373000    0.84110800
H      -1.44059600    0.95995800   -0.88726800
H      -1.66019800   -1.56300000   -0.14029800
H      -0.37572900   -1.18311600   -1.31058900
H       0.58522400    2.15764900    0.09887200
H       2.52358800    0.65661700    0.33854700
""",
)

entry(
    index = 109,
    label = "[O]OC1CCOOC1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  O u0 p2 c0 {1,S} {7,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8665,0.0250763,6.16102e-05,-9.84367e-08,4.07412e-11,-10822.7,12.8106], Tmin=(10,'K'), Tmax=(852.499,'K')),
            NASAPolynomial(coeffs=[3.77852,0.0511619,-2.94605e-05,8.10715e-09,-8.62699e-13,-11740.6,7.74953], Tmin=(852.499,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.9294,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.11696900   -1.29497200   -0.82365400
O       0.06618900   -1.84026400   -0.03245000
O      -1.81676500    1.07712400    0.45522000
O      -1.74222900    2.36943000    0.37221000
C      -0.70730100    0.43617200   -0.21629400
C       0.56119700    0.59279000    0.60040800
C      -1.06498800   -1.04791300   -0.33444100
C       1.67053800   -0.22336700   -0.06677600
H      -0.61555600    0.91602800   -1.18911900
H       0.83114300    1.64412200    0.67273200
H       0.36589300    0.21819300    1.60479700
H       2.21637100    0.36358500   -0.80552300
H       2.37138900   -0.61105900    0.67405600
H      -1.44185400   -1.29068800   -1.32853400
H      -1.81089500   -1.30928100    0.41746800
""",
)

entry(
    index = 110,
    label = "C#C[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95581,0.00298556,3.60956e-05,-9.64008e-08,7.38874e-11,19622.8,0.81361], Tmin=(10,'K'), Tmax=(465.174,'K')),
            NASAPolynomial(coeffs=[4.52963,0.00673693,-4.00863e-06,1.21388e-09,-1.46057e-13,19475.4,-2.52565], Tmin=(465.174,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (163.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.76690700   -0.01229200    0.01590400
C      -0.65395400    0.00564900    0.25941700
C       0.59627200   -0.00403900    0.13228300
H      -1.70922500    0.01068100    0.36249600
""",
)

entry(
    index = 111,
    label = "[CH2]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9882,0.000666305,2.74965e-05,-4.3923e-08,2.27898e-11,-3101.87,5.79676], Tmin=(10,'K'), Tmax=(498.082,'K')),
            NASAPolynomial(coeffs=[2.56749,0.0120674,-6.81323e-06,1.9658e-09,-2.26034e-13,-2960.24,11.6617], Tmin=(498.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.7964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       0.92554100    0.04572200    0.43481400
C      -0.42115400    0.20989700    0.33655300
H      -0.87900300    0.57640900    1.24038700
H      -0.84771300    0.43922900   -0.62984700
H       1.28515000   -0.20235800   -0.41947700
""",
)

entry(
    index = 112,
    label = "C=CO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96256,0.00211337,5.82906e-05,-1.02343e-07,5.52298e-11,-16314.1,6.21269], Tmin=(10,'K'), Tmax=(590.451,'K')),
            NASAPolynomial(coeffs=[2.27805,0.0221611,-1.45786e-05,4.70359e-09,-5.82538e-13,-16265.7,12.1772], Tmin=(590.451,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-135.66,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.24033800    0.05775600   -0.77844000
C       0.26852200    0.36397200    0.11534900
C       0.11147700   -0.15707400    1.32248300
H      -0.39766700    1.11718300   -0.28391900
H       0.78466600   -0.91050300    1.71161100
H      -0.70490100    0.16805000    1.94686700
H       1.81869500   -0.61255400   -0.40125600
""",
)

entry(
    index = 113,
    label = "[CH2]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73367,0.018566,-9.19182e-06,2.46331e-09,-3.50912e-13,-4594.71,9.30723], Tmin=(10,'K'), Tmax=(1014.51,'K')),
            NASAPolynomial(coeffs=[3.37704,0.0195138,-9.91562e-06,2.49366e-09,-2.48661e-13,-4498.77,11.1491], Tmin=(1014.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.2472,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.16262100    0.02939400    1.07233400
C      -0.26245700   -0.43755700    0.08208700
C      -0.00007700    0.57022500   -0.97206400
H       0.65675200   -0.68343900    0.62622300
H      -0.61725200   -1.37268800   -0.36645700
H       0.30237800    0.27154100   -1.96387900
H       0.07525000    1.61123000   -0.69386500
H      -1.95439100    0.34130000    0.62656800
""",
)

entry(
    index = 114,
    label = "C=C[C]=O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91703,0.00709026,3.83528e-05,-7.13245e-08,3.91984e-11,10660.5,8.65741], Tmin=(10,'K'), Tmax=(563.521,'K')),
            NASAPolynomial(coeffs=[2.45692,0.0219549,-1.31936e-05,3.8289e-09,-4.29793e-13,10753.6,14.2301], Tmin=(563.521,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.6242,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       2.28205400    0.08564700    0.92013700
C       0.12347100    0.29638600   -0.09018000
C      -1.12674500   -0.13339400    0.00414400
C       1.14018400   -0.19320000    0.86599100
H       0.45263800    1.00268500   -0.84585000
H      -1.40226600   -0.83896800    0.77744700
H      -1.89692200    0.20176900   -0.67662200
""",
)

entry(
    index = 115,
    label = "C=CCO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80789,0.0172169,4.82076e-05,-1.61395e-07,1.62096e-10,-16486.7,9.85715], Tmin=(10,'K'), Tmax=(254.193,'K')),
            NASAPolynomial(coeffs=[3.12955,0.0278914,-1.47828e-05,3.80841e-09,-3.82391e-13,-16452.2,12.2007], Tmin=(254.193,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O       1.85205400    0.53574900    0.66131200
C       0.96409500    0.19748500   -0.37742000
C       0.57124700   -1.24970700   -0.40148800
C       1.07862400   -2.17780300    0.39306600
H       1.47336800    0.45186100   -1.30944600
H       0.05765800    0.81395700   -0.34042900
H      -0.18736400   -1.51316800   -1.13165900
H       0.75229800   -3.20657400    0.33697800
H       1.85166200   -1.93697800    1.11131600
H       1.42706100    0.32674000    1.49761600
""",
)

entry(
    index = 116,
    label = "CC=CO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {1,S} {3,D} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83131,0.0147396,2.56968e-05,-4.32493e-08,1.87738e-11,-19671.4,9.17874], Tmin=(10,'K'), Tmax=(751.758,'K')),
            NASAPolynomial(coeffs=[1.96924,0.0303524,-1.68392e-05,4.56694e-09,-4.84729e-13,-19552.7,16.5587], Tmin=(751.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-163.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (224.491,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O      -1.74342100    0.66479600    0.17022600
C       1.12778400    0.17006900    1.04708800
C       0.09675100   -0.82540700    0.61079900
C      -1.14726200   -0.55501900    0.23668000
H       2.00526700    0.13602500    0.39965400
H       1.46806500   -0.03661300    2.06285500
H       0.76410800    1.19848200    1.03640400
H       0.38616400   -1.86709300    0.59647600
H      -1.83291000   -1.33432900   -0.06556200
H      -1.11964300    1.34370800    0.44194400
""",
)

entry(
    index = 117,
    label = "C[CH]C(C)O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
5  C u1 p0 c0 {2,S} {4,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44582,0.0490472,-8.99897e-05,1.56608e-07,-1.02931e-10,-13817.8,12.2314], Tmin=(10,'K'), Tmax=(538.199,'K')),
            NASAPolynomial(coeffs=[1.02689,0.0466033,-2.62614e-05,7.16442e-09,-7.62424e-13,-13261.6,25.1505], Tmin=(538.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-114.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.27489100   -0.83399300   -2.20040200
C      -1.07307100   -0.34350800   -0.87384300
C      -2.35207000    0.25917000   -0.31605800
C       1.40705700    0.21192700   -1.33836500
C       0.07221100    0.61122500   -0.82308900
H      -0.82530100   -1.24748400   -0.30357400
H      -2.61868800    1.15672200   -0.87854500
H      -2.22448700    0.53988200    0.72978200
H      -3.16941800   -0.45486500   -0.39372100
H       1.99875400    1.07307600   -1.64793300
H       1.30350700   -0.46731600   -2.18455900
H       1.98953200   -0.31471900   -0.57107700
H      -0.02317000    1.50124500   -0.21492500
H      -1.40134100   -0.07025300   -2.77251800
""",
)

entry(
    index = 118,
    label = "CC(O)C(C)O[O]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {16,S}
2  O u0 p2 c0 {3,S} {5,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
5  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
6  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25416,0.0715538,-0.000151329,2.74538e-07,-1.97277e-10,-32168.4,13.4898], Tmin=(10,'K'), Tmax=(453.424,'K')),
            NASAPolynomial(coeffs=[3.07241,0.0544667,-3.29716e-05,9.60848e-09,-1.08189e-12,-31959.8,16.3415], Tmin=(453.424,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-267.486,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (361.68,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.34993100    1.18368200   -0.60296700
O      -0.36483100   -2.18139900    0.24595900
O       0.90953800   -2.13149500    0.00397100
C      -0.75113100    0.20424200    0.22975500
C      -1.08924500   -1.12734300   -0.43765700
C      -1.23549300    0.30627900    1.66436200
C      -2.54916600   -1.50773500   -0.38653900
H       0.33915100    0.29532300    0.20136100
H      -0.71500000   -1.09828800   -1.46038000
H      -0.88476100    1.23663300    2.11264200
H      -0.85138500   -0.52023100    2.26223500
H      -2.32413100    0.29855200    1.70244600
H      -2.85656300   -1.71836600    0.63685000
H      -2.73492200   -2.39256300   -0.99158400
H      -3.14342100   -0.68109100   -0.77126100
H      -1.17455700    2.05269000   -0.23486700
""",
)

entry(
    index = 119,
    label = "[CH]C",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u2 p0 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00702,-0.000566984,3.01023e-05,-3.69109e-08,1.46157e-11,40066.2,6.07464], Tmin=(10,'K'), Tmax=(658.302,'K')),
            NASAPolynomial(coeffs=[1.2229,0.0163504,-8.44652e-06,2.12868e-09,-2.10499e-13,40432.7,18.3423], Tmin=(658.302,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (333.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.42179900    0.00248500    0.08410000
C       1.00167100   -0.34263000    0.07591500
H      -0.97700100   -0.66392000    0.74704900
H      -0.59439400    1.02603700    0.43539400
H      -0.87122100   -0.08344200   -0.91163100
H       1.86284300    0.06137000   -0.43092700
""",
)

entry(
    index = 120,
    label = "[CH2]C[CH2]",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9171,0.00625487,6.45336e-05,-1.34522e-07,9.05428e-11,35159.5,8.38164], Tmin=(10,'K'), Tmax=(380.54,'K')),
            NASAPolynomial(coeffs=[2.00954,0.0263058,-1.45018e-05,3.93836e-09,-4.19979e-13,35304.7,15.7415], Tmin=(380.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (292.317,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.07810300   -0.29916500    0.36873500
C       1.14374900    0.64725800   -0.05278500
C      -1.20783700   -0.09716800   -0.34861300
H       0.42670800   -1.34039600    0.21763100
H      -0.07812700   -0.23591800    1.45160700
H       2.02772900    0.78804100    0.54939300
H       1.12180900    1.08646600   -1.03894000
H      -2.12359100   -0.52627500    0.02707700
H      -1.21739700    0.34656700   -1.33293900
""",
)

entry(
    index = 121,
    label = "O=O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50704,-0.000409012,1.2518e-06,1.57644e-09,-2.0454e-12,17501.7,3.59491], Tmin=(10,'K'), Tmax=(631.504,'K')),
            NASAPolynomial(coeffs=[2.87661,0.00207556,-1.06646e-06,2.40965e-10,-1.91747e-14,17611.4,6.58473], Tmin=(631.504,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (145.52,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       0.59432200    0.00000000    0.00000000
O      -0.59432200    0.00000000   -0.00000000
""",
)

entry(
    index = 122,
    label = "[O]C[CH]O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {4,S} {8,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {1,S} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93388,0.0061409,0.000109282,-3.39293e-07,3.51802e-10,-126.235,10.4203], Tmin=(10,'K'), Tmax=(244.403,'K')),
            NASAPolynomial(coeffs=[2.67648,0.0267202,-1.70227e-05,5.23425e-09,-6.18326e-13,-64.7731,14.7149], Tmin=(244.403,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.03424,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.75813900    0.37500000   -0.92049400
O       0.15076700   -2.61343000   -0.78499900
C       0.74896100   -1.44823900   -1.23952000
C       0.39283200   -0.21794800   -0.49959800
H       1.83005900   -1.64654500   -1.16523200
H       0.53965900   -1.32926200   -2.31098100
H       0.67569000   -0.09428000    0.53826100
H      -1.00174900    1.08554600   -0.32295800
""",
)

entry(
    index = 123,
    label = "OC1CO1",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05032,-0.00451526,9.71092e-05,-1.58114e-07,8.23804e-11,-31623.4,8.82338], Tmin=(10,'K'), Tmax=(601.283,'K')),
            NASAPolynomial(coeffs=[1.08499,0.0283174,-1.74922e-05,5.19897e-09,-5.93699e-13,-31503.7,19.6509], Tmin=(601.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-262.939,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.50728500   -0.55182100    1.06481900
O       1.60370100   -0.00384400    0.14510900
C       0.33909100   -0.50375100   -0.04499800
C      -0.86306900    0.32578500   -0.01405600
H       0.38020200   -1.39986000   -0.65104500
H      -1.75196200    0.04327900   -0.56467900
H      -0.75750400    1.38244000    0.20602700
H       1.55682600    0.70757200    0.79182200
""",
)

entry(
    index = 124,
    label = "[CH2]C(O)C=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {3,S} {7,S} {8,S}
5  C u0 p0 c0 {2,D} {3,S} {9,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74275,0.0239016,0.000149672,-7.09433e-07,8.9714e-10,-18101.3,10.7484], Tmin=(10,'K'), Tmax=(291.445,'K')),
            NASAPolynomial(coeffs=[5.47597,0.028286,-1.78905e-05,5.53232e-09,-6.60593e-13,-18322,2.47083], Tmin=(291.445,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-150.471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.20483500    1.69093900    0.17883600
O       1.30973300   -0.62833200   -1.85978200
C      -0.17291200    0.33991500   -0.22967100
C      -0.16154800   -0.60488500    0.91204800
C       1.15024000    0.15575000   -0.97103800
H      -0.97428600    0.09717200   -0.93438200
H      -0.43180000   -1.63825900    0.76198400
H       0.35230800   -0.31759400    1.81831300
H       1.96361800    0.79538600   -0.57996000
H      -0.90699500    1.79846000    0.82558000
""",
)

entry(
    index = 125,
    label = "C[C]CO",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
4  C u2 p0 c0 {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46216,0.0409233,-7.49912e-05,8.97193e-08,-4.0853e-11,16739.9,11.1219], Tmin=(10,'K'), Tmax=(706.767,'K')),
            NASAPolynomial(coeffs=[3.62216,0.0259396,-1.33119e-05,3.35607e-09,-3.35149e-13,17068.9,12.893], Tmin=(706.767,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (220.334,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 3
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -0.91073300    0.80282900    0.70773400
C      -1.04673500   -0.09622500   -0.39395400
C      -2.56952800   -1.99523100    0.71270300
C      -2.22550100   -0.96381700   -0.27443800
H      -1.07093300    0.45030200   -1.34199800
H      -0.12743900   -0.69253200   -0.38705100
H      -2.44947100   -1.61100000    1.73163700
H      -3.60173400   -2.32749400    0.59979000
H      -1.92602000   -2.87770800    0.61633200
H      -1.72818800    1.30369500    0.77628000
""",
)

entry(
    index = 126,
    label = "[O]OCC(O)C=O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {12,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {7,D}
4  O u1 p2 c0 {2,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
7  C u0 p0 c0 {3,D} {5,S} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69026,0.024961,0.000193643,-6.76853e-07,6.58488e-10,-36185.8,12.9326], Tmin=(10,'K'), Tmax=(367.467,'K')),
            NASAPolynomial(coeffs=[5.73644,0.0409847,-2.80941e-05,9.04151e-09,-1.10128e-12,-36594.7,1.59115], Tmin=(367.467,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-300.834,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (266.063,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.26911100   -1.33694600    0.00570900
O      -1.58470100    1.34232900    1.07597700
O      -2.07207700    0.09876600   -2.07904900
O      -1.54791400    2.08918600    2.13550400
C      -0.49604800   -0.23237000   -0.33735100
C      -0.31752700    0.70200900    0.84264300
C      -1.09811200    0.50922100   -1.51474800
H       0.51132400   -0.54382200   -0.65096000
H      -0.04508200    0.14334800    1.73515400
H       0.42097100    1.47932700    0.64251900
H      -0.58833600    1.43568500   -1.82989300
H      -2.01758500   -1.36219800   -0.60691200
""",
)

entry(
    index = 127,
    label = "O=[C]C(O)COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {5,S} {11,S}
3  O u0 p2 c0 {1,S} {12,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
7  C u1 p0 c0 {4,D} {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53797,0.0391682,0.000158615,-7.05745e-07,7.58524e-10,-33665.1,13.867], Tmin=(10,'K'), Tmax=(357.641,'K')),
            NASAPolynomial(coeffs=[8.16565,0.035094,-2.42903e-05,8.00025e-09,-9.96322e-13,-34301.1,-7.96405], Tmin=(357.641,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-279.864,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (261.906,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.50942800   -2.10215300    0.10498000
O      -1.07101900    0.06508500   -1.61345500
O      -2.47572600   -3.05188600    0.52210800
O       1.32191700   -0.39342600   -0.21874000
C      -1.04462100    0.15259700   -0.22284500
C      -1.99872200   -0.82127600    0.44825500
C       0.36495000   -0.07399300    0.37395400
H      -1.32842100    1.16811000    0.05411300
H      -3.00260900   -0.68764600    0.04453800
H      -2.00216600   -0.68347900    1.53219600
H      -0.83419300   -0.83507200   -1.86355700
H      -2.00197000   -3.50917000    1.22771500
""",
)

entry(
    index = 128,
    label = "O[CH]COO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {1,S} {10,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u1 p0 c0 {2,S} {4,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86955,0.0139442,0.000206789,-9.9238e-07,1.50769e-09,-19016.9,10.9566], Tmin=(10,'K'), Tmax=(212.563,'K')),
            NASAPolynomial(coeffs=[3.51395,0.0334506,-2.12923e-05,6.57716e-09,-7.821e-13,-19030.8,11.4405], Tmin=(212.563,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-158.06,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
O      -1.02003900   -0.57289500    0.71036600
O       1.69766100   -2.08080000    1.27893200
O      -0.78932900   -0.84789100    2.08850500
C      -0.31562300   -1.58725600   -0.02941900
C       1.14291900   -1.57412700    0.15061900
H      -0.73874200   -2.55556800    0.26109900
H      -0.58359900   -1.37615100   -1.06373400
H       1.83243400   -1.04757700   -0.48759300
H       0.99002600   -2.33484800    1.88281000
H      -0.18681600   -0.13291100    2.32859800
""",
)

entry(
    index = 129,
    label = "C=CC(=O)O[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {1,S}
4 C u0 p0 c0 {5,S} {6,D} {7,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 C u0 p0 c0 {4,D} {8,S} {9,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61345,0.0424015,-0.000133659,3.77706e-07,-3.94936e-10,-7992.75,9.59075], Tmin=(10,'K'), Tmax=(327.903,'K')),
            NASAPolynomial(coeffs=[2.99348,0.0341827,-2.38679e-05,7.70839e-09,-9.35509e-13,-7867.25,13.1842], Tmin=(327.903,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-66.4573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (199.547,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
O       1.51351300   -1.44163700   -0.50796200
O       1.20878100    0.81349900   -0.72605400
O       2.65329200   -1.28694000   -1.12083700
C      -0.46560300   -0.52791700    0.35814900
C       0.79550000   -0.22363200   -0.34125600
C      -1.31143900    0.45455900    0.62997800
H      -0.65003700   -1.55866000    0.62435700
H      -2.24525100    0.26942900    1.14128300
H      -1.07709000    1.47092700    0.34038100
""",
)

entry(
    index = 130,
    label = "C[C](C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5042,0.050478,-0.000180948,4.22334e-07,-3.2625e-10,4715.77,8.34714], Tmin=(10,'K'), Tmax=(464.945,'K')),
            NASAPolynomial(coeffs=[-0.275783,0.0421338,-2.21932e-05,5.66792e-09,-5.65999e-13,5508.95,28.4384], Tmin=(464.945,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.2073,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       1.35950800   -0.55743800   -0.15750100
C      -1.17082800   -0.90125900    0.00708500
C      -0.18154000    1.44748400    0.23513400
C       0.01835100   -0.02898800    0.21959500
H       2.16237000    0.02533700    0.29663100
H       1.51661600   -0.51927300   -1.24573500
H       1.47797600   -1.60027100    0.14071600
H      -2.03442200   -0.54644400    0.57167700
H      -0.96824400   -1.93333100    0.29728600
H      -1.47112900   -0.92273800   -1.05111700
H      -0.30237900    1.84894900   -0.78203500
H      -1.07852100    1.72471500    0.79105700
H       0.67234300    1.96315800    0.67720700
""",
)

entry(
    index = 131,
    label = "CC(C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93415,0.00375136,0.000118284,-1.93963e-07,1.0293e-10,-16864.6,7.76036], Tmin=(10,'K'), Tmax=(485.971,'K')),
            NASAPolynomial(coeffs=[-1.85113,0.0513696,-2.86953e-05,7.66617e-09,-7.94353e-13,-16302.3,31.4963], Tmin=(485.971,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-140.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (320.107,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.05298300    0.06162100   -0.40600400
C       0.48734700    1.32520400    0.32923800
C      -1.42356600   -0.22645500   -0.15560800
C       0.91201100   -1.12700300    0.01233500
H       0.19277300    0.22438600   -1.47846300
H      -0.10793100    2.18656700    0.02423800
H       1.53699000    1.55328400    0.14061900
H       0.36139500    1.19625000    1.40698300
H      -1.59952900   -0.39380500    0.90978500
H      -2.04999800    0.60897000   -0.47029000
H      -1.75072000   -1.11774100   -0.69220200
H       0.79547500   -1.31829400    1.08183700
H       1.96904600   -0.94015000   -0.18030000
H       0.62392400   -2.03283700   -0.52226700
""",
)

entry(
    index = 132,
    label = "CC[S]",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77363,0.0229221,-5.36731e-05,1.25603e-07,-1.01946e-10,10097,23.4235], Tmin=(10,'K'), Tmax=(454.26,'K')),
            NASAPolynomial(coeffs=[2.23813,0.0235423,-1.31218e-05,3.57245e-09,-3.8054e-13,10369.6,31.0848], Tmin=(454.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.9463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
S       1.68488600    1.16883300   -0.60505700
C      -0.81211800    0.03071200   -0.05065000
C       0.68816900   -0.14611800    0.11160300
H      -1.14232300    0.95499900    0.42057600
H      -1.08091700    0.07764800   -1.10466900
H      -1.34950300   -0.80150400    0.40628000
H       0.97542900   -0.20736000    1.16403300
H       1.03637600   -1.07710900   -0.34191500
""",
)

entry(
    index = 133,
    label = "CC=S",
    molecule = 
"""
1 S u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94225,0.00621594,2.22805e-05,-3.04939e-08,1.17522e-11,8530.96,7.84245], Tmin=(10,'K'), Tmax=(844.427,'K')),
            NASAPolynomial(coeffs=[2.28586,0.0193477,-1.0435e-05,2.74713e-09,-2.83598e-13,8622.26,14.4377], Tmin=(844.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.9342,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (153.818,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
S       1.88269100   -0.98351300   -0.43308800
C      -0.67720900   -0.03856700   -0.00453600
C       0.80353600    0.11513000    0.03374000
H      -0.96592800   -1.00962100   -0.39654000
H      -1.08570000    0.09109900    1.00094100
H      -1.11251900    0.75322700   -0.61955100
H       1.15523000    1.07234400    0.41903400
""",
)

entry(
    index = 134,
    label = "C=C[CH]C=C",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90109,0.00593522,0.000141782,-2.7649e-07,1.65269e-10,23541.3,8.90267], Tmin=(10,'K'), Tmax=(540.378,'K')),
            NASAPolynomial(coeffs=[1.35622,0.0463188,-3.0124e-05,9.37632e-09,-1.12035e-12,23501.7,16.7031], Tmin=(540.378,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (195.696,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.03467600    0.68150200    0.41681300
C      -1.21852900    0.03487200    0.43106500
C       1.00680100    0.47839400   -0.58420300
C      -2.16220800    0.21729600    1.38360400
C       2.21356200    1.09016200   -0.61359400
H      -1.42489800   -0.65281100   -0.38354700
H       0.26385600    1.37359200    1.22069300
H       0.75521600   -0.21867000   -1.37785200
H      -3.10784000   -0.30265000    1.34975700
H      -1.99386900    0.89410100    2.21121700
H       2.92476000    0.90064000   -1.40351300
H       2.50089200    1.79111300    0.15935400
""",
)

entry(
    index = 135,
    label = "C=CCC=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74127,0.0265361,1.2661e-05,-2.69801e-08,1.0087e-11,12002,11.6577], Tmin=(10,'K'), Tmax=(1007.47,'K')),
            NASAPolynomial(coeffs=[3.85804,0.0369961,-1.91765e-05,4.84979e-09,-4.82068e-13,11424.1,8.34223], Tmin=(1007.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.03034300   -0.38108100    0.67271700
C      -1.18524100   -0.58103200   -0.17681000
C       0.94722000    0.71283900    0.19393700
C      -2.43115500   -0.42485500    0.24081000
C       0.66283700    1.59794600   -0.74841000
H       0.60325900   -1.31346600    0.70782800
H      -0.26830800   -0.17404400    1.70423400
H      -1.00050300   -0.86951800   -1.20738900
H       1.91291000    0.75852500    0.68704300
H      -3.27437100   -0.58855300   -0.41629400
H      -2.64903400   -0.12795500    1.25996000
H       1.37550300    2.35978300   -1.03272500
H      -0.29200300    1.59649200   -1.25904400
""",
)

entry(
    index = 136,
    label = "[CH2]C(C)C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79673,0.0163221,7.07859e-05,-1.47603e-07,9.36767e-11,7599.23,9.9128], Tmin=(10,'K'), Tmax=(408.139,'K')),
            NASAPolynomial(coeffs=[1.17819,0.0419854,-2.35332e-05,6.46178e-09,-6.94218e-13,7812.98,20.1991], Tmin=(408.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.1513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.12847600   -0.13158700   -0.31032600
C      -0.99688600    1.04421700    0.13627100
C       1.35470200    0.17417200   -0.10374000
C      -0.52065600   -1.38502900    0.38964000
H      -0.28931800   -0.26882900   -1.39021300
H      -0.85042900    1.23513600    1.20104000
H      -0.73857500    1.95091600   -0.41136300
H      -2.05470600    0.83656200   -0.02674600
H       1.55839300    0.34434200    0.95508800
H       1.65005300    1.06695600   -0.65556400
H       1.97799200   -0.65552400   -0.43811700
H      -1.55011000   -1.56117900    0.66667700
H       0.17676000   -2.20539600    0.48022200
""",
)

entry(
    index = 137,
    label = "C=C(C)C",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89275,0.00763247,0.000103913,-2.25686e-07,1.61376e-10,-2846.58,7.84977], Tmin=(10,'K'), Tmax=(356.141,'K')),
            NASAPolynomial(coeffs=[1.2887,0.0368798,-1.92707e-05,4.90319e-09,-4.8962e-13,-2661.1,17.7243], Tmin=(356.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.6957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       1.37673200    0.03756900    0.22539300
C      -0.95298800    1.01924600    0.02195200
C      -0.07996800   -0.19950600   -0.04670300
C      -0.56238600   -1.40276300   -0.32831600
H       1.78674100    0.75726300   -0.48691100
H       1.95399400   -0.88243800    0.16051800
H       1.51511100    0.46640700    1.22057000
H      -0.61825000    1.77054600   -0.69702000
H      -1.99451600    0.78130300   -0.18417000
H      -0.88976100    1.47987500    1.01050700
H       0.08168600   -2.27145800   -0.37380000
H      -1.61619500   -1.55604400   -0.52202000
""",
)

entry(
    index = 138,
    label = "CS",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97468,0.00395663,1.50648e-05,-1.75497e-08,5.79674e-12,-3344.24,6.32934], Tmin=(10,'K'), Tmax=(994.074,'K')),
            NASAPolynomial(coeffs=[2.52117,0.0141989,-7.01975e-06,1.70721e-09,-1.6433e-13,-3272.35,12.2412], Tmin=(994.074,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.7971,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (128.874,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
S       1.13467000   -0.69390300   -0.37063900
C      -0.49479500    0.02965900   -0.02511800
H      -0.70601400    0.03058600    1.04000900
H      -0.57121400    1.03514900   -0.42792300
H      -1.22007700   -0.60569800   -0.52650900
H       1.85743000    0.20420800    0.31017900
""",
)

entry(
    index = 139,
    label = "[S]S",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99339,0.000376171,1.26896e-05,-2.18815e-08,1.17214e-11,12045.2,7.33225], Tmin=(10,'K'), Tmax=(573.311,'K')),
            NASAPolynomial(coeffs=[3.50177,0.00518351,-3.49173e-06,1.12513e-09,-1.38196e-13,12079,9.23312], Tmin=(573.311,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
S      -0.31572100    0.64748500    0.00000000
S       1.45266700   -0.22370900   -0.00000000
H      -1.13694600   -0.42377600    0.00000000
""",
)

entry(
    index = 140,
    label = "C=S",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05797,-0.00392813,2.83216e-05,-3.42697e-08,1.36322e-11,14463.2,4.79903], Tmin=(10,'K'), Tmax=(763.722,'K')),
            NASAPolynomial(coeffs=[2.23507,0.00937035,-5.16468e-06,1.39207e-09,-1.46654e-13,14632.2,12.3859], Tmin=(763.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
S       1.48052600   -0.14682100   -0.05645500
C      -0.11140400    0.01110800    0.00424800
H      -0.59374800    0.98503600    0.02447300
H      -0.77537400   -0.84922300    0.02773400
""",
)

entry(
    index = 141,
    label = "C=C=C",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06006,-0.0060188,9.79699e-05,-1.82759e-07,1.13683e-10,21210,4.87475], Tmin=(10,'K'), Tmax=(478.941,'K')),
            NASAPolynomial(coeffs=[1.58156,0.0220418,-1.29668e-05,3.74955e-09,-4.22622e-13,21363,14.1261], Tmin=(478.941,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (176.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       1.29911900    0.00666200    0.01345500
C      -1.29842800   -0.05328600    0.03107600
C       0.00034400   -0.02323600    0.02208200
H       1.84476500    0.67244100    0.66914900
H       1.86621800   -0.63357100   -0.64939300
H      -1.83508300   -0.72514500    0.68797500
H      -1.87453400    0.59286200   -0.61815900
""",
)

entry(
    index = 142,
    label = "C=CC(=C)C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89764,0.00600592,0.000143503,-2.71549e-07,1.57134e-10,8358.39,9.35652], Tmin=(10,'K'), Tmax=(560.405,'K')),
            NASAPolynomial(coeffs=[1.22014,0.0482044,-3.12429e-05,9.84637e-09,-1.193e-12,8295.95,17.4888], Tmin=(560.405,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.4536,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.79834100   -1.16833600    0.16234200
C      -0.45715300    0.28611600    0.02219000
C       0.95345900    0.65427100   -0.13924300
C      -1.39125300    1.23618800    0.04067100
C       1.96927000   -0.20225800   -0.17241800
H      -0.46513700   -1.72930300   -0.71258800
H      -0.29899800   -1.60017100    1.03149400
H      -1.87112700   -1.30683600    0.27479900
H       1.15178500    1.71660700   -0.23678800
H       2.98671000    0.14141100   -0.29463500
H       1.82049700   -1.27012300   -0.07919100
H      -2.43985400    0.99733900    0.15810300
H      -1.12794900    2.28116000   -0.06176200
""",
)

entry(
    index = 143,
    label = "[CH2]C(C=C)C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,D} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {9,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  C u0 p0 c0 {2,D} {12,S} {13,S}
6  C u0 p0 c0 {3,D} {14,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81901,0.0329744,1.01951e-05,-2.54681e-08,8.99237e-12,33472.8,14.2848], Tmin=(10,'K'), Tmax=(1146.18,'K')),
            NASAPolynomial(coeffs=[7.7333,0.0368462,-1.78162e-05,4.16978e-09,-3.82938e-13,31423.9,-10.1572], Tmin=(1146.18,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (278.355,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 2

Geometry:
C      -0.05510700    0.07562700   -0.36816300
C       1.22202800   -0.62154300    0.03235100
C      -1.10656100   -0.19821000    0.68494500
C       0.17340800    1.52541600   -0.62157300
C       1.76402000   -1.63787000   -0.61849400
C      -1.59228700    0.68498300    1.54314400
H      -0.40334700   -0.40058700   -1.29738100
H       1.69034500   -0.23489100    0.93292600
H      -1.43711400   -1.23063600    0.73397200
H      -0.66820800    2.19433200   -0.72355800
H       1.15070600    1.87807700   -0.91328500
H       1.30829200   -2.03744000   -1.51680200
H       2.67882700   -2.10409500   -0.27919300
H      -2.32400200    0.39687000    2.28539300
H      -1.27261200    1.71942000    1.53744900
""",
)

entry(
    index = 144,
    label = "C=CC(=C)C=C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {7,S}
3  C u0 p0 c0 {1,S} {6,D} {8,S}
4  C u0 p0 c0 {1,D} {11,S} {12,S}
5  C u0 p0 c0 {2,D} {9,S} {10,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59417,0.0351735,2.05692e-05,-6.10822e-08,3.21812e-11,21264.7,11.4498], Tmin=(10,'K'), Tmax=(692.951,'K')),
            NASAPolynomial(coeffs=[3.51718,0.0465033,-2.75189e-05,7.85124e-09,-8.669e-13,21014,9.90723], Tmin=(692.951,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (176.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 2

Geometry:
C       0.11823300   -0.45810200    0.63643700
C      -1.02408600    0.43194300    0.88165600
C       1.03870800   -0.13049600   -0.47055000
C       0.29798600   -1.54570700    1.38984500
C      -1.22501200    1.60115800    0.28359500
C       2.36022900   -0.20270100   -0.38961700
H      -1.73575300    0.08341600    1.62249600
H       0.57738600    0.19266100   -1.39810300
H      -2.08890700    2.20687400    0.51804600
H      -0.53037800    1.99540100   -0.44663800
H      -0.37432400   -1.77393700    2.20683400
H       1.11037900   -2.23324000    1.19942500
H       2.85064400   -0.47984400    0.53516500
H       2.98924900    0.02344700   -1.23954000
""",
)

entry(
    index = 145,
    label = "[NH2]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00627,-0.000314224,1.21046e-06,1.49873e-09,-1.36817e-12,22574.9,0.598701], Tmin=(10,'K'), Tmax=(786.392,'K')),
            NASAPolynomial(coeffs=[3.25204,0.0018732,1.83406e-07,-2.97057e-10,5.04139e-14,22744.5,4.38037], Tmin=(786.392,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (187.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
N      -0.00187900    0.42537000   -0.00000000
H      -0.80125100   -0.21615700    0.00000000
H       0.80313000   -0.20921300   -0.00000000
""",
)

entry(
    index = 146,
    label = "N",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01918,-0.00112743,6.86381e-06,-1.21552e-09,-2.25039e-12,-4870.57,0.27669], Tmin=(10,'K'), Tmax=(654.813,'K')),
            NASAPolynomial(coeffs=[2.40219,0.00564443,-1.53436e-06,9.15527e-11,1.59259e-14,-4592.22,7.9015], Tmin=(654.813,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.4891,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
N      -0.00062400    0.00141500    0.28825100
H       0.91533900   -0.20205300   -0.09315400
H      -0.63188300   -0.69251700   -0.09425400
H      -0.28283300    0.89315500   -0.10084300
""",
)

entry(
    index = 147,
    label = "[N]=N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01387,-0.000832898,4.73521e-06,-1.58648e-10,-2.53988e-12,29825.4,4.13247], Tmin=(10,'K'), Tmax=(615.272,'K')),
            NASAPolynomial(coeffs=[2.80141,0.00449459,-2.02416e-06,4.16295e-10,-3.11933e-14,30022.9,9.78599], Tmin=(615.272,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (247.987,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
N      -0.05643700    0.38171800    0.00000000
N       0.97538100   -0.15658600    0.00000000
H      -0.91884400   -0.22513200    0.00000000
""",
)

entry(
    index = 148,
    label = "[C]1=CC=CC=C1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u1 p0 c0 {4,S} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20972,-0.0176857,0.000201143,-3.24207e-07,1.68755e-10,38329.5,9.54366], Tmin=(10,'K'), Tmax=(610.271,'K')),
            NASAPolynomial(coeffs=[-0.851512,0.0457841,-2.93269e-05,8.90704e-09,-1.03108e-12,38383.1,26.8394], Tmin=(610.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (318.687,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 2
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.05301400    1.15561800   -0.00053100
C       1.18377900    0.52343800   -0.00640400
C      -1.22676600    0.41288400    0.00598400
C       1.25910700   -0.86914100   -0.00581100
C      -1.17427100   -0.98074400    0.00669400
C       0.07116900   -1.55175400    0.00073400
H       2.09322900    1.10999500   -0.01146000
H      -0.10259000    2.23574600   -0.00103500
H      -2.18606600    0.91375100    0.01053200
H       2.21444400   -1.37635900   -0.01033400
H      -2.07912200   -1.57333300    0.01173100
""",
)

entry(
    index = 149,
    label = "C1=CC=CC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,D} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {1,D} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15086,-0.0138972,0.000136831,4.30602e-09,-3.0163e-10,8502.49,7.26684], Tmin=(10,'K'), Tmax=(304.952,'K')),
            NASAPolynomial(coeffs=[-3.85266,0.0563248,-3.76055e-05,1.18808e-08,-1.42361e-12,9152.25,39.0241], Tmin=(304.952,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.6996,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C       0.79927700   -1.13486600    0.01481200
C       1.38256600    0.12470400   -0.00209600
C       0.58330400    1.25947900   -0.01689900
C      -0.79924300    1.13482800   -0.01479500
C      -1.38251600   -0.12466100    0.00211200
C      -0.58323400   -1.25952300    0.01691600
H       1.42206400   -2.01914900    0.02634700
H       2.45972800    0.22186900   -0.00373500
H       1.03785900    2.24088000   -0.03007300
H      -1.42198900    2.01913700   -0.02633100
H      -2.45977700   -0.22187000    0.00375200
H      -1.03783900   -2.24092800    0.03009000
""",
)

entry(
    index = 150,
    label = "C1#CC=CC=C1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {6,S} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16199,-0.0147476,0.000190547,-3.27896e-07,1.82018e-10,55684.4,8.74401], Tmin=(10,'K'), Tmax=(574.225,'K')),
            NASAPolynomial(coeffs=[0.232451,0.0404232,-2.6185e-05,8.03142e-09,-9.3787e-13,55677.4,21.5313], Tmin=(574.225,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (462.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Spin multiplicity: 1
External symmetry: -1.0
Optical isomers: 1

Geometry:
C      -0.74943600    0.68781300    0.15378000
C       0.64634000    0.78473300    0.21911600
C      -1.42001900   -0.54276400    0.10380400
C       1.48189000   -0.34128300    0.23968300
C       0.72321100   -1.49115700    0.18695400
C      -0.50841200   -1.57658500    0.12928200
H      -1.33512700    1.59820600    0.14128400
H       1.09949500    1.76724900    0.25523700
H      -2.49550400   -0.61851600    0.05343100
H       2.55756200   -0.26769600    0.29002900
""",
)

