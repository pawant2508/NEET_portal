import streamlit as st # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

#questions for the mock test
questions = [
{
    "question": "A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is",
    "options": [
            "Along northward",
            "Along north-east",
            "Along south-west",
            "Along eastward"
        ],
        "correct_answer": "Along northward"
    },

    {
        "question": "An ac source is connected to a capacitor C. Due to decrease in its operating frequency",
        "options": [
            "Displacement current increases",
            "Displacement current decreases",
            "Capacitive reactance remains constant",
            "Capacitive reactance decreases"
        ],
        "correct_answer": "Displacement current decreases"
    },

    {
        "question": "The net magnetic flux through any closed surface is",
        "options": [
            "Positive",
            "Infinity",
            "Negative",
            "Zero"
        ],
        "correct_answer": "Zero"
    },

    {
        "question": "The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is",
        "options": [
            "2 : 1",
            "1 : 3",
            "3 : 1",
            "1 : 2"
        ],
        "correct_answer": "2 : 1"
    },

    {
        "question": "In hydrogen spectrum, the shortest wavelength in the Balmer series is λ. The shortest wavelength in the Bracket series is",
        "options": [
            "4λ",
            "9λ",
            "16λ",
            "2λ"
        ],
        "correct_answer": "16λ"
    },

    {
        "question": "A 12 V, 60 W lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of 220 V. Assuming the transformer to be ideal, what is the current in the primary winding?",
        "options": [
            "2.7 A",
            "3.7 A",
            "0.37 A",
            "0.27 A"
        ],
        "correct_answer": "0.27 A"
    },

    {
        "question": "The magnetic energy stored in an inductor of inductance 4 µH carrying a current of 2 A is",
        "options": [
            "4 mJ",
            "8 mJ",
            "8 µJ",
            "4 µJ"
        ],
        "correct_answer": "8 µJ"
    },

    {
        "question": "The potential energy of a long spring when stretched by 2 cm is U. If the spring is stretched by 8 cm, potential energy stored in it will be",
        "options": [
            "4 U",
            "8 U",
            "16 U",
            "2 U"
        ],
        "correct_answer": "16 U"
    },

    {
        "question": "The errors in the measurement which arise due to unpredictable fluctuations in temperature and voltage supply are",
        "options": [
            "Personal errors",
            "Least count errors",
            "Random errors",
            "Instrumental errors"
        ],
        "correct_answer": "Random errors"
    },

    {
        "question": "Resistance of a carbon resistor determined from colour codes is (22000 ± 5%) Ω. The colour of third band must be",
        "options": [
            "Green",
            "Orange",
            "Yellow",
            "Red"
        ],
        "correct_answer": "Yellow"
    },

    {
        "question": "A metal wire has mass (0.4 ± 0.002) g, radius (0.3 ± 0.001) mm and length (5 ± 0.02) cm. The maximum possible percentage error in the measurement of density will nearly be",
        "options": [
            "1.3%",
            "1.6%",
            "1.4%",
            "1.2%"
        ],
        "correct_answer": "1.3%"
    },

    {
        "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 10^10 Hz and amplitude 48 V m–1. Then the amplitude of oscillating magnetic field is (Speed of light in free space = 3 × 10^8 m s–1)",
        "options": [
            "1.6 × 10^–8 T",
            "1.6 × 10^–7 T",
            "1.6 × 10^–6 T",
            "1.6 × 10^–9 T"
        ],
        "correct_answer": "1.6 × 10^–7 T"
    },

    {
        "question": "The ratio of radius of gyration of a solid sphere of mass M and radius R about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is",
        "options": [
            "5 : 3",
            "2 : 5",
            "5 : 2",
            "3 : 5"
        ],
        "correct_answer": "5 : 3"
    },

    {
        "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
        "options": [
            "5.06 × 10^–4 J",
            "3.01 × 10^–4 J",
            "50.1 × 10^–4 J",
            "30.16 × 10^–4 J"
        ],
        "correct_answer": "30.16 × 10^–4 J"
    },

    {
        "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 µF and resistance R is 100 Ω. The frequency at which resonance occurs is",
        "options": [
            "15.9 kHz",
            "1.59 rad/s",
            "1.59 kHz",
            "15.9 rad/s"
        ],
        "correct_answer": "15.9 kHz"
    },

    {
        "question": "The venturi-meter works on",
        "options": [
            "Bernoulli’s principle",
            "The principle of parallel axes",
            "The principle of perpendicular axes",
            "Huygen’s principle"
        ],
        "correct_answer": "Bernoulli’s principle"
    },

    {
        "question": "The temperature of a gas is –50°C. To what temperature the gas should be heated so that the rms speed is increased by 3 times?",
        "options": [
            "3295°C",
            "3097 K",
            "223 K",
            "669°C"
        ],
        "correct_answer": "3097 K"
    },

    {
        "question": "A vehicle travels half the distance with speed v and the remaining distance with speed 2v. Its average speed is",
        "options": [
            "2V/3",
            "4V/3",
            "3V/4",
            "V/3"
        ],
        "correct_answer": "4V/3"
    },

    {
        "question": "The angular acceleration of a body, moving along the circumference of a circle, is",
        "options": [
            "Along the radius towards the centre",
            "Along the tangent to its position",
            "Along the axis of rotation",
            "Along the radius, away from centre"
        ],
        "correct_answer": "Along the tangent to its position"
    },

    {
        "question": "Let a wire be suspended from the ceiling (rigid support) and stretched by a weight W attached at its free end. The longitudinal stress at any point of cross-sectional area A of the wire is",
        "options": [
            "W/A",
            "W/2A",
            "Zero",
            "2W/A"
        ],
        "correct_answer": "W/A"
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
        "question": "An electric dipole is placed at an angle of 30° with an electric field of intensity 2 × 10^5 N C^–1. It experiences a torque equal to 4 N m. Calculate the magnitude of charge on the dipole, if the dipole length is 2 cm.",
        "options": [
            "6 mC",
            "4 mC",
            "2 mC",
            "8 mC"
        ],
        "correct_answer": "6 mC"
    },

    {
        "question": "A Carnot engine has an efficiency of 50% when its source is at a temperature 327°C. The temperature of the sink is",
        "options": [
            "15°C",
            "100°C",
            "200°C",
            "27°C"
        ],
        "correct_answer": "27°C"
    },

    {

        "question": "For Young’s double slit experiment, two statements are given below: Statement I : If screen is moved away from the plane of slits, angular separation of the fringes remains constant. Statement II : If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },

    {
        "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
        "options": [
            "Both Na and K",
            "K only",
            "Na only",
            "Cs only"
        ],
        "correct_answer": "Na only"
    },

    {
        "question": "Given below are two statements: Statement I: Photovoltaic devices can convert optical radiation into electricity. Statement II: Zener diode is designed to operate under reverse bias in breakdown region. In the light of the above statements, choose the most appropriate answer from the options given below.",
        "options": [
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct",
            "Both Statement I and Statement II are correct"
        ],
        "correct_answer": "Statement I is correct but Statement II is incorrect"
    },

    {
        "question": "A bullet is fired from a gun at the speed of 280 m s^–1 in the direction 30° above the horizontal. The maximum height attained by the bullet is (g = 9.8 m s^–2, sin30° = 0.5)",
        "options": [
            "2000 m",
            "1000 m",
            "3000 m",
            "2800 m"
        ],
        "correct_answer": "2000 m"
    },

    {
        "question": "A satellite is orbiting just above the surface of the earth with period T. If d is the density of the earth and G is the universal constant of gravitation, the quantity 3Gd/π represents",
        "options": [
            "T^2",
            "T^3",
            "√T",
            "T"
        ],
        "correct_answer": "T^2"
    },

    {
        "question": "The radius of inner most orbit of hydrogen atom is 5.3 × 10^–11 m. What is the radius of third allowed orbit of hydrogen atom?",
        "options": [
            "1.06 Å",
            "1.59 Å",
            "4.77 Å",
            "0.53 Å"
        ],
        "correct_answer": "1.59 Å"
    },

    {
        "question": "A wire carrying a current I along the positive x-axis has length L. It is kept in a magnetic field B. The magnitude of the magnetic force acting on the wire is",
        "options": [
            "√5 lL",
            "5 lL",
            "√3 lL",
            "3 lL"
        ],
        "correct_answer": "3 lL"
    },

    {
        "question": "10 resistors, each of resistance R are connected in series to a battery of emf E and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased n times. The value of n is",
        "options": [
            "(1) 100",
            "(2) 1",
            "(3) 1000",
            "(4) 10"
        ],
        "correct_answer": "(1) 100"
    },

    {
        "question": "Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is 0.15 (g = 10 m s–2).",
        "options": [
            "(1) 150 m s–2",
            "(2) 1.5 m s–2",
            "(3) 50 m s–2",
            "(4) 1.2 m s–2"
        ],
        "correct_answer": "(1) 150 m s–2"
    },

    {
        "question": "Two thin lenses are of same focal lengths (f), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be",
        "options": [
            "(1) f/ 4",
            "(2) f/ 2",
            "(3) Infinite",
            "(4) Zero"
        ],
        "correct_answer": "(4) Zero"
    },

    {
        "question": "A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity 4 m s–1. The ball strikes the water surface after 4 s. The height of bridge above water surface is (Take g = 10 m s–2)",
        "options": [
            "(1) 60 m",
            "(2) 64 m",
            "(3) 68 m",
            "(4) 56 m"
        ],
        "correct_answer": "(2) 64 m"
    },

    {
        "question": "The resistance of platinum wire at 0°C is 2 Ω and 6.8 Ω at 80°C. The temperature coefficient of resistance of the wire is",
        "options": [
            "(1) 3 × 10–3 °C–1",
            "(2) 3 × 10–2 °C–1",
            "(3) 3 × 10–1 °C–1",
            "(4) 3 × 10–4 °C–1"
        ],
        "correct_answer": "(1) 3 × 10–3 °C–1"
    },

    {
        "question": "A bullet from a gun is fired on a rectangular wooden block with velocity u. When bullet travels 24 cm through the block along its length horizontally, velocity of bullet becomes 3u. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is",
        "options": [
            "(1) 24 cm",
            "(2) 28 cm",
            "(3) 30 cm",
            "(4) 27 cm"
        ],
        "correct_answer": "(2) 28 cm"
    },

    {
        "question": "The element expected to form largest ion to achieve the nearest noble gas configuration is",
        "options": [
            "(1) F",
            "(2) N",
            "(3) Na",
            "(4) O"
        ],
        "correct_answer": "(3) Na"
    },

    {
        "question": "In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with Fe3+ due to the formation of",
        "options": [
            "(1) NaSCN",
            "(2) [Fe(CN)5NOS]4–",
            "(3) [Fe(SCN)]2+",
            "(4) Fe4[Fe(CN)6]3xH2O"
        ],
        "correct_answer": "(2) [Fe(CN)5NOS]4–"
    },

    {
        "question": "Which one is an example of heterogenous catalysis?",
        "options": [
            "(1) Hydrolysis of sugar catalysed by H+ ions",
            "(2) Decomposition of ozone in presence of nitrogen monoxide",
            "(3) Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron",
            "(4) Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen"
        ],
        "correct_answer": "(3) Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron"
    },

    {
        "question": "Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R Assertion A : Helium is used to dilute oxygen in diving apparatus. Reason R : Helium has high solubility in O2. In the light of the above statements, choose the correct answer from the options given below",
        "options": [
            "(1) Both A and R are true and R is NOT the correct explanation of A",
            "(2) A is true but R is false",
            "(3) A is false but R is true",
            "(4) Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "(1) Both A and R are true and R is NOT the correct explanation of A"
    },

    {
        "question": "The conductivity of centimolar solution of KCl at 25°C is 0.0210 ohm–1 cm–1 and the resistance of the cell containing the solution at 25°C is 60 ohm. The value of cell constant is",
        "options": [
            "(1) 3.28 cm–1",
            "(2) 1.26 cm–1",
            "(3) 3.34 cm–1",
            "(4) 1.34 cm–1"
        ],
        "correct_answer": "(1) 3.28 cm–1"
    },

    {
        "question": "The number of  bonds,  bonds and lone pair of electrons in pyridine, respectively are:",
        "options": [
            "(1) 12, 3, 0",
            "(2) 11, 3, 1",
            "(3) 12, 2, 1",
            "(4) 11, 2, 0"
        ],
        "correct_answer": "(1) 12, 3, 0"
    },

    {
        "question": "Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : Assertion A : Metallic sodium dissolves in liquid ammonia giving a deep blue solution, which is paramagnetic. Reason R : The deep blue solution is due to the formation of amide. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "(1) Both A and R are true but R is NOT the correct explanation of A",
            "(2) A is true but R is false",
            "(3) A is false but R is true",
            "(4) Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "(4) Both A and R are true and R is the correct explanation of A"
    },

    {
        "question": "Intermolecular forces are forces of attraction and repulsion between interacting particles that will include : A. dipole - dipole forces B. dipole - induced dipole forces C. hydrogen bonding D. covalent bonding E. dispersion forces Choose the most appropriate answer from the options given below :",
        "options": [
            "(1) A, B, C, D are correct",
            "(2) A, B, C, E are correct",
            "(3) A, C, D, E are correct",
            "(4) B, C, D, E are correct"
        ],
        "correct_answer": "(2) A, B, C, E are correct"
    },

    {
        "question": "For a certain reaction, the rate = k[A]2 [B], when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would",
        "options": [
            "(1) Increase by a factor of six",
            "(2) Increase by a factor of nine",
            "(3) Increase by a factor of three",
            "(4) Decrease by a factor of nine"
        ],
        "correct_answer": "(2) Increase by a factor of nine"
    },

    {
        "question": "Which of the following statements are NOT correct? A. Hydrogen is used to reduce heavy metal oxides to metals. B. Heavy water is used to study reaction mechanism. C. Hydrogen is used to make saturated fats from oils. D. The H–H bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements. E. Hydrogen reduces oxides of metals that are more active than iron. Choose the most appropriate answer from the options given below:",
        "options": [
            "(1) B, D only",
            "(2) D, E only",
            "(3) A, B, C only",
            "(4) B, C, D, E only"
        ],
        "correct_answer": "(4) B, C, D, E only"
    },

    {
        "question": "Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in presence of calcium oxide is :",
        "options": [
            "(1) 32",
            "(2) 30",
            "(3) 18",
            "(4) 16"
        ],
        "correct_answer": "(1) 32"
    },

    {
        "question": "A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy 1/3 of tetrahedral voids. If the formula of the compound is AxBy, then the value of x + y is in option",
        "options": [
            "(1) 4",
            "(2) 3",
            "(3) 2",
            "(4) 5"
        ],
        "correct_answer": "(2) 3"
    },

    {
        "question": "The stability of Cu2+ is more than Cu+ salts in aqueous solution due to",
        "options": [
            "(1) Enthalpy of atomization",
            "(2) Hydration energy",
            "(3) Second ionisation enthalpy",
            "(4) First ionisation enthalpy"
        ],
        "correct_answer": "(2) Hydration energy"
    },

    {
        "question": "Given below are two statements : Statement I : A unit formed by the attachment of a base to 1' position of sugar is known as nucleoside. Statement II : When nucleoside is linked to phosphorous acid at 5'-position of sugar moiety, we get nucleotide. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "(1) Both Statement I and Statement II are false",
            "(2) Statement I is true but Statement II is false",
            "(3) Statement I is false but Statement II is true",
            "(4) Both Statement I and Statement II are true"
        ],
        "correct_answer": "(4) Both Statement I and Statement II are true"
    },

    {
        "question": "Which one of the following statements is correct?",
        "options": [
            "(1) All enzymes that utilise ATP in phosphate transfer require Ca as the cofactor",
            "(2) The bone in human body is an inert and unchanging substance",
            "(3) Mg plays roles in neuromuscular function and interneuronal transmission",
            "(4) The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g"
        ],
        "correct_answer": "(3) Mg plays roles in neuromuscular function and interneuronal transmission"
    },

    {
        "question": "Match List-I with List-II. List-I List-II A. Coke I. Carbon atoms are sp3 hybridised B. Diamond II. Used as a dry lubricant C. Fullerene III. Used as a reducing agent D. Graphite IV. Cage like molecules Choose the correct answer from the options given below :",
        "options": [
            "(1) A-IV, B-I, C-II, D-III",
            "(2) A-III, B-I, C-IV, D-II",
            "(3) A-III, B-IV, C-I, D-II",
            "(4) A-II, B-IV, C-I, D-III"
        ],
        "correct_answer": "(3) A-III, B-IV, C-I, D-II"
    },

    {
        "question": "Amongst the given options which of the following molecules/ ion acts as a Lewis acid?",
        "options": [
            "(1) H2O",
            "(2) BF3",
            "(3) OH–",
            "(4) NH3"
        ],
        "correct_answer": "(2) BF3"
    },

    {
        "question": "Some tranquilizers are listed below. Which one from the following belongs to barbiturates?",
        "options": [
            "(1) Meprobamate",
            "(2) Valium",
            "(3) Veronal",
            "(4) Chlordiazepoxide"
        ],
        "correct_answer": "(3) Veronal"
    },

    {
        "question": "Homoleptic complex from the following complexes is",
        "options": [
            "(1) Diamminechloridonitrito-N-platinum (II)",
            "(2) Pentaamminecarbonatocobalt (III) chloride",
            "(3) Triamminetriaquachromium (III) chloride",
            "(4) Potassium trioxalatoaluminate (III)"
        ],
        "correct_answer": "(2) Pentaamminecarbonatocobalt (III) chloride"
    },

    {
        "question": "Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : Assertion A : A reaction can have zero activation energy. Reason R : The minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value, is called activation energy. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "(1) Both A and R are true and R is NOT the correct explanation of A",
            "(2) A is true but R is false",
            "(3) A is false but R is true",
            "(4) Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "(4) Both A and R are true and R is the correct explanation of A"
    },

    {
        "question": "Select the correct statements from the following A. Atoms of all elements are composed of two fundamental particles. B. The mass of the electron is 9.10939 × 10–31 kg. C. All the isotopes of a given element show same chemical properties: D. Protons and electrons are collectively known as nucleons. E. Dalton’s atomic theory, regarded the atom as an ultimate particles of matter Choose the correct answer from the options given below",
        "options": [
            "(1) C, D and E only",
            "(2) A and E only",
            "(3) B, C and E only",
            "(4) A, B and C only"
        ],
        "correct_answer": "(4) A, B and C only"
    },

    {
        "question": "Match List-I with List-II : List-I (Oxoacids of Sulphur) List-II (Bonds) A. Peroxodisulphuric acid I. Two S–OH, Four S=O, One S–O–S B. Sulphuric acid II. Two S–OH, One S=O C. Pyrosulphuric acid III. Two S–OH, Four S=O, One S–O–O–S D. Sulphurous acid IV. Two S–OH, Two S=O Choose the correct answer from the options given below.",
        "options": [
            "(1) A–III, B–IV, C–I, D–II",
            "(2) A–I, B–III, C–IV, D–II",
            "(3) A–III, B–IV, C–II, D–I",
            "(4) A–I, B–III, C–II, D–IV"
        ],
        "correct_answer": "(3) A–III, B–IV, C–II, D–I"
    },

    {
        "question": "What fraction of one edge centred octahedral void lies in one unit cell of fcc?",
        "options": [
            "(1) 1/3",
            "(2) 1/4",
            "(3) 1/12",
            "(4) 1/2"
        ],
        "correct_answer": "(4) 1/2"
    },

    {
        "question": "Given below are two statements : Statement I : The nutrient deficient water bodies lead to eutrophication Statement II : Eutrophication leads to decrease in the level of oxygen in the water bodies. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "(1) Both Statement I and Statement II are false.",
            "(2) Statement I is correct but Statement II is false.",
            "(3) Statement I is incorrect but Statement II is true.",
            "(4) Both Statement I and Statement II are true."
        ],
        "correct_answer": "(4) Both Statement I and Statement II are true."
    },

    {
        "question": "The reaction that does NOT take place in a blast furnace between 900 K to 1500 K temperature range during extraction of iron is :",
        "options": [
            "(1) FeO + CO ➝ Fe + CO2",
            "(2) C + CO2 ➝ 2CO",
            "(3) CaO + SiO2 ➝CaSiO3",
            "(4) Fe2O3 + CO ➝ 2FeO + CO2"
        ],
        "correct_answer": "(3) CaO + SiO2 ➝CaSiO3"
    },

    {
        "question": "The equilibrium concentrations of the species in the reaction A+ B ⇋C +D are 2, 3, 10 and 6 mol L–1,respectively at 300 K. ∆Gº for the reaction is (R = 2 cal/mol K)",
        "options": [
            "(1) –137.26 cal",
            "(2) –1381.80 cal",
            "(3) –13.73 cal",
            "(4) 1372.60 cal"
        ],
        "correct_answer": "(1) –137.26 cal"
    },

    {
        "question": "Pumice stone is an example of",
        "options": [
            "(1) Gel",
            "(2) Solid sol",
            "(3) Foam",
            "(4) Sol"
        ],
        "correct_answer": "(3) Foam"
    },

    {
        "question": "The phenomenon of pleiotropism refers to",
        "options": [
            "(1) Presence of two alleles, each of the two genes controlling a single trait",
            "(2) A single gene affecting multiple phenotypic expression",
            "(3) More than two genes affecting a single character",
            "(4) Presence of several alleles of a single gene controlling a single crossover"
        ],
        "correct_answer": "(2) A single gene affecting multiple phenotypic expression"
    },

    {
        "question": "In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as",
        "options": [
            "(1) Dedifferentiation",
            "(2) Development",
            "(3) Senescence",
            "(4) Differentiation"
        ],
        "correct_answer": "(1) Dedifferentiation"
    },

    {
        "question": "Movement and accumulation of ions across a membrane against their concentration gradient can be explained by",
        "options": [
            "(1) Facilitated Diffusion",
            "(2) Passive Transport",
            "(3) Active Transport",
            "(4) Osmosis"
        ],
        "correct_answer": "(3) Active Transport"
    },

    {
        "question": "Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?",
        "options": [
            "(1) Over exploitation for economic gain",
            "(2) Alien species invasions",
            "(3) Co-extinctions",
            "(4) Habitat loss and fragmentation"
        ],
        "correct_answer": "(4) Habitat loss and fragmentation"
    },

    {
        "question": "Upon exposure to UV radiation, DNA stained with ethidium bromide will show",
        "options": [
            "Bright blue colour",
            "Bright yellow colour",
            "Bright orange colour",
            "Bright red colour"
        ],
        "correct_answer": "Bright orange colour"
    },

    {
        "question": "What is the role of RNA polymerase III in the process of transcription in Eukaryotes?",
        "options": [
            "Transcription of tRNA, 5S rRNA and snRNA",
            "Transcription of precursor of mRNA",
            "Transcription of only snRNAs",
            "Transcription of rRNAs (28S, 18S and 5.8S)"
        ],
        "correct_answer": "Transcription of tRNA, 5S rRNA and snRNA"
    },

    {
        "question": "The historic Convention on Biological Diversity, ‘The Earth Summit’ was held in Rio de Janeiro in the year",
        "options": [
            "1992",
            "1986",
            "2002",
            "1985"
        ],
        "correct_answer": "1992"
    },

    {
        "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : ATP is used at two steps in glycolysis. Reason R : First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1, 6-diphosphate. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true.",
            "Both A and R are true and R is the correct explanation of A."
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A."
    },

    {
        "question": "The thickness of ozone in a column of air in the atmosphere is measured in terms of :",
        "options": [
            "Decibels",
            "Decameter",
            "Kilobase",
            "Dobson units"
        ],
        "correct_answer": "Dobson units"
    },

    {
        "question": "Given below are two statements : Statement I : Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body. Statement II : Exarch condition is the most common feature of the root system. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false",
            "Statement I is correct but Statement II is false",
            "Statement I is incorrect but Statement II is true",
            "Both Statement I and Statement II are true"
        ],
        "correct_answer": "Statement I is correct but Statement II is false"
    },

    {
        "question": "Identify the pair of heterosporous pteridophytes among the following :",
        "options": [
            "Selaginella and Salvinia",
            "Psilotum and Salvinia",
            "Equisetum and Salvinia",
            "Lycopodium and Selaginella"
        ],
        "correct_answer": "Selaginella and Salvinia"
    },
{
    "question": "Identify the correct statements:",
    "options": [
        "Detrivores perform fragmentation.",
        "The humus is further degraded by some microbes during mineralization.",
        "Water soluble inorganic nutrients go down into the soil and get precipitated by a process called leaching.",
        "The detritus food chain begins with living organisms.",
        "Earthworms break down detritus into smaller particles by a process called catabolism."
    ],
    "correct_answer": "B, C, D only"
},

