import streamlit as st # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

# Define fixed questions for the mock test
questions = [
    {
        "question": "A bullet is fired from a gun at the speed of 280 m s–1 in the direction 30° above the horizontal. The maximum height attained by the bullet is (g = 9.8 m s–2, sin30° = 0.5)",
        "options": [
            "2800 m",
            "2000 m",
            "1000 m",
            "3000 m"
        ],
        "correct_answer": "1000 m"
    },
    {
        "question": "A metal wire has mass (0.4 ± 0.002) g, radius (0.3 ± 0.001) mm and length (5 ± 0.02) cm. The maximum possible percentage error in the measurement of density will nearly be",
        "options": [
            "1.2%",
            "1.3%",
            "1.6%",
            "1.4%"
        ],
        "correct_answer": "1.6%"
    },
    {
        "question": "Given below are two statements: Statement I: Photovoltaic devices can convert optical radiation into electricity. Statement II: Zener diode is designed to operate under reverse bias in breakdown region. In the light of the above statements, choose the most appropriate answer from the options given below.",
        "options": [
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct"
        ],
        "correct_answer": "Both Statement I and Statement II are correct"
    },
    {
        "question": "The magnetic energy stored in an inductor of inductance 4 µH carrying a current of 2 A is",
        "options": [
            "4 µJ",
            "4 mJ",
            "8 mJ",
            "8 µJ"
        ],
        "correct_answer": "8 µJ"
    },
    {
        "question": "If 0 ∮ E dS ⋅ = ∫ ∇E · dS over a surface, then",
        "options": [
            "The number of flux lines entering the surface must be equal to the number of flux lines leaving it",
            "The magnitude of electric field on the surface is constant",
            "All the charges must necessarily be inside the surface",
            "The electric field inside the surface is necessarily uniform"
        ],
        "correct_answer": "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
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
        "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 µF and resistance R is 100 Ω. The frequency at which resonance occurs is",
        "options": [
            "15.9 rad/s",
            "15.9 kHz",
            "1.59 rad/s",
            "1.59 kHz"
        ],
        "correct_answer": "1.59 kHz"
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
        "question": "Let a wire be suspended from the ceiling (rigid support) and stretched by a weight W attached at its free end. The longitudinal stress at any point of cross-sectional area A of the wire is",
        "options": [
            "2W/A",
            "W/A",
            "W/2A",
            "Zero"
        ],
        "correct_answer": "W/A"
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
        "question": "Resistance of a carbon resistor determined from colour codes is (22000 ± 5%) Ω. The colour of third band must be",
        "options": [
            "Red",
            "Green",
            "Orange",
            "Yellow"
        ],
        "correct_answer": "Orange"
    },
    {
        "question": "The minimum wavelength of X-rays produced by an electron accelerated through a potential difference of V volts is proportional to",
        "options": [
            "V",
            "1/V",
            "1/V",
            "V^2"
        ],
        "correct_answer": "1/V"
    },
    {
        "question": "For Young’s double slit experiment, two statements are given below: Statement I : If screen is moved away from the plane of slits, angular separation of the fringes remains constant. Statement II : If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true."
        ],
        "correct_answer": "Statement I is true but Statement II is false."
    },
    {
        "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
        "options": [
            "Cs only",
            "Both Na and K",
            "K only",
            "Na only"
        ],
        "correct_answer": "Cs only"
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
        "question": "An electric dipole is placed at an angle of 30° with an electric field of intensity 2 × 10^5 N C^–1. It experiences a torque equal to 4 N m. Calculate the magnitude of charge on the dipole, if the dipole length is 2 cm.",
        "options": [
            "8 mC",
            "6 mC",
            "4 mC",
            "2 mC"
        ],
        "correct_answer": "2 mC"
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
        "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 10^10 Hz and amplitude 48 V m^–1. Then the amplitude of oscillating magnetic field is (Speed of light in free space = 3 × 10^8 m s^–1)",
        "options": [
            "1.6 × 10^–9 T",
            "1.6 × 10^–8 T",
            "1.6 × 10^–7 T",
            "1.6 × 10^–6 T"
        ],
        "correct_answer": "1.6 × 10^–7 T"
    },
    {
        "question": "Light travels a distance x in time t1 in air and 10x in time t2 in another denser medium. What is the critical angle for this medium?",
        "options": [
            "1/2 * sin^(-1)(t1/t2)",
            "1/2 * sin^(-1)(10t1/t2)",
            "1/2 * sin^(-1)(1/10t1/t2)",
            "1/2 * sin^(-1)(10/t1t2)"
        ],
        "correct_answer": "1/2 * sin^(-1)(10/t1t2)"
    },
    {
        "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m^–1)",
        "options": [
            "30.16 × 10^–4 J",
            "5.06 × 10^–4 J",
            "3.01 × 10^–4 J",
            "50.1 × 10^–4 J"
        ],
        "correct_answer": "3.01 × 10^–4 J"
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
        "question": "The angular acceleration of a body, moving along the circumference of a circle, is",
        "options": [
            "Along the radius, away from centre",
            "Along the radius towards the centre",
            "Along the tangent to its position",
            "Along the axis of rotation"
        ],
        "correct_answer": "Along the axis of rotation"
    },
    {
        "question": "A vehicle travels half the distance with speed v and the remaining distance with speed 2v. Its average speed is",
        "options": [
            "3v",
            "2/3 v",
            "4/3 v",
            "3/4 v"
        ],
        "correct_answer": "4/3 v"
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
        "question": "Two bodies of mass m and 9m are placed at a distance R. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be (G = gravitational constant)",
        "options": [
            "8 - Gm/R",
            "12 - Gm/R",
            "16 - Gm/R",
            "20 - Gm/R"
        ],
        "correct_answer": "16 - Gm/R"
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
        "question": "Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is 0.15 (g = 10 m s–2).",
        "options": [
            "1.2 m s–2",
            "150 m s–2",
            "1.5 m s–2",
            "50 m s–2"
        ],
        "correct_answer": "1.5 m s–2"
    },
    {
        "question": "A wire carrying a current I along the positive x-axis has length L. It is kept in a magnetic field B = 2i + 3j – 4k T. The magnitude of the magnetic force acting on the wire is",
        "options": [
            "3 µIL",
            "5 µIL",
            "5 µIL",
            "3 µIL"
        ],
        "correct_answer": "5 µIL"
    },
    {
        "question": "A bullet from a gun is fired on a rectangular wooden block with velocity u. When bullet travels 24 cm through the block along its length horizontally, velocity of bullet becomes 3u. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is",
        "options": [
            "27 cm",
            "24 cm",
            "28 cm",
            "30 cm"
        ],
        "correct_answer": "27 cm"
    },
    {
        "question": "Two thin lenses are of same focal lengths (f), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be",
        "options": [
            "Zero",
            "f/4",
            "f/2",
            "Infinite"
        ],
        "correct_answer": "Zero"
    },
    {
        "question": "A satellite is orbiting just above the surface of the earth with period T. If d is the density of the earth and G is the universal constant of gravitation, the quantity 3Gd/π represents",
        "options": [
            "T",
            "T^2",
            "T^3",
            "T"
        ],
        "correct_answer": "T^2"
    },
    {
        "question": "The resistance of platinum wire at 0°C is 2 Ω and 6.8 Ω at 80°C. The temperature coefficient of resistance of the wire is",
        "options": [
            "3 × 10–4 °C–1",
            "3 × 10–3 °C–1",
            "3 × 10–2 °C–1",
            "3 × 10–1 °C–1"
        ],
        "correct_answer": "3 × 10–2 °C–1"
    },
    {
        "question": "10 resistors, each of resistance R are connected in series to a battery of emf E and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased n times. The value of n is",
        "options": [
            "10",
            "100",
            "1",
            "1000"
        ],
        "correct_answer": "100"
    },
    {
        "question": "The radius of inner most orbit of hydrogen atom is 5.3 × 10–11 m. What is the radius of third allowed orbit of hydrogen atom?",
        "options": [
            "0.53 Å",
            "1.06 Å",
            "1.59 Å",
            "4.77 Å"
        ],
        "correct_answer": "4.77 Å"
    },
    {
        "question": "A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity 4 m s–1. The ball strikes the water surface after 4 s. The height of bridge above water surface is (Take g = 10 m s–2)",
        "options": [
            "56 m",
            "60 m",
            "64 m",
            "68 m"
        ],
        "correct_answer": "64 m"
    },
    {
        "question": "The relation between nm, (nm = the number of permissible values of magnetic quantum number (m)) for a given value of azimuthal quantum number (l), is",
        "options": [
            "n - 1 = 2l",
            "l = 2nm + 1",
            "nm = 2l^2 + 1",
            "nm = l + 2"
        ],
        "correct_answer": "n - 1 = 2l"
    },
    {
        "question": "The element expected to form largest ion to achieve the nearest noble gas configuration is",
        "options": [
            "O",
            "F",
            "N",
            "Na"
        ],
        "correct_answer": "N"
    },
    {
        "question": "Which amongst the following molecules on polymerization produces neoprene?",
        "options": [
            "HC≡CH",
            "Cl−CH2−CH2−Cl",
            "HC=CCl",
            "CH3−CH2−CH2−Cl"
        ],
        "correct_answer": "Cl−CH2−CH2−Cl"
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
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R: Assertion A: A reaction can have zero activation energy. Reason R: The minimum extra amount of energy absorbed by reactant molecules so that their energy becomes equal to threshold value, is called activation energy. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true and R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "Both A and R are true and R is NOT the correct explanation of A"
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
        "question": "A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy 1/3 of tetrahedral voids. If the formula of the compound is AxBy, then the value of x + y is in option",
        "options": [
            "5",
            "4",
            "3",
            "2"
        ],
        "correct_answer": "5"
    },
    {
        "question": "The right option for the mass of CO2 produced by heating 20 g of 20% pure limestone is (Atomic mass of Ca = 40) 1200 K CaCO3 → CaO + CO2",
        "options": [
            "1.12 g",
            "1.76 g",
            "2.64 g",
            "1.32 g"
        ],
        "correct_answer": "1.76 g"
    },
    {
        "question": "Taking stability as the factor, which one of the following represents correct relationship?",
        "options": [
            "TlCI3 > TlCI",
            "InI3 > InI",
            "AlCl > AlCl3",
            "TlI > TlI3"
        ],
        "correct_answer": "TlCI3 > TlCI"
    },
    {
        "question": "Select the correct statements from the following",
        "options": [
            "A, B and C only",
            "C, D and E only",
            "A and E only",
            "B, C and E only"
        ],
        "correct_answer": "B, C and E only"
    },
    {
        "question": "For a certain reaction, the rate = k[A]2[B], when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would",
        "options": [
            "Decrease by a factor of nine",
            "Increase by a factor of six",
            "Increase by a factor of nine",
            "Increase by a factor of three"
        ],
        "correct_answer": "Increase by a factor of nine"
    },
    {
        "question": "Given below are two statements: Statement I: A unit formed by the attachment of a base to 1 position of sugar is known as nucleoside. Statement II: When nucleoside is linked to phosphorous acid at 5 -position of sugar moiety, we get nucleotide. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true",
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true"
        ],
        "correct_answer": "Statement I is true but Statement II is false"
    },
    {
        "question": "Amongst the given options which of the following molecules/ ion acts as a Lewis acid?",
        "options": [
            "NH3",
            "H2O",
            "BF3",
            "OH–"
        ],
        "correct_answer": "BF3"
    },
    {
        "question": "Which of the following reactions will NOT give primary amine as the product?",
        "options": [
            "Br2/KOH 2 CH3CONH2 Product 3 2 →",
            "(i) LiAlH4 (ii) H2O CH3CN Product →",
            "(i) LiAlH4 (ii) H2O CH3NC Product →",
            "(i) LiAlH4 2 (ii) H2O CH3CONH2 Product →",
        ],
        "correct_answer": "(i) LiAlH4 (ii) H2O CH3NC Product →"
    },
    {
        "question": "Amongst the following the total number of species NOT having eight electrons around central atom in its outermost shell, is NH3, AlCl3, BeCl2, CCl4, PCl5:",
        "options": [
            "3",
            "2",
            "4",
            "1"
        ],
        "correct_answer": "3"
    },
    {
        "question": "Which of the following statements are NOT correct?",
        "options": [
            "B, C, D, E only",
            "B, D only",
            "D, E only",
            "A, B, C only"
        ],
        "correct_answer": "D, E only"
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
        "question": "The number of σ bonds, π bonds and lone pair of electrons in pyridine, respectively are:",
        "options": [
            "11, 2, 0",
            "12, 3, 0",
            "11, 3, 1",
            "12, 2, 1"
        ],
        "correct_answer": "11, 3, 1"
    },
    {
        "question": "Which one of the following statements is correct?",
        "options": [
            "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g",
            "All enzymes that utilise ATP in phosphate transfer require Ca as the cofactor",
            "The bone in human body is an inert and unchanging substance",
            "Mg plays roles in neuromuscular function and interneuronal transmission"
        ],
        "correct_answer": "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g"
    },
    {
        "question": "Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : Assertion A : Metallic sodium dissolves in liquid ammonia giving a deep blue solution, which is paramagnetic. Reason R : The deep blue solution is due to the formation of amide. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "A is true but R is false"
    },
    {
        "question": "The correct order of energies of molecular orbitals of N2 molecule, is",
        "options": [
            "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < σ2pz < (π*2px = π*2py) < σ*2pz",
            "σ1s < σ*1s < σ2s < σ*2s < σ2pz < (π2px = π2py) < (π*2px = π*2py) < σ*2pz",
            "σ1s < σ*1s < σ2s < σ*2s < σ2pz < σ*2pz < (π2px = π2py) < (π*2px = π*2py)",
            "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < (π*2px = π*2py) < σ2pz < σ*2pz"
        ],
        "correct_answer": "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < σ2pz < (π*2px = π*2py) < σ*2pz"
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
        "question": "Intermolecular forces are forces of attraction and repulsion between interacting particles that will include : A. dipole - dipole forces B. dipole - induced dipole forces C. hydrogen bonding D. covalent bonding E. dispersion forces Choose the most appropriate answer from the options given below :",
        "options": [
            "B, C, D, E are correct",
            "A, B, C, D are correct",
            "A, B, C, E are correct",
            "A, C, D, E are correct"
        ],
        "correct_answer": "A, B, C, E are correct"
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
        "question": "Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R Assertion A : Helium is used to dilute oxygen in diving apparatus. Reason R : Helium has high solubility in O2. In the light of the above statements, choose the correct answer from the options given below",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true and R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "Both A and R are true but R is NOT the correct explanation of A"
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
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R Assertion A : In equation ∆rG = –nFEcell’ value of ∆rG depends on n. Reasons R : Ecell is an intensive property and ∆rG is an extensive property. In the light of the above statements, choose the correct answer from the options given below",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true and R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "Both A and R are true and R is NOT the correct explanation of A"
    },
    {
        "question": "In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with Fe3+ due to the formation of",
        "options": [
            "Fe4[Fe(CN)6]3.xH2O",
            "NaSCN",
            "[Fe(CN)5NOS]4–",
            "[Fe(SCN)]2+"
        ],
        "correct_answer": "[Fe(SCN)]2+"
    },
    {
        "question": "Pumice stone is an example of",
        "options": [
            "Sol",
            "Gel",
            "Solid sol",
            "Foam"
        ],
        "correct_answer": "Solid sol"
    },
    {
        "question": "Given below are two statements : Statement I : The nutrient deficient water bodies lead to eutrophication Statement II : Eutrophication leads to decrease in the level of oxygen in the water bodies. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true."
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true."
    },
    {
        "question": "The reaction that does NOT take place in a blast furnace between 900 K to 1500 K temperature range during extraction of iron is :",
        "options": [
            "Fe2O3 + CO → 2FeO + CO2",
            "FeO + CO → Fe + CO2",
            "C + CO2 → 2CO",
            "CaO + SiO2 → CaSiO3"
        ],
        "correct_answer": "Fe2O3 + CO → 2FeO + CO2"
    },
    {
        "question": "The equilibrium concentrations of the species in the reaction A B C D + + are 2, 3, 10 and 6 mol L–1, respectively at 300 K. ∆Gº for the reaction is (R = 2 cal/mol K)",
        "options": [
            "1372.60 cal",
            "–137.26 cal",
            "–1381.80 cal",
            "–13.73 cal"
        ],
        "correct_answer": "–1381.80 cal"
    },
    {
        "question": "Which of the following statements are INCORRECT? A. All the transition metals except scandium form MO oxides which are ionic. B. The highest oxidation number corresponding to the group number in transition metal oxides is attained in Sc2O3 to Mn2O7. C. Basic character increases from V2O3 to V2O4 to V2O5. D. V2O4 dissolves in acids to give 3– VO4 salts. E. CrO is basic but Cr2O3 is amphoteric. Choose the correct answer from the options given below:",
        "options": [
            "A and E only",
            "B and D only",
            "C and D only",
            "B and C only"
        ],
        "correct_answer": "C and D only"
    },
    {
        "question": "Movement and accumulation of ions across a membrane against their concentration gradient can be explained by",
        "options": [
            "Osmosis",
            "Facilitated Diffusion",
            "Passive Transport",
            "Active Transport"
        ],
        "correct_answer": "Active Transport"
    },
    {
        "question": "How many ATP and NADPH2 are required for the synthesis of one molecule of Glucose during Calvin cycle?",
        "options": [
            "12 ATP and 12 NADPH2",
            "18 ATP and 12 NADPH2",
            "12 ATP and 16 NADPH2",
            "18 ATP and 16 NADPH2"
        ],
        "correct_answer": "18 ATP and 12 NADPH2"
    },
    {
        "question": "Which micronutrient is required for splitting of water molecule during photosynthesis?",
        "options": [
            "Manganese",
            "Molybdenum",
            "Magnesium",
            "Copper"
        ],
        "correct_answer": "Manganese"
    },
    {
        "question": "Given below are two statements : Statement I : Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body. Statement II : Exarch condition is the most common feature of the root system. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true",
            "Both Statement I and Statement II are false",
            "Statement I is correct but Statement II is false",
            "Statement I is incorrect but Statement II is true"
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true"
    },
    {
        "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : Late wood has fewer xylary elements with narrow vessels. Reason R : Cambium is less active in winters. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A"
    },
    {
        "question": "During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out",
        "options": [
            "RNA",
            "DNA",
            "Histones",
            "Polysaccharides"
        ],
        "correct_answer": "DNA"
    },
    {
        "question": "In gene gun method used to introduce alien DNA into host cells, microparticles of ________ metal are used.",
        "options": [
            "Copper",
            "Zinc",
            "Tungsten or gold",
            "Silver"
        ],
        "correct_answer": "Tungsten or gold"
    },
    {
        "question": "The historic Convention on Biological Diversity, ‘The Earth Summit’ was held in Rio de Janeiro in the year",
        "options": [
            "1985",
            "1992",
            "1986",
            "2002"
        ],
        "correct_answer": "1992"
    },
    {
        "question": "In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :",
        "options": [
            "Synergids, Primary endosperm nucleus and zygote",
            "Antipodals, synergids, and primary endosperm nucleus",
            "Synergids, Zygote and Primary endosperm nucleus",
            "Synergids, antipodals and Polar nuclei"
        ],
        "correct_answer": "Synergids, Zygote and Primary endosperm nucleus"
    },
    {
        "question": "Upon exposure to UV radiation, DNA stained with ethidium bromide will show",
        "options": [
            "Bright red colour",
            "Bright blue colour",
            "Bright yellow colour",
            "Bright orange colour"
        ],
        "correct_answer": "Bright orange colour"
    },
    {
        "question": "Family Fabaceae differs from Solanaceae and Liliaceae. With respect to the stamens, pick out the characteristics specific to family Fabaceae but not found in Solanaceae or Liliaceae.",
        "options": [
            "Diadelphous and Dithecous anthers",
            "Polyadelphous and epipetalous stamens",
            "Monoadelphous and Monothecous anthers",
            "Epiphyllous and Dithecous anthers"
        ],
        "correct_answer": "Diadelphous and Dithecous anthers"
    },
    {
        "question": "Which hormone promotes internode/petiole elongation in deep water rice?",
        "options": [
            "GA3",
            "Kinetin",
            "Ethylene",
            "2, 4-D"
        ],
        "correct_answer": "Ethylene"
    },
    {
        "question": "Frequency of recombination between gene pairs on same chromosome as a measure of the distance between genes to map their position on chromosome, was used for the first time by",
        "options": [
            "Thomas Hunt Morgan",
            "Sutton and Boveri",
            "Alfred Sturtevant",
            "Henking"
        ],
        "correct_answer": "Alfred Sturtevant"
    },
    {
        "question": "Identify the pair of heterosporous pteridophytes among the following :",
        "options": [
            "Lycopodium and Selaginella",
            "Selaginella and Salvinia",
            "Psilotum and Salvinia",
            "Equisetum and Salvinia"
        ],
        "correct_answer": "Selaginella and Salvinia"
    },
    {
        "question": "What is the role of RNA polymerase III in the process of transcription in Eukaryotes?",
        "options": [
            "Transcription of rRNAs (28S, 18S and 5.8S)",
            "Transcription of tRNA, 5S rRNA and snRNA",
            "Transcription of precursor of mRNA",
            "Transcription of only snRNAs"
        ],
        "correct_answer": "Transcription of tRNA, 5S rRNA and snRNA"
    },
    {
        "question": "Expressed Sequence Tags (ESTs) refers to",
        "options": [
            "All genes that are expressed as RNA.",
            "All genes that are expressed as proteins.",
            "All genes whether expressed or unexpressed.",
            "Certain important expressed genes."
        ],
        "correct_answer": "All genes that are expressed as RNA."
    },
    {
        "question": "Cellulose does not form blue colour with Iodine because",
        "options": [
            "It is a disaccharide",
            "It is a helical molecule",
            "It does not contain complex helices and hence cannot hold iodine molecules",
            "It breaks down when iodine reacts with it"
        ],
        "correct_answer": "It does not contain complex helices and hence cannot hold iodine molecules"
    },
    {
        "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : ATP is used at two steps in glycolysis. Reason R : First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1, 6-diphosphate. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true and R is the correct explanation of A.",
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true."
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A."
    },
    {
        "question": "The phenomenon of pleiotropism refers to",
        "options": [
            "Presence of several alleles of a single gene controlling a single crossover",
            "Presence of two alleles, each of the two genes controlling a single trait",
            "A single gene affecting multiple phenotypic expression",
            "More than two genes affecting a single character"
        ],
        "correct_answer": "A single gene affecting multiple phenotypic expression"
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
        "correct_answer": "Detrivores perform fragmentation."
    },
    {
        "question": "The thickness of ozone in a column of air in the atmosphere is measured in terms of :",
        "options": [
            "Dobson units",
            "Decibels",
            "Decameter",
            "Kilobase"
        ],
        "correct_answer": "Dobson units"
    },
    {
        "question": "Given below are two statements : Statement I : The forces generated transpiration can lift a xylem-sized column of water over 130 meters height. Statement II : Transpiration cools leaf surfaces sometimes 10 to 15 degrees evaporative cooling. In the light of the above statements, choose the most appropriate answer from the options given below :",
        "options": [
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct"
        ],
        "correct_answer": "Both Statement I and Statement II are correct"
    },
    {
        "question": "What is the function of tassels in the corn cob?",
        "options": [
            "To attract insects",
            "To trap pollen grains",
            "To disperse pollen grains",
            "To protect seeds"
        ],
        "correct_answer": "To trap pollen grains"
    },
    {
        "question": "The reaction centre in PS II has an absorption maxima at",
        "options": [
            "680 nm",
            "700 nm",
            "660 nm",
            "780 nm"
        ],
        "correct_answer": "680 nm"
    },
    {
        "question": "In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as",
        "options": [
            "Differentiation",
            "Dedifferentiation",
            "Development",
            "Senescence"
        ],
        "correct_answer": "Dedifferentiation"
    },
    {
        "question": "Given below are two statements : One labelled as Assertion A and the other labelled as Reason R: Assertion A : The first stage of gametophyte in the life cycle of moss is protonema stage. Reason R : Protonema develops directly from spores produced in capsule. In the light of the above statements, choose the most appropriate answer from options given below:",
        "options": [
            "Both A and R are correct and R is the correct explanation of A",
            "Both A and R are correct but R is NOT the correct explanation of A",
            "A is correct but R is not correct",
            "A is not correct but R is correct"
        ],
        "correct_answer": "Both A and R are correct and R is the correct explanation of A"
    },
    {
        "question": "Among eukaryotes, replication of DNA takes place in :",
        "options": [
            "M phase",
            "S phase",
            "G1 phase",
            "G2 phase"
        ],
        "correct_answer": "S phase"
    },
    {
        "question": "Axile placentation is observed in",
        "options": [
            "Mustard, Cucumber and Primrose",
            "China rose, Beans and Lupin",
            "Tomato, Dianthus and Pea",
            "China rose, Petunia and Lemon"
        ],
        "correct_answer": "China rose, Petunia and Lemon"
    },
    {
        "question": "In the equation GPP − R = NPP, GPP is Gross Primary Productivity NPP is Net Primary Productivity R here is ________.",
        "options": [
            "Photosynthetically active radiation",
            "Respiratory quotient",
            "Respiratory loss",
            "Reproductive allocation"
        ],
        "correct_answer": "Respiratory loss"
    },
    {
        "question": "Which of the following stages of meiosis involves division of centromere?",
        "options": [
            "Metaphase I",
            "Metaphase II",
            "Anaphase II",
            "Telophase"
        ],
        "correct_answer": "Anaphase II"
    },
    {
        "question": "Spraying of which of the following phytohormone on juvenile conifers helps hastening the maturity period, that leads early seed production?",
        "options": [
            "Indole-3-butyric Acid",
            "Gibberellic Acid",
            "Zeatin",
            "Abscisic Acid"
        ],
        "correct_answer": "Gibberellic Acid"
    },
    {
        "question": "Unequivocal proof that DNA is the genetic material was first proposed by",
        "options": [
            "Frederick Griffith",
            "Alfred Hershey and Martha Chase",
            "Avery, Macleoid and McCarthy",
            "Wilkins and Franklin"
        ],
        "correct_answer": "Alfred Hershey and Martha Chase"
    },
    {
        "question": "Large, colourful, fragrant flowers with nectar are seen in",
        "options": [
            "Insect pollinated plants",
            "Bird pollinated plants",
            "Bat pollinated plants",
            "Wind pollinated plants"
        ],
        "correct_answer": "Insect pollinated plants"
    },
    {
        "question": "The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?",
        "options": [
            "Zygotene",
            "Pachytene",
            "Diplotene",
            "Diakinesis"
        ],
        "correct_answer": "Pachytene"
    },
    {
        "question": "Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?",
        "options": [
            "Habitat loss and fragmentation",
            "Over exploitation for economic gain",
            "Alien species invasions",
            "Co-extinctions"
        ],
        "correct_answer": "Habitat loss and fragmentation"
    },
    {
        "question": "Identify the correct statements:",
        "options": [
            "Lenticels are the lens-shaped openings permitting the exchange of gases.",
            "Bark formed early in the season is called hard bark.",
            "Bark is a technical term that refers to all tissues exterior to vascular cambium.",
            "Bark refers to periderm and secondary phloem.",
            "Phellogen is single-layered in thickness."
        ],
        "correct_answer": "A and D only"
    },
    {
        "question": "Melonate inhibits the growth of pathogenic bacteria by inhibiting the activity of",
        "options": [
            "Succinic dehydrogenase",
            "Amylase",
            "Lipase",
            "Dinitrogenase"
        ],
        "correct_answer": "Succinic dehydrogenase"
    },
    {
        "question": "Which of the following statements are correct about Klinefelter’s Syndrome?",
        "options": [
            "This disorder was first described by Langdon Down (1866).",
            "Such an individual has overall masculine development. However, the feminine development is also expressed.",
            "The affected individual is short statured.",
            "Physical, psychomotor and mental development is retarded.",
            "Such individuals are sterile."
        ],
        "correct_answer": "B and E only"
    },
    {
        "question": "Which of the following combinations is required for chemiosmosis?",
        "options": [
            "Membrane, proton pump, proton gradient, ATP synthase",
            "Membrane, proton pump, proton gradient, NADP synthase",
            "Proton pump, electron gradient, ATP synthase",
            "Proton pump, electron gradient, NADP synthase"
        ],
        "correct_answer": "Membrane, proton pump, proton gradient, ATP synthase"
    },
    {
        "question": "How many different proteins does the ribosome consist of?",
        "options": [
            "80",
            "60",
            "40",
            "20"
        ],
        "correct_answer": "80"
    },
    {
        "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem. Reason R : Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A"
    },
    {
        "question": "Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : Assertion A : In gymnosperms the pollen grains are released from the microsporangium and carried by air currents. Reason R : Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "correct_answer": "A is true but R is false"
    },
    {
        "question": "Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence. A Insertion of recombinant DNA into the host cell B Cutting of DNA at specific location by restriction enzyme C Isolation of desired DNA fragment D Amplification of gene of interest using PCR Choose the correct answer from the options given below :",
        "options": [
            "B, C, D, A",
            "C, A, B, D",
            "C, B, D, A",
            "B, D, A, C"
        ],
        "correct_answer": "B, C, D, A"
    },
    {
        "question": "Given below are two statements: Statement I : Gause’s ‘Competitive Exclusion Principle’ states that two closely related species competing for the same resources cannot co-exist indefinitely and competitively inferior one will be eliminated eventually. Statement II : In general, carnivores are more adversely affected by competition than herbivores. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is correct Statement II is false.",
            "Statement I is incorrect but Statement II is true."
        ],
        "correct_answer": "Statement I is correct Statement II is false."
    },
    {
        "question": "Which one of the following statements is NOT correct?",
        "options": [
            "The micro-organisms involved in biodegradation of organic matter in a sewage polluted water body consume a lot of oxygen causing the death of aquatic organisms",
            "Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries",
            "Water hyacinth grows abundantly in eutrophic water bodies and leads to an imbalance in the ecosystem dynamics of the water body",
            "The amount of some toxic substances of industrial waste water increases in the organisms at successive trophic levels"
        ],
        "correct_answer": "Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries"
    },
    {
        "question": "In which blood corpuscles, the HIV undergoes replication and produces progeny viruses?",
        "options": [
            "TH cells",
            "B-lymphocytes",
            "Basophils",
            "Eosinophils"
        ],
        "correct_answer": "TH cells"
    },
    {
        "question": "Which of the following is not a cloning vector?",
        "options": [
            "BAC",
            "YAC",
            "pBR322",
            "Probe"
        ],
        "correct_answer": "Probe"
    },
    {
        "question": "Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by",
        "options": [
            "Sphincter of Oddi",
            "Ileo-caecal valve",
            "Gastro-oesophageal sphincter",
            "Pyloric sphincter"
        ],
        "correct_answer": "Ileo-caecal valve"
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R. Assertion A : Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme. Reason R : Ban on amniocentesis checks increasing menace of female foeticide. In the light of the above statements, choose the correct answer from the options given below.",
        "options": [
            "Both A and R are true and R is the correct explanation of A.",
            "Both A and R are true and R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true."
        ],
        "correct_answer": "A is false but R is true."
    },
    {
        "question": "Which one of the following techniques does not serve the purpose of early diagnosis of a disease for its early treatment?",
        "options": [
            "Recombinant DNA Technology",
            "Serum and Urine analysis",
            "Polymerase Chain Reaction (PCR) technique",
            "Enzyme Linked Immuno-Sorbent Assay (ELISA) technique"
        ],
        "correct_answer": "Serum and Urine analysis"
    },
    {
        "question": "Statement A: Psoriasis and Alzheimer’s disease are the result of autoimmunity.",
        "Statement_B": "Autoimmune response is responsible for non-acceptance of transplanted tissue/organ.",
        "options": [
            "Both Statement A and Statement B are correct.",
            "Both Statement A and Statement B are incorrect.",
            "Statement A is correct but Statement B is incorrect.",
            "Statement A is incorrect but Statement B is correct."
        ],
        "correct_answer": "Statement A is correct but Statement B is incorrect."
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. Assertion A: Endometrium is necessary for implantation of blastocyst. Reason R: In the absence of fertilization, the corpus luteum degenerates that causes disintegration of endometrium. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both A and R are true and R is the correct explanation of A.",
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true."
        ],
        "correct_answer": "Both A and R are true but R is NOT the correct explanation of A."
    },
    {
        "question": "Given below are two statements: Statement I: Ligaments are dense irregular tissue. Statement II: Cartilage is dense regular tissue. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true",
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true"
        ],
        "correct_answer": "Both Statement I and Statement II are false"
    },
    {
        "question": "Which of the following functions is carried out by cytoskeleton in a cell?",
        "options": [
            "Nuclear division",
            "Protein synthesis",
            "Motility",
            "Transportation"
        ],
        "correct_answer": "Motility"
    },
    {
        "question": "Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.",
        "options": [
            "Tasmanian wolf, Bobcat, Marsupial mole",
            "Numbat, Spotted cuscus, Flying phalanger",
            "Mole, Flying squirrel, Tasmanian tiger cat",
            "Lemur, Anteater, Wolf"
        ],
        "correct_answer": "Numbat, Spotted cuscus, Flying phalanger"
    },
    {
        "question": "Which of the following statements are correct regarding female reproductive cycle?",
        "options": [
            "In non-primate mammals cyclical changes during reproduction are called oestrus cycle.",
            "First menstrual cycle begins at puberty and is called menopause.",
            "Lack of menstruation may be indicative of pregnancy.",
            "Cyclic menstruation extends between menarche and menopause."
        ],
        "correct_answer": "A, C and D only"
    },
    {
        "question": "Broad palm with single palm crease is visible in a person suffering from-",
        "options": [
            "Down’s syndrome",
            "Turner’s syndrome",
            "Klinefelter’s syndrome",
            "Thalassemia"
        ],
        "correct_answer": "Down’s syndrome"
    },
    {
        "question": "Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?",
        "options": [
            "Genital herpes",
            "Gonorrhoea",
            "Hepatitis-B",
            "HIV Infection"
        ],
        "correct_answer": "Gonorrhoea"
    },
    {
        "question": "Given below are two statements: Statement I: In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid. Statement II: In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true."
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true."
    },
    {
        "question": "Given below are two statements: Statement I: RNA mutates at a faster rate. Statement II: Viruses having RNA genome and shorter life span mutate and evolve faster. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Radial symmetry is NOT found in adults of phylum ______.",
        "options": [
            "Ctenophora",
            "Hemichordates",
            "Coelenterata",
            "Echinodermata"
        ],
        "correct_answer": "Hemichordates"
    },
    {
        "question": "Which of the following are NOT considered as the part of endomembrane system?",
        "options": [
            "Mitochondria",
            "Endoplasmic reticulum",
            "Chloroplasts",
            "Golgi complex",
            "Peroxisomes"
        ],
        "correct_answer": "A, C and E only"
    },
    {
        "question": "Given below are two statements : Statement I : Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat. Statement II : When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor. In the light of the above statements, choose the correct answer from the options given below :",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Given below are two statements: Statement I: A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal). Statement II: Adult human haemoglobin, consists of 4 subunits (two subunits of α type and two subunits of β type.) In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true",
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true"
        ],
        "correct_answer": "Statement I is false but Statement II is true"
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. Assertion A: Nephrons are of two types: Cortical & Juxta medullary, based on their relative position in cortex and medulla. Reason R: Juxta medullary nephrons have short loop of Henle whereas, cortical nephrons have longer loop of Henle. In the light of the above statements, choose the correct answer from the options given below: ",
        "options": [
            "Both A and R are true and R is the correct explanation of A.",
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true."
        ],
        "correct_answer": "A is true but R is false."
    },
    {
        "question": "Which of the following statements is correct?",
        "options": [
            "Eutrophication refers to increase in domestic sewage and waste water in lakes.",
            "Biomagnification refers to increase in concentration of the toxicant at successive trophic levels.",
            "Presence of large amount of nutrients in water restricts ‘Algal Bloom’",
            "Algal Bloom decreases fish mortality"
        ],
        "correct_answer": "Biomagnification refers to increase in concentration of the toxicant at successive trophic levels."
    },
    {
        "question": "Given below are two statements: Statement I: Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct. Statement II: The cavity of the cervix is called cervical canal which along with vagina forms birth canal. In the light of the above statements, choose the correct answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are true.",
            "Both Statement I and Statement II are false.",
            "Statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Vital capacity of lung is _________.",
        "options": [
            "IRV + ERV",
            "IRV + ERV + TV + RV",
            "IRV + ERV + TV – RV",
            "IRV + ERV + TV"
        ],
        "correct_answer": "IRV + ERV + TV"
    },
    {
        "question": "In cockroach, excretion is brought about byA. Phallic gland B. Urecose gland C. Nephrocytes D. Fat body E. Collaterial glands Choose the correct answer from the options given below :",
        "options": [
            "A and E only",
            "A, B and E only",
            "B, C and D only",
            "B and D only"
        ],
        "correct_answer": "B, C and D only"
    },
    {
        "question": "Which one of the is the sequence on corresponding coding strand, if the sequence on mRNA formed is as follows 5’AUCGAUCGAUCGAUCGAUCGAUCG AUCG 3’?",
        "options": [
            "5’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 3’",
            "3’ UAGCUAGCUAGCUAGCUAGCUAGCUAGC 5’",
            "5’ ATCGATCGATCGATCGATCGATCGATCG 3’",
            "3’ ATCGATCGATCGATCGATCGATCGATCG 5’"
        ],
        "correct_answer": "5’ ATCGATCGATCGATCGATCGATCGATCG 3’"
    },
    {
        "question": "Which of the following statements is incorrect?",
        "options": [
            "Yeasts have filamentous bodies with long thread-like hyphae.",
            "Morels and truffles are edible delicacies.",
            "Claviceps is a source of many alkaloids and LSD.",
            "Conidia are produced exogenously and ascospores endogenously."
        ],
        "correct_answer": "Yeasts have filamentous bodies with long thread-like hyphae."
    },
    {
        "question": "Which of the following is characteristic feature of cockroach regarding sexual dimorphism?",
        "options": [
            "Dark brown body colour and anal cerci",
            "Presence of anal styles",
            "Presence of sclerites",
            "Presence of anal cerci"
        ],
        "correct_answer": "Presence of anal styles"
    },
    {
        "question": "The unique mammalian characteristics are:",
        "options": [
            "hairs, tympanic membrane and mammary glands",
            "hairs, pinna and mammary glands",
            "hairs, pinna and indirect development",
            "pinna, monocondylic skull and mammary glands"
        ],
        "correct_answer": "hairs, pinna and mammary glands"
    },
    {
        "question": "Select the correct statements.",
        "options": [
            "A and C only",
            "B and D only",
            "A, C and E only",
            "B and E only"
        ],
        "correct_answer": "B and D only"
    },
    {
        "question": "Which of the following statements are correct?",
        "options": [
            "D and E only",
            "C and E only",
            "B and C only",
            "A and B only"
        ],
        "correct_answer": "B and C only"
    },
    {
        "question": "The parts of human brain that helps in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:",
        "options": [
            "Limbic system and hypothalamus",
            "Corpora quadrigemina and hippocampus",
            "Brain stem and epithalamus",
            "Corpus callosum and thalamus"
        ],
        "correct_answer": "Limbic system and hypothalamus"
    },
    {
        "question": "Which of the following are NOT under the control of thyroid hormone? A. Maintenance of water and electrolyte balance B. Regulation of basal metabolic rate C. Normal rhythm of sleep-wake cycle D. Development of immune system E. Support the process of RBCs formation Choose the correct answer from the options given below:",
        "options": [
            "A and D only",
            "B and C only",
            "C and D only",
            "D and E only"
        ],
        "correct_answer": "C and D only"
    },
    {
        "question": "Select the correct statements with reference to chordates. A. Presence of a mid-dorsal, solid and double nerve cord. B. Presence of closed circulatory system. C. Presence of paired pharyngeal gill slits. D. Presence of dorsal heart E. Triploblastic pseudocoelomate animals. Choose the correct answer from the options given below:",
        "options": [
            "A, C and D only",
            "B and C only",
            "B, D and E only",
            "C, D and E only"
        ],
        "correct_answer": "B and C only"
    },
    {
        "question": "Which of the following statements are correct regarding skeletal muscle?",
        "options": [
            "Muscle bundles are held together by collagenous connective tissue layer called fascicle.",
            "Sarcoplasmic reticulum of muscle fibre is a storehouse of calcium ions.",
            "Striated appearance of skeletal muscle fibre is due to the distribution pattern of actin and myosin proteins.",
            "M line is considered as the functional unit of contraction called sarcomere."
        ],
        "correct_answer": "Sarcoplasmic reticulum of muscle fibre is a storehouse of calcium ions."
    },
    {
        "question": "Which one of the following is NOT an advantage of inbreeding?",
        "options": [
            "It decreases homozygosity.",
            "It exposes harmful recessive genes but are eliminated by selection.",
            "Elimination of less desirable genes and accumulation of superior genes takes place due to it.",
            "It decreases the productivity of inbred population, after continuous inbreeding."
        ],
        "correct_answer": "It decreases the productivity of inbred population, after continuous inbreeding."
    },
    {
        "question": "Which of the features of life forms can be seen in non-living objects too?",
        "options": [
            "Reproduction", 
            "Consciousness",
            "Growth", 
            "Sensitivity to touch"
        ],
        "correct_answer": "Growth"
    },
    {
        "question": "Select the incorrect match w.r.t. mango.",
        "options": [
            "Family – Anacardiaceae",
            "Class – Dicotyledonae",
            "Order – Sapindales",
            "Division – Plantae"
        ],
        "correct_answer": "Division – Plantae"
    },
    {
        "question": "How many TCA cycles are required for the complete oxidation of one molecule of glucose?",
        "options": [
            "One",
            "Two",      
            "Three",        
            "Four"
        ],
        "correct_answer": "Two"
    },
    {
        "question": "Read the following statements and select the correct option.\nStatement A: In Mung bean, resistance to yellow mosaic virus is due to mutation breeding.\nStatement B: Parbhani Kranti is resistant to yellow mosaic virus.",
        "options": [
            "Only statement A is correct",
            "Only statement B is correct",
            "Both statements A and B are correct",
            "Both statements A and B are incorrect"
        ],
        "correct_answer": "Only statement A is correct"
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
        "options": [
            "Pond",     
            "Aquatic regions",      
            "Wetland",      
            "Dry areas"
        ],
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
    {
        "question": "The genetic material in tobacco mosaic virus is",
        "options": [
            "dsDNA",        
            "ssDNA",        
            "dsRNA",        
            "ssRNA"
        ],
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
    {
        "question": "National park",
        "options": [
            "Is Ex-situ conservation strategy",
            "Is reserved for betterment of wildlife",
            "Consists of core, buffer and transition zones",
            "In also called Island of pristine forests"
        ],
        "correct_answer": "Consists of core, buffer and transition zones"
    },
    {
        "question": "Which of the following statements is incorrect w.r.t. active transport?",
        "options": [
            "It requires special membrane proteins",
            "It is highly selective",
            "The carrier proteins are sensitive to inhibitors",
            "It is downhill transport"
        ],
        "correct_answer": "It is downhill transport"
    },
    {
        "question": "Which among the following shows haplontic life cycle?",
        "options": [
            "Spirogyra",
            "Ectocarpus",
            "Fucus", 
            "Cycas"
        ],
        "correct_answer": "Ectocarpus"
    },
    {
        "question": "Select the odd one out w.r.t. day neutral plants.",
        "options": [
            "Cucumber",
            "Tobacco",
            "Tomato",
            "Pepper"
        ],
        "correct_answer": "Pepper"
    },
    {
        "question": "Non-photosynthetic bacteria which fix atmospheric nitrogen while free living in the soil is",
        "options": [
            "Anabaena",
            "Nostoc",
            "Azospirillum",
            "Oscillatoria"
        ],
        "correct_answer": "Azospirillum"
    },
    {
        "question": "Which of the following is not amongst the major functions of epidermal tissue system in flowering plants?",
        "options": [
            "Protection",
            "Gaseous exchange",
            "Photosynthesis",
            "Absorption of water and minerals"
        ],
        "correct_answer": "Photosynthesis"
    },
    {
        "question": "Read the given statements and select the correct option.\nStatement-A: Respiratory system of cockroach consists of a network of trachea, that open through 20 small holes called spiracles.\nStatement-B: Many species of cockroach are of great economic importance.",
        "options": [
            "Both statements are correct",
            "Both statements are incorrect",
            "Only statement A is correct",
            "Only statement B is correct"
        ],
        "correct_answer": "Both statements are correct"
    },
    {
        "question": "The main function of epithelium lining the dry surface of skin is",
        "options": [
            "Protection against chemical and mechanical stresses",
            "Secretion",
            "Absorption",
            "Forming a diffusion boundary"
        ],
        "correct_answer": "Protection against chemical and mechanical stresses"
    },
    {
        "question": "Which one of the following is a fat soluble vitamin and its related deficiency disease?",
        "options": [
            "Vitamin A : Rickets",
            "Vitamin B3 : Pellagra",
            "Vitamin C : Scurvy",
            "Vitamin K : Faulty blood clotting"
        ],
        "correct_answer": "Vitamin A : Rickets"
    },
    {
        "question": "Which of the following enzymes are not present in succus entericus?",
        "options": [
            "Dipeptidases",
            "Lipases",
            "Amylases",
            "Nucleosidases"
        ],
        "correct_answer": "Amylases"
    },
    {
        "question": "The formed elements in blood which are phagocytic in function but differ in their contribution in total WBCs count are\na. Neutrophils\nb. Eosinophils\nc. Basophils\nd. Lymphocytes\ne. Monocytes\nSelect the correct option.",
        "options": [
            "a and e",
            "a, b and c",
            "e and d",
            "b and c"
        ],
        "correct_answer": "e and d"
    },
    {
        "question": "Given below are four statements regarding human circulatory system.\na. Heart failure is sometimes called congestive heart failure.\nb. During joint diastole, all four chambers of heart are in contracted state.\nc. A special neural centre is present in the medulla oblongata that can moderate the cardiac function through ANS.\nd. Maximum filling of blood in ventricles occurs during joint diastole.\nWhich of the above statements are correct?",
        "options": [
            "a, b and c",
            "a, b, c and d",
            "b, c and d", 
            "a, c and d"
        ],
        "correct_answer": "a, b and c"
    },
    {
        "question": "Choose the odd one w.r.t. closed circulatory system.",
        "options": [
            "Nereis",
            "Ichthyophis",
            "Palaemon",
            "Pteropus"
        ],
        "correct_answer": "Ichthyophis"
    },
    {
        "question": "Select the layer of filtration membrane of nephrons which is responsible for the formation of the filtration slits.",
        "options": [
            "Endothelium of vasa recta",
            "Basement membrane of PCT",
            "Endothelium of glomerular blood vessels",
            "Podocytes forming visceral layer of Bowman’s capsule"
        ],
        "correct_answer": "Podocytes forming visceral layer of Bowman’s capsule"
    },
    {
        "question": "Identify the disorder among the following whose common cause is the decreased levels of estrogen in blood plasma.",
        "options": [
            "Tetany",
            "Gout",
            "Osteoporosis",
            "Arthritis"
        ],
        "correct_answer": "Osteoporosis"
    },
    {
        "question": "Select the bone that is a part of axial skeleton.",
        "options": [
            "Coccyx",
            "Clavicle",
            "Carpal",
            "Coxal"
        ],
        "correct_answer": "Coccyx"
    }
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
        st.title("Mock Test 7 for NEET Examination")
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