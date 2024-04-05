import streamlit as st # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

# Define fixed questions for the mock test  
# Questions for the mock test
questions = [
    {
        "question": "The ratio of radius of gyration of a solid sphere of mass M and radius R about its own axis to the radius of gyration of the thin hollow sphere of same mass and radius about its axis is",
        "options": [
            "5 : 3",
            "2 : 5",
            "5 : 2",
            "3 : 5"
        ],
        "correct_answer": "3 : 5"
    },
    {
        "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
        "options": [
            "Both Na and K",
            "K only",
            "Na only",
            "Cs only"
        ],
        "correct_answer": "Cs only"
    },
    {
        "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
        "options": [
            "5.06 × 10–4 J",
            "3.01 × 10–4 J",
            "50.1 × 10–4 J",
            "30.16 × 10–4 J"
        ],
        "correct_answer": "3.01 × 10–4 J"
    },
    {
        "question": "Resistance of a carbon resistor determined from colour codes is (22000 ± 5%) Ω. The colour of third band must be",
        "options": [
            "Green",
            "Orange",
            "Yellow",
            "Red"
        ],
        "correct_answer": "Orange"
    },
    {
        "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 μF and resistance R is 100 Ω. The frequency at which resonance occurs is",
        "options": [
            "15.9 kHz",
            "1.59 rad/s",
            "1.59 kHz",
            "15.9 rad/s"
        ],
        "correct_answer": "1.59 kHz"
    },
    {
        "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 10^10 Hz and amplitude 48 V m–1. Then the amplitude of oscillating magnetic field is (Speed of light in free space = 3 × 10^8 m s–1)",
        "options": [
            "1.6 × 10–8 T",
            "1.6 × 10–7 T",
            "1.6 × 10–6 T",
            "1.6 × 10–9 T"
        ],
        "correct_answer": "1.6 × 10–7 T"
    },
    {
        "question": "Given below are two statements:\nStatement I: Photovoltaic devices can convert optical radiation into electricity.\nStatement II: Zener diode is designed to operate under reverse bias in breakdown region.\nIn the light of the above statements, choose the most appropriate correct_answer from the options given below.",
        "options": [
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct",
            "Both Statement I and Statement II are correct"
        ],
        "correct_answer": "Both Statement I and Statement II are correct"
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
        "question": "If ∇∫ E ⋅ dS = 0 over a surface, then",
        "options": [
            "The magnitude of electric field on the surface is constant",
            "All the charges must necessarily be inside the surface",
            "The electric field inside the surface is necessarily uniform",
            "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
        ],
        "correct_answer": "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
    },
    {
        "question": "If the galvanometer G does not show any deflection in the circuit shown, the value of R is given by",
        "options": [
            "50 Ω",
            "100 Ω",
            "400 Ω",
            "200 Ω"
        ],
        "correct_answer": "100 Ω"
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
        "question": "The minimum wavelength of X-rays produced by an electron accelerated through a potential difference of V volts is proportional to",
        "options": [
            "1/V",
            "1/V^2",
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
        "question": "A metal wire has mass (0.4 ± 0.002) g, radius (0.3 ± 0.001) mm and length (5 ± 0.02) cm. The maximum possible percentage error in the measurement of density will nearly be",
        "options": [
            "1.3%",
            "1.6%",
            "1.4%",
            "1.2%"
        ],
        "correct_answer": "1.6%"
    },
    {
        "question": "For Young’s double slit experiment, two statements are given below:\nStatement I : If screen is moved away from the plane of slits, angular separation of the fringes remains constant.\nStatement II : If the monochromatic source is replaced by another monochromatic source of larger wavelength, the angular separation of fringes decreases.\nIn the light of the above statements, choose the correct correct_answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Statement I is true but Statement II is false."
    },
    {
        "question": "The potential energy of a long spring when stretched by 2 cm is U. If the spring is stretched by 8 cm, potential energy stored in it will be",
        "options": [
            "4U",
            "8U",
            "16U",
            "2U"
        ],
        "correct_answer": "16U"
    },
    {
        "question": "Light travels a distance x in time t1 in air and 10x in time t2 in another denser medium. What is the critical angle for this medium?",
        "options": [
            "sin⁻¹(10t2/t1)",
            "sin⁻¹(t1/10t2)",
            "sin⁻¹(10t1/t2)",
            "sin⁻¹(t2/t1)"
        ],
        "correct_answer": "sin⁻¹(10t1/t2)"
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
        "question": "A football player is moving southward and suddenly turns eastward with the same speed to avoid an opponent. The force that acts on the player while turning is",
        "options": [
            "Along northward",
            "Along north-east",
            "Along south-west",
            "Along eastward"
        ],
        "correct_answer": "Along north-east"
    },
    {
        "question": "The magnitude and direction of the current in the following circuit is",
        "options": [
            "0.5 A from A to B through E",
            "5 A from A to B through E",
            "1.5 A from B to A through E",
            "0.2 A from B to A through E"
        ],
        "correct_answer": "0.5 A from A to B through E"
    },
    {
        "question": "The angular acceleration of a body, moving along the circumference of a circle, is",
        "options": [
            "Along the radius towards the centre",
            "Along the tangent to its position",
            "Along the axis of rotation",
            "Along the radius, away from centre"
        ],
        "correct_answer": " Along the axis of rotation"
    },
    {
        "question": "A bullet is fired from a gun at the speed of 280 m s–1 in the direction 30° above the horizontal. The maximum height attained by the bullet is (g = 9.8 m s–2, sin30° = 0.5)",
        "options": [
            "2000 m",
            "1000 m",
            "3000 m",
            "2800 m"
        ],
        "correct_answer": "1000 m"
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
        "question": "The equivalent capacitance of the system shown in the following circuit is",
        "image_url": "image_url_for_circuit_25.png",
        "options": [
            "3 μF",
            "6 μF",
            "9 μF",
            "2 μF"
        ],
        "correct_answer": "2 μF"
    },
    {
        "question": "A vehicle travels half the distance with speed v and the remaining distance with speed 2v. Its average speed is",
        "options": [
            "2v",
            "4v/3",
            "3v/4",
            "v/3"
        ],
        "correct_answer": "4v/3"
    },
    {
        "question": "The half life of a radioactive substance is 20 minutes. In how much time, the activity of substance drops to 1/16th of its initial value?",
        "options": [
            "40 minutes",
            "60 minutes",
            "80 minutes",
            "20 minutes"
        ],
        "correct_answer": "80 minutes"
    },
    {
        "question": "The temperature of a gas is –50°C. To what temperature the gas should be heated so that the rms speed is increased by 3 times?",
        "options": [
            "3295°C",
            "3097 K",
            "223 K",
            "669°C"
        ],
        "correct_answer": "3295°C"
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
        "question": "The magnetic energy stored in an inductor of inductance 4 μH carrying a current of 2 A is",
        "options": [
            "4 mJ",
            "8 mJ",
            "8 μJ",
            "4 μJ"
        ],
        "correct_answer": "8 μJ"
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
        "question": "An electric dipole is placed at an angle of 30° with an electric field of intensity 2 × 10^5 N C–1. It experiences a torque equal to 4 N m. Calculate the magnitude of charge on the dipole, if the dipole length is 2 cm.",
        "options": [
            "6 mC",
            "4 mC",
            "2 mC",
            "8 mC"
        ],
        "correct_answer": "2 mC"
    },
    {
        "question": "In hydrogen spectrum, the shortest wavelength in the Balmer series is λ. The shortest wavelength in the Bracket series is",
        "options": [
            "4λ",
            "9λ",
            "16λ",
            "2λ"
        ],
        "correct_answer": "4λ"
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
        "question": "Two bodies of mass m and 9m are placed at a distance R. The gravitational potential on the line joining the bodies where the gravitational field equals zero, will be (G = gravitational constant)",
        "options": [
            "−12Gm/R",
            "−16Gm/R",
            "−20Gm/R",
            "−8Gm/R"
        ],
        "correct_answer": "−16Gm/R"
    },
    {
        "question": "A bullet from a gun is fired on a rectangular wooden block with velocity u. When bullet travels 24 cm through the block along its length horizontally, velocity of bullet becomes u/3. Then it further penetrates into the block in the same direction before coming to rest exactly at the other end of the block. The total length of the block is",
        "options": [
            "24 cm",
            "28 cm",
            "30 cm",
            "27 cm"
        ],
        "correct_answer": "27 cm"
    },
    {
        "question": "The radius of innermost orbit of hydrogen atom is 5.3 × 10^−11 m. What is the radius of third allowed orbit of hydrogen atom?",
        "options": [
            "1.06 Å",
            "1.59 Å",
            "4.77 Å",
            "0.53 Å"
        ],
        "correct_answer": "4.77 Å"
    },
    {
        "question": "Calculate the maximum acceleration of a moving car so that a body lying on the floor of the car remains stationary. The coefficient of static friction between the body and the floor is 0.15 (g = 10 m s^−2).",
        "options": [
            "150 m s^−2",
            "1.5 m s^−2",
            "50 m s^−2",
            "1.2 m s^−2"
        ],
        "correct_answer": "1.5 m s^−2"
    },
    {
        "question": "10 resistors, each of resistance R are connected in series to a battery of emf E and negligible internal resistance. Then those are connected in parallel to the same battery, the current is increased n times. The value of n is",
        "options": [
            "100",
            "1",
            "1000",
            "10"
        ],
        "correct_answer": "100"
    },
    {
        "question": "A horizontal bridge is built across a river. A student standing on the bridge throws a small ball vertically upwards with a velocity 4 m s^−1. The ball strikes the water surface after 4 s. The height of bridge above water surface is (Take g = 10 m s^−2)",
        "options": [
            "60 m",
            "64 m",
            "68 m",
            "56 m"
        ],
        "correct_answer": "64 m"
    },
    {
        "question": "The net impedance of circuit (as shown in figure) will be",
        "image_url": "image_url_for_circuit_41.png",
        "options": [
            "15 Ω",
            "55 Ω",
            "25 Ω",
            "102 Ω"
        ],
        "correct_answer": "55 Ω"
    },
    {
        "question": "A satellite is orbiting just above the surface of the earth with period T. If d is the density of the earth and G is the universal constant of gravitation, the quantity 3π(Gd)^2 represents",
        "options": [
            "T^2",
            "T^3",
            "T",
            "T^−1"
        ],
        "correct_answer": "T^2"
    },
    {
        "question": "Two thin lenses are of the same focal lengths (f), but one is convex and the other one is concave. When they are placed in contact with each other, the equivalent focal length of the combination will be",
        "options": [
            "f",
            "f/4",
            "Infinite",
            "Zero"
        ],
        "correct_answer": "Infinite"
    },
    {
        "question": "For the following logic circuit, the truth table is",
        "image_url": "image_url_for_circuit_44.png",
        "options": [
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        ],
        "correct_answer": "Option 1"
    },
    {
        "question": "A very long conducting wire is bent in a semi-circular shape from A to B as shown in the figure. The magnetic field at point P for a steady current configuration is given by",
        "image_url": "image_url_for_wire_45.png",
        "options": [
            "μ₀i/4R pointed away from the page",
            "μ₀i[−2/(4Rπ)] pointed away from the page",
            "μ₀i[−2/(4Rπ)] pointed into the page",
            "μ₀i/4R pointed into the page"
        ],
        "correct_answer": "μ₀i[−2/(4Rπ)] pointed away from the page"
    },
    {
        "question": "The resistance of platinum wire at 0°C is 2 Ω and 6.8 Ω at 80°C. The temperature coefficient of resistance of the wire is",
        "options": [
            "3 × 10^−3 °C^−1",
            "3 × 10^−2 °C^−1",
            "3 × 10^−1 °C^−1",
            "3 × 10^−4 °C^−1"
        ],
        "correct_answer": "3 × 10^−2 °C^−1"
    },
    {
        "question": "An electric dipole is placed as shown in the figure. The electric potential (in 10^2 V) at point P due to the dipole is (ε₀ = permittivity of free space and K = 1)",
        "image_url": "image_url_for_dipole_47.png",
        "options": [
            "5qK / 8πε₀",
            "8qK / 5πε₀",
            "8qK / 3πε₀",
            "3qK / 8πε₀"
        ],
        "correct_answer": "3qK / 8πε₀"
    },
    {
        "question": "In the figure shown here, what is the equivalent focal length of the combination of lenses (Assume that all layers are thin)?",
        "image_url": "image_url_for_lenses_48.png",
        "options": [
            "–40 cm",
            "–100 cm",
            "–50 cm",
            "40 cm"
        ],
        "correct_answer": "–100 cm"
    },
    {
        "question": "A wire carrying a current I along the positive x-axis has length L. It is kept in a magnetic field B = (2iˆ + 3ˆj – 4kˆ) T. The magnitude of the magnetic force acting on the wire is",
        "options": [
            "5|L|",
            "5√(L)",
            "3|L|",
            "3√(L)"
        ],
        "correct_answer": "5|L|"
    },
    {
        "question": "The x-t graph of a particle performing simple harmonic motion is shown in the figure. The acceleration of the particle at t = 2 s is",
        "image_url": "image_url_for_graph_50.png",
        "options": [
            "π²/(8) m/s²",
            "π²/(16) m/s²",
            "–π²/(16) m/s²",
            "–π²/(8) m/s²"
        ],
        "correct_answer": "–π²/(16) m/s²"
    },
    {
        "question": "The stability of Cu2+ is more than Cu+ salts in aqueous solution due to",
        "options": [
            "Enthalpy of atomization",
            "Hydration energy",
            "Second ionisation enthalpy",
            "First ionisation enthalpy"
        ],
        "correct_answer": "Hydration energy"
    },
    {
        "question": "Which one is an example of heterogenous catalysis?",
        "options": [
            "Hydrolysis of sugar catalysed by H+ ions",
            "Decomposition of ozone in presence of nitrogen monoxide",
            "Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron",
            "Oxidation of sulphur dioxide into sulphur trioxide in the presence of oxides of nitrogen"
        ],
        "correct_answer": "Combination between dinitrogen and dihydrogen to form ammonia in the presence of finely divided iron"
    },
    {
        "question": "Which amongst the following options are correct graphical representation of Boyle’s Law?",
        "options": [
            "Option (1)",
            "Option (2)",
            "Option (3)",
            "Option (4)"
        ],
        "correct_answer": "Option (1)"
    },
    {
        "question": "In Lassaigne’s extract of an organic compound, both nitrogen and sulphur are present, which gives blood red colour with Fe3+ due to the formation of",
        "options": [
            "NaSCN",
            "[Fe(CN)5NOS]4–",
            "[Fe(SCN)]2+",
            "Fe4[Fe(CN)6]3xH2O"
        ],
        "correct_answer": "[Fe(SCN)]2+"
    },
    {
        "question": "Consider the following reaction and identify the product (P).",
        "image_url": "image_url_for_reaction_56.png",
        "options": [
            "CH3CH = CH – CH3",
            "Product (2)",
            "Product (3)",
            "Product (4)"
        ],
        "correct_answer": "Product (4)"
    },
    {
        "question": "For a certain reaction, the rate = k[A]2[B], when the initial concentration of A is tripled keeping concentration of B constant, the initial rate would",
        "options": [
            "Increase by a factor of six",
            "Increase by a factor of nine",
            "Increase by a factor of three",
            "Decrease by a factor of nine"
        ],
        "correct_answer": "Increase by a factor of nine"
    },
    {
        "question": "Which one of the following statements is correct?",
        "options": [
            "All enzymes that utilise ATP in phosphate transfer require Ca as the cofactor",
            "The bone in human body is an inert and unchanging substance",
            "Mg plays roles in neuromuscular function and interneuronal transmission",
            "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g"
        ],
        "correct_answer": "The daily requirement of Mg and Ca in the human body is estimated to be 0.2-0.3 g"
    },
    {
        "question": "A compound is formed by two elements A and B. The element B forms cubic close packed structure and atoms of A occupy 1/3 of tetrahedral voids. If the formula of the compound is AxBy, then the value of x + y is in option",
        "options": [
            "4",
            "3",
            "2",
            "5"
        ],
        "correct_answer": "5"
    },
    {
        "question": "Homoleptic complex from the following complexes is",
        "options": [
            "Diamminechloridonitrito-N-platinum (II)",
            "Pentaamminecarbonatocobalt (III) chloride",
            "Triamminetriaquachromium (III) chloride",
            "Potassium trioxalatoaluminate (III)"
        ],
        "correct_answer": "Potassium trioxalatoaluminate (III)"
    },
    {
        "question": "The correct order of energies of molecular orbitals of N2 molecule, is",
        "options": [
            "σ1s < σ*1s < σ2s < σ*2s < σ2pz < (π2px = π2py) < (π*2px = π*2py) < σ*2pz",
            "σ1s < σ*1s < σ2s < σ*2s < σ2pz < σ*2pz < (π2px = π2py) < (π*2px = π*2py)",
            "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < (π*2px = π*2py) < σ2pz < σ*2pz",
            "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < σ2pz < (π*2px = π*2py) < σ*2pz"
        ],
        "correct_answer": "σ1s < σ*1s < σ2s < σ*2s < (π2px = π2py) < σ2pz < (π*2px = π*2py) < σ*2pz"
    },
    {
        "question": "Taking stability as the factor, which one of the following represents correct relationship?",
        "options": [
            "InI3 > InI",
            "AlCl > AlCl3",
            "TlI > TlI3",
            "TICI3 > TICI"
        ],
        "correct_answer": "TlI > TII3"
    },
    {
        "question": "Select the correct statements from the following",
        "options": [
            "Atoms of all elements are composed of two fundamental particles.",
            "The mass of the electron is 9.10939 × 10^−31 kg.",
            "All the isotopes of a given element show same chemical properties:",
            "Protons and electrons are collectively known as nucleons.",
            "Dalton’s atomic theory, regarded the atom as an ultimate particles of matter"
        ],
        "correct_answer": "B, C and E only"
    },
    {
        "question": "Which of the following statements are NOT correct?",
        "options": [
            "A. Hydrogen is used to reduce heavy metal oxides to metals.",
            "B. Heavy water is used to study reaction mechanism.",
            "C. Hydrogen is used to make saturated fats from oils.",
            "D. The H-H bond dissociation enthalpy is lowest as compared to a single bond between two atoms of any elements.",
            "E. Hydrogen reduces oxides of metals that are more active than iron."
        ],
        "correct_answer": "D, E only"
    },
    {
        "question": "The given compound is an example of",
        "image_url": "image_url_for_compound_67.png",
        "options": [
            "Aryl halide",
            "Allylic halide",
            "Vinylic halide",
            "Benzylic halide"
        ],
        "correct_answer": "Allylic halide"
    },
    {
        "question": "Identify product (A) in the following reaction:",
        "image_url": "image_url_for_reaction_68.png",
        "options": [
            "Product (1)",
            "Product (2)",
            "Product (3)",
            "Product (4)"
        ],
        "correct_answer": "Product (4)"
    },
    {
        "question": "The conductivity of centimolar solution of KCl at 25°C is 0.0210 ohm–1 cm–1 and the resistance of the cell containing the solution at 25°C is 60 ohm. The value of cell constant is",
        "options": [
            "3.28 cm–1",
            "1.26 cm–1",
            "3.34 cm–1",
            "1.34 cm–1"
        ],
        "correct_answer": "1.26 cm–1"
    },
    {
        "question": "Amongst the given options which of the following molecules/ ion acts as a Lewis acid?",
        "options": [
            "H2O",
            "BF3",
            "OH–",
            "NH3"
        ],
        "correct_answer": "BF3"
    },
    {
        "question": "The relation between nm, (nm = the number of permissible values of magnetic quantum number (m)) for a given value of azimuthal quantum number (l), is",
        "options": [
            "l = 2nm + 1",
            "nm = 2l2 + 1",
            "nm = l + 2",
            "l = nm – 1"
        ],
        "correct_answer": "l = nm – 1"
    },
    {
        "question": "Amongst the following the total number of species NOT having eight electrons around central atom in its outermost shell, is",
        "options": [
            "NH3",
            "AlCl3",
            "BeCl2",
            "CCl4",
            "PCl5"
        ],
        "correct_answer": "4"
    },
    {
        "question": "Intermolecular forces are forces of attraction and repulsion between interacting particles that will include",
        "options": [
            "A. dipole-dipole forces",
            "B. dipole-induced dipole forces",
            "C. hydrogen bonding",
            "D. covalent bonding",
            "E. dispersion forces"
        ],
        "correct_answer": "A, B, C, E are correct"
    },
    {
        "question": "The element expected to form the largest ion to achieve the nearest noble gas configuration is",
        "options": [
            "F",
            "N",
            "Na",
            "O"
        ],
        "correct_answer": "N"
    },
    {
        "question": "Some tranquilizers are listed below. Which one from the following belongs to barbiturates?",
        "options": [
            "Meprobamate",
            "Valium",
            "Veronal",
            "Chlordiazepoxide"
        ],
        "correct_answer": "Veronal"
    },
    {
        "question": "Amongst the following molecules on polymerization produces neoprene?",
        "options": [
            "H2C = C – CH = CH2",
            "H2C = CH – C ≡ CH",
            "H2C = C – CH = CH2",
            "H2C = CH – CH = CH2"
        ],
        "correct_answer": "H2C = C – CH = CH2"
    },
    {
        "question": "Complete the following reaction",
        "image_url": "image_url_for_reaction_80.png",
        "options": [
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        ],
        "correct_answer": "Option 3"
    },
    {
        "question": "Weight (g) of two moles of the organic compound, which is obtained by heating sodium ethanoate with sodium hydroxide in the presence of calcium oxide is :",
        "options": [
            "32",
            "30",
            "18",
            "16"
        ],
        "correct_answer": "32"
    },
    {
        "question": "Which of the following reactions will NOT give a primary amine as the product?",
        "options": [
            "CH3CN → (i) LiAlH4 → Product (ii) H3O+",
            "CH3NC → (i) LiAlH4 → Product (ii) H3O+",
            "CH3CONH2 → (i) LiAlH4 → Product (ii) H3O+",
            "CH3CONH2 → Br2/KOH → Product"
        ],
        "correct_answer": "CH3NC → (i) LiAlH4 → Product (ii) H3O+"
    },
    {
        "question": "The right option for the mass of CO2 produced by heating 20 g of 20% pure limestone is (Atomic mass of Ca = 40)",
        "options": [
            "1.76 g",
            "2.64 g",
            "1.32 g",
            "1.12 g"
        ],
        "correct_answer": "1.76 g"
    },
    {
        "question": "Identify the product in the following reaction:",
        "image_url": "image_url_for_reaction_84.png",
        "options": [
            "(1)",
            "(2)",
            "(3)",
            "(4)"
        ],
        "correct_answer": "(1)"
    },
    {
        "question": "The number of σ bonds, π bonds, and lone pair of electrons in pyridine, respectively are:",
        "options": [
            "12, 3, 0",
            "11, 3, 1",
            "12, 2, 1",
            "11, 2, 0"
        ],
        "correct_answer": "11, 3, 1"
    },
    {
        "question": "Which amongst the following options is the correct relation between change in enthalpy and change in internal energy?",
        "options": [
            "ΔH = ΔU + ΔngRT",
            "ΔH – ΔU = –ΔnRT",
            "ΔH + ΔU = ΔnR",
            "ΔH = ΔU – ΔngRT"
        ],
        "correct_answer": "ΔH = ΔU + ΔngRT"
    },
    {
        "question": "Consider the following reaction : Identify products A and B.",
        "image_url": "image_url_for_reaction_87.png",
        "options": [
            "(1)",
            "(2)",
            "(3)",
            "(4)"
        ],
        "correct_answer": "(2)"
    },
    {
        "question": "Which of the following statements are INCORRECT?",
        "options": [
            "All the transition metals except scandium form MO oxides which are ionic.",
            "The highest oxidation number corresponding to the group number in transition metal oxides is attained in Sc2O3 to Mn2O7.",
            "Basic character increases from V2O3 to V2O4 to V2O5.",
            "V2O4 dissolves in acids to give VO3– salts.",
            "CrO is basic but Cr2O3 is amphoteric."
        ],
        "correct_answer": "C and D only"
    },
    {
        "question": "Which amongst the following is most readily dehydrated under acidic conditions?",
        "options": [
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        ],
        "correct_answer": "Option 1"
    },
    {
        "question": "The reaction that does NOT take place in a blast furnace between 900 K to 1500 K temperature range during extraction of iron is :",
        "options": [
            "FeO + CO → Fe + CO2",
            "C + CO2 → 2CO",
            "CaO + SiO2 → CaSiO3",
            "Fe2O3 + CO → 2FeO + CO2"
        ],
        "correct_answer": "Fe2O3 + CO → 2FeO + CO2"
    },
    {
        "question": "Identify the major product obtained in the following reaction:",
        "image_url": "image_url_for_reaction_91.png",
        "options": [
            "(1)",
            "(2)",
            "(3)",
            "(4)"
        ],
        "correct_answer": "(2)"
    },
    {
        "question": "What fraction of one edge centred octahedral void lies in one unit cell of fcc?",
        "options": [
            "1/3",
            "1/4",
            "1/12",
            "1/2"
        ],
        "correct_answer": "1/4"
    },
    {
        "question": "The equilibrium concentrations of the species in the reaction A + B → C + D are 2, 3, 10, and 6 mol L–1, respectively at 300 K. ΔGº for the reaction is (R = 2 cal/mol K)",
        "options": [
            "–137.26 cal",
            "–1381.80 cal",
            "–13.73 cal",
            "–1372.60 cal"
        ],
        "correct_answer": "–1381.80 cal"
    },
    {
        "question": "Consider the following compounds/species: The number of compounds/species which obey Huckel’s rule is :",
        "image_url": "image_url_for_compounds_94.png",
        "options": [
            "6",
            "2",
            "5",
            "4"
        ],
        "correct_answer": "4"
    },
    {
        "question": "Which complex compound is most stable?",
        "options": [
            "Co(NH3)3(NO3)3",
            "CoCl2(en)2NO3",
            "Co(NH3)6(SO4)3",
            "Co(NH3)4(H2O)Br(NO3)2"
        ],
        "correct_answer": "CoCl2(en)2NO3"
    },
    {
        "question": "On balancing the given redox reaction, aCr2O7^2− + bSO2^−(aq) + cH^+(aq) → 2aCr^3+(aq) + bSO4^2−(aq) + cH2O(l), the coefficients a, b, and c are found to be, respectively-",
        "options": [
            "3, 8, 1",
            "1, 8, 3",
            "8, 1, 3",
            "1, 3, 8"
        ],
        "correct_answer": "1, 3, 8"
    },
    {
        "question": "Given below are two statements: Statement I : The nutrient deficient water bodies lead to eutrophication Statement II : Eutrophication leads to decrease in the level of oxygen in the water bodies. In the light of the above statements, choose the correct correct_answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false",
            "statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true."
    },
    {
        "question": "Identify the final product [D] obtained in the following sequence of reactions: CH3CHO → [A] → [B]",
        "options": [
            "CH3COCH3",
            "C4H10",
            "HC≡CNa+",
            "CH4"
        ],
        "correct_answer": "CH4"
    },
    {
        "question": "Pumice stone is an example of",
        "options": [
            "Gel",
            "Solid sol",
            "Foam",
            "Sol"
        ],
        "correct_answer": "Solid sol"
    },
    {
        "question": "Match List-I with List – II: List-I (Oxoacids of Sulphur) List-II (Bonds)",
        "options": [
            "A–III, B–IV, C–I, D–II",
            "A–I, B–III, C–IV, D–II",
            "A–III, B–IV, C–II, D–I",
            "A–I, B–III, C–II, D–IV"
        ],
        "correct_answer": "A–III, B–IV, C–I, D–II"
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
        "question": "Movement and accumulation of ions across a membrane against their concentration gradient can be explained by",
        "options": [
            "Facilitated Diffusion",
            "Passive Transport",
            "Active Transport",
            "Osmosis"
        ],
        "correct_answer": "Active Transport"
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
        "question": "In tissue culture experiments, leaf mesophyll cells are put in a culture medium to form callus. This phenomenon may be called as",
        "options": [
            "Dedifferentiation",
            "Development",
            "Senescence",
            "Differentiation"
        ],
        "correct_answer": "Dedifferentiation"
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
        "question": "In the equation GPP is Gross Primary Productivity NPP is Net Primary Productivity R here is.",
        "options": [
            "Respiratory quotient",
            "Respiratory loss",
            "Reproductive allocation",
            "Photosynthetically active radiation"
        ],
        "correct_answer": "Respiratory loss"
    },
    {
        "question": "In gene gun method used to introduce alien DNA into host cells, microparticles of metal are used.",
        "options": [
            "Zinc",
            "Tungsten or gold",
            "Silver",
            "Copper"
        ],
        "correct_answer": "Tungsten or gold"
    },
    {
        "question": "The phenomenon of pleiotropism refers to",
        "options": [
            "Presence of two alleles, each of the two genes controlling a single trait",
            "A single gene affecting multiple phenotypic expression",
            "More than two genes affecting a single character",
            "Presence of several alleles of a single gene controlling a single crossover"
        ],
        "correct_answer": "A single gene affecting multiple phenotypic expression"
    },
    {
        "question": "Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R : Assertion A : Late wood has fewer xylary elements with narrow vessels. Reason R : Cambium is less active in winters. In the light of the above statements, choose the correct correct_answer from the options given below :",
        "options": [
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true",
            "Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A"
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
        "question": "Axile placentation is observed in",
        "options": [
            "China rose, Beans and Lupin",
            "Tomato, Dianthus and Pea",
            "China rose, Petunia and Lemon",
            "Mustard, Cucumber and Primrose"
        ],
        "correct_answer": "China rose, Petunia and Lemon"
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
        "question": "The thickness of ozone in a column of air in the atmosphere is measured in terms of:",
        "options": {
            "Decibels",
            "Decameter",
            "Kilobase",
            "Dobson units"
        },
        "correct_answer": "Dobson units"
    },
    {
    "question": "What is the function of tassels in the corn cob?",
    "options": [
        "To trap pollen grains",
        "To disperse pollen grains",
        "To protect seeds",
        "To attract insects"
    ],
    "correct_answer": "To trap pollen grains"
    },
    {
        "question": "Assertion A: The first stage of gametophyte in the life cycle of moss is protonema stage. Reason R: Protonema develops directly from spores produced in capsule.",
        "options": [
            "Both A and R are correct but R is not the correct explanation of A",
            "A is correct but R is not correct",
            "A is not correct but R is correct",
            "Both A and R are correct and R is correct explanation of A"
        ],
        "correct_answer": "Both A and R are correct and R is correct explanation of A"
    },
    {
        "question": "Statement I: The forces generated transpiration can lift a xylem-sized column of water over 130 meters height. Statement II: Transpiration cools leaf surfaces sometimes 10 to 15 degrees evaporative cooling.",
        "options": [
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct",
            "Both Statement I and Statement II are correct"
        ],
        "correct_answer": "Both Statement I and Statement II are correct"
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
        "question": "Expressed Sequence Tags (ESTs) refers to",
        "options": [
            "All genes that are expressed as proteins.",
            "All genes whether expressed or unexpressed.",
            "Certain important expressed genes.",
            "All genes that are expressed as RNA."
        ],
        "correct_answer": "All genes that are expressed as RNA."
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
        "question": "Assertion A: ATP is used at two steps in glycolysis. Reason R: First ATP is used in converting glucose into glucose-6-phosphate and second ATP is used in conversion of fructose-6-phosphate into fructose-1, 6-diphosphate.",
        "options": [
            "Both A and R are true but R is NOT the correct explanation of A.",
            "A is true but R is false.",
            "A is false but R is true.",
            "Both A and R are true and R is the correct explanation of A."
        ],
        "correct_answer": "Both A and R are true and R is the correct explanation of A."
    },
    {
        "question": "Unequivocal proof that DNA is the genetic material was first proposed by",
        "options": [
            "Alfred Hershey and Martha Chase",
            "Avery, Macleoid and McCarthy",
            "Wilkins and Franklin",
            "Frederick Griffith"
        ],
        "correct_answer": "Alfred Hershey and Martha Chase"
    },
    {
        "question": "Identify the correct statements: A. Detrivores perform fragmentation. B. The humus is further degraded by some microbes during mineralization. C. Water soluble inorganic nutrients go down into the soil and get precipitated by a process called leaching. D. The detritus food chain begins with living organisms. E. Earthworms break down detritus into smaller particles by a process called catabolism.",
        "options": [
            "B, C, D only",
            "C, D, E only",
            "D, E, A only",
            "A, B, C only"
        ],
        "correct_answer": "A, B, C only"
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
        "question": "In angiosperm, the haploid, diploid and triploid structures of a fertilized embryo sac sequentially are :",
        "options": [
            "Antipodals, synergids, and primary endosperm nucleus",
            "Synergids, Zygote and Primary endosperm nucleus",
            "Synergids, antipodals and Polar nuclei",
            "Synergids, Primary endosperm nucleus and zygote"
        ],
        "correct_answer": "Synergids, Zygote and Primary endosperm nucleus"
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
        "question": "Cellulose does not form blue colour with Iodine because",
        "options": [
            "It is a helical molecule",
            "It does not contain complex helices and hence cannot hold iodine molecules",
            "It breakes down when iodine reacts with it",
            "It is a disaccharide"
        ],
        "correct_answer": "It does not contain complex helices and hence cannot hold iodine molecules"
    },
    {
        "question": "Among ‘The Evil Quartet’, which one is considered the most important cause driving extinction of species?",
        "options": [
            "Over exploitation for economic gain",
            "Alien species invasions",
            "Co-extinctions",
            "Habitat loss and fragmentation"
        ],
        "correct_answer": "Habitat loss and fragmentation"
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
        "question": "Statement I: Endarch and exarch are the terms often used for describing the position of secondary xylem in the plant body. Statement II: Exarch condition is the most common feature of the root system.",
        "options": [
            "Both Statement I and Statement II are false",
            "Statement I is correct but Statement II is false",
            "Statement I is incorrect but Statement II is true",
            "Both Statement I and Statement II are true"
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true"
    },
    {
        "question": "The process of appearance of recombination nodules occurs at which sub stage of prophase I in meiosis?",
        "options": [
            "Pachytene",
            "Diplotene",
            "Diakinesis",
            "Zygotene"
        ],
        "correct_answer": "Pachytene"
    },
    {
        "question": "Given below are two statements : One labelled as Assertion A and the other labelled as Reason R : Assertion A : In gymnosperms the pollen grains are released from the microsporangium and carried by air currents. Reason R : Air currents carry the pollen grains to the mouth of the archegonia where the male gametes are discharged and pollen tube is not formed. In the light of the above statements, choose the correct correct_answer from the options given below :",
        "options": [
            "Both A and R are true but R is NOT the current explanation of A",
            "A is true but R is false",
            "A is false but R is true",
            "Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "A is true but R is false"
    },
    {
        "question": "Which one of the following statements is NOT correct?",
        "options": [
            "Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries",
            "Water hyacinth grows abundantly in eutrophic water bodies and leads to an imbalance in the ecosystem dynamics of the water body",
            "The amount of some  toxic substances of industrial waste water increases in the organisms at successive trophic levels",
            "The micro-organisms involved in biodegradation of organic matter in a sewage polluted water body consume a lot of oxygen causing the death of aquatic organisms"
        ],
        "correct_answer": "Algal blooms caused by excess of organic matter in water improve water quality and promote fisheries"
    },
    {
        "question": "Which of the following combinations is required for chemiosmosis?",
        "options": [
            "Membrane, proton pump, proton gradient, NADP synthase",
            "Proton pump, electron gradient, ATP synthase",
            "Proton pump, electron gradient, NADP synthase",
            "Membrane, proton pump, proton gradient, ATP synthase"
        ],
        "correct_answer": "Membrane, proton pump, proton gradient, ATP synthase"
    },
    {
        "question": "Match List I with List II : List I List II",
        "options": [
            "A. M Phase : I. Synthesis of auxin",
            "B. G2 Phase : II. Component of nitrate reductase",
            "C. Quiescent stage : III. Activator of catalase",
            "D. G1 Phase : IV. Cell elongation and differentiation"
        ],
        "correct_answer": "B. G2 Phase : II. Component of nitrate reductase"
    },
    {
        "question": "Match List I with List II : List I (Interaction) List II (Species A and B)",
        "options": [
            "A.Mutualism : I. +(A), 0(B)",
            "B.Commensalism : II. –(A), 0(B)",
            "C.Amensalism : III. +(A), –(B)",
            "D.Parasitism : IV. +(A), +(B)"
        ],
        "correct_answer": "A.Mutualism : I. +(A), 0(B)"
    },
    {
        "question": "Given below are two statements: Statement I : Gause’s ‘Competitive Exclusion Principle’ states that two closely related species competing for the same resources cannot co-exist indefinitely and competitively inferior one will be eliminated eventually. Statement II : In general, carnivores are more adversely affected by competition than herbivores. In the light of the above statements, choose the correct correct_answer from the options given below:",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is correct Statement II is false.",
            "Statement I is incorrec but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Statement I is correct Statement II is false."
    },
    {
        "question": "Match List I with List II: List I List II",
        "options": [
            "A.Iron : I. Synthesis of auxin",
            "B.Zinc : II. Component of nitrate reductase",
            "C.Boron : III. Activator of catalase",
            "D.Molybdenum : IV. Cell elongation and differentiation"
        ],
        "correct_answer": "B.Zinc : II. Component of nitrate reductase"
    },
    {
        "question": "Which of the following statements are correct about Klinefelter’s Syndrome? A. This disorder was first described by Langdon Down (1866). B. Such an individual has overall masculine development. However, the feminine developement is also expressed. C. The affected individual is short statured. D. Physical, psychomotor and mental development is retarded. E. Such individuals are sterile. Choose the correct correct_answer from the options given below:",
        "options": [
            "C and D only",
            "B and E only",
            "A and E only",
            "A and B only"
        ],
        "correct_answer": "B and E only"
    },
    {
        "question": "Identify the correct statements: A. Lenticels are the lens-shaped openings permitting the exchange of gases. B. Bark formed early in the season is called hard bark. C. Bark is a technical term that refers to all tissues exterior to vascular cambium. D. Bark refers to periderm and secondary phloem. E. Phellogen is single-layered in thickness. Choose the correct correct_answer from the options given below:",
        "options": [
            "A and D only",
            "A, B and D only",
            "B and C only",
            "B, C and E only"
        ],
        "correct_answer": "A and D only"
    },
    {
        "question": "How many different proteins does the ribosome consist of?",
        "options": [
            "60",
            "40",
            "20",
            "80"
        ],
        "correct_answer": "80"

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
        "question": "Match List I with List II:",
        "options": [
            "A.Cohesion : IV. Attraction towards polar surfaces",
            "B.Adhesion : III. Mutual attraction among water molecules",
            "C.Surface tension: I. More attraction in liquid phase",
            "D.Guttation:  II. Water loss in liquid phase"
        ],
        "correct_answer": "D.Guttation:  II. Water loss in liquid phase"
    },
    {
        "question": "Match List I with List II:",
        "options": [
            "A.Oxidative decarboxylation : II. Pyruvate dehydrogenase",
            "B.Glycolysis : IV. EMP pathway",
            "C.Oxidative phosphorylation : III. Electron transport system",
            "D.Tricarboxylic acid cycle : I. Citrate synthase"
        ],
        "correct_answer": "C.Oxidative phosphorylation : III. Electron transport system"
    },
    {
        "question": "Given below are two statements: One is labelled as Assertion A and the other is labelled as Reason R:",
        "assertion": "A flower is defined as modified shoot wherein the shoot apical meristem changes to floral meristem.",
        "reason": "Internode of the shoot gets condensed to produce different floral appendages laterally at successive node instead of leaves.",
        "options": [
            "Both A and R are true but R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true",
            "Both A and R are true and R correct explanation of A"
        ],
        "correct_answer": "Both A and R are true and R correct explanation of A"
    },
    {
        "question": "Main steps in the formation of Recombinant DNA are given below. Arrange these steps in a correct sequence.",
        "options": [
            "Insertion of recombinant DNA into the host cell",
            "Cutting of DNA at specific location by restriction enzyme",
            "Isolation of desired DNA fragment",
            "Amplification of gene of interest using PCR"
        ],
        "correct_answer": "Amplification of gene of interest using PCR"
    },
    {
        "question": "Which of the following statements are correct regarding female reproductive cycle?",
        "options": [
            "In non-primate mammals cyclical changes during reproduction are called oestrus cycle.",
            "First menstrual cycle begins at puberty and is called menopause.",
            "Lack of menstruation may be indicative of pregnancy.",
            "Cyclic menstruation extends between menarche and menopause."
        ],
        "correct_answer": "Lack of menstruation may be indicative of pregnancy."
    },
    {
        "question": "Given below are two statements: one is labelled as Assertion A and other is labelled as Reason R.",
        "assertion": "Amniocentesis for sex determination is one of the strategies of Reproductive and Child Health Care Programme.",
        "reason": "Ban on amniocentesis checks increasing menace of female foeticide.",
        "options": [
            "Both A and R are true and R is NOT the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true",
            "Both A and R are true and R is the correct explanation of A"
        ],
        "correct_answer": "A is false but R is true"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "A.Leopard and a Lion in a forest/grassland:  I. Competition",
            "B.A Cuckoo laying egg in a Crow’s nest : II. Brood parasitism",
            "C.Fungi and root of a higher plant in Mycorrhizae : III. Mutualism",
            "D.A cattle egret and a Cattle in a field : IV. Commensalism"
        ],
        "correct_answer": "D.A cattle egret and a Cattle in a field : IV. Commensalism"
    },
    {
        "question": "Vital capacity of lung is _ .",
        "options": [
            "IRV + ERV + TV + RV",
            "IRV + ERV + TV – RV",
            "IRV + ERV + TV",
            "IRV + ERV"
        ],
        "correct_answer": "IRV + ERV + TV"
    },
    {
        "question": "Which one of the following common sexually transmitted diseases is completely curable when detected early and treated properly?",
        "options": [
            "Gonorrhoea",
            "Hepatitis-B",
            "HIV Infection",
            "Genital herpes"
        ],
        "correct_answer": "Gonorrhoea"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "A.CCK : III. Gastric gland",
            "B.GIP : IV. Pancreas",
            "C.ANF : II. Heart",
            "D.ADH : I. Kidney"
        ],
        "correct_answer": "D. ADH : I. Kidney"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "A.Ringworm : II. Trichophyton",
            "B.Filariasis: III. Wuchereria bancrofti",
            "C.Malaria : IV. Plasmodium vivax",
            "D.Pneumonia : I. Haemophilus influenzae"
        ],
        "correct_answer": "D.Pneumonia : I. Haemophilus influenzae"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "P-wave: III. Depolarisation of atria",
            "Q-wave: I. Beginning of systole",
            "QRS complex: IV. Depolarisation of ventricles",
            "T-wave: II. Repolarisation of ventricles"
        ],
        "correct_answer": "T-wave: II. Repolarisation of ventricles"
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
        "question": "Given below are two statements:",
        "assertion": "Low temperature preserves the enzyme in a temporarily inactive state whereas high temperature destroys enzymatic activity because proteins are denatured by heat.",
        "reason": "When the inhibitor closely resembles the substrate in its molecular structure and inhibits the activity of the enzyme, it is known as competitive inhibitor.",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Given below are two statements: Statement I: Ligaments are dense irregular tissue. Statement II: Cartilage is dense regular tissue. In the light of the above statements, choose the correct correct_answer from the options given below:",
        "assertion": "Both Statement I and Statement II are false",
        "options": [
            "Both Statement I and Statement II are false",
            "Statement I is true but Statement II is false",
            "Statement I is false but Statement II is true",
            "Both Statement I and Statement II are true"
        ],
        "correct_answer": "Both Statement I and Statement II are false"
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
        "correct_answer": "Mitochondria"
    },
    {
        "question": "Given below are two statements: Statement I: A protein is imagined as a line, the left end represented by first amino acid (C-terminal) and the right end represented by last amino acid (N-terminal). Statement II: Adult human haemoglobin, consists of 4 subunits (two subunits of  type and two subunits of  type.) In the light of the above statements, choose the correct correct_answer from the options given below:",
        "assertion": "Statement I is false but Statement II is true",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true"
        ],
        "correct_answer": "Statement I is false but Statement II is true."
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
        "question": "Match List I with List II.",
        "options": [
            "A.Taenia : I. Nephridia",
            "B.Paramoecium : II. Contractile vacuole",
            "C.Periplaneta : III. Flame cells",
            "D.Pheretima : IV. Urecose gland"
        ],
        "correct_answer": "B.Paramoecium : II. Contractile vacuole"
    },
    {
        "question": "Given below are two statements: Statement I:.Electrostatic precipitator is most widely used in thermal power plant .Statement II : Electrostatic precipitator in thermal power plant removes ionising radiations In the light of the above statements, choose the most appropriate correct_answer from the options given below:",
        "assertion": "Statement I is correct but Statement II is incorrect",
        "options": [
            "Both Statement I and Statement II are incorrect.",
            "Statement I is correct but Statement II is incorrect.",
            "Statement I is incorrect but Statement II is correct.",
            "Both Statement I and Statement II are correct."
        ],
        "correct_answer": "Statement I is correct but Statement II is incorrect."
    },
    {
        "question": "Given below are two statements: Statement I: Vas deferens receives a duct from seminal vesicle and opens into urethra as the ejaculatory duct. Statement Il: The cavity of the cervix is called cervical canal which along with vagina forms birth canal. In the light of the above statements, choose the correct correct_answer from the options given below:",
        "assertion": "Both Statement I and Statement II are true",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Radial symmetry is NOT found in adults of phylum .",
        "options": [
            "Hemichordata",
            "Coelenterata",
            "Echinodermata",
            "Ctenophora"
        ],
        "correct_answer": "Hemichordata"
    },
    {
        "question": "Match List I.with List II",
        "options": [
            "A.Peptic cells : III. Proenzyme pepsinogen",
            "B.Goblet cells : I. Mucus",
            "C.Oxyntic cells : IV. HCl and intrinsic factor for absorption of vitamin B12",
            "D.Hepatic cells : II. Bile juice"
        ],
        "correct_answer": "B.Goblet cells : I. Mucus"
    },
    {
        "question": "Match List I with List II with respect in human eye.",
        "options": [            
            "A.Fovea : III. Point of greatest visual acuity or resolution.",
            "B.Iris :  I. Visible coloured portion of eye that regulates diameter of pupil.",
            "C.Blind spot : IV. Point where optic nerve leaves the eyeball and photoreceptor cells are absent.",
            "D.Sclera : II. External layer of eye formed of dense connective tissue."
        ],
        "correct_answer": "D.Sclera : II. External layer of eye formed of dense connective tissue."
    },
    {
        "question": "Which of the following functions is carried out by cytoskeleton in a cell?",
        "options": [
            "Protein synthesis",
            "Motility",
            "Transportation",
            "Nuclear division"
        ],
        "correct_answer": "Motility"
    },
    {
        "question": "Once the undigested and unabsorbed substances enter the caecum, their backflow is prevented by",
        "options": [
            "Ileo-caecal valve",
            "Gastro-oesophageal sphincter",
            "Pyloric sphincter",
            "Sphincter of Oddi"
        ],
        "correct_answer": "Ileo-caecal valve"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "A. Vasectomy : III. Surgical method",
            "B.Coitus interruptus : IV. Natural method",
            "C. Cervical caps : II. Barrier method",
            "D. Saheli : I. Oral method"
        ],
        "correct_answer": "A. Vasectomy : III. Surgical method"
    },
    {
        "question": "Match List I with List II.",
        "options": [
            "A. Cartilaginous Joint : II. Between adjacent vertebrae in vertebral column",
            "B. Ball and Socket Joint : IV. Between Humerus and Pectoral girdle",
            "C. Fibrous Joint : I. Between flat skull bones",
            "D. Saddle Joint : III. Between carpal and metacarpal of thumb"
        ],
        "correct_answer": "D. Saddle Joint : III. Between carpal and metacarpal of thumb"
    },
    {
        "question": "Given below are two statements: Statement I: RNA mutates at a faster rate. Statement II: Viruses having RNA genome and shorter life span mutate and evolve faster. In the light of the above statements, choose the correct correct_answer from the options given below:",
        "assertion": "Both Statement I and Statement II are true",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is true but Statement II is false.",
            "Statement I is false but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Both Statement I and Statement II are true."
    },
    {
        "question": "Given below are two statements: Statement I: In prokaryotes, the positively charged DNA is held with some negatively charged proteins in a region called nucleoid. Statement II: In eukaryotes, the negatively charged DNA is wrapped around the positively charged histone octamer to form nucleosome.",
        "assertion": "Statement I is incorrect but Statement II is true",
        "options": [
            "Both Statement I and Statement II are false.",
            "Statement I is correct but Statement II is false.",
            "Statement I is incorrect but Statement II is true.",
            "Both Statement I and Statement II are true."
        ],
        "correct_answer": "Statement I is incorrect but Statement II is true."
    },
    {
        "question": "Which one of the following symbols represents mating between relatives in human pedigree analysis?",
        "options": [
            "Symbol 1",
            "Symbol 2",
            "Symbol 3",
            "Symbol 4"
        ],
        "correct_answer": "Symbol 1"
    },
    {
        "question": "Select the correct group/set of Australian Marsupials exhibiting adaptive radiation.",
        "options": [
            "Numbat, Spotted cuscus, Flying phalanger",
            "Mole, Flying squirrel, Tasmanian tiger cat",
            "Lemur, Anteater, Wolf",
            "Tasmanian wolf, Bobcat, Marsupial mole"
        ],
        "correct_answer": "Numbat, Spotted cuscus, Flying phalanger"
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
      "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
      "options": [
        "Both Na and K",
        "K only",
        "Na only",
        "Cs only"
      ],
      "correct_answer": "K only"
    },
    {
      "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
      "options": [
        "5.06 × 10–4 J",
        "3.01 × 10–4 J",
        "50.1 × 10–4 J",
        "30.16 × 10–4 J"
      ],
      "correct_answer": "3.01 × 10–4 J"
    },
    {
      "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 μF and resistance R is 100 Ω. The frequency at which resonance occurs is",
      "options": [
        "15.9 kHz",
        "1.59 rad/s",
        "1.59 kHz",
        "15.9 rad/s"
      ],
      "correct_answer": "1.59 kHz"
    },
    {
      "question": "In a plane electromagnetic wave travelling in free space, the electric field component oscillates sinusoidally at a frequency of 2.0 × 1010 Hz and amplitude 48 V m–1. Then the amplitude of oscillating magnetic field is (Speed of light in free space = 3 × 108 m s–1)",
      "options": [
        "1.6 × 10–8 T",
        "1.6 × 10–7 T",
        "1.6 × 10–6 T",
        "1.6 × 10–9 T"
      ],
      "correct_answer": "1.6 × 10–7 T"
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
        st.title("Mock Test 6 for NEET Examination")
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