{
    "question": "Axile placentation is observed in",
    "options": [
        "China rose, Beans and Lupin",
        "Tomato, Dianthus and Pea",
        "China rose, Petunia and Lemon",
        "Mustard, Cucumber and Primrose"
    ],
    "correct_answer": "China rose, Beans and Lupin"
},

{
    "question": "Family Fabaceae differs from Solanaceae and Liliaceae. With respect to the stamens, pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae.",
    "options": [
        "Polyadelphous and epipetalous stamens",
        "Monoadelphous and Monothecous anthers",
        "Epiphyllous and Dithecous anthers",
        "Diadelphous and Dithecous anthers"
    ],
    "correct_answer": "Diadelphous and Dithecous anthers"
},

{
    "question": "The reaction centre in PS II has an absorption maxima at",
    "options": [
        "700 nm",
        "660 nm",
        "780 nm",
        "680 nm"
    ],
    "correct_answer": "680 nm"
},

{
    "question": "During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out",
    "options": [
        "DNA",
        "Histones",
        "Polysaccharides",
        "RNA"
    ],
    "correct_answer": "DNA"
},

{
    "question": "Among eukaryotes, replication of DNA takes place in :",
    "options": [
        "S phase",
        "G1 phase",
        "G2 phase",
        "M phase"
    ],
    "correct_answer": "S phase"
},

