import streamlit as st  # type: ignore
from firebase_admin import firestore # type: ignore
import firebase_admin # type: ignore
import time

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize Firebase app
    firebase_admin.initialize_app()

# questions for the mock test
questions = [
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
    "question": "The intensity of the electric field produced by the radiation coming from a 200 W bulb at a distance of 3 m is",
    "options": [
      "0.022 W/m2",
      "0.88 W/m2",
      "0.046 W/m2",
      "0.059 W/m2"
    ],
    "correct_answer": "0.022 W/m2"
  },
  {
    "question": "The dimensional formula for thermal resistance is",
    "options": [
      "M^−1L^−2T^3K",
      "ML^2T^−2K^−1",
      "ML^2T^−3K",
      "ML^2T^−2K^−2"
    ],
    "correct_answer": "ML^2T^−3K"
  },
  {
    "question": "A wall has two layers A and B made of different materials. The thickness of both the layers is same. The thermal conductivity of A and B are KA and KB such that KA = 3KB. The temperature across wall is 20°C. In thermal equilibrium",
    "options": [
      "Temperature difference across A = 15°C",
      "Temperature difference across A = 5°C",
      "Temperature difference across A = 10°C",
      "Temperature difference across A = 25°C"
    ],
    "correct_answer": "Temperature difference across A = 15°C"
  },
  {
    "question": "Consider the Bohr model of hydrogen like atom. Column-I contains some entries and Column-II contains proportionality on atomic number Z.",
    "options": [
      "A(R), B(P), C(S), D(Q)",
      "A(P), B(Q), C(R), D(S)",
      "A(R), B(Q), C(S), D(P)",
      "A(S), B(P), C(Q), D(R)"
    ],
    "correct_answer": "A(R), B(P), C(S), D(Q)"
  },
  {
    "question": "For thermonuclear fusion reaction, the estimated temperature of the system should be about",
    "options": [
      "3 × 10^9 K",
      "3 × 10^5 K",
      "3 × 10^3 K",
      "3 × 10^6 K"
    ],
    "correct_answer": "3 × 10^6 K"
  },
  {
    "question": "Consider the following two statements. (A) For a charged particle moving from point ‘P’ to point ‘Q’, the net work done by an electrostatic field on the particle is independent of the path connecting point P to point Q. (B) The net work done by a conservative force on an object moving along closed loop is zero. Which of the following option is true?",
    "options": [
      "Statement A is correct while statement B is incorrect",
      "Statement B is correct while statement A is incorrect",
      "Statement A and statement B, both are correct",
      "Statement A and statement B, both are incorrect"
    ],
    "correct_answer": "Statement A and statement B, both are correct"
  },
  {
    "question": "The acceleration ‘a’ of a body starting from rest varies with time ‘t’ as a = 3t + 4 in SI units. The velocity of the body at time t = 2 s will be",
    "options": [
      "10 m/s",
      "18 m/s",
      "14 m/s",
      "26 m/s"
    ],
    "correct_answer": "10 m/s"
  },
  {
    "question": "The velocity of a small ball of mass 10 g and density 7.8 g/cc when dropped in a container filled with glycerine becomes constant after some time. If the density of glycerine is 1.3 g/cc, what is the viscous force acting on the ball?",
    "options": [
      "5.126 × 10^3 dyne",
      "8.166 × 10^3 dyne",
      "7.521 × 10^3 dyne",
      "1633.33 dyne"
    ],
    "correct_answer": "8.166 × 10^3 dyne"
  },
  {
    "question": "A source of sound is travelling towards a stationary observer. The frequency of sound heard by the observer is 20% more than the actual frequency. If the speed of sound is v, then speed of source is",
    "options": [
      "v/4",
      "v/3",
      "v/2",
      "v/6"
    ],
    "correct_answer": "v/6"
  },
{
    "question": "A wave of length 2 m is superposed on its reflected wave to form a stationary wave. A node is located at x = 3 m. The next node will be located at x =",
    "options": [
      "3.25 m",
      "3.50 m",
      "3.75 m",
      "4 m"
    ],
    "correct_answer": "3.25 m"
  },
  {
    "question": "In a common emitter amplifier, using output resistance of 5000 Ω and the input resistance 2000 Ω, if the peak value of input signal voltage is 100 mV and β = 50, then the peak value of output voltage is",
    "options": [
      "5 × 10^–6 V",
      "12.5 × 10^–4 V",
      "12.5 V",
      "1.25 V"
    ],
    "correct_answer": "12.5 V"
  },
  {
    "question": "When n-p-n transistor is used as an amplifier",
    "options": [
      "Electron move from emitter to collector",
      "Holes move from emitter to base",
      "Electrons move from collector to base",
      "Holes move from base to collector"
    ],
    "correct_answer": "Electrons move from collector to base"
  },
  {
    "question": "A circular railway track of radius r is banked at angle θ so that a train moving with speed v can safely go round the track. A student writes: tanθ = rg/v^2. Why this relation is not correct?",
    "options": [
      "(i)",
      "(ii)",
      "Both (i) and (ii)",
      "Neither (i) nor (ii)"
    ],
    "correct_answer": "Both (i) and (ii)"
  },
  {
    "question": "The product of 1.2, 2.54 and 3.257 is",
    "options": [
      "9.934",
      "9.93",
      "9.9346",
      "9.9"
    ],
    "correct_answer": "9.9346"
  },
  {
    "question": "A time varying horizontal force F = at acts on a block of mass m kept on a smooth horizontal surface. An identical block is kept on the first block. The coefficient of friction between the blocks is μ. The time after which the relative sliding between the blocks prevails is",
    "options": [
      "2mg/a",
      "2μmg/a",
      "μmg/a",
      "2μmga"
    ],
    "correct_answer": "2mg/a"
  },
  {
    "question": "Two wires P and Q are made of same material and have same volume. The length of P is 3 times that of Q. If they are stretched by same force, then find out the ratio of increment in their lengths.",
    "options": [
      "3 : 4",
      "5 : 8",
      "6 : 7",
      "9 : 1"
    ],
    "correct_answer": "6 : 7"
  },
  {
    "question": "In a thermodynamic process, work done on the system is 100 J and heat given to system is 500 cal. Then calculate change in internal energy of system. (approx)",
    "options": [
      "254 cal",
      "245 cal",
      "524 cal",
      "542 cal"
    ],
    "correct_answer": "254 cal"
  },
  {
    "question": "A short bar magnet is placed with its north pole pointing north. The neutral point is 10 cm away from the centre of the magnet. If H (horizontal component of earth’s magnetic filed) = 0.4G, calculate the magnetic moment of magnet.",
    "options": [
      "0.8 A m^2",
      "0.1 A m^2",
      "0.4 A m^2",
      "0.6 A m^2"
    ],
    "correct_answer": "0.4 A m^2"
  },
  {
    "question": "An inductor of resistance 200 Ω and self inductance 1 H is connected to an ac-source of frequency 100/π Hz. Find out the phase difference between voltage and current in circuit.",
    "options": [
      "60°",
      "30°",
      "45°",
      "Zero"
    ],
    "correct_answer": "Zero"
  },
  {
    "question": "Calculate the least amount of work that must be done to freeze one gram of water at 0°C by means of a refrigerator. Temperature of surroundings is 27°C. Latent heat of fusion L = 80 cal/g.",
    "options": [
      "2.91 cal",
      "3.91 cal",
      "6 cal",
      "7.91 cal"
    ],
    "correct_answer": "2.91 cal"
  },
  {
    "question": "If the duration of an event measured is 5.00 second, then the maximum percentage error in the measurement will be",
    "options": [
      "0.01%",
      "0.4%",
      "0.2%",
      "0.3%"
    ],
    "correct_answer": "0.01%"
  },
  {
    "question": "The magnetic induction at a point distance ‘X’ from the centre, on the axis of a circular current carrying coil is inversely proportional to (if X >> radius of coil)",
    "options": [
      "X",
      "X^2",
      "X^3",
      "X^3/2"
    ],
    "correct_answer": "X^3"
  },
  {
    "question": "A piece of pure gold of density 19.3 g/cc is suspected to be hollow inside. It weighs 38.250 g in air and 33.865 g in water. Calculate the volume of the hollow portion of the gold.",
    "options": [
      "6.403 cm^3",
      "5.402 cm^3",
      "1.659 cm^3",
      "2.403 cm^3"
    ],
    "correct_answer": "6.403 cm^3"
  },
{
    "question": "A 400 W sodium street lamp emits yellow light of wavelength 0.6 μm. Assuming it to be 50% efficient in converting electrical energy to light the approximate number of photons of yellow light it emits per second is",
    "options": [
      "3 × 10^20",
      "1.2 × 10^18",
      "5 × 10^22",
      "6 × 10^20"
    ],
    "correct_answer": "1.2 × 10^18"
  },
  {
    "question": "The 6563 Å wavelength emitted by a hydrogen in star is found to be red-shifted by 15 Å. The speed with which star is receding away from the earth is",
    "options": [
      "5.79 × 10^6 m/s",
      "7.62 × 10^3 m/s",
      "6.85 × 10^5 m/s",
      "4.22 × 10^5 m/s"
    ],
    "correct_answer": "5.79 × 10^6 m/s"
  },
  {
    "question": "An object is kept at a distance of 20 cm from a concave lens of focal length 10 cm. At what distance from the lens should a concave mirror of focal length 30 cm be placed such that the final image coincides with object?",
    "options": [
      "10 cm",
      "20 cm",
      "160/3 cm",
      "100/3 cm"
    ],
    "correct_answer": "160/3 cm"
  },
  {
    "question": "Limiting friction due to normal force 10 N and coefficient of friction 0.2 is",
    "options": [
      "10 N",
      "20 N",
      "2 N",
      "4 N"
    ],
    "correct_answer": "2 N"
  },
  {
    "question": "The KC for the reaction A + B 2C is 9. If one mole A and B are mixed initially in 10 L container then equilibrium concentration of C is",
    "options": [
      "3/5 M",
      "3/50 M",
      "6/5 M",
      "3/25 M"
    ],
    "correct_answer": "6/5 M"
  },
  {
    "question": "Octet rule is not valid in",
    "options": [
      "N2O3",
      "N2O",
      "NO",
      "N2O5"
    ],
    "correct_answer": "N2O"
  },
  {
    "question": "Which of the following mixture of solution will lead to the formation of negatively charged colloidal [Agl]/l– sol?",
    "options": [
      "100 ml of 0.1 M AgNO3 + 100 ml of 0.1 M KI",
      "100 ml of 0.1 M AgNO3 + 50 ml of 0.1 M KI",
      "100 ml of 0.1 M AgNO3 + 75 ml of 0.1 M KI",
      "100 ml of 0.1 M AgNO3 + 150 ml of 0.1 M KI"
    ],
    "correct_answer": "100 ml of 0.1 M AgNO3 + 50 ml of 0.1 M KI"
  },
  {
    "question": "For a first order reaction, ratio of time required for 99.9% completion to the 90% completion of the reaction is",
    "options": [
      "9 : 1",
      "6 : 1",
      "3 : 1",
      "10 : 1"
    ],
    "correct_answer": "10 : 1"
  },
  {
    "question": "A solution of nitric acid has 63% nitric acid by mass. If density of solution is 1.5 g mL–1 then molarity of the solution is",
    "options": [
      "2.5 M",
      "5 M",
      "10 M",
      "15 M"
    ],
    "correct_answer": "10 M"
  },
  {
    "question": "In the brown ring test for nitrate ion the brown coloured complex so formed is",
    "options": [
      "[Fe(H2O)5NO]3+",
      "[Fe(H2O)5NO]2+",
      "Fe4[Fe(CN)6].xH2O",
      "[Fe(CN)5NO]2–"
    ],
    "correct_answer": "[Fe(H2O)5NO]2+"
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
        "question": "The incorrect statement regarding carbon monoxide is",
        "options": [
            "It is colourless and odourless gas",
            "It is highly poisonous gas due to its ability to form highly stable carboxy-haemoglobin complex",
            "It is a powerful reducing agent and reduces all metal oxides",
            "It contain one sigma and two π bonds between carbon and oxygen."
        ],
        "correct_answer": "It contain one sigma and two π bonds between carbon and oxygen."
    },
    {
        "question": "A vessel contains H2 and O2 in 1 : 2 molar ratio at 5 atm pressure. The ratio of their rate of diffusion is",
        "options": [
            "1: 4",
            "2 : 1",
            "2 : 3",
            "1 : 3"
        ],
        "correct_answer": "1: 4"
    },
    {
        "question": "Which of the following ions has electronic configuration [Ar] 3d5?",
        "options": [
            "Mn3+",
            "Fe2+",
            "Co4+",
            "Cr2+"
        ],
        "correct_answer": "Mn3+"
    },
    {
        "question": "Which of the following statements about Hydrogen is correct?",
        "options": [
            "Hydrogen has three isotopes of which Deuterium is the most common",
            "In laboratory dihydrogen is prepared by the reaction of granulated Zn with dilHCl",
            "Tritium is isotope of hydrogen contains equal number of protons and neutrons",
            "Dihydrogen does not act as a reducing agent"
        ],
        "correct_answer": "Hydrogen has three isotopes of which Deuterium is the most common"
    },
    {
        "question": "The number of moles of nitrogen molecules required to produce 50 moles of ammonia through Haber’s process is",
        "options": [
            "30",
            "25",
            "35",
            "20"
        ],
        "correct_answer": "30"
    },
    {
        "question": "Statement-I: Work done during free expansion of an ideal gas in a isothermal process is zero.\nStatement-II: Work is a path function. In the light of above statements choose the correct option among the following.",
        "options": [
            "Statement-I is true but statement-II is false",
            "Statement-I is false but statement-II is true",
            "Both statement-I and statement-II are true",
            "Both statement-I and statement-II are false"
        ],
        "correct_answer": "Both statement-I and statement-II are false"
    },
    {
        "question": "Identify the incorrect statement among the following.",
        "options": [
            "Pig iron can be moulded into a variety of shapes",
            "Mineral’s are naturally occurring chemical substances in the earth’s crust",
            "Sulphides ore are concentrated by froth floation process",
            "Zn can be used to reduce alumina"
        ],
        "correct_answer": "Zn can be used to reduce alumina"
    },
    {
        "question": "Statement-I: Lithium is the strongest reducing agent among alkali metals.\nStatement-II: Fluorine is the strongest oxidising agent among halogens. In the light of above statements choose the correct option a among the following.",
        "options": [
            "Statement-I is true but statement-II is false",
            "Statement-I is false but statement-II is true",
            "Both statement-I and statement-II are false",
            "Both statement-I and statement-II are true"
        ],
        "correct_answer": "Statement-I is false but statement-II is true"
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
        "question": "Which of the following is not an experimental quantity?",
        "options": ["Order", "Molecularity", "Rate constant", "Reaction rate"],
        "correct_answer": "Order"
    },
    {
        "question": "In which of the following both the dispersed phase and dispersion medium are not liquid?",
        "options": ["Milk", "Hair cream", "Butter", "Paints"],
        "correct_answer": "Hair cream"
    },
    {
        "question": "Which of the following does not favours covalent character in ionic compound?",
        "options": [
            "Smaller size of cation",
            "Larger size of anion",
            "Greater charge on cation",
            "Lesser charge on anion"
        ],
        "correct_answer": "Lesser charge on anion"
    },
    {
        "question": "If enthalpy of hydrogenation of benzene to cyclohexane is –200 kJ mol–1 and resonance energy of benzene is –152 kJ mol–1 then enthalpy of hydrogenation of cyclohexene will be",
        "options": ["–8 kJ mol–1", "–16 kJ mol–1", "–32 kJ mol–1", "–48 kJ mol–1"],
        "correct_answer": "–48 kJ mol–1"
    },
    {
        "question": "Identify the incorrect relation.",
        "options": [
            "VC = 3b",
            "TC =8a/27 Rb",
            "PC = a/27b^2",
            "TB = 27a/Rb"
        ],
        "correct_answer": "TB = 27a/Rb"
    },
    {
        "question": "Statement-I: Quick lime slaked with soda gives solid soda lime.\nStatement-II: Lime water is the aqueous solution of calcium carbonate. In the light of above two statements, select the correct options among the following.",
        "options": [
            "Statement-I is true and statement-II is false",
            "Statement-I is false and statement-II is true",
            "Both statements-I and II are true",
            "Both statement-I and II are false"
        ],
        "correct_answer": "Statement-I is true and statement-II is false"
    },
    {
        "question": "If atomic radius of the first orbit of H-atom is x, then the radius of the 3rd orbit of H-atom will be",
        "options": ["x/3", "9x", "x/9", "3x"],
        "correct_answer": "9x"
    },
    {
        "question": "When Cu2+ (1M)/Cu(s) electrode is diluted 10 times, the electrode potential",
        "options": [
            "Increases by 0.029 V",
            "Increases by 0.236 V",
            "Decreases by 0.315 V",
            "Decreases by 0.029 V"
        ],
        "correct_answer": "Increases by 0.029 V"
    },
    {
        "question": "Statement-I: CO is a π-acid ligand.\nStatement-II: CO is a stronger ligand than CN . In light of above statements, choose the correct answer.",
        "options": [
            "Both statement-I and statement-II are correct",
            "Both statement-I and statement-II are incorrect",
            "Statement-I is correct but statement-II is incorrect",
            "Statement-I is incorrect but statement-II is correct"
        ],
        "correct_answer": "Both statement-I and statement-II are correct"
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
        "question": "Read the given features. (a) Nitrogenase activity in heterocyst (b) Mucilagenous sheath covering (c) Presence of carbon as well as nitrogen fixing (d) Presence of flagella How many of the given features is/are true for Nostoc?",
        "options": ["One", "Two", "Three", "Four"],
        "correct_answer": "Three"
    },
    {
        "question": "Both diatoms and dinoflagellates are protists but differ in",
        "options": ["Mode of nutrition", "Cell wall composition", "Body organisation", "Cell type"],
        "correct_answer": "Cell wall composition"
    },
    {
        "question": "Kuru disease is caused by",
        "options": [
            "A proteinaceous infectious particle",
            "A virus, containing ssRNA",
            "An infectious RNA particle",
            "A virus, containing dsRNA"
        ],
        "correct_answer": "A proteinaceous infectious particle"
    },
    {
        "question": "Read the given statements and select the correct option. Statement A: Photosynthesis is under the influence of external factors only. Statement B: Photosynthesis process utilizes less than 1% of the water absorbed by a plant.",
        "options": [
            "Only statement A is correct",
            "Only statement B is correct",
            "Both statements are correct",
            "Both statements are incorrect"
        ],
        "correct_answer": "Both statements are incorrect"
    },
    {
        "question": "The biosphere reserves consist of (1) An area of active cooperation between reserve management and the local people that comprises outermost part of Biosphere Reserve (2) Transition zone that is the innermost part of it (3) Natural zone that surrounds the core zone (4) Buffer zone as the outermost part of biosphere reserve",
        "options": [
            "An area of active cooperation between reserve management and the local people that comprises outermost part of Biosphere Reserve",
            "Transition zone that is the innermost part of it",
            "Natural zone that surrounds the core zone",
            "Buffer zone as the outermost part of biosphere reserve"
        ],
        "correct_answer": "Buffer zone as the outermost part of biosphere reserve"
    },
    {
        "question": "Van Mahotsava is related to",
        "options": [
            "Conservation of forests",
            "Melting of polar ice caps",
            "Integrated waste water treatment",
            "Handling human excreta using dry composting toilets"
        ],
        "correct_answer": "Conservation of forests"
    },
    {
        "question": "Choose the correct one for DNA",
        "options": [
            "Presence of uracil",
            "Mutates at faster rate",
            "Able to Generate its replica",
            "Has free 2' OH in pentose sugar"
        ],
        "correct_answer": "Able to Generate its replica"
    },
    {
        "question": "During DNA replication, DNA ligase",
        "options": [
            "Unwinds double helical DNA",
            "Joins discontinuously synthesized fragments on template with polarity 5' -> 3'",
            "Provides energy for polymerisation reaction",
            "Has topoisomerase activity"
        ],
        "correct_answer": "Joins discontinuously synthesized fragments on template with polarity 5' -> 3'"
    },
    {
        "question": "During DNA replication, elongation of new strand is catalysed by",
        "options": [
            "DNA dependent DNA polymerase",
            "DNA helicase",
            "DNA gyrase",
            "Phosphorylase"
        ],
        "correct_answer": "DNA dependent DNA polymerase"
    },
    {
        "question": "2 to 8 apical and equal flagella are found in members of",
        "options": ["Red algae", "Brown algae", "Phaeophyceae", "Green algae"],
        "correct_answer": "Brown algae"
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
        "question": "Select the physiological effects of gibberellins in the plant and mark the correct option. (a) Delay senescence (b) Increases length of stem in sugarcane (c) It can promote flowering in pineapple plant (d) It control xylem differentiation and helps in cell division",
        "options": ["(c) and (d)", "Only (a)", "(a) and (b)", "(a),(b) and (d)"],
        "correct_answer": "(a),(b) and (d)"
    },
    {
        "question": "Bulbil is a vegetative propagule of",
        "options": ["Water hyacinth", "Ginger", "Bryophyllum", "Agave"],
        "correct_answer": "Bryophyllum"
    },
    {
        "question": "Some species of Asteraceae and grasses have evolved the special mechanism called apomixis. It refers to",
        "options": [
            "Production of fruits without fertilisation",
            "Pollination by moth",
            "Production of seeds without fertilisation",
            "Formation of diploid pollen grain"
        ],
        "correct_answer": "Production of seeds without fertilisation"
    },
    {
        "question": "Select the incorrect statement",
        "options": [
            "Citric acid is produced by bacteria only",
            "A clot buster called streptokinase is produced by bacteria Streptococcus",
            "Statins and ethanol are produced by yeast",
            "Lipases helps in removing oily stains"
        ],
        "correct_answer": "Citric acid is produced by bacteria only"
    },
    {
        "question": "Which of the following statements is not true?",
        "options": [
            "Cork is formed by extra-stelar cambium",
            "Cell walls of phellogen become thick due to the deposition of suberin",
            "Phellogen, phellem and phelloderm are collectively known as periderm",
            "Bark in trees also includes secondary phloem"
        ],
        "correct_answer": "Cork is formed by extra-stelar cambium"
    },
    {
        "question": "The structure which is present in both dicot and monocot stem is",
        "options": ["Hypodermis", "Endodermis", "Medullary rays", "Pith"],
        "correct_answer": "Medullary rays"
    },
    {
        "question": "A number of leaflets are present on a common axis called rachis. This statement is true for",
        "options": ["Guava", "Silk cotton", "Nerium", "Neem"],
        "correct_answer": "Silk cotton"
    },
    {
        "question": "In the floral formula, the symbols A2+4 and A3+3 respectively are given for the members of families",
        "options": [
            "Solanaceae and Brassicaceae",
            "Brassicaceae and Liliaceae",
            "Fabaceae and Brassicaceae",
            "Liliaceae and Fabaceae"
        ],
        "correct_answer": "Brassicaceae and Liliaceae"
    },
    {
        "question": "The structures in plant cells which are not surrounded by any membrane are",
        "options": ["Gas vacuole and centriole", "Ribosome and nucleolus", "Lysosome and food vacuole", "Gas vacuole and nucleolus"],
        "correct_answer": "Ribosome and nucleolus"
    },
    {
        "question": "Select the incorrect statement regarding cytoskeleton.",
        "options": [
            "It is a network of filamentous structures",
            "It consists of microtubules, microfilaments and intermediate filaments",
            "It is found in multicellular organisms only",
            "It maintains the shape of the cell"
        ],
        "correct_answer": "It is found in multicellular organisms only"
    },
    {
        "question": "Which of the features of life forms can be seen in non-living objects too?",
        "options": ["Reproduction", "Consciousness", "Growth", "Sensitivity to touch"],
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
        "options": ["One", "Two", "Three", "Four"],
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
        "options": ["Spirogyra", "Ectocarpus", "Fucus", "Cycas"],
        "correct_answer": "Ectocarpus"
    },
    {
        "question": "Select the odd one out w.r.t. day neutral plants.",
        "options": ["Cucumber", "Tobacco", "Tomato", "Pepper"],
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
        "options": ["a and e", "a, b and c", "e and d", "b and c"],
        "correct_answer": "e and d"
    },
    {
        "question": "Given below are four statements regarding human circulatory system.\na. Heart failure is sometimes called congestive heart failure.\nb. During joint diastole, all four chambers of heart are in contracted state.\nc. A special neural centre is present in the medulla oblongata that can moderate the cardiac function through ANS.\nd. Maximum filling of blood in ventricles occurs during joint diastole.\nWhich of the above statements are correct?",
        "options": ["a, b and c", "a, b, c and d", "b, c and d", "a, c and d"],
        "correct_answer": "a, b and c"
    },
    {
        "question": "Choose the odd one w.r.t. closed circulatory system.",
        "options": ["Nereis", "Ichthyophis", "Palaemon", "Pteropus"],
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
        "options": ["Tetany", "Gout", "Osteoporosis", "Arthritis"],
        "correct_answer": "Osteoporosis"
    },
    {
        "question": "Select the bone that is a part of axial skeleton.",
        "options": ["Coccyx", "Clavicle", "Carpal", "Coxal"],
        "correct_answer": "Coccyx"
    },
    {
        "question": "Choose the best breeding method for animals that have below average growth rate in beef cattle",
        "options": ["Out-crossing", "Cross-breeding", "Interspecific hybridisation", "Inbreeding"],
        "correct_answer": "Cross-breeding"
    },
    {
        "question": "True coelom and metamerism evolved for the first time in members of phylum",
        "options": ["Annelida", "Arthropoda", "Aschelminthes", "Echinodermata"],
        "correct_answer": "Annelida"
    },
    {
        "question": "Assertion (A): Insects are placed in phylum Arthropoda.\nReason (R): Insects have jointed appendages.\nIn the light of above statements, choose the correct answer from the options given below.",
        "options": [
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
            "(A) is true but (R) is false",
            "(A) is false but (R) is true"
        ],
        "correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)"
    },
    {
        "question": "The pregnancy in which implantation of embryo occurs at a site other than uterus is called",
        "options": ["Ectopic pregnancy", "Pregnancy before menarche", "Pregnancy after menopause", "Normal pregnancy"],
        "correct_answer": "Ectopic pregnancy"
    },
    {
        "question": "Read the following statements A and B and choose the correct option.\nStatement A: In a normal pregnant woman, synthesis of estrogen and progesterone is under control of high levels of circulating LH.\nStatement B: Signals for parturition originate from oxytocin released from maternal pituitary.",
        "options": [
            "Both statements A and B are correct",
            "Both statements A and B are incorrect",
            "Only statement A is correct",
            "Only statement B is correct"
        ],
        "correct_answer": "Only statement B is correct"
    },
    {
        "question": "What does ICSI stand for?",
        "options": [
            "Inter Cytoplasmic Sperm Injection",
            "Intra Cellular Sperm Injection",
            "Intra Cytoplasmic Sperm Insemination",
            "Intra Cytoplasmic Sperm Injection"
        ],
        "correct_answer": "Intra Cytoplasmic Sperm Injection"
    },
    {
        "question": "If the safety testing of polio vaccine on transgenic mice is successful, it could replace the use of",
        "options": ["Sheep", "Cows", "Fish", "Monkeys"],
        "correct_answer": "Monkeys"
    },
    {
        "question": "Graves’ disease is caused due to",
        "options": [
            "Hypersecretion of thyroid hormones",
            "Hyposecretion of thyroid hormones",
            "Hypersecretion of pineal gland",
            "Hyposecretion of PTH"
        ],
        "correct_answer": "Hypersecretion of thyroid hormones"
    },
    {
        "question": "Agriculture came around how many years ago?",
        "options": ["18,000", "10,000", "40,000", "75,000"],
        "correct_answer": "10,000"
    },
    {
        "question": "In solutions of different pHs, the structure of amino acid changes. If the nature of aqueous solutions of two different amino acids ‘X’ and ‘Y’ is basic and acidic, then ‘X’ and ‘Y’ respectively are",
        "options": [
            "Phenylalanine and Lysine",
            "Lysine and Glutamate",
            "Glycine and Glutamate",
            "Alanine and Phenylalanine"
        ],
        "correct_answer": "Alanine and Phenylalanine"
    },
    {
        "question": "How many of the following are true w.r.t. first cellular forms originated on earth?\n(a) They were probably single cells.\n(b) They were present in water environment.\n(c) They probably arose rapidly through evolutionary forces from living molecules.\n(d) Did not possibly originate till about 2000 mya.",
        "options": ["One", "Three", "Two", "Four"],
        "correct_answer": "Four"
    },
    {
        "question": "Calculate the number of hydrogen bonds present in the sequence of a stretch of a double helical DNA 3' AATCCGAT5'.",
        "options": ["19", "16", "21", "25"],
        "correct_answer": "21"
    },
    {
        "question": "Chemicals released from mast cells during allergic reactions include\n(a) Histamine\n(b) Serotonin\n(c) Adrenaline\n(d) Steroids\nSelect the correct option.",
        "options": [
            "(a) and (b)",
            "(b) and (c)",
            "(a), (c) and (d)",
            "(b), (c) and (d)"
        ],
        "correct_answer": "(a) and (b)"
    },
    {
        "question": "Read the statements given below and select the correct answer for T-lymphocytes and macrophages.\n(1) Both are part of cellular barrier of innate immunity.\n(2) Both of them are unique components of specific immune response in vertebrates.\n(3) T-lymphocytes are responsible for acquired immunity whereas macrophages are components of non-specific immune response.\n(4) Macrophages provide specific immune response and T-lymphocytes provide innate immune response.",
        "options": [
            "Both statements are correct",
            "Both statements are incorrect",
            "Only statement A is correct",
            "Only statement B is correct"
        ],
        "correct_answer": "Only statement A is correct"
    },
    {
        "question": "Select the correct option to complete the analogy.\nColostrum : Natural passive immunity :: ATS : ___",
        "options": [
            "Natural active immunity",
            "Natural passive immunity",
            "Artificial active immunity",
            "Artificial passive immunity"
        ],
        "correct_answer": "Artificial active immunity"
    },
    {
        "question": "To isolate DNA from a fungal cell, the cell should not be treated with",
        "options": [
            "Chitinase",
            "Proteases",
            "Ribonucleases",
            "Deoxyribonucleases"
        ],
        "correct_answer": "Ribonucleases"
    },
    {
        "question": "Genetic engineering can help to overcome which limitation that is encountered during traditional hybridisation procedures for animal breeding?",
        "options": [
            "Insertion of desirable genes only",
            "High cost involved in breeding",
            "Inclusion of undesirable genes",
            "No creation of unique combinations of genetic setup"
        ],
        "correct_answer": "Inclusion of undesirable genes"
    },
    {
        "question": "One of the representative of phylum Chordata is",
        "options": ["Starfish", "Angel fish", "Cuttle fish", "Shell fish"],
        "correct_answer": "Cuttle fish"
    },
    {
        "question": "JG cells get activated to release renin when\n(a) Glomerular blood flow increases\n(b) Glomerular blood pressure decreases\n(c) Glomerular blood flow decreases\n(d) Glomerular blood pressure increases\nChoose the option with correct set.",
        "options": ["(a) and (d) only", "(a), (b) and (d)", "(b), (c) and (d)", "(b) and (c) only"],
        "correct_answer": "(a) and (d) only"
    },
    {
        "question": "A centre that can reduce the duration of inspiration is present in _______ region of the brain.\nSelect the correct option to fill in the blank.",
        "options": ["Cerebrum", "Medulla oblongata", "Pons", "Cerebellum"],
        "correct_answer": "Medulla oblongata"
    },
    {
        "question": "Read the following statements carefully and select the correct answer from the options given below.\n(a) The secondary follicle forms a new membrane called zona pellucida surrounding it.\n(b) The reproductive cycle in female primates is called menstrual cycle.\n(c) Generally one ovum is released during middle of each menstrual cycle.\n(d) LH surge induces the rupture of Graafian follicle and thereby the release of corpus luteum.",
        "options": [
            "Statements (a) and (b) are correct",
            "Statements (a), (b) and (c) are correct",
            "Statements (b), (c) and (d) are correct",
            "Statements (b) and (c) are correct"
        ],
        "correct_answer": "Statements (b) and (c) are correct"
    },
    {
        "question": "What would be the stroke volume if heart beats for 75 times per minute and cardiac output is 6 litres?",
        "options": ["70 mL", "80 mL", "100 mL", "90 mL"],
        "correct_answer": "80 mL"
    },
    {
        "question": "The neurotransmitters released during nerve impulse conduction through a chemical synapse bind to their receptors on/in the",
        "options": [
            "Pre-synaptic membrane",
            "Axon terminal of pre-synaptic neuron",
            "Synaptic cleft",
            "Post-synaptic membrane"
        ],
        "correct_answer": "Post-synaptic membrane"
    },
    {
        "question": "Read the statements carefully.\nStatement A: Complications due to PIDs lead to infections like STIs.\nStatement B: The age group 15-24 is the high risk group for the occurrence of STIs.",
        "options": [
            "Only statement A is correct",
            "Only statement B is correct",
            "Both the statements are correct",
            "Both the statements are incorrect"
        ],
        "correct_answer": "Both the statements are incorrect"
    },
    {
        "question": "Meloidogyne incognita is a nematode that parasitizes the ___ of tobacco plant. Choose the option which fills the blank correctly.",
        "options": ["Roots", "Stems", "Leaves", "Seeds"],
        "correct_answer": "Roots"
    },
    {
        "question": "Which among the following is not a physiological effect of cortisol?",
        "options": [
            "Suppresses immune response",
            "Stimulates erythropoiesis",
            "Produces inflammatory reactions",
            "Maintains renal functions"
        ],
        "correct_answer": "Stimulates erythropoiesis"
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
        st.title("Mock Test 2 for NEET Examination")
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