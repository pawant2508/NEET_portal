import streamlit as st  # type: ignore
from firebase_admin import firestore  # type: ignore
import firebase_admin  # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

#questions for the mock test
questions = [
    {
        "question": "The minimum wavelength of X-rays produced by an electron accelerated through a potential difference of V volts is proportional to",
        "options": [
            "V",
            "1/V",
            "1/V^2",
            "V^2"
        ],
        "correct_answer": "1/V"
    },
    {
        "question": "A Carnot engine has an efficiency of 50% when its source is at a temperature 327°C. The temperature of the sink is",
        "options": [
            "27°C",
            "15°C",
            "100°C",
            "200°C"
        ],
        "correct_answer": "27°C"
    },
    {
        "question": "A bullet is fired from a gun at the speed of 280 m/s in the direction 30° above the horizontal. The maximum height attained by the bullet is (g = 9.8 m/s², sin30° = 0.5)",
        "options": [
            "2800 m",
            "2000 m",
            "1000 m",
            "3000 m"
        ],
        "correct_answer": "1000 m"
    },
    {
        "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 μF and resistance R is 100 Ω. The frequency at which resonance occurs is",
        "options": [
            "15.9 rad/s",
            "15.9 kHz",
            "1.59 rad/s",
            "1.59 kHz"
        ],
        "correct_answer": "1.59 kHz"
    },
    {
        "question": "Given below are two statements:\nStatement I: Photovoltaic devices can convert optical radiation into electricity.\nStatement II: Zener diode is designed to operate under reverse bias in breakdown region.\nIn the light of the above statements, choose the most appropriate answer from the options given below.",
        "options": [
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct"
        ],
        "correct_answer": "Both Statement I and Statement II are correct"
    },
    {
        "question": "Light travels a distance x in time t1 in air and 10x in time t2 in another denser medium. What is the critical angle for this medium?",
        "options": [
            "(1/2) * sin^(-1)(t1/t2)",
            "(1/10) * sin^(-1)(t1/t2)",
            "sin^(-1)(10 * t1/t2)",
            "(1/10) * sin^(-1)(t2/t1)"
        ],
        "correct_answer": "(1/10) * sin^(-1)(t2/t1)"
    },
    {
        "question": "In hydrogen spectrum, the shortest wavelength in the Balmer series is λ. The shortest wavelength in the Bracket series is",
        "options": [
            "2λ",
            "4λ",
            "9λ",
            "16λ"
        ],
        "correct_answer": "4λ"
    },
    {
        "question": "If the galvanometer G does not show any deflection in the circuit shown, the value of R is given by",
        "options": [
            "200 Ω",
            "50 Ω",
            "100 Ω",
            "400 Ω"
        ],
        "correct_answer": "100 Ω"
    },
    {
        "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
        "options": [
            "30.16 × 10⁻⁴ J",
            "5.06 × 10⁻⁴ J",
            "3.01 × 10⁻⁴ J",
            "50.1 × 10⁻⁴ J"
        ],
        "correct_answer": "3.01 × 10⁻⁴ J"
    },
    {
        "question": "The magnetic energy stored in an inductor of inductance 4 μH carrying a current of 2 A is",
        "options": [
            "4 μJ",
            "4 mJ",
            "8 mJ",
            "8 μJ"
        ],
        "correct_answer": "8 μJ"
    },
    {
        "question": "A 12 V, 60 W lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of 220 V. Assuming the transformer to be ideal, what is the current in the primary winding?",
        "options": [
            "0.27 A",
            "2.7 A",
            "3.7 A",
            "0.37 A"
        ],
        "correct_answer": "0.27 A"
    },
    {
        "question": "An electric dipole is placed at an angle of 30° with an electric field of intensity 2 × 10⁵ N C⁻¹. It experiences a torque equal to 4 N m. Calculate the magnitude of charge on the dipole, if the dipole length is 2 cm.",
        "options": [
            "8 mC",
            "6 mC",
            "4 mC",
            "2 mC"
        ],
        "correct_answer": "2 mC"
    },
    {
        "question": "A vehicle travels half the distance with speed v and the remaining distance with speed 2v. Its average speed is",
        "options": [
            "3v",
            "2/3v",
            "4/3v",
            "3/4v"
        ],
        "correct_answer": "4/3v"
    },
    {
        "question": "If ∮sE dS = ∫ over a surface, then",
        "options": [
            "The number of flux lines entering the surface must be equal to the number of flux lines leaving it",
            "The magnitude of electric field on the surface is constant",
            "All the charges must necessarily be inside the surface",
            "The electric field inside the surface is necessarily uniform"
        ],
        "correct_answer": "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
    },
    {
        "question": "The work functions of Caesium (Cs), Potassium (K), and Sodium (Na) are 2.14 eV, 2.30 eV, and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
        "options": [
            "Cs only",
            "Both Na and K",
            "K only",
            "Na only"
        ],
        "correct_answer": "Cs only"
    },
    {
        "question": "The temperature of a gas is –50°C. To what temperature the gas should be heated so that the rms speed is increased by 3 times?",
        "options": [
            "669°C",
            "3295°C",
            "3097 K",
            "223 K"
        ],
        "correct_answer": "3295°C"
    },
    {
        "question": "The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is",
        "options": [
            "1 : 2",
            "2 : 1",
            "1 : 3",
            "3 : 1"
        ],
        "correct_answer": "2 : 1"
    },
    {
        "question": "Resistance of a carbon resistor determined from color codes is (22000 ± 5%) Ω. The color of the third band must be",
        "options": [
            "Red",
            "Green",
            "Orange",
            "Yellow"
        ],
        "correct_answer": "Orange"
    },
    {
        "question": "Resistance of a carbon resistor determined from color codes is (22000 ± 5%) Ω. The color of the third band must be",
        "options": [
            "Red",
            "Green",
            "Orange",
            "Yellow"
        ],
        "correct_answer": "Orange"
    },
    {
        "question": "A metal wire has mass, radius, and length. The maximum possible percentage error in the measurement of density will nearly be",
        "options": [
            "1.2%",
            "1.3%",
            "1.6%",
            "1.4%"
        ],
        "correct_answer": "1.6%"
    },
    {
        "question": "The equivalent capacitance of the system shown in the following circuit is",
        "options": [
            "2 μF",
            "3 μF",
            "6 μF",
            "9 μF"
        ],
        "correct_answer": "2 μF"
    },
    {
        "question": "Two bodies of mass m and 9m are placed at a distance R. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be (G = gravitational constant)",
        "options": [
            "8Gm/R",
            "12Gm/R",
            "16Gm/R",
            "20Gm/R"
        ],
        "correct_answer": "16Gm/R"
    },
    {
        "question": "The venturi-meter works on",
        "options": [
            "Huygen’s principle",
            "Bernoulli’s principle",
            "The principle of parallel axes",
            "The principle of perpendicular axes"
        ],
        "correct_answer": "Bernoulli’s principle"
    },
    {
        "question": "The half life of a radioactive substance is 20 minutes. In how much time, the activity of substance drops to 1/16 of its initial value?",
        "options": [
            "20 minutes",
            "40 minutes",
            "60 minutes",
            "80 minutes"
        ],
        "correct_answer": "80 minutes"
    },
    {
        "question": "A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is",
        "options": [
            "Along eastward",
            "Along northward",
            "Along north-east",
            "Along south-west"
        ],
        "correct_answer": "Along north-east"
    },
    {
        "question": "The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are",
        "options": [
            "Instrumental errors",
            "Personal errors",
            "Least count errors",
            "Random errors"
        ],
        "correct_answer": "Random errors"
    },
    {
        "question": "The angular acceleration of a body, moving along the circumference of a circle, is",
        "options": [
            "Along the radius, away from centre",
            "Along the radius towards the centre",
            "Along the tangent to its position",
            "Along the axis of rotation"
        ],
        "correct_answer": "Along the tangent to its position"
    },
    {
        "question": "A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?",
        "options": [
            "A centre-tapped transformer",
            "p-n junction diodes",
            "Capacitor",
            "Load resistance"
        ],
        "correct_answer": "Capacitor"
    },
    {
        "question": "The ratio of radius of gyration of a solid sphere of mass M and radius R about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is",
        "options": [
            "3 : 5",
            "5 : 3",
            "2 : 5",
            "5 : 2"
        ],
        "correct_answer": "3 : 5"
    },
    {
        "question": "The magnitude and direction of the current in the following circuit is",
        "options": [
            "0.2 A from B to A through E",
            "0.5 A from A to B through E",
            "5/9 A from A to B through E",
            "1.5 A from B to A through E"
        ],
        "correct_answer": "0.5 A from A to B through E"
    },
    {
        "question": "An ac source is connected to a capacitor C. Due to decrease in its operating frequency",
        "options": [
            "Capacitive reactance decreases",
            "Displacement current increases",
            "Displacement current decreases",
            "Capacitive reactance remains constant"
        ],
        "correct_answer": "Displacement current decreases"
    },
    {
        "question": "The net magnetic flux through any closed surface is",
        "options": [
            "Zero",
            "Positive",
            "Infinity",
            "Negative"
        ],
        "correct_answer": "Zero"
    },
    {
        "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 10^10 Hz and amplitude 48 V m^-1. Then the amplitude of oscillating magnetic field is",
        "options": [
            "1.6 × 10^–9 T",
            "1.6 × 10^–8 T",
            "1.6 × 10^–7 T",
            "1.6 × 10^–6 T"
        ],
        "correct_answer": "1.6 × 10^–7 T"
    },
    {
        "question": "The potential energy of a long spring when stretched by 2 cm is U. If the spring is stretched by 8 cm, potential energy stored in it will be",
        "options": [
            "2 U",
            "4 U",
            "8 U",
            "16 U"
        ],
        "correct_answer": "16 U"
    },
     {
        "question": "A bullet from a gun is fired on a rectangular wooden block with velocity u. When bullet travels 24 cm through the block along its length horizontally, velocity of bullet becomes 3u. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is",
        "options": [
            "(1) 27 cm",
            "(2) 24 cm",
            "(3) 28 cm",
            "(4) 30 cm"
        ],
        "correct_answer": "(1) 27 cm"
    },
    {
        "question": "A satellite is orbiting just above the surface of the earth with period T. If d is the density of the earth and G is the universal constant of gravitation, the quantity 3Gdπ represents",
        "options": [
            "(1) T",
            "(2) T^2",
            "(3) T^3",
            "(4) T"
        ],
        "correct_answer": "(2) T^2"
    },
    {
        "question": "The radius of innermost orbit of hydrogen atom is 5.3 × 10–11 m. What is the radius of third allowed orbit of hydrogen atom?",
        "options": [
            "(1) 0.53 Å",
            "(2) 1.06 Å",
            "(3) 1.59 Å",
            "(4) 4.77 Å"
        ],
        "correct_answer": "(4) 4.77 Å"
    },
    {
        "question": "The net impedance of circuit (as shown in figure) will be",
        "options": [
            "(1) 10Ω",
            "(2) 15Ω",
            "(3) 5Ω",
            "(4) 25Ω"
        ],
        "correct_answer": "(3) 5Ω"
    },
    {
        "question": "The x-t graph of a particle performing simple harmonic motion is shown in the figure. The acceleration of the particle at t = 2 s is",
        "options": [
            "(1) 2^-2 m/s^8π",
            "(2) 2^-2 m/s^8π",
            "(3) 2^-2 m/s^16π",
            "(4) 2^-2 m/s^16π"
        ],
        "correct_answer": "(4) 2^-2 m/s^16π"
    },
    {
        "question": "In the figure shown here, what is the equivalent focal length of the combination of lenses (Assume that all layers are thin)?",
        "options": [
            "40 cm",
            "-40 cm",
            "-100 cm",
            "-50 cm"
        ],
        "correct_answer": "-100 cm"
    },
    {
        "question": "An electric dipole is placed as shown in the figure. The electric potential (in 10^2 V) at point P due to the dipole is (ε₀ = permittivity of free space and K = 1/4πε₀):",
        "options": [
            "3/8 * (qK)",
            "5/8 * (qK)",
            "8/5 * (qK)",
            "8/3 * (qK)"
        ],
        "correct_answer": "3/8 * (qK)"
    },
    {
        "question": "A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity 4 m/s. The ball strikes the water surface after 4 s. The height of bridge above water surface is (Take g = 10 m/s²):",
        "options": [
            "56 m",
            "60 m",
            "64 m",
            "68 m"
        ],
        "correct_answer": "64 m"
    },
   {
        "question": "Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is 0.15 (g = 10 m/s²):",
        "options": [
            "1.2 m/s²",
            "150 m/s²",
            "1.5 m/s²",
            "50 m/s²"
        ],
        "correct_answer": "(3) 1.5 m/s²"
    },
    {
        "question": "10 resistors, each of resistance R are connected in series to a battery of emf E and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased n times. The value of n is:",
        "options": [
            "10",
            "100",
            "1",
            "1000"
        ],
        "correct_answer": "(2) 100"
    },
    {
        "question": "For the following logic circuit, the truth table is",
        "options": [
            "0 0 1\n0 1 1\n1 0 1\n1 1 0\nA B Y",
            "000\n0 1 1\n1 0 1\n111\nA B Y",
            "0 0 1\n0 1 0\n1 0 1\n1 1 0\nA B Y",
            "000\n0 1 0\n1 0 0\n111\nA B Y"
        ],
        "correct_answer": "(2) 000\n0 1 1\n1 0 1\n111\nA B Y"
    },
    {
        "question": "A very long conducting wire is bent in a semi-circular shape from A to B as shown in figure. The magnetic field at point P for steady current configuration is given by",
        "options": [
            "0\n4iRμ pointed into the page",
            "0\n4iRμ pointed away from the page",
            "0 2\n1\n4iRμ [− π] pointed away from page",
            "0 2\n1\n4iRμ [− π] pointed into the page"
        ],
        "correct_answer": "(3) 0 2\n1\n4iRμ [− π] pointed away from page"
    },
    {
        "question": "The resistance of platinum wire at 0°C is 2 Ω and 6.8 Ω at 80°C. The temperature coefficient of resistance of the wire is",
        "options": [
            "3 × 10⁻⁴ °C⁻¹",
            "3 × 10⁻³ °C⁻¹",
            "3 × 10⁻² °C⁻¹",
            "3 × 10⁻¹ °C⁻¹"
        ],
        "correct_answer": "(3) 3 × 10⁻² °C⁻¹"
    },
    {
        "question": "A wire carrying a current I along the positive x-axis has length L. It is kept in a magnetic field B = (2i + 3j – 4k) T. The magnitude of the magnetic force acting on the wire is",
        "options": [
            "3 lL",
            "5 lL",
            "5 lL",
            "3 lL"
        ],
        "correct_answer": "(3) 5 lL"
    },
    {
        "question": "Two thin lenses are of same focal lengths (f), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be",
        "options": [
            "Zero",
            "4f",
            "2f",
            "Infinite"
        ],
        "correct_answer": "(4) Infinite"
    },
    {
        "question": "Select the correct statements from the following",
        "options": [
            "Atoms of all elements are composed of two fundamental particles.",
            "The mass of the electron is 9.10939 × 10–31 kg.",
            "All the isotopes of a given element show same chemical properties.",
            "Protons and electrons are collectively known as nucleons.",
            "Dalton’s atomic theory, regarded the atom as an ultimate particle of matter."
        ],
        "correct_answer": "(4) B, C and E only"
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R:",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true and R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": ""
    },
    {
    "question": "Amongst the following the total number of species NOT having eight electrons around central atom in its outermost shell, is",
    "options": [
        "3",
        "2",
        "4",
        "1"
    ],
    "correct_answer": "3"
    },
    {
    "question": "Which amongst the following molecules on polymerization produces neoprene?",
    "options": [
        "H C CH – CH CH 2 2  ",
        "2 2 Cl | H C C– CH CH  ",
        "H C CH – C CH 2  ",
        "| 2 2 CH3 H C C – CH CH  "
    ],
    "correct_answer": "(2) 2 2 Cl | H C C– CH CH  "
    },
    {
    "question": "In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with Fe3+ due to the formation of",
    "options": [
        "Fe4[Fe(CN)6]3xH2O",
        "NaSCN",
        "[Fe(CN)5NOS]4–",
        "[Fe(SCN)]2+"
    ],
    "correct_answer": "[Fe(SCN)]2+"
    },
    {
        "question": "Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is:",
        "options": [
            "16",
            "32",
            "30",
            "18"
        ],
        "correct_answer": "32"
    },
    {
        "question": "Some tranquilizers are listed below. Which one from the following belongs to barbiturates?",
        "options": [
            "Chlordiazepoxide",
            "Meprobamate",
            "Valium",
            "Veronal"
        ],
        "correct_answer": "Veronal"
    },
    {
        "question": "The conductivity of centimolar solution of KCl at 25°C is 0.0210 ohm–1 cm–1 and the resistance of the cell containing the solution at 25°C is 60 ohm. The value of cell constant is",
        "options": [
            "1.34 cm–1",
            "3.28 cm–1",
            "1.26 cm–1",
            "3.34 cm–1"
        ],
        "correct_answer": "1.26 cm–1"
    },
    {
        "question": "Complete the following reaction [C] is",
        "options": [
            "(2)",
            "(3)",
            "(4)",
            "(1)"
        ],
        "correct_answer": "(1)"
    },
    {
        "question": "Homoleptic complex from the following complexes is",
        "options": [
            "Potassium trioxalatoaluminate (III)",
            "Diamminechloridonitrito-N-platinum (II)",
            "Pentaamminecarbonatocobalt (III) chloride",
            "Triamminetriaquachromium (III) chloride"
        ],
        "correct_answer": "Potassium trioxalatoaluminate (III)"
    },
    {
    "question": "The relation between nm, (nm = the number of permissible values of magnetic quantum number (m)) for a given value of azimuthal quantum number (l), is",
    "options": [
        "n – 1 m 2 l =",
        "l = 2nm + 1",
        "nm = 2l 2 + 1",
        "nm = l + 2"
    ],
    "correct_answer": "n – 1 m 2 l ="
    },
    {
        "question": "The stability of Cu2+ is more than Cu+ salts in aqueous solution due to",
        "options": [
            "First ionisation enthalpy",
            "Enthalpy of atomization",
            "Hydration energy",
            "Second ionisation enthalpy"
        ],
        "correct_answer": "Hydration energy"
    },
    {
        "question": "Taking stability as the factor, which one of the following represents correct relationship?",
        "options": [
            "TCI3 > TCI",
            "nI3 > InI",
            "AlCl > AlCl3",
            "TI > TI3"
        ],
        "correct_answer": "TI > TI3"
    },
    {
        "question": "Which one is an example of heterogenous catalysis?",
        "options": [
            "Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen",
            "Hydrolysis of sugar catalysed by H+ ions",
            "Decomposition of ozone in presence of nitrogen monoxide",
            "Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron"
        ],
        "correct_answer": "Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron"
    },
    {
        "question": "The number of  bonds,  bonds and lone pair of electrons in pyridine, respectively are:",
        "options": [
            "11, 2, 0",
            "12, 3, 0",
            "11, 3, 1",
            "12, 2, 1"
        ],
        "correct_answer": "11, 3, 1"
    },
    {
    "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R Assertion A : Helium is used to dilute oxygen in diving apparatus. Reason R : Helium has high solubility in O2. In the light of the above statements, choose the correct answer from the options given below",
    "options": [
        "Both A and R are true and R is the correct explanation of A",
        "Both A and R are true and R is NOT the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true"
    ],
    "correct_answer": "Both A and R are true and R is NOT the correct explanation of A"
    },
    {
        "question": "Amongst the given options which of the following molecules/ion acts as a Lewis acid?",
        "options": [
            "NH3",
            "H2O",
            "BF3",
            "OH–"
        ],
        "correct_answer": "BF3"
    },
    {
        "question": "The element expected to form the largest ion to achieve the nearest noble gas configuration is",
        "options": [
            "O",
            "F",
            "N",
            "Na"
        ],
        "correct_answer": "N"
    },
    {
        "question": "The given compound is an example of ______.",
        "options": [
            "Benzylic halide",
            "Aryl halide",
            "Allylic halide",
            "Vinylic halide"
        ],
        "correct_answer": "Allylic halide"
    },
    {
        "question": "Given below are two statements:\nStatement I: A unit formed by the attachment of a base to 1’ position of sugar is known as nucleoside.\nStatement II: When nucleoside is linked to phosphorous acid at 5’-position of sugar moiety, we get nucleotide.\nIn the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true",
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true"
        ],
        "correct_answer": "Statement I is true but Statement II is false"
    },
    {
        "question": "Intermolecular forces are forces of attraction and repulsion between interacting particles that will include:",
        "options": [
            "dipole-dipole forces",
            "dipole-induced dipole forces",
            "hydrogen bonding",
            "covalent bonding",
            "dispersion forces"
        ],
        "correct_answer": "A, B, C, E are correct"
    },
    {
        "question": "Which of the following statements are NOT correct?",
        "options": [
            "Hydrogen is used to reduce heavy metal oxides to metals.",
            "Heavy water is used to study reaction mechanism.",
            "Hydrogen is used to make saturated fats from oils.",
            "The H–H bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements.",
            "Hydrogen reduces oxides of metals that are more active than iron."
        ],
        "correct_answer": "D, E only"
    },
    {
        "question": "Which one of the following statements is correct?",
        "options": [
            "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g",
            "All enzymes that utilize ATP in phosphate transfer require Ca as the cofactor",
            "The bone in the human body is an inert and unchanging substance",
            "Mg plays roles in neuromuscular function and interneuronal transmission"
        ],
        "correct_answer": "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g"
    },
    {
        "question": "Match List-I with List-II.",
        "options": [
            "A. Coke – Carbon atoms are sp3 hybridised",
            "B. Diamond – Used as a dry lubricant",
            "C. Fullerene – Cage like molecules",
            "D. Graphite – Used as a reducing agent"
        ],
        "correct_answer": "A-III, B-I, C-IV, D-II"
    },
    {
        "question": "The right option for the mass of CO2 produced by heating 20 g of 20% pure limestone is (Atomic mass of Ca = 40)",
        "options": [
            "1.12 g",
            "1.76 g",
            "2.64 g",
            "1.32 g"
        ],
        "correct_answer": "1.76 g"
    },
    {
      "question": "The ratio of radius of gyration of a solid sphere of mass M and radius R about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is",
      "options": [
        "(1) 5 : 3",
        "(2) 2 : 5",
        "(3) 5 : 2",
        "(4) 3 : 5"
      ],
      "correct_answer": "(1) 5 : 3"
    },
    {
      "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
      "options": [
        "(1) Both Na and K",
        "(2) K only",
        "(3) Na only",
        "(4) Cs only"
      ],
      "correct_answer": "(2) K only"
    },
    {
      "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
      "options": [
        "(1) 5.06 × 10–4 J",
        "(2) 3.01 × 10–4 J",
        "(3) 50.1 × 10–4 J",
        "(4) 30.16 × 10–4 J"
      ],
      "correct_answer": "(2) 3.01 × 10–4 J"
    },
    {
      "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 μF and resistance R is 100 Ω. The frequency at which resonance occurs is",
      "options": [
        "(1) 15.9 kHz",
        "(2) 1.59 rad/s",
        "(3) 1.59 kHz",
        "(4) 15.9 rad/s"
      ],
      "correct_answer": "(3) 1.59 kHz"
    },
    {
      "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 1010 Hz and amplitude 48 V m–1. Then the amplitude of oscillating magnetic field is (Speed of light in free space = 3 × 108 m s–1)",
      "options": [
        "(1) 1.6 × 10–8 T",
        "(2) 1.6 × 10–7 T",
        "(3) 1.6 × 10–6 T",
        "(4) 1.6 × 10–9 T"
      ],
      "correct_answer": "(2) 1.6 × 10–7 T"
    },
    {
      "question": "Given below are two statements:\nStatement I: Photovoltaic devices can convert optical radiation into electricity.\nStatement II: Zener diode is designed to operate under reverse bias in breakdown region.\nIn the light of the above statements, choose the most appropriate answer from the options given below.",
      "options": [
        "(1) Both Statement I and Statement II are incorrect",
        "(2) Statement I is correct but Statement II is incorrect",
        "(3) Statement I is incorrect but Statement II is correct",
        "(4) Both Statement I and Statement II are correct"
      ],
      "correct_answer": "(4) Both Statement I and Statement II are correct"
    },
    {
      "question": "The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are",
      "options": [
        "(1) Personal errors",
        "(2) Least count errors",
        "(3) Random errors",
        "(4) Instrumental errors"
      ],
      "correct_answer": "(3) Random errors"
    },
    {
      "question": "If ∫ E ⋅dS = 0 over a surface, then",
      "options": [
        "The magnitude of electric field on the surface is constant",
        "All the charges must necessarily be inside the surface",
        "The electric field inside the surface is necessarily uniform",
        "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
      ],
      "correct_answer": "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
    },
    {
      "question": "An ac source is connected to a capacitor C. Due to decrease in its operating frequency",
      "options": [
        "Displacement current increases",
        "Displacement current decreases",
        "Capacitive reactance remains constant",
        "Capacitive reactance decreases"
      ],
      "correct_answer": "Capacitive reactance decreases"
    },
    {
      "question": "The minimum wavelength of X-rays produced by an electron accelerated through a potential difference of V volts is proportional to",
      "options": [
        "1/V",
        "1/V",
        "V^2",
        "V"
      ],
      "correct_answer": "1/V"
    },
    {
      "question": "The venturi-meter works on",
      "options": [
        "Bernoulli’s principle",
        "The principle of parallel axes",
        "The principle of perpendicular axes",
        "Huygens’s principle"
      ],
      "correct_answer": "Bernoulli’s principle"
    },
    {
      "question": "A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?",
      "options": [
        "p-n junction diodes",
        "Capacitor",
        "Load resistance",
        "A centre-tapped transformer"
      ],
      "correct_answer": "Capacitor"
    },
{
"question": "A variable force F = 5kx N acts on a body moving along the x-axis. What will be the work done by this force in displacing the body from x = 2 m to x = 5 m? (Where k is a constant)",
"options": [
"(205/2 k) J",
"(105/2 k) J",
"(52k) J",
"(51k) J"
],
"correct_answer": "(105/2 k) J"
},