{
    "question": "The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?",
    "options": [
        "Pachytene",
        "Diplotene",
        "Diakinesis",
        "Zygotene"
    ],
    "correct_answer": "Zygotene"
},

{
    "question": "How many ATP and NADPH2 are required for the synthesis of one molecule of Glucose during Calvin cycle?",
    "options": [
        "18 ATP and 12 NADPH2",
        "12 ATP and 16 NADPH2",
        "18 ATP and 16 NADPH2",
        "12 ATP and 12 NADPH2"
    ],
    "correct_answer": "18 ATP and 12 NADPH2"
},

{
    "question": "In the equation GPP -R= NPP GPP is Gross Primary Productivity NPP is Net Primary Productivity R here is ________.",
    "options": [
        "Respiratory quotient",
        "Respiratory loss",
        "Reproductive allocation",
        "Photosynthetically active radiation"
    ],
    "correct_answer": "Respiratory loss"
},

{
    "question": "Large, colourful, fragrant flowers with nectar are seen in",
    "options": [
        "Bird pollinated plants",
        "Bat pollinated plants",
        "Wind pollinated plants",
        "Insect pollinated plants"
    ],
    "correct_answer": "Insect pollinated plants"
},

{
    "question": "Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period, that leads early seed production?",
    "options": [
        "Gibberellic Acid",
        "Zeatin",
        "Abscisic Acid",
        "Indole-3-butyric Acid"
    ],
    "correct_answer": "Gibberellic Acid"
},

