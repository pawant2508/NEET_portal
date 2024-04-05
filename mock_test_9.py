import streamlit as st # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin  # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

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
        "question": "Water falls from a height of 60 m at the rate of 10 kg/s to operate a turbine. The losses due to frictional forces are 20% of the input energy. The power generated by the turbine is (g =10 m/s2)",
        "options": [
          "4.8 W",
          "4.8 kW",
          "2.4 kW",
          "6 kW"
        ],
        "correct_answer": "4.8 kW"
      },
      {
        "question": "Match Column-I and Column-II and choose the correct match from the given choices",
        "options": [
          "A  P, B  Q, C  R, D  S",
          "A  Q, B  S, C  R, D  P",
          "A  P, B  S, C  R, D  Q",
          "A  Q, B  R, C  S, D  P"
        ],
        "correct_answer": "A  P, B  Q, C  R, D  S"
      },
      {
        "question": "Consider the following statements (A) and (B) and identify the correct answer.\n(A) Zener diode can be used as voltage regulator.\n(B) In unbiased p-n junction, at thermal equilibrium, drift current is equal to diffusion current.",
        "options": [
          "A is correct but B is incorrect",
          "Both A and B are correct",
          "A is incorrect but B is correct",
          "Both A and B are incorrect"
        ],
        "correct_answer": "Both A and B are correct"
      },
      {
        "question": "A particle is released from height h above the ground. At a certain height, its kinetic energy is two times its potential energy. The speed of the particle at this instant is",
        "options": [
          "2gh",
          "2/3gh",
          "3gh",
          "4/3g"
        ],
        "correct_answer": "2gh"
      },
      {
        "question": "On rounding off the number 4.645 up to three significant figures, the result is",
        "options": [
          "4.64",
          "4.65",
          "4.63",
          "4.60"
        ],
        "correct_answer": "4.65"
      },
      {
        "question": "If the dimensional formula of a physical quantity is given as [MpL qTr ], then the physical quantity will be",
        "options": [
          "Strain if, p = 0, q = 0, r = –1",
          "Stress if, p = 1, q = 1, r = 2",
          "Force if, p = 1, q = 2, r = –2",
          "Surface tension if, p = 1, q = 0, r = –2"
        ],
        "correct_answer": "Force if, p = 1, q = 2, r = –2"
      },
      {
        "question": "Eight drops of the same size are charged at 110 V each. They combine to form a bigger drop. The ratio of potentials of the bigger to each small drop will be",
        "options": [
          "4",
          "2",
          "3",
          "1"
        ],
        "correct_answer": "2"
      },
      {
        "question": "The escape velocity of a body on the surface of an imaginary planet which has thrice the radius as of earth and double the mass of earth, is (ve is the escape velocity at the surface of earth)",
        "options": [
          "2/3ev",
          "3/2ev",
          "2/3ev",
          "3/2ev"
        ],
        "correct_answer": "2/3ev"
      },
      {
        "question": "The sleepers are used below the rails",
        "options": [
          "To increase the cross-sectional area",
          "To decrease the cross-sectional area",
          "To reduce the pressure due to weight of train on rails",
          "Both (1) and (3)"
        ],
        "correct_answer": "To reduce the pressure due to weight of train on rails"
      },
      {
        "question": "A uniform magnetic field of 1.5 T exists in a cylindrical region of radius 10 cm. Its direction is parallel to the axis from east to west. A wire carrying current 5 A in the north to south direction passes through this region. What is the magnitude and direction of the force on the wire, if the wire intersects the axis?",
        "options": [
          "1.5 N, upwards",
          "2.5 N, upwards",
          "1.5 N, downwards",
          "2.5 N, downwards"
        ],
        "correct_answer": "1.5 N, downwards"
      },
      {
        "question": "Which among the following have negative susceptibility?",
        "options": [
          "Calcium",
          "Aluminium",
          "Bismuth",
          "Iron"
        ],
        "correct_answer": "Bismuth"
      },
      {
        "question": "Current in a coil falls from 5.0 A to 1.0 A in 0.1 s. If an average emf of 200 V is induced, then self-inductance of the coil is",
        "options": [
          "4 H",
          "5 H",
          "2 H",
          "10 H"
        ],
        "correct_answer": "2 H"
      },
      {
        "question": "Which among the following represents the expression of displacement current during charging of a capacitor? (Symbols have their usual meaning)",
        "options": [
          "c dV/dt",
          "Ε0 d/dt (Φε)",
          "ε0 dEA/dt",
          "All of these"
        ],
        "correct_answer": "All of these"
      },
      {
        "question": "A series LCR circuit containing 4 H inductor, 100 μF capacitor and 40 Ω resistor is connected to 220 V variable frequency ac source. The frequency of source at which power transferred to the circuit is half the power at resonant angular frequency is nearly",
        "options": [
          "45 rad/s",
          "55 rad/s",
          "50 rad/s",
          "Both (1) and (2)"
        ],
        "correct_answer": "50 rad/s"
      },
      {
        "question": "Column-I contains certain physical quantities and Column-II contains mathematical relations. Symbols used have their usual meaning. Match the Column-I and Column-II.",
        "options": [
          "A → P, B → Q, C → R, D → S",
          "A → P, B → R, C → S, D → Q",
          "A → P, B → R, C → Q, D → S",
          "A → Q, B → P, C → S, D → R"
        ],
        "correct_answer": "A → P, B → R, C → S, D → Q"
      },
      {
        "question": "The De Broglie wavelength λ associated with electrons accelerating through potential difference of 54 V is",
        "options": [
          "0.167 nm",
          "1.227 nm",
          "0.613 nm",
          "0.286 nm"
        ],
        "correct_answer": "0.167 nm"
      },
      {
        "question": "Electric potential at a point P(x, y, z) is V = (x + y + z) V. The electric field at that point is",
        "options": [
          "−i + j + k (V/m)",
          "−i + j + k (V/m)",
          "(x^2 + y^2 + z^2) (V/m)",
          "(V/m) i + j + k"
        ],
        "correct_answer": "−i + j + k (V/m)"
      },
      {
        "question": "A nucleus with mass number 220 initially at rest emits an α-particle. If the Q value of reaction is 11 MeV, then kinetic energy of the α-particle is nearly",
        "options": [
          "10.8 MeV",
          "0.2 MeV",
          "5.5 MeV",
          "9.8 MeV"
        ],
        "correct_answer": "10.8 MeV"
      },
      {
        "question": "The energy of an electron in the nth Bohr’s orbit is proportional to",
        "options": [
          "n^2",
          "n",
          "n^-2",
          "n^-1"
        ],
        "correct_answer": "n^-1"
      },
      {
        "question": "A simple magnifier has converging lens of focal length 2 cm. What is its magnifying power when the image is formed at the near point (D)?",
        "options": [
          "12.5",
          "13.5",
          "14.5",
          "25"
        ],
        "correct_answer": "12.5"
      },
      {
          "question": "The wavefront associated with a line source of wave is",
          "options": [
              "Spherical",
              "Cylindrical",
              "Paraboloid",
              "Ellipsoid"
          ],
          "correct_answer": "Spherical"
      },
      {
          "question": "The coefficient of volume expansion of an ideal gas at constant pressure and at temperature T K is equal to",
          "options": [
              "T",
              "T",
              "2/1 T",
              "1/T"
          ],
          "correct_answer": "1/T"
      },
      {
          "question": "Which among the following is not a greenhouse gas?",
          "options": [
              "CO2",
              "CH4",
              "N2O",
              "O2"
          ],
          "correct_answer": "O2"
      },
      {
          "question": "An electric heater supplies heat to a gaseous system at a rate of 100 W. If the system performs work at a rate of 80 joules per second, then what is the rate at which internal energy increases?",
          "options": [
              "10 J/s",
              "20 J/s",
              "25 J/s",
              "40 J/s"
          ],
          "correct_answer": "20 J/s"
      },
      {
          "question": "A Carnot engine working between 300 K and 600 K has a work output 600 J per cycle. The amount of heat energy supplied to the engine from the source in each cycle is",
          "options": [
              "1200 J",
              "600 J",
              "3600 J",
              "2400 J"
          ],
          "correct_answer": "1200 J"
      },
      {
         
          "question": "A train moves towards a stationary observer with speed 32 m/s. The train sounds whistle and its frequency perceived by observer is f1. If train speed is reduced to 16 m/s. the frequency perceived is f2. The ratio of f1/f2 is (take speed of sound 320 m/s)",
          "options": [
              "18/19",
              "19/18",
              "17/18",
              "18/17"
          ],
          "correct_answer": "18/19"
      },
      {
          "question": "If the emitter current in a common emitter mode of a transistor is 10.2 mA, then the collector current will be (given β = 50)",
          "options": [
              "10 mA",
              "0.2 mA",
              "10.4 mA",
              "9.8 mA"
          ],
          "correct_answer": "10.4 mA"
      },
      {
          "question": "The condition of minimum deviation is achieved in an equilateral prism kept on the prism table of a spectrometer. If the angle of incidence is 53°, the angle of deviation is",
          "options": [
              "40°",
              "46°",
              "53°",
              "43°"
          ],
          "correct_answer": "53°"
      },
      {
          "question": "Highest bond order among the following species is of",
          "options": [
              "O2",
              "O2⁺",
              "O2⁻",
              "2 O2"
          ],
          "correct_answer": "O2"
      },
      {
          
          "question": "Incorrect set of quantum numbers for an electron in an atom is n l ml ms",
          "options": [
              "3 2 0 1/2",
              "2 1 –1 1/2",
              "1 0 0 1/2",
              "2 1 –2 1/2"
          ],
          "correct_answer": "2 1 –1 1/2"
      },
      {
          
          "question": "Statement-I: Terylene is a condensation polymer. Statement-II: Bakelite is a thermosetting plastic. In the light of above statements, choose the correct answer from the options given below.",
          "options": [
              "Statement-I is true but statement-II is false",
              "Statement-I is false but statement-II is true",
              "Both statement-I and statement-II are false",
              "Both statement-I and statement-II are true"
          ],
          "correct_answer": "Both statement-I and statement-II are true"
      },
      {
          
          "question": "Oxidation state of three carbon atoms in C3O2 are",
          "options": [
              "+1, +1, +2",
              "0, +2, +2",
              "0, 0, +4",
              "–2, +3, +3"
          ],
          "correct_answer": "0, +2, +2"
      },
      {
          
          "question": "Gold sol is most easily coagulated by",
          "options": [
              "Mg²⁺",
              "Al³⁺",
              "Cl⁻",
              "SO₄²⁻"
          ],
          "correct_answer": "Al³⁺"
      },
      {
          
          "question": "Maximum prescribed concentration of nitrates in drinking water is",
          "options": [
              "50 ppb",
              "50 ppm",
              "10 ppm",
              "100 pp"
          ],
          "correct_answer": "50 ppm"
      },
      {
        
        "question": "On electrolysis of dilute Na2SO4 using Pt electrodes, the product obtained at the anode will be",
        "options": [
          "SO2(g)",
          "O2(g)",
          "Na(s)",
          "H2(g)"
        ],
        "correct_answer": "O2(g)"
      },
      {
        
        "question": "Most water-soluble sulphate of 2nd group among the following is",
        "options": [
          "BaSO4",
          "CaSO4",
          "BeSO4",
          "MgSO4"
        ],
        "correct_answer": "MgSO4"
      },
      {
        
        "question": "Which among the following equimolar aqueous salt solutions is most acidic in nature?",
        "options": [
          "Sodium sulphate",
          "Potassium acetate",
          "Ammonium chloride",
          "Ammonium acetate"
        ],
        "correct_answer": "Ammonium chloride"
      },
      {
        
        "question": "Which one of the following conditions will favor the maximum formation of the product in the reaction? A(g) + B(g) ↔ C(g) + 2D(g), ΔrH = + x kJ",
        "options": [
          "High pressure and low temperature",
          "High pressure and high temperature",
          "Low pressure and high temperature",
          "Low pressure and low temperature"
        ],
        "correct_answer": "High pressure and low temperature"
      },
      {
        
        "question": "Identify the correct match.",
        "options": [
          "Unnilunium (i) Bohrium",
          "Unnilpentium (ii) Nobelium",
          "Unnilennium (iii) Lawrencium",
          "Unnilhexium (iv) Seaborgium"
        ],
        "correct_answer": "(d), (iv)"
      },
      {
        
        "question": "Which of the following molecules will have zero dipole moment?",
        "options": [
          " ClF3",
          " XeF4",
          "SF4",
          " NF3"
        ],
        "correct_answer": "XeF4"
      },
      {
        
        "question": "An element has a face-centered cubic (fcc) structure with a unit cell edge length of 200 pm. The atomic radius is",
        "options": [
          "100/2pm",
          "200/2pm",
          "100/3pm",
          "3*100 pm"
        ],
        "correct_answer": "100/2pm"
      },
      {
        
        "question": "The mixture which shows negative deviation from Raoult’s law is",
        "options": [
          "Phenol + aniline",
          "Ethanol + water",
          "Benzene + acetone",
          "Acetone + carbon disulphide"
        ],
        "correct_answer": "Ethanol + water"
      },
      {
        
        "question": "Which among the following aqueous solutions will have the highest freezing point?",
        "options": [
          "0.1 m NaCl",
          "0.1 m Urea",
          "0.1 m K2SO4",
          "0.1 m MgCl2"
        ],
        "correct_answer": "0.1 m MgCl2"
      },
      {
        
        "question": "Match the metal ions given in Column I with the spin only magnetic moments of the ions given in Column II and assign the correct code.",
        "options": [
          "a(ii), b(iv), c(v), d(i)",
          "a(iv), b(v), c(i), d(ii)",
          "a(ii), b(iii), c(v), d(i)",
          "a(i), b(iii), c(v), d(iv)"
        ],
        "correct_answer": "a(ii), b(iv), c(v), d(i)"
      },
      {
        
        "question": "The geometry and magnetic behaviour of the complex ion, [Ni(CN)4]2– are",
        "options": [
          "Tetrahedral geometry and paramagnetic",
          "Square planar geometry and diamagnetic",
          "Square planar geometry and paramagnetic",
          "Tetrahedral geometry and diamagnetic"
        ],
        "correct_answer": "Square planar geometry and paramagnetic"
      },
      {
        
        "question": "The correct increasing order of field strength of ligands is",
        "options": [
          "I– < F– < SCN– < S2–",
          "S2– < F– < I– < SCN–",
          "I– < SCN– < S2– < F–",
          "SCN– < S2– < I– < F–"
        ],
        "correct_answer": "I– < F– < SCN– < S2–"
      },
      {
        
        "question": "The major products A and B formed in the following reaction are CH3 – O – CH2 – CH2 – CH3, excess HI   A + B",
        "options": [
          "CH3 – I + (CH3)2CH – I",
          "CH3 – OH + CH3 – CH2 – CH2 – I",
          "CH3 – I + CH3 – CH2 – CH2 – I",
          "CH3 – I + CH3 – CH2 – CH2 – OH"
        ],
        "correct_answer": "CH3 – I + CH3 – CH2 – CH2 – I"
      },
      {
        
        "question": "The hydrocarbon that gives more than one mono-chloro product on chlorination in presence of diffused sunlight, is",
        "options": [
          "Ethane",
          "Neopentane",
          " Cyclohexane",
          "Isobutane"
        ],
        "correct_answer": "Cyclohexane"
      },
      {
        
        "question": "Given below are two statements: Statement-I: Dipole-induced dipole interactions are present in HCI and Ne pair. Statement-II: London forces are associated with polar molecules. In the light of above statements, choose the correct answer from the options given below.",
        "options": [
          "Statement-I is correct but statement-II is incorrect",
          "Statement-I is incorrect but statement-II is correct",
          "Both statement-I and statement-II are incorrect",
          "Both statement-I and statement-II are correct"
        ],
        "correct_answer": "Statement-I is correct but statement-II is incorrect"
      },
      {
        
        "question": "Match list-I with list-II",
        "lists": {
          "List-I": ["Thermodynamic parameters", "a. ΔrH° < 0 and ΔrS° < 0", "b. ΔrH° < 0 and ΔrS° > 0", "c. ΔrH° > 0 and ΔrS° > 0", "d. ΔrH° > 0 and ΔrS° < 0"],
          "List-II": ["Reaction spontaneity", "(i) Non-spontaneous at low temperature", "(ii) Non-spontaneous at all temperature", "(iii) Spontaneous only at low temperature", "(iv) Spontaneous at all temperature"]
        },
        "options": [
          "a(iii), b(i), c(iv), d(ii)",
          "a(iv), b(ii), c(i), d(iii)",
          "a(iv), b(i), c(iii), d(ii)",
          "a(iii), b(iv), c(i), d(ii)"
        ],
        "correct_answer": "a(iv), b(ii), c(i), d(iii)"
      },
      {
        
        "question": "The number of moles of ammonia molecules produced by 10 moles of nitrogen in excess of hydrogen through Haber’s process is",
        "options": ["(1) 30", "(2) 20", "(3) 10", "(4) 15"],
        "correct_answer": "(1) 30"
      },
      {
        
        "question": "When vapours of a primary alcohol is passed over heated copper at 573 K, the product formed is",
        "options": [
          "An aldehyde",
          "An alkene",
          "An ether",
          "A ketone"
        ],
        "correct_answer": " An aldehyde"
      },
      {
        
        "question": "Which of the following compounds will not give positive iodoform test?",
        "options": [
          "Ethanol",
          "Propanone",
          "Benzophenone",
          "Butan-2-ol"
        ],
        "correct_answer": "Benzophenone"
      },
      {
        
        "question": "Which one among the following is the correct expression for isothermal reversible change?",
        "options": [
          "w = –2.303 nR log Vf/Vi",
          "w = –2.303 nRT log Vf/Vi",
          "w = –2.303 nRT log Vi/Vf",
          "w = –nRT log Vf/Vi"
        ],
        "correct_answer": "w = –2.303 nRT log Vf/Vi"
      },
      {
      
      "question": "If the rate constant of a first order reaction is 1.386 × 10–2 s–1 than the half-life period of the reaction will be",
      "options": [
        "50 s",
        " 75 s",
        "25 s",
        "100 s"
      ],
      "correct_answer": " 50 s"
      },
      {
          
          "question": "Essential amino acid among the following is",
          "options": [
              "Alanine",
              "Threonine",
              "Glutamic acid",
              "Serine"
          ],
          "correct_answer": "Threonine"
      },
      {
  
          "question": "In which of the following arrangements the given sequence is not strictly according to the properties indicated against it?",
          "options": [
              " H2O < H2S < H2Se: Increasing acidic character",
              " HBr < HI < HF: Increasing boiling point",
              " HOCI < HOBr < HOI: Increasing acidic strength",
              " As2O3 < Sb2O3 < Bi2O3: Increasing basic character"
          ],
          "correct_answer": " HOCI < HOBr < HOI: Increasing acidic strength"
      },
      {
          
          "question": "Statement-I: AlCl3 is dimerised through halogen bridging. Statement-II: Maximum covalency of boron is six. In the light of the above statements, choose the correct answer from the options given below",
          "options": [
              "Statement-I is incorrect but statement-II is correct",
              "Both statement-I and statement-II are correct",
              "Both statement-I and statement-II are incorrect",
              "Statement-I is correct but statement-II is incorrect"
          ],
          "correct_answer": "Both statement-I and statement-II are incorrect"
      },
      {
          
          "question": "If the conductivity of 0.002 M acetic acid is 9 × 10–5 S cm–1 then the degree of dissociation of 0.002 M acetic acid will be [given: (H+) = 349 S cm2 mol–1 and (CH3COO–) = 41 S cm2 mol–1 ]",
          "options": [
              "0.12",
              "0.25",
              "0.03",
              "0.31"
          ],
          "correct_answer": "0.25"
      },
      {
          
          "question": "Fe2O3 is reduced to FeO in blast furnace in the temperature range of",
          "options": [
              "900-1500 K",
              "800-1200 K",
              "500-800 K",
              "300-500 K"
          ],
          "correct_answer": "800-1200 K"
      },
      {
          
          "question": "Given below are two statements: Statement-I: In all the conformations of ethane, the bond angles are different. Statement-II: In all the conformations of ethane, the bond lengths remain the same. In the light of above statements, choose the correct answer from the options given below.",
          "options": [
              "Statement-I is incorrect but statement-II is correct",
              "Both statement-I and statement-II are correct",
              "Both statement-I and statement-II are incorrect",
              "Statement-I is correct but statement-II is incorrect"
          ],
          "correct_answer": "Both statement-I and statement-II are incorrect"
      },
      {
          
          "question": "Total number of structural isomers of C3H8O are",
          "options": [
              "2",
              "3",
              "4",
              "5"
          ],
          "correct_answer": "4"
      },
      {
          
          "question": "Which among the following reactions is not used for the preparation of benzaldehyde?",
          "options": [
              "Gatterman-Koch reaction",
              "Etard reaction",
              "Hell-Volhard-Zelinsky reaction",
              "Stephen reaction"
          ],
          "correct_answer": "Stephen reaction"
      },
      {
          
          "question": "Right option for the ratio of number of octahedral voids and total octahedral and tetrahedral voids in face centred cubic unit cell is",
          "options": [
              "1 : 2",
              "2 : 3",
              "1 : 3",
              "3 : 2"
          ],
          "correct_answer": "1 : 3"
      },
      {
          
          "question": "Minimum ionic radii among the following is of",
          "options": [
              "Eu3+",
              "Ce3+",
              "Tm3+",
              "Dy3+"
          ],
          "correct_answer": "Tm3+"
      },
      {
          
          "question": "Which one of the following will have largest number of atoms?",
          "options": [
              "3.4 g NH3",
              "3.6 g H2O",
              "0.16 g CH4",
              "13.2 g CO2"
          ],
          "correct_answer": "13.2 g CO2"
      },
      {
          
          "question": "The number of photons of light with a wavelength 6626 pm that provide 1 J of energy is (Planck’s constant (h) = 6.626 ×10–34 Js)",
          "options": [
              "6.66 × 10^15",
              "1.11 × 10^16",
              "2.22 × 10^17",
              "3.33 × 10^16"
          ],
          "correct_answer": "6.66 × 10^15"
      },
      {
          
          "question": "Select the incorrect match.",
          "options": {
              "Herbarium – Preserved plant specimens on sheets",
              "Museum – Conserved animal specimens in a particular area",
              "Key – Analytical in nature",
              "Monograph – Information on any one taxon"
          },
          "correct_answer": "Museum – Conserved animal specimens in a particular area"
      },
      {
          
          "question": "All of the following criteria were used by R.H. Whittaker to propose five kingdom classification, except",
          "options": {
              "Mode of nutrition",
              "Cell structure",
              "Ribosome structure",
              "Cell type"
          },
          "correct_answer": "Ribosome structure"
      },
      {
          
          "question": "Which of the following protists are photosynthetic and good indicators of water pollution?",
          "options": {
              "Diatoms",
              "Dinoflagellates",
              "Euglenoids",
              "Slime moulds"
          },
          "correct_answer": "Diatoms"
      },
      {
         
          "question": "Hydrocolloids like agar agar are present in",
          "options": {
              "Green algae",
              "Red algae",
              "Brown algae",
              "Blue-green algae"
          },
          "correct_answer": "Red algae"
      },
      {
          
          "question": "Select the incorrect statement w.r.t pteridophytes.",
          "options": {
              "Equisetum produces cones",
              "They include ferns and horsetails",
              "The main plant body is sporophyte",
              "Prothallus is gametophytic non-photosynthetic structure"
          },
          "correct_answer": "Prothallus is gametophytic non-photosynthetic structure"
      },
      {
          
          "question": "Axillary buds of stems may also get modified into woody, straight and pointed structures called thorns as in",
          "options": {
              "Opuntia",
              "Bougainvillea",
              "Pumpkin",
              "Cucumber"
          },
          "correct_answer":  "Pumpkin"
      },
      {
          
          "question": "Select the mismatched pair w.r.t. stamen.",
          "options": {
              "Epipetalous – Brinjal",
              "Epitepalous – Mustard",
              "Diadelphous – Pea",
              "Polyadelphous – Citrus"
          },
          "correct_answer": "Epipetalous – Brinjal"
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
        st.title("Mock Test 9 for NEET Examination")
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