{
"question": "A northbound cart is moving at 5 m/s when it collides with a southbound cart, moving at 1 m/s. If the northbound cart is twice as heavy as the southbound cart, what is their final velocity after they collide and become stuck together?",
"options": [
"2 m/s north",
"3 m/s north",
"2 m/s south",
"3 m/s south"
],
"correct_answer": "2 m/s north"
},

{
"question": "If an electrical generator plant increases its daily amount of output energy by 100%, the plant's average output power increases by:",
"options": [
"25%",
"50%",
"100%",
"200%"
],
"correct_answer": "100%"
},
 {
      "question": "The venturi-meter works on",
      "options": [
        "Bernoulli’s principle",
        "The principle of parallel axes",
        "The principle of perpendicular axes",
        "Huygens’s principle"
      ],
      "correct_answer": "Bernoulli’s principle"
    },
    {
      "question": "A full wave rectifier circuit consists of two p-n junction diodes, a centre-tapped transformer, capacitor and a load resistance. Which of these components remove the ac ripple from the rectified output?",
      "options": [
        "p-n junction diodes",
        "Capacitor",
        "Load resistance",
        "A centre-tapped transformer"
      ],
      "correct_answer": "Capacitor"
    },
{
      "question": "What is the SI unit of electric charge?",
      "options": ["Coulomb", "Ampere", "Ohm", "Volt"],
      "correct_answer": "Coulomb"
    },
    {
      "question": "Which of the following is not a fundamental force?",
      "options": ["Gravitational force", "Electromagnetic force", "Nuclear force", "Frictional force"],
      "correct_answer": "Frictional force"
    },
    {
      "question": "What is the unit of measurement for frequency?",
      "options": ["Hertz", "Newton", "Pascal", "Joule"],
      "correct_answer": "Hertz"
    },
{
      "question": "What is the chemical symbol for gold?",
      "options": ["Ag", "Au", "Fe", "Hg"],
      "correct_answer": "Au"
    },
    {
      "question": "Which gas is used in the process of respiration?",
      "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"],
      "correct_answer": "Oxygen"
    },
    {
      "question": "What is the pH of a neutral solution?",
      "options": ["7", "0", "14", "1"],
      "correct_answer": "7"
    },
{
      "question": "What is the powerhouse of the cell?",
      "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"],
      "correct_answer": "Mitochondria"
    },
    {
      "question": "Which of the following is not a type of blood cell?",
      "options": ["Erythrocyte", "Leukocyte", "Thrombocyte", "Melanocyte"],
      "correct_answer": "Melanocyte"
    },
    {
      "question": "What is the largest organ in the human body?",
      "options": ["Brain", "Skin", "Liver", "Heart"],
      "correct_answer": "Skin"
    },
{
      "question": "What is the SI unit of electric charge?",
      "options": ["Coulomb", "Ampere", "Volt", "Ohm"],
      "correct_answer": "Coulomb"
    },
    {
      "question": "Which of the following is an example of a vector quantity?",
      "options": ["Temperature", "Mass", "Distance", "Velocity"],
      "correct_answer": "Velocity"
    },
    {
      "question": "What is the formula to calculate kinetic energy?",
      "options": ["mv^2", "1/2mv^2", "mgh", "mg"],
      "correct_answer": "1/2mv^2"
    },
{
      "question": "Which of the following is a noble gas?",
      "options": ["Nitrogen", "Oxygen", "Argon", "Hydrogen"],
      "correct_answer": "Argon"
    },
    {
      "question": "What is the chemical symbol for gold?",
      "options": ["Au", "Ag", "G", "Go"],
      "correct_answer": "Au"
    },
    {
      "question": "What is the chemical formula for table salt?",
      "options": ["NaCl", "HCl", "H2SO4", "CaCO3"],
      "correct_answer": "NaCl"
    },
 {
      "question": "Which organelle is known as the 'powerhouse of the cell'?",
      "options": ["Nucleus", "Mitochondria", "Golgi Apparatus", "Endoplasmic Reticulum"],
      "correct_answer": "Mitochondria"
    },
    {
      "question": "Which blood vessels carry blood away from the heart?",
      "options": ["Veins", "Arteries", "Capillaries", "Venules"],
      "correct_answer": "Arteries"
    },
    {
      "question": "What is the primary function of the kidneys?",
      "options": ["Digestion", "Respiration", "Filtration", "Circulation"],
      "correct_answer": "Filtration"
    },
{
"question": "The element expected to form largest ion to achieve the nearest noble gas configuration is",
"options": [
"F",
"N",
"Na",
"O"
],
"correct_answer": "Na"
},
{
"question": "Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is:",
"options": [
"32",
"30",
"18",
"16"
],
"correct_answer": "32"
},
{
      "question": "A body of mass 5 kg is acted upon by a constant force of 20 N for a duration of 2 s. The change in momentum of the body will be?",
      "options": {
        "a": "40 kg m/s",
        "b": "10 kg m/s",
        "c": "20 kg m/s",
        "d": "5 kg m/s"
      },
      "correct_answer": "c"
    },
    {
      "question": "Which of the following is a vector quantity?",
      "options": {
        "a": "Speed",
        "b": "Distance",
        "c": "Velocity",
        "d": "Mass"
      },
      "correct_answer": "c"
    },
    {
      "question": "The phenomenon of splitting of white light into its constituent colours on passing through a glass prism is called?",
      "options": {
        "a": "Reflection",
        "b": "Refraction",
        "c": "Dispersion",
        "d": "Diffraction"
      },
      "correct_answer": "c"
    },
 {
      "question": "The number of moles of solute present in 1 kg of a solvent is called its?",
      "options": {
        "a": "Molality",
        "b": "Molarity",
        "c": "Normality",
        "d": "Mole fraction"
      },
      "correct_answer": "a"
    },
    {
      "question": "Which of the following is not an allotrope of carbon?",
      "options": {
        "a": "Diamond",
        "b": "Graphite",
        "c": "Buckminsterfullerene",
        "d": "Silica"
      },
      "correct_answer": "d"
    },
    {
      "question": "The process of conversion of vapour into liquid is called?",
      "options": {
        "a": "Evaporation",
        "b": "Condensation",
        "c": "Sublimation",
        "d": "Fusion"
      },
      "correct_answer": "b"
    },
{
      "question": "Which of the following is not a function of the liver?",
      "options": {
        "a": "Detoxification",
        "b": "Carbohydrate metabolism",
        "c": "Blood clotting",
        "d": "Hormone production"
      },
      "correct_answer": "d"
    },
    {
      "question": "Which of the following is the largest gland in the human body?",
      "options": {
        "a": "Pancreas",
        "b": "Thyroid gland",
        "c": "Liver",
        "d": "Pituitary gland"
      },
      "correct_answer": "c"
    },
    {
      "question": "Which of the following is the powerhouse of the cell?",
      "options": {
        "a": "Nucleus",
        "b": "Mitochondria",
        "c": "Ribosome",
        "d": "Endoplasmic reticulum"
      },
      "correct_answer": "b"
    },
{
      "question": "What is the SI unit of electric charge?",
      "options": ["A) Ampere", "B) Coulomb", "C) Volt", "D) Ohm"],
      "correct_answer": "B) Coulomb"
    },
    {
      "question": "Which of the following is NOT a vector quantity?",
      "options": ["A) Force", "B) Velocity", "C) Energy", "D) Displacement"],
      "correct_answer": "C) Energy"
    },
    {
      "question": "What is the work done when a force of 10 N moves a body through a distance of 5 m in its direction?",
      "options": ["A) 10 J", "B) 15 J", "C) 50 J", "D) 100 J"],
      "correct_answer": "C) 50 J"
    },
{
      "question": "Which of the following elements is a metalloid?",
      "options": ["A) Sodium", "B) Silicon", "C) Chlorine", "D) Iron"],
      "correct_answer": "B) Silicon"
    },
    {
      "question": "The pH of a neutral solution is:",
      "options": ["A) 0", "B) 7", "C) 14", "D) -7"],
      "correct_answer": "B) 7"
    },
{
      "question": "Which of the following is NOT a greenhouse gas?",
      "options": ["A) Carbon dioxide", "B) Methane", "C) Nitrous oxide", "D) Oxygen"],
      "correct_answer": "D) Oxygen"
    },
{
      "question": "What is the primary function of the mitochondria?",
      "options": ["A) Protein synthesis", "B) Cell division", "C) Energy production", "D) Storage of genetic material"],
      "correct_answer": "Energy production"
    },
    {
      "question": "Which organelle is responsible for detoxifying harmful substances in a cell?",
      "options": ["A) Nucleus", "B) Golgi apparatus", "C) Lysosome", "D) Peroxisome"],
      "correct_answer": "Peroxisome"
    },
    {
      "question": "Which of the following is NOT a function of the liver?",
      "options": ["A) Carbohydrate metabolism", "B) Blood filtration", "C) Detoxification", "D) Protein synthesis"],
      "correct_answer": "Blood filtration"
    },
 {
      "question": "What is the SI unit of force?",
      "options": ["Newton", "Joule", "Watt", "Pascal"],
      "correct_answer": "Newton"
    },
    {
      "question": "Which of the following is not a vector quantity?",
      "options": ["Velocity", "Acceleration", "Temperature", "Force"],
      "correct_answer": "Temperature"
    },
{
      "question": "Which element has the atomic number 6?",
      "options": ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
      "correct_answer": "Carbon"
    },
    {
      "question": "Which gas is known as laughing gas?",
      "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Nitrous Oxide"],
      "correct_answer": "Nitrous Oxide"
    },
 {
      "question": "Which part of the human brain is responsible for regulating body temperature?",
      "options": ["Cerebellum", "Hypothalamus", "Medulla Oblongata", "Cerebrum"],
      "correct_answer": "Hypothalamus"
    },
    {
      "question": "Which blood vessel carries deoxygenated blood from the heart to the lungs?",
      "options": ["Aorta", "Pulmonary Artery", "Pulmonary Vein", "Vena Cava"],
      "correct_answer": "Pulmonary Artery"
    },
{
      "question": "Question 1: A particle is moving along a straight line. Its position x at time t is given by x = 3t^2 - 2t + 5. What is the acceleration of the particle at t = 2s?",
      "options": ["10 m/s²", "14 m/s²", "18 m/s²", "22 m/s²"],
      "correct_answer": "14 m/s²"
    },
    {
      "question": "Question 2: Two resistors of resistance 6 ohms and 12 ohms are connected in parallel across a 12V battery. What is the total current drawn from the battery?",
      "options": ["1 A", "2 A", "3 A", "4 A"],
      "correct_answer": "3 A"
    },
{
      "question": "Question 1: What is the standard electrode potential of a hydrogen electrode?",
      "options": ["0.00 V", "0.34 V", "0.76 V", "1.23 V"],
      "correct_answer": "0.00 V"
    },
    {
      "question": "Question 2: Which of the following compounds exhibits hydrogen bonding to the greatest extent?",
      "options": ["Ethanol", "Methanol", "Water", "Acetone"],
      "correct_answer": "Water"
    },
  {
      "question": "Question 1: What is the function of the Golgi apparatus in a cell?",
      "options": ["Protein synthesis", "Cellular respiration", "Cell division", "Modification and packaging of proteins"],
      "correct_answer": "Modification and packaging of proteins"
    },
    {
      "question": "Question 2: Which of the following hormones is NOT produced by the anterior pituitary gland?",
      "options": ["Growth hormone", "Thyroid-stimulating hormone", "Adrenocorticotropic hormone", "Oxytocin"],
      "correct_answer": "Oxytocin"
    },
{
      "question": "A particle is projected with a velocity of 20 m/s at an angle of 30 degrees with the horizontal. What is the time taken for the particle to reach the highest point of its trajectory?",
      "options": ["1.0 s", "2.0 s", "0.5 s", "0.9 s"],
      "correct_answer": "1.0 s"
    },
    {
      "question": "A conducting loop carrying a current is placed in a magnetic field. What will happen if the magnetic field is increased?",
      "options": ["Loop expands", "Loop contracts", "No change", "Loop rotates"],
      "correct_answer": "Loop contracts"
    },
{
      "question": "Which of the following is a Lewis acid?",
      "options": ["NaCl", "H2O", "BF3", "HCl"],
      "correct_answer": "BF3"
    },
    {
      "question": "Which type of bond is formed between two chlorine atoms in a chlorine molecule (Cl2)?",
      "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"],
      "correct_answer": "Covalent bond"
    },
{
      "question": "What is the function of the Golgi apparatus in a cell?",
      "options": ["Photosynthesis", "Protein synthesis", "Cellular respiration", "Modification and packaging of proteins"],
      "correct_answer": "Modification and packaging of proteins"
    },
    {
      "question": "Which of the following is an example of a monocot plant?",
      "options": ["Mango", "Wheat", "Pea", "Rose"],
      "correct_answer": "Wheat"
    },
{
      "question": "Which of the following is not a function of the liver?",
      "options": ["Production of bile", "Detoxification", "Storage of glycogen", "Production of insulin"],
      "correct_answer": "Production of insulin"
    },
    {
      "question": "Which of the following is a function of the respiratory system?",
      "options": ["Transport of oxygen", "Pumping blood", "Digesting food", "Regulating body temperature"],
      "correct_answer": "Transport of oxygen"
    },
    {
      "question": "What is the main function of the mitochondria?",
      "options": ["Photosynthesis", "Cellular respiration", "Protein synthesis", "Storage of genetic material"],
      "correct_answer": "Cellular respiration"
    },
    {
      "question": "Which of the following is a characteristic of eukaryotic cells?",
      "options": ["No nucleus", "Simple structure", "Presence of membrane-bound organelles", "Unicellular"],
      "correct_answer": "Presence of membrane-bound organelles"
    },
    {
      "question": "What is the role of ribosomes in a cell?",
      "options": ["Energy production", "Cellular communication", "Protein synthesis", "Cell division"],
      "correct_answer": "Protein synthesis"
    },
    {
      "question": "What is the function of the circulatory system?",
      "options": ["Respiration", "Transport of nutrients and waste products", "Digestion", "Skeletal support"],
      "correct_answer": "Transport of nutrients and waste products"
    },
    {
      "question": "Which of the following is a function of the nucleus?",
      "options": ["Storage of nutrients", "Cellular respiration", "Control of cell activities", "Protein synthesis"],
      "correct_answer": "Control of cell activities"
    },
    {
      "question": "Which of the following is a characteristic of prokaryotic cells?",
      "options": ["Presence of membrane-bound organelles", "Complex structure", "Nucleus", "Unicellular"],
      "correct_answer": "Unicellular"
    },
    {
      "question": "What is the function of chloroplasts in plant cells?",
      "options": ["Cellular respiration", "Protein synthesis", "Photosynthesis", "Storage of genetic material"],
      "correct_answer": "Photosynthesis"
    },
    {
      "question": "What is the primary function of the nervous system?",
      "options": ["Regulation of body temperature", "Transport of nutrients", "Coordination of body activities", "Respiration"],
      "correct_answer": "Coordination of body activities"
    },
   {
      "question": "What is the chemical symbol for gold?",
      "options": ["Au", "Ag", "Pt", "Cu"],
      "correct_answer": "Au"
    },
    {
      "question": "What is the pH value of a neutral solution?",
      "options": ["7", "0", "14", "1"],
      "correct_answer": "7"
    },
    {
      "question": "Which gas is known as laughing gas?",
      "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Nitrous Oxide"],
      "correct_answer": "Nitrous Oxide"
    },
    {
      "question": "What is the chemical formula for water?",
      "options": ["H2O", "CO2", "CH4", "NH3"],
      "correct_answer": "H2O"
    },
    {
      "question": "Which element has the atomic number 6?",
      "options": ["Oxygen", "Carbon", "Nitrogen", "Hydrogen"],
      "correct_answer": "Carbon"
    },
    {
      "question": "What is the process of conversion of a liquid into a gas at its boiling point?",
      "options": ["Vaporization", "Condensation", "Sublimation", "Evaporation"],
      "correct_answer": "Evaporation"
    },
    {
      "question": "Which gas is responsible for the depletion of the ozone layer?",
      "options": ["Oxygen", "Methane", "Carbon Dioxide", "Chlorofluorocarbons (CFCs)"],
      "correct_answer": "Chlorofluorocarbons (CFCs)"
    },
    {
      "question": "Which of the following is a noble gas?",
      "options": ["Helium", "Neon", "Argon", "All of the above"],
      "correct_answer": "All of the above"
    },
    {
      "question": "What is the chemical formula for table salt?",
      "options": ["NaCl", "H2SO4", "HCl", "NaOH"],
      "correct_answer": "NaCl"
    },
    {
      "question": "Which type of bond is formed between two chlorine atoms in a chlorine molecule (Cl2)?",
      "options": ["Covalent bond", "Ionic bond", "Metallic bond", "Hydrogen bond"],
      "correct_answer": "Covalent bond"
    },
    {
      "question": "Which of the following compounds is classified as an aromatic hydrocarbon?",
      "options": ["Ethane", "Benzene", "Propane", "Methanol"],
      "correct_answer": "Benzene"
    },
    {
      "question": "What is the molecular geometry of sulfur hexafluoride (SF6)?",
      "options": ["Tetrahedral", "Trigonal planar", "Octahedral", "Trigonal bipyramidal"],
      "correct_answer": "Octahedral"
    },
    {
      "question": "What is the pH of a solution with a hydroxide ion concentration of 1 x 10^-3 M?",
      "options": ["1", "3", "11", "9"],
      "correct_answer": "11"
    },
    {
      "question": "Which of the following compounds is a strong electrolyte when dissolved in water?",
      "options": ["Acetic acid", "Sodium chloride", "Ethanol", "Sucrose"],
      "correct_answer": "Sodium chloride"
    },
    {
      "question": "What is the standard reduction potential of the hydrogen electrode under standard conditions?",
      "options": ["0 V", "-0.76 V", "1.23 V", "-1.36 V"],
      "correct_answer": "0 V"
    },
    {
      "question": "Which of the following is NOT a transition metal?",
      "options": ["Copper", "Iron", "Aluminum", "Nickel"],
      "correct_answer": "Aluminum"
    },
    {
      "question": "What is the hybridization of the central atom in sulfur dioxide (SO2)?",
      "options": ["Sp", "Sp2", "Sp3", "Sp3d"],
      "correct_answer": "Sp2"
    },
    {
      "question": "Which of the following is a homologous series?",
      "options": ["Alcohols", "Aldehydes", "Amines", "Carboxylic acids"],
      "correct_answer": "Alcohols"
    },
    {
      "question": "What is the primary function of a catalyst in a chemical reaction?",
      "options": ["Decrease reaction rate", "Increase activation energy", "Increase yield of products", "Lower activation energy"],
      "correct_answer": "Lower activation energy"
    },
    {
      "question": "What is the percentage composition of oxygen in sodium sulfate (Na2SO4)?",
      "options": ["20%", "32%", "40%", "48%"],
      "correct_answer": "32%"
    },
{
        "question": "The genetic material in tobacco mosaic virus is",
        "options": ["dsDNA", "ssDNA", "dsRNA", "ssRNA"],
        "correct_answer": "ssRNA"
    },

    {
        "question": "Translation refers to",
        "options": [
            "Formation of newly synthesized DNA over parental DNA",
            "Copying genetic information from one strand of DNA into RNA",
            "Polymerisation of amino acids to form a polypeptide",
            "Movement of ribosome on mRNA"
        ],
        "correct_answer": "Polymerisation of amino acids to form a polypeptide"
    },

    {
        "question": "Algal bloom",
        "options": [
            "Leads to increase in DO content of water body",
            "Imparts a distinct colour to water body",
            "Leads to decrease in BOD content of water body",
            "Is always beneficial to human beings"
        ],
        "correct_answer": "Imparts a distinct colour to water body"
    },
]
def conduct_mock_test(questions):
    score = 0
    start_time = time.time()  # Record the start time
    for q_idx, q in enumerate(questions):
        st.write(f"{q_idx + 1}. {q['question']}")
        user_answer = st.radio(f"Options for question {q_idx + 1}:", options=q["options"], index=None, key=f"question_{q_idx}_index")
        if user_answer == q["correct_answer"]:
            score += 4
        else:
            score -= 1
        # Check if 3 hours have elapsed
        if time.time() - start_time >= 3 * 60 * 60:
            st.warning("Time's up! You have exceeded the time limit.")
            break
    return max(score, 0)  # Ensure score is non-negative

def app():
    # Initialize Firestore client
    db = firestore.client()

    # Check if user is logged in
    if 'username' not in st.session_state or not st.session_state['username']:
        st.error('Please login first.')
        return

    try:
        st.title("Mock Test 4 for NEET Examination")
        st.write("Please answer the following questions:")
        st.write("**Time Duration Of Exam 3hr**")

        score = conduct_mock_test(questions)
        st.write(f"Your score is: {score}")
        countdown_placeholder = st.empty()  # Placeholder for countdown timer
        
        # Display countdown timer
        end_time = time.time() + 3 * 60 * 60  # 3 hours from the current time
        while time.time() < end_time:
            remaining_time = int(end_time - time.time())
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            seconds = remaining_time % 60
            countdown_placeholder.write(f"Time Remaining: {hours:02d}:{minutes:02d}:{seconds:02d}")
            time.sleep(1)  # Update every second

        countdown_placeholder.empty()  # Clear countdown timer after time is up

    except Exception as e:
        st.error(f"An error occurred: {e}")
        
if __name__ == "__main__":
    app()