{
    "question": "Which micronutrient is required for splitting of water molecule during photosynthesis?",
    "options": [
        "Molybdenum",
        "Magnesium",
        "Copper",
        "Manganese"
    ],
    "correct_answer": "Manganese"
},

{
    "question": "Expressed Sequence Tags (ESTs) refers to",
    "options": [
        "All genes that are expressed as proteins.",
        "All genes whether expressed or unexpressed.",
        "Certain important expressed genes.",
        "All genes that are expressed as RNA."
    ],
    "correct_answer": "Certain important expressed genes."
},

{
    "question": "Frequency of recombination between gene pairs on same chromosome as a measure of the distance between genes to map their position on chromosome, was used for the first time by",
    "options": [
        "Sutton and Boveri",
        "Alfred Sturtevant",
        "Henking",
        "Thomas Hunt Morgan"
    ],
    "correct_answer": "Alfred Sturtevant"
},

{
    "question": "Given below are two statements : Statement I : The forces generated transpiration can lift a xylem-sized column of water over 130 meters height. Statement II : Transpiration cools leaf surfaces sometimes 10 to 15 degrees evaporative cooling. In the light of the above statements, choose the most appropriate answer from the options given below :",
    "options": [
        "Both Statement I and Statement II are incorrect",
        "Statement I is correct but Statement II is incorrect",
        "Statement I is incorrect but Statement II is correct",
        "Both Statement I and Statement II are correct"
    ],
    "correct_answer": "Both Statement I and Statement II are correct"
},

{
    "question": "In gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used.",
    "options": [
        "Zinc",
        "Tungsten or gold",
        "Silver",
        "Copper"
    ],
    "correct_answer": "Tungsten or gold"
},

{
    "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : Late wood has fewer xylary elements with narrow vessels. Reason R : Cambium is less active in winters. In the light of the above statements, choose the correct answer from the options given below :",
    "options": [
        "Both A and R are true but R is NOT the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true",
        "Both A and R are true and R is the correct explanation of A"
    ],
    "correct_answer": "A is true but R is false"
},

{
    "question": "What is the function of tassels in the corn cob?",
    "options": [
        "To trap pollen grains",
        "To disperse pollen grains",
        "To protect seeds",
        "To attract insects"
    ],
    "correct_answer": "To disperse pollen grains"
},

{
    "question": "In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :",
    "options": [
        "Antipodals, synergids, and primary endosperm nucleus",
        "Synergids, Zygote and Primary endosperm nucleus",
        "Synergids, antipodals and Polar nuclei",
        "Synergids, Primary endosperm nucleus and zygote"
    ],
    "correct_answer": "Synergids, Primary endosperm nucleus and zygote"
},

{
    "question": "Which hormone promotes internode/petiole elongation in deep water rice?",
    "options": [
        "Kinetin",
        "Ethylene",
        "2, 4-D",
        "GA3"
    ],
    "correct_answer": "Ethylene"
},

{
    "question": "Which of the following stages of meiosis involves division of centromere?",
    "options": [
        "Metaphase II",
        "Anaphase II",
        "Telophase",
        "Metaphase I"
    ],
    "correct_answer": "Anaphase II"
},

{
    "question": "Unequivocal proof that DNA is the genetic material was first proposed by",
    "options": [
        "Alfred Hershey and Martha Chase",
        "Avery, Macleoid and McCarthy",
        "Wilkins and Franklin",
        "Frederick Griffith"
    ],
    "correct_answer": "Avery, Macleoid and McCarthy"
},

{
    "question": "Cellulose does not form blue colour with Iodine because",
    "options": [
        "It is a helical molecule",
        "It does not contain complex helices and hence cannot hold iodine molecules",
        "It breaks down when iodine reacts with it",
        "It is a disaccharide"
    ],
    "correct_answer": "It does not contain complex helices and hence cannot hold iodine molecules"
},

{
    "question": "Match List I with List II : List I List II A. Oxidative decarboxylation I. Citrate synthase B. Glycolysis II. Pyruvate dehydrogenase C. Oxidative phosphorylation III. Electron transport system D. Tricarboxylic acid cycle IV. EMP pathway Choose the correct answer from the options given below :",
    "options": [
        "A – II, B – IV, C – I, D – III",
        "A – III, B – I, C – II, D – IV",
        "A – II, B – IV, C – III, D – I",
        "A – III, B – IV, C – II, D – I"
    ],
    "correct_answer": "A – II, B – IV, C – I, D – III"
},

{
    "question": "Which of the following combinations is required for chemiosmosis?",
    "options": [
        "Membrane, proton pump, proton gradient, NADP synthase",
        "Proton pump, electron gradient, ATP synthase",
        "Proton pump, electron gradient, NADP synthase",
        "Membrane, proton pump, proton gradient, ATP synthase"
    ],
    "correct_answer": "Proton pump, electron gradient, ATP synthase"
},

{
    "question": "Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of",
    "options": [
        "Amylase",
        "Lipase",
        "Dinitrogenase",
        "Succinic dehydrogenase"
    ],
    "correct_answer": "Succinic dehydrogenase"
},

{
    "question": "Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : Assertion A : In gymnosperms the pollen grains are released from the microsporangium and carried by air currents. Reason R : Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed. In the light of the above statements, choose the correct answer from the options given below :",
    "options": [
        "Both A and R are true but R is NOT the current explanation of A",
        "A is true but R is false",
        "A is false but R is true",
        "Both A and R are true and R is the correct explanation of A"
    ],
    "correct_answer": "A is true but R is false"
},

{
    "question": "Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence. A. Insertion of recombinant DNA into the host cell B. Cutting of DNA at specific location by restriction enzyme C. Isolation of desired DNA fragment D. Amplification of gene of interest using PCR Choose the correct answer from the options given below :",
    "options": [
        "C, A, B, D",
        "C, B, D, A",
        "B, D, A, C",
        "B, C, D, A"
    ],
    "correct_answer": "C, B, D, A"
},

{
    "question": "Match List I with List II : ListI List II (Interaction) (Species A and B) A. Mutualism I. +(A), 0(B) B. Commensalism II. –(A), 0(B) C. Amensalism III. +(A), –(B) D. Parasitism IV. +(A), +(B) Choose the correct answer from the options given below: ",
    "options": [
        "A-IV, B-I, C-II, D-III",
        "A-IV, B-III, C-I, D-II",
        "A-III, B-I, C-IV, D-II",
        "A-IV, B-II, C-I, D-III"
    ],
    "correct_answer": "A-IV, B-I, C-II, D-III"
},

{
    "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem. Reason R : Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves. In the light of the above statements, choose the correct answer from the options given below :",
    "options": [
        "Both A and R are true but R is NOT the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true",
        "Both A and R are true and R is the correct explanation of A"
    ],
    "correct_answer": "Both A and R are true and R is the correct explanation of A"
},
{
    "question": "Identify the correct statements: A. Lenticels are the lens-shaped openings permitting the exchange of gases. B. Bark formed early in the season is called hard bark. C. Bark is a technical term that refers to all tissues exterior to vascular cambium. D. Bark refers to periderm and secondary phloem. E. Phellogen is single-layered in thickness. Choose the correct answer from the options given below: ",
    "options": [
        "A and D only",
        "A, B and D only",
        "B and C only",
        "B, C and E only"
    ],
    "correct_answer": "B, C and E only"
},

{
    "question": "Which of the following statements are correct about Klinefelter’s Syndrome? A. This disorder was first described by Langdon Down (1866). B. Such an individual has overall masculine development. However, the feminine developement is also expressed. C. The affected individual is short statured. D. Physical, psychomotor and mental development is retarded. E. Such individuals are sterile. Choose the correct answer from the options given below: ",
    "options": [
        "C and D only",
        "B and E only",
        "A and E only",
        "A and B only"
    ],
    "correct_answer": "A and B only"
},

{
    "question": "Match List I with List II : List I List II A. M Phase I. Proteins are synthesized B. G2Phase II. Inactive phase C. Quiescent stage III. Interval between mitosis and initiation of DNA replication D. G1Phase IV. Equational division Choose the correct answer from the options given below :",
    "options": [
        "A-IV, B-II, C-I, D-III",
        "A-IV, B-I, C-II, D-III",
        "A-II, B-IV, C-I, D-III",
        "A-III, B-II, C-IV, D-I"
    ],
    "correct_answer": "A-IV, B-I, C-II, D-III"
},

{
    "question": "Match List I with List II: List I List II A. Iron I. Synthesis of auxin B. Zinc II. Component of nitrate reductase C. Boron III. Activator of catalase D. Molybdenum IV. Cell elongation and differentiation Choose the correct answer from the options given below: ",
    "options": [
        "A-II, B-III, C-IV, D-I",
        "A-III, B-I, C-IV, D-II",
        "A-II, B-IV, C-I, D-III",
        "A-III, B-II, C-I, D-IV"
    ],
    "correct_answer": "A-II, B-IV, C-I, D-III"
},

{
    "question": "Given below are two statements: Statement I: In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid. Statement II: In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome. In the light of the above statements, choose the correct answer from the options given below: ",
    "options": [
        "Both Statement I and Statement II are false.",
        "Statement I is correct but Statement II is false.",
        "Statement I is incorrect but Statement II is true.",
        "Both Statement I and Statement II are true."
    ],
    "correct_answer": "Both Statement I and Statement II are true."
},

{
    "question": "In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?",
    "options": [
        "B-lymphocytes",
        "Basophils",
        "Eosinophils",
        "TH cells"
    ],
    "correct_answer": "TH cells"
},

{
    "question": "Which of the following statements is correct?",
    "options": [
        "Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.",
        "Presence of large amount of nutrients in water restricts ‘Algal Bloom’",
        "Algal Bloom decreases fish mortality",
        "Eutrophication refers to increase in domestic sewage and waste water in lakes."
    ],
    "correct_answer": "Biomagnification refers to increase in concentration of the toxicant at successive trophic levels."
},

    {
        "question": "Match List I with List II. List I List II A. P-wave I. Beginning of systole B. Q-wave II. Repolarisation of ventricles C. QRS complex III. Depolarisation of atria D. T-wave IV. Depolarisation of ventricles Choose the correct answer from the options given below :",
        "options": [
            "A-IV, B-III, C-II, D-I",
            "A-II, B-IV, C-I, D-III",
            "A-I, B-II, C-III, D-IV",
            "A-III, B-I, C-IV, D-I"
        ],
        "correct_answer": "A-I, B-II, C-III, D-IV"
    },

    {
        "question": "Broad palm with single palm crease is visible in a person suffering from-",
        "options": [
            "Turner’s syndrome",
            "Klinefelter’s syndrome",
            "Thalassemia",
            "Down’s syndrome"
        ],
        "correct_answer": "Down’s syndrome"
    },

    {
        "question": "Given below are two statements: Statement I: RNA mutates at a faster rate. Statement II: Viruses having RNA genome and shorter life span mutate and evolve faster. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },

    {
        "question": "Given below are two statements: Statement I: Ligaments are dense irregular tissue. Statement II: Cartilage is dense regular tissue. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true",
            "Both Statement I and Statement II are true"
        ],
        "correct_answer": "Statement I is true but Statement II is false"
    },

    {
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. Assertion A: Nephrons are of two types: Cortical & Juxta medullary, based on their relative position in cortex and medulla. Reason R: Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true.",
            "Both A and R are true and R is the correct explanation of A."
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A."
    },

    {
        "question": "Which of the following is not a cloning vector?",
        "options": [
            "YAC",
            "pBR322",
            "Probe",
            "BAC"
        ],
        "correct_answer": "Probe"
    },

    {
        "question": "Given below are two statements: Statement I: A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal). Statement II: Adult human haemoglobin, consists of 4 subunits (two subunits of α type and two subunits of β type.) In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },

{
    "question": " Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by",
    "options": [
        "(1) Ileo-caecal valve",
        "(2) Gastro-oesophageal sphincter",
        "(3) Pyloric sphincter",
        "(4) Sphincter of Oddi"
    ],
    "correct_answer": "(1) Ileo-caecal valve"
},

{
    "question": " Match List I with List II.",
    "options": [
        "A. Vasectomy I. Oral method",
        "B. Coitus interruptus II. Barrier method",
        "C. Cervical caps III. Surgical method",
        "D. Saheli IV. Natural method"
    ],
    "correct_answer": "(3) A-IV, B-II, C-I, D-III"
},

{
    "question": " Which of the following functions is carried out by cytoskeleton in a cell?",
    "options": [
        "(1) Protein synthesis",
        "(2) Motility",
        "(3) Transportation",
        "(4) Nuclear division"
    ],
    "correct_answer": "(2) Motility"
},

{
    "question": " Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?",
    "options": [
        "(1) Gonorrhoea",
        "(2) Hepatitis-B",
        "(3) HIV Infection",
        "(4) Genital herpes"
    ],
    "correct_answer": "(1) Gonorrhoea"
},

{
    "question": " Vital capacity of lung is _________.",
    "options": [
        "(1) IRV + ERV + TV + RV",
        "(2) IRV + ERV + TV – RV",
        "(3) IRV + ERV + TV",
        "(4) IRV + ERV"
    ],
    "correct_answer": "(1) IRV + ERV + TV + RV"
},
{
    "question": " Which of the following are NOT considered as the part of endomembrane system?",
    "options": [
        "A. Mitochondria",
        "B. Endoplasmic reticulum",
        "C. Chloroplasts",
        "D. Golgi complex",
        "E. Peroxisomes"
    ],
    "correct_answer": "(1) A, C and E only"
},

{
    "question": " Match List I with List II.",
    "options": [
        "A. CCK I. Kidney",
        "B. GIP II. Heart",
        "C. ANF III. Gastric gland",
        "D. ADH IV. Pancreas"
    ],
    "correct_answer": "(3) A-IV, B-II, C-III, D-I"
},

{
    "question": "Match List I with List II.",
    "options": [
        "A. Gene ‘a’ I. β-galactosidase",
        "B. Gene ‘y’ II. Transacetylase",
        "C. Gene ‘i’ III. Permease",
        "D. Gene ‘z’ IV. Repressor protein"
    ],
    "correct_answer": "(1) A-II, B-III, C-IV, D-I"
},

{
    "question": " Match List I with List II with respect to the human eye.",
    "options": [
        "A. Fovea I. Visible coloured portion of eye that regulates diameter of pupil.",
        "B. Iris II. External layer of eye formed of dense connective tissue.",
        "C. Blind spot III. Point of greatest visual acuity or resolution.",
        "D. Sclera IV. Point where optic nerve leaves the eyeball and photoreceptor cells are absent."
    ],
    "correct_answer": "(1) A-IV, B-III, C-II, D-I"
},

{
    "question": "Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.",
    "options": [
        "(1) Numbat, Spotted cuscus, Flying phalanger",
        "(2) Mole, Flying squirrel, Tasmanian tiger cat",
        "(3) Lemur, Anteater, Wolf",
        "(4) Tasmanian wolf, Bobcat, Marsupial mole"
    ],
    "correct_answer": "(1) Numbat, Spotted cuscus, Flying phalanger"
},

{
    "question": "Given below are two statements:",
    "options": [
        "Statement I: Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct.",
        "Statement II: The cavity of the cervix is called cervical canal which along with vagina forms birth canal."
    ],
    "correct_answer": "(4) Both Statement I and Statement II are true."
},

{
    "question": "Match List I with List II.",
    "options": [
        "A. Heroin I. Effect on cardiovascular system",
        "B. Marijuana II. Slow down body function",
        "C. Cocaine III. Painkiller",
        "D. Morphine IV. Interfere with transport of dopamine"
    ],
    "correct_answer": "(1) A-I, B-II, C-III, D-IV"
},

{
    "question": " Match List I with List II.",
    "options": [
        "A. Ringworm I. Haemophilus influenzae",
        "B. Filariasis II. Trichophyton",
        "C. Malaria III. Wuchereria bancrofti",
        "D. Pneumonia IV. Plasmodium vivax"
    ],
    "correct_answer": "(2) A-III, B-II, C-I, D-IV"
},

{
    "question": " Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R.",
    "options": [
        "Assertion A : Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme.",
        "Reason R : Ban on amniocentesis checks increasing menace of female foeticide."
    ],
    "correct_answer": "Both A and R are true and R is the correct explanation of A."
},

{
    "question": "Radial symmetry is NOT found in adults of phylum ______.",
    "options": [
        "(1) Hemichordata",
        "(2) Coelenterata",
        "(3) Echinodermata",
        "(4) Ctenophora"
    ],
    "correct_answer": "Echinodermata"
},

{
    "question": " Given below are two statements :",
    "options": [
        "Statement I : Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.",
        "Statement II : When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor."
    ],
    "correct_answer": "Both Statement I and Statement II are true."
},
{
    "question": "Which of the following statements are correct regarding the female reproductive cycle?",
    "options": [
        "A. In non-primate mammals cyclical changes during reproduction are called oestrus cycle.",
        "B. First menstrual cycle begins at puberty and is called menopause.",
        "C. Lack of menstruation may be indicative of pregnancy.",
        "D. Cyclic menstruation extends between menarche and menopause."
    ],
    "correct_answer": "A and B only"
},

{
    "question": "Given below are two statements:",
    "options": [
        "Statement I: Electrostatic precipitator is most widely used in thermal power plant.",
        "Statement II : Electrostatic precipitator in thermal power plant removes ionising radiations."
    ],
    "correct_answer": "tatement I is correct but Statement II is incorrect."
},

{
    "question": " Match List I with List II",
    "options": [
        "A. Peptic cells I. Mucus",
        "B. Goblet cells II. Bile juice",
        "C. Oxyntic cells III. Proenzyme pepsinogen",
        "D. Hepatic cells IV. HCl and intrinsic factor for absorption of vitamin B12"
    ],
    "correct_answer": "A-II, B-I, C-III, D-IV"
},

{
    "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R.",
    "options": [
        "Assertion A: Endometrium is necessary for implantation of blastocyst.",
        "Reason R: In the absence of fertilization, the corpus luteum degenerates that causes disintegration of endometrium."
    ],
    "correct_answer": "Both A and R are true and R is the correct explanation of A."
},
{
  "question": "Which one of the following techniques does not serve the purpose of early diagnosis of a disease for its early treatment?",
  "options": [
    "(1) Serum and Urine analysis",
    "(2) Polymerase Chain Reaction (PCR) technique",
    "(3) Enzyme Linked Immuno-Sorbent Assay (ELISA) technique",
    "(4) Recombinant DNA Technology"
  ],
  "correct_answer": "Recombinant DNA Technology"
},
{
  "question": "Given below are two statements:",
  "options": [
    {
      "Statement I": "During G0 phase of cell cycle, the cell is metabolically inactive.",
      "Statement II": "The centrosome undergoes duplication during S phase of interphase."
    }
  ],
  "correct_answer": "Both Statement I and Statement II are correct."
},

{
  "question": "In cockroach, excretion is brought about by?",
  "options": [
    "A. Phallic gland",
    "B. Urecose gland",
    "C. Nephrocytes",
    "D. Fat body",
    "E. Collaterial glands"
  ],
  "correct_answer": "(3) B and D only"
},

{
  "question": "Select the correct statements.",
  "options": [
    "A. Tetrad formation is seen during Leptotene.",
    "B. During Anaphase, the centromeres split and chromatids separate.",
    "C. Terminalization takes place during Pachytene.",
    "D. Nucleolus, Golgi complex and ER are reformed during Telophase.",
    "E. Crossing over takes place between sister chromatids of homologous chromosome."
  ],
  "correct_answer": "(4) A and C only"
},

{
  "question": "Which of the following are NOT under the control of thyroid hormone?",
  "options": [
    "A. Maintenance of water and electrolyte balance",
    "B. Regulation of basal metabolic rate",
    "C. Normal rhythm of sleep-wake cycle",
    "D. Development of immune system",
    "E. Support the process of RBCs formation"
  ],
  "correct_answer": "(3) D and E only"
},

{
  "question": "Which of the following is characteristic feature of cockroach regarding sexual dimorphism?",
  "options": [
    "1. Presence of anal styles",
    "2. Presence of sclerites",
    "3. Presence of anal cerci",
    "4. Dark brown body colour and anal cerci"
  ],
  "correct_answer": "(4) Dark brown body colour and anal cerci"
},

 {
    "question": "Which of the following statements are correct?",
    "options": [
        "Basophils are most abundant cells of the total WBCs",
        "Basophils secrete histamine, serotonin, and heparin",
        "Basophils are involved in inflammatory response",
        "Basophils have a kidney-shaped nucleus",
        "Basophils are agranulocytes"
    ],
    "correct_answer": "(3) A and B only"
},
{
    "question": "Select the correct statements with reference to chordates.",
    "options": [
        "Presence of a mid-dorsal, solid, and double nerve cord.",
        "Presence of a closed circulatory system.",
        "Presence of paired pharyngeal gill slits.",
        "Presence of a dorsal heart.",
        "Triploblastic pseudocoelomate animals."
    ],
    "correct_answer": "(4) A, C and D only"
},

{
    "question": "The unique mammalian characteristics are:",
    "options": [
        "hairs, pinna and mammary glands",
        "hairs, pinna and indirect development",
        "pinna, monocondylic skull and mammary glands",
        "hairs, tympanic membrane and mammary glands"
    ],
    "correct_answer": "(1) hairs, pinna and mammary glands"
},

 {
    "question": "The unique mammalian characteristics are:",
    "options": [
        "hairs, pinna and mammary glands",
        "hairs, pinna and indirect development",
        "pinna, monocondylic skull and mammary glands",
        "hairs, tympanic membrane and mammary glands"
    ],
    "correct_answer": "(1) hairs, pinna and mammary glands"
},

{
    "question": " The parts of human brain that help in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:",
    "options": [
        "Corpora quadrigemina and hippocampus",
        "Brain stem and epithalamus",
        "Corpus callosum and thalamus",
        "Limbic system and hypothalamus"
    ],
    "correct_answer": "(4) Limbic system and hypothalamus"
},

{
    "question": " Which one of the following is the sequence on corresponding coding strand, if the sequence on mRNA formed is as follows 5’AUCGAUCGAUCGAUCGAUCGAUCG AUCG 3’?",
    "options": [
        "3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’",
        "5’ ATCGATCGATCGATCGATCGATCGATCG 3’",
        "3’ ATCGATCGATCGATCGATCGATCGATCG 5’",
        "5’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 3’"
    ],
    "correct_answer": "(1) 3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’"
},

{
    "question": " Which of the following statements are correct regarding skeletal muscle?",
    "options": [
        "A. Muscle bundles are held together by collagenous connective tissue layer called fascicle.",
        "B. Sarcoplasmic reticulum of muscle fibre is a store house of calcium ions.",
        "C. Striated appearance of skeletal muscle fibre is due to distribution pattern of actin and myosin proteins.",
        "D. M line is considered as functional unit of contraction called sarcomere."
    ],
    "correct_answer": "(2) A, C and D only"
},

{
    "question": "Which one of the following is NOT an advantage of inbreeding?",
    "options": [
        "It exposes harmful recessive genes but are eliminated by selection.",
        "Elimination of less desirable genes and accumulation of superior genes takes place due to it.",
        "It decreases the productivity of inbred population, after continuous inbreeding.",
        "It decreases homozygosity."
    ],
    "correct_answer": "(3) It decreases the productivity of inbred population after continuous inbreeding."
},
 
{
    "question": "A solid sphere rolling on a smooth horizontal surface with constant velocity v enters into rough horizontal surface with same speed v. Choose the correct statement.",
    "options": [
      "Speed of sphere will decrease to 5v/7",
      "Speed of sphere will decrease to 2v/7",
      "Speed of sphere will increase to 7v/5",
      "Speed of sphere will not change"
    ],
    "correct_answer": "Speed of sphere will decrease to 2v/7"
  },

  {
    "question": "Two coaxial solenoids are brought closer till they completely overlap. Their mutual inductance will",
    "options": [
      "Keep on decreasing",
      "Keep on increasing",
      "First decease and then increase",
      "First increase and then decrease"
    ],
    "correct_answer": "First increase and then decrease"
  },

  {
    "question": "A biconvex lens, kept in air, when silvered on one side will act as",
    "options": [
      "Converging lens",
      "Diverging lens",
      "Converging mirror",
      "Diverging mirror"
    ],
    "correct_answer": "Diverging mirror"
  },

  {
    "question": "Choose the correct statement about order of colours in primary and secondary rainbow.",
    "options": [
      "Violet is innermost colour in primary rainbow whereas violet is outermost colour in secondary rainbow",
      "Violet is outermost colour in primary rainbow whereas it is innermost in secondary rainbow",
      "Violet is outermost colour in both primary and secondary rainbow",
      "Violet is innermost colour in both primary and secondary rainbow"
    ],
    "correct_answer": "Violet is innermost colour in primary rainbow whereas violet is outermost colour in secondary rainbow"
  },

  {
    "question": "The phenomenon of the red shift is due to",
    "options": [
      "Increase in wavelength due to doppler effect",
      "Decrease in wavelength due to doppler effect",
      "Increase in frequency due to doppler effect",
      "Both (2) and (3)"
    ],
    "correct_answer": "Increase in wavelength due to doppler effect"
  },
  
 {
    "question": "Statement-I: The first ionisation enthalpy of molecular oxygen is almost identical with that of Xe.\nStatement-II: The electron gain enthalpy Ar is identical with Kr.\nIn the light of the above statements, identify the correct option.",
    "options": [
      "Statement-I is correct but statement-II is incorrect",
      "Statement-I is incorrect but statement-I is correct",
      "Both statement-I and statement-II are true",
      "Both statement-I and statement-II are false"
    ],
    "correct_answer": "Both statement-I and statement-II are false"
  },

  {
    "question": "Monomers of PHBV are",
    "options": [
      "3-hydroxybutanoic acid and 3-hydroxypentanoic acid",
      "2-hydroxypropanoic acid and 3-hydroxybutanoic acid",
      "Ethylene glycol and 3-hydroxypentanoic acid",
      "Adipic acid and hexamethylenediamine"
    ],
    "correct_answer": "3-hydroxybutanoic acid and 3-hydroxypentanoic acid"
  },

{
        "question": "Identify the incorrect statement.",
        "options": [
            "Barbiturates are hypnotic",
            "Norethindrone is an example of synthetic progesterone derivative",
            "Sulphur dioxide and sulphite are useful antioxidants for wine and beer",
            "Aspartame is a trichloroderivative of sucrose"
        ],
        "correct_answer": "Aspartame is a trichloroderivative of sucrose"
    },

    {
        "question": "Ionic mobility of which of the following metal ions is lowest when aqueous solution of their salt are put under an electric field?",
        "options": [
            "Be",
            "Mg",
            "Ca",
            "Sr"
        ],
        "correct_answer": "Sr"
    },

    {
        "question": "Which of the following gas is the major contributor to global warming?",
        "options": [
            "O3",
            "CO2",
            "H2O",
            "N2O"
        ],
        "correct_answer": "CO2"
    },
 
{
        "question": "An atom at the corner of a simple cubic unit cell is shared among how many unit cells?",
        "options": ["2", "4", "6", "8"],
        "correct_answer": "8"
    },

    {
        "question": "Total number of atoms present in a unit cell of diamond is",
        "options": ["6", "8", "4", "2"],
        "correct_answer": "8"
    },

    {
        "question": "IUPAC name of the compound [CoCl2(en)2]Cl is",
        "options": [
            "Bis (ethane-1, 2-diamine) dichloridocobalt (III) chloride",
            "Bis (ethane-1, 2-diamine) dichloridocobalt (II) chloride",
            "Dichloridobis (ethane-1, 2-diamine) cobalt (III) chloride",
            "Dichloridobis (ethane-1, 2-diamine) cobalt (II) chloride"
        ],
        "correct_answer": "Dichloridobis (ethane-1, 2-diamine) cobalt (III) chloride"
    },

    {
        "question": "Statement-I: The stereoisomers related to each other as superimposable mirror images are called enantiomers. Statement-II: If one of the enantiomers is dextro rotatory, the other will be laevo rotatory. In light of above statements, choose the correct answer.",
        "options": [
            "Statement-I is correct but statement-II is incorrect",
            "Statement-I is incorrect but statement-II is correct",
            "Both statement-I and statement-II are correct",
            "Both statement-I and statement-II are incorrect"
        ],
        "correct_answer": "Both statement-I and statement-II are correct"
    },

    {
        "question": "Concentration of CH3COO– ions in a mixture of 0.1 M CH3COOH and 0.1 M HCl is [Ka (CH3COOH) = 1.8 × 10–5]",
        "options": ["1.8 × 10–5 M", "4.2 × 10–3 M", "2.1 × 10–3 M", "2.1 × 10–4 M"],
        "correct_answer": "2.1 × 10–3 M"
    },

 {
        "question": "Consider the following statements about crystallisation technique.\n(a) It is based on the difference in the solubilities of the compound and impurities in a suitable solvent.\n(b) The impure compound is dissolved in a solvent in which it is sparingly soluble at room temperature but appreciably soluble at higher temperature.\n(c) Impurities, which impart colour to the solution are removed by adsorbing over activated charcoal.\nThe correct statements are:",
        "options": [
            "(a) and (b) only",
            "(b) and (c) only",
            "(a) and (c) only",
            "(a), (b) and (c)"
        ],
        "correct_answer": "(a), (b) and (c)"
    },

    {
        "question": "Addition of Br2 to propene in presence of CCl4 involves which intermediate?",
        "options": ["Carbene", "Carbon free radicals", "Carbanion", "Cyclic bromonium ion"],
        "correct_answer": "Cyclic bromonium ion"
    },

{
        "question": "If a cross between violet flowered pea plant and white flowered pea plant produces 50% offspring with violet flowers and 50% offspring with white flowers, the genotypes of parents should be",
        "options": ["Aa × aa", "Aa × Aa", "AA × aa", "AA × Aa"],
        "correct_answer": "Aa × Aa"
    },

    {
        "question": "All of the following were the reasons for use of Drosophila as ideal material for genetic studies, except",
        "options": [
            "It can be grown in simple synthetic medium",
            "Male is larger than female",
            "Easily observable hereditary variations are present",
            "Single mating produces large number of progenies"
        ],
        "correct_answer": "Male is larger than female"
    },

    {
        "question": "A cross was made between a pure round yellow seeded pea plant with wrinkled green seeded pea plant. The F1 progeny obtained is heterozygous round yellow seeded pea plants that were selfed and total 400 seeds are collected. What is the total number of seeds with recombinant traits?",
        "options": ["150", "200", "75", "100"],
        "correct_answer": "100"
    },
    
{
        "question": "Select the incorrect match.",
        "options": [
            "Psilopsida – Pteris",
            "Lycopsida – Selaginella",
            "Pteropsida – Adiantum",
            "Sphenopsida – Equisetum"
        ],
        "correct_answer": "Lycopsida – Selaginella"
    },

    {
        "question": "Which among the following elements is not remobilised?",
        "options": ["Phosphorus", "Nitrogen", "Calcium", "Potassium"],
        "correct_answer": "Calcium"
    },

    {
        "question": "Which of the following bacteria help in denitrification?",
        "options": ["Nitrobacter", "Thiobacillus", "Nitrosomonas", "Nitrococcus"],
        "correct_answer": "Thiobacillus"
    },

    {
        "question": "Centromere splits and chromatids separate during",
        "options": ["Anaphase", "Telophase", "Prophase", "Metaphase"],
        "correct_answer": "Anaphase"
    },

    {
        "question": "Read the following statements and select the correct option. Statement A: Meiosis involves two sequential cycles of nuclear and cell division but only one single cycle of DNA replication. Statement B: Interphase lasts less than 5% of the duration of cell cycle.",
        "options": [
            "Only statement A is correct",
            "Only statement B is correct",
            "Both statements are incorrect",
            "Both statements are correct"
        ],
        "correct_answer": "Both statements are incorrect"
    },

{
        "question": "In the population interaction called commensalism,",
        "options": [
            "Both species are benefitted",
            "One species is benefitted and other is neither harmed nor benefitted",
            "One species is benefitted and other one is harmed",
            "Both species are harmed"
        ],
        "correct_answer": "One species is benefitted and other is neither harmed nor benefitted"
    },

    {
        "question": "Xerarch succession starts in/on",
        "options": ["Pond", "Aquatic regions", "Wetland", "Dry areas"],
        "correct_answer": "Dry areas"
    },

    {
        "question": "Starch synthesis gene in pea seeds shows",
        "options": [
            "Complete dominance",
            "Co-dominance",
            "Incomplete dominance",
            "Epistasis"
        ],
        "correct_answer": "Incomplete dominance"
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
        st.title("Mock Test 8 for NEET Examination")
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