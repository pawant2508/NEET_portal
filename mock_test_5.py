import streamlit as st  # type: ignore
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
        "question": "Consider the following statements and choose the correct option.\nStatement-A: In nuclear reactors, the control rods are made of cadmium.\nStatement-B: In nuclear reactors, heavy water can be used as moderator.\n(1) Only A is correct\n(2) Only B is correct\n(3) Both A and B are correct\n(4) Both A and B are incorrect",
        "options": [
            "Only A is correct",
            "Only B is correct",
            "Both A and B are correct",
            "Both A and B are incorrect"
        ],
        "correct_answer": "Both A and B are correct"
    },
    {
        "question": "An engine approaches a wall with a constant speed. When it is at a distance of 0.9 km it blows a whistle, whose echo is heard by driver after 5 s. If the speed of sound in air is 330 m/s calculate the speed of engine.",
        "options": [
            "60 m/s",
            "45 m/s",
            "90 m/s",
            "30 m/s"
        ],
        "correct_answer": "60 m/s"
    },
    {
        "question": "The dominant mechanisms for motion of charge carriers in forward and reverse biased silicon p-n junctions are",
        "options": [
            "Drift in forward bias, diffusion in reverse bias",
            "Diffusion in forward bias, drift in reverse bias",
            "Diffusion in both forward and reverse bias",
            "Drift in both forward and reverse bias"
        ],
        "correct_answer": "Diffusion in forward bias, drift in reverse bias"
    },
    {
        "question": "In an n-p-n transistor circuit, the collector current is 10 mA. If 90% of the electrons emitted from the emitter reaches the collector, then the emitter current and base currents are",
        "options": [
            "0.11 mA, 1.1 mA",
            "10 mA, 11.11 mA",
            "11.11 mA, 1.11 mA",
            "0.01 mA, 11.11 mA"
        ],
        "correct_answer": "11.11 mA, 1.11 mA"
    },
    {
        "question": "The least count of a stop watch is 1/5 second. The time of oscillations of a pendulum is measured to be 25 s. The maximum percentage error in this measurement is",
        "options": [
            "8 %",
            "1 %",
            "0.8 %",
            "16 %"
        ],
        "correct_answer": "0.8 %"
    },
    {
        "question": "Fundamental unit out of the following is",
        "options": [
            "Ampere",
            "Gauss",
            "Ohm",
            "Weber"
        ],
        "correct_answer": "Ampere"
    },
    {
        "question": "A small block of mass 200 g moves with uniform speed in a horizontal circular groove, with vertical side walls of radius 25 cm. If the block takes 2 s to complete one round, find the normal reaction by the side wall of the groove on the block.",
        "options": [
            "3.8 N",
            "5.8 N",
            "6 N",
            "0.48 N"
        ],
        "correct_answer": "6 N"
    },
    {
        "question": "Cross section area of a steel wire (Y = 2.0 × 10^11 N/m^2) is 0.1 cm^2. The required force, to increase its length by 10%, will be",
        "options": [
            "4 * 10^5 N",
            "5 * 10^5 N",
            "6 * 10^5 N",
            "2 * 10^5 N"
        ],
        "correct_answer": "6 * 10^5 N"
    },
    {
      "question": "A diatomic gas obeys the law PV^x = constant. For what value of x, it has negative molar specific heat?",
      "options": [
        "x > 1.4",
        "x < 1.4",
        "1 < x < 1.4",
        "0 < x < 1"
      ],
      "correct_answer": "x > 1.4"
    },
    {
        "question": "An electric bulb of volume 300 cm^3 was sealed off during manufacturing at a pressure of 10^(-2) mm of mercury at 27°C. Compute the approximate number of air molecules contained in the bulb. Given that R = 8.31 J/mol K and NA = 6.02 × 10^23 per mol.",
        "options": [
            "6 * 10^10",
            "600 * 10^12",
            "9.6 * 10^16",
        "3 * 10^15"
    ],
    "correct_answer": "9.6 * 10^16"
    },
    {
        "question": "The permanent magnetic moment of atoms of a material is zero. The material",
        "options": [
            "Must be paramagnetic",
            "Must be diamagnetic",
            "Must be ferromagnetic",
            "May be paramagnetic"
        ],
        "correct_answer": "Must be diamagnetic"
    },
    {
        "question": "A coil has a resistance of 10 Ω and an inductance of 0.4 henry. It is connected to an AC source of 6.5 V, 30π Hz. Find the average power consumed in the circuit.",
        "options": [
            "3 W/5",
            "8 W/5",
            "5 W/8",
            "Zero"
        ],
        "correct_answer": "Zero"
    },
    {
        "question": "Two spheres one solid and other hollow are kept in atmosphere at same temperature. Both are made of same material and they have equal radius. The cooling rate would be",
        "options": [
            "Greater for hollow sphere",
            "Greater for solid sphere",
            "Equal for both solid and hollow sphere",
            "Insufficient information"
    ],
    "correct_answer": "Equal for both solid and hollow sphere"
    },
    {
        "question": "Two slits in Young’s experiment have width in the ratio 1 : 25. The ratio of intensity at the maxima and minima in the interference pattern is",
        "options": [
            "9/4",
            "4/9",
            "136/29",
            "29/136"
        ],
        "correct_answer": "29/136"
    },
    {
        "question": "The correct expression for Ampere-Maxwell’s law is",
        "options": [
            "B dl i i ⋅ = μ0c2d [",
            "-d B E dl dt ϕ ⋅ = ∫",
            "B ds ⋅ = 0 ⋅ ∫",
            "∫in0q E ds ⋅ = ε ⋅"
        ],
        "correct_answer": "-d B E dl dt ϕ ⋅ = ∫"
    },
    {
        "question": "A body starting from rest was observed to cover 20 m in 1 second and 40 m during the next second accelerating uniformly. How far had it travelled before the first observation was taken?",
        "options": [
            "10 m",
            "5 m",
            "2.5 m",
            "7.5 m"
        ],
        "correct_answer": "2.5 m"
    },
    {
        "question": "There is an air bubble of radius 1.0 mm in a liquid of surface tension 0.075 N/m and density 10^3 kg/m³. The bubble is at a depth of 10.0 cm below the free surface. By what amount is the pressure inside the bubble greater than the atmospheric pressure? (Surface tension of water = 0.075 N/m)",
        "options": [
            "550 N/m²",
            "1150 N/m²",
            "2150 N/m²",
            "680 N/m²"
        ],
        "correct_answer": "550 N/m²"
    },
    {
        "question": "The distance between H⁺ and Cl⁻ ions in HCl molecule is 1.28 Å. What will be the potential due to this dipole at a distance of 12 Å on the axis of dipole?",
        "options": [
            "0.013 V",
            "0.13 V",
            "1.3 V",
            "13.0 V"
        ],
        "correct_answer": "0.13 V"
    },
    {
        "question": "What is the colour of third band of a coded resistor having resistance equal to 2.3 × 10² Ω?",
        "options": [
            "Red",
            "Black",
            "Orange",
            "Brown"
        ],
        "correct_answer": "Orange"
    },
    {
        "question": "The electric field in the copper wire of area of cross section 2 mm² carrying a current of 1 A is (resistivity of copper is 1.7 × 10⁻⁸ Ω m)",
        "options": [
            "8.5 × 10⁻² V/m",
            "8.5 × 10⁻³ V/m",
            "8.5 V/m",
            "0.00085 V/m"
        ],
        "correct_answer": "8.5 V/m"
    },
    {
        "question": "An ideal battery of emf ε is connected with two resistors of resistance R each and an ideal inductor of self-inductance L as shown in figure. Ratio of current passing through switch S, immediately and long time after it is closed, will be",
        "options": [
            "1 : 1",
            "1 : 2",
            "3 : 1",
            "1 :"
        ],
        "correct_answer": "1 :"
    },
    {
        "question": "Amplitude of a damped harmonic oscillator reduces to half of its initial value in T time. In how much time will amplitude be one fourth of its initial value?",
        "options": [
            "2T",
            "3T",
            "4T",
            "8T"
        ],
        "correct_answer": "4T"
    },
    {
        "question": "Amplitude of a damped harmonic oscillator reduces to half of its initial value in T time. In how much time will amplitude be one fourth of its initial value?",
        "options": [
            "2T",
            "3T",
            "4T",
            "8T"
        ],
        "correct_answer": "4T"
    },
    {
        "question": "Amplitude of a damped harmonic oscillator reduces to half of its initial value in T time. In how much time will amplitude be one fourth of its initial value?",
        "options": [
            "2T",
            "3T",
            "4T",
            "8T"
    ],
    "correct_answer": "4T"
    },
    {
        "question": "A particle is undergoing circular motion of radius R with angular speed ω. It is brought to rest in T time and then again accelerated to same angular speed in 2T time. Angular displacement of the particle in this time interval of 3/2 T is (consider uniform acceleration and retardation)",
        "options": [
            "4ωT",
            "2ωT",
            "3/4 ωT",
            "ωT"
        ],
        "correct_answer": "2ωT"
    },
    {
        "question": "An object is placed at 2f distance in front of a convex lens of focal length f. As object is displaced towards the focus with speed v, the image will",
        "options": [
            "Displace towards the lens with speed greater than v.",
            "Displace towards the lens with speed less than v.",
            "Displace away from the lens with speed greater than v.",
            "Displace away from the lens with speed less than v."
        ],
        "correct_answer": "Displace towards the lens with speed less than v."
    },
    {
        "question": "A light ray is incident at 30° on a mirror. The deviation suffered by it is",
        "options": [
            "150°",
            "120°",
            "60°",
            "30°"
        ],
        "correct_answer": "60°"
    },
    {
        "question": "Two identical conducting spheres carrying charges –12 µC and 8 µC respectively are kept in contact and then separated from each other. Which of the statement is true?",
        "options": [
            "In each sphere 1.25 × 10^13 electrons are in deficit",
            "In each sphere 1.25 × 10^13 electrons are in excess",
            "One sphere has 1.25 × 10^13 electrons are in excess while other has 1.25 × 10^13 electrons are in deficit",
            "One sphere has excess of electrons while other has deficiency of electrons"
        ],
        "correct_answer": "One sphere has 1.25 × 10^13 electrons are in excess while other has 1.25 × 10^13 electrons are in deficit"
    },
    {
        "question": "An electric dipole is placed at an angle of 37° with an uniform electric filed of intensity 4 × 10^5 NC^−1. Dipole experiences a torque equal to 8 N m. If dipole is 2 cm long then charge on the dipole is",
        "options": [
            "1.67 mC",
            "5 mC",
            "2.38 mC",
            "3.2 mC"
        ],
        "correct_answer": "1.67 mC"
    },
    {
        "question": "A car weighing 1000 kg working against a resistance of 500 N accelerates from rest to 30 m s^−1 in 10 second. The work done by the engine of the car during this time interval will be",
        "options": [
            "4.5 × 10^6 J",
            "4.5 × 10^7 J",
            "5.25 × 10^5 J",
            "5.25 × 10^7 J"
        ],
        "correct_answer": "5.25 × 10^5 J"
    },
    {
        "question": "Four particles are fired with same speed at angles 27°, 42°, 57°, and 68° with the horizontal. The range of projectile will be largest for the one projected at angle",
        "options": [
            "27°",
            "42°",
            "57°",
            "68°"
        ],
      "correct_answer": "42°"
    },
    {
        "question": "The escape velocity from the surface of a planet of mass m and radius R is 60 km/s. If the planet’s mass and radius becomes 4m and R respectively, then the corresponding escape velocity would be",
        "options": [
            "30 km/s",
            "120 km/s",
            "60 km/s",
            "148 km/s"
        ],
        "correct_answer": "120 km/s"
    },
    {
        "question": "A particle of mass m is placed at the centre of a uniform spherical shell of mass 3m and radius R. The gravitational potential on the surface of the shell is",
        "options": [
            "-Gm/R",
            "-3Gm/R",
            "-4Gm/R",
            "-2Gm/R"
        ],
        "correct_answer": "-2Gm/R"
    },
    {
        "question": "Two identical particles moving with velocities ( ) –1 4 3 m/s iˆ + jˆ = + and ( ) –1 2 m/s iˆ + jˆ = +, at t = 0. If the two particles collide after 2 seconds, and then move as a single particle, then find the common velocity of particles after collision.",
        "options": [
            "-(1/8) m/s iˆ + (5/8) m/s jˆ",
            "-(1/8) m/s iˆ - (5/8) m/s jˆ",
            "-13 m/s iˆ + 4 m/s jˆ",
            "5 m/s iˆ - 3 m/s jˆ"
        ],
        "correct_answer": "-(1/8) m/s iˆ + (5/8) m/s jˆ"
    },
    {
        "question": "The ratio of SI unit to CGS unit of Planck’s constant is",
        "options": [
            "10^7",
            "10^(-7)",
            "10^3",
            "10^5"
        ],
        "correct_answer": "10^7"
    },
    {
        "question": "An electric current passes through a long straight wire. At a distance 5 cm from the wire, the magnetic field is B. The magnetic field at 10 cm from the wire would be",
        "options": [
            "4B",
            "4B",
            "2B",
            "B"
        ],
        "correct_answer": "2B"
    },
    {
        "question": "Two thin identical equiconvex glass lenses of focal length f each are placed in contact. The space between the two lenses is filled with water. The focal length of combination will be",
        "options": [
            "(4/3)f",
            "(3/4)f",
            "(2/3)f",
            "(3/2)f"
        ],
        "correct_answer": "(4/3)f"
    },
    {
        "question": "To keep rotating a pulley having moment of inertia 10 kg m^2 with angular speed of 20 rad/s a constant torque of 5 N m is required. The energy lost per unit time due to frictional forces is",
        "options": [
            "10 W",
            "1000 W",
            "100 W",
            "50 W"
        ],
        "correct_answer": "100 W"
    },
    {
        "question": "Which among the following oxide of nitrogen exists as solid at room temperature?",
        "options": [
            "NO2",
            "N2O3",
            "N2O",
            "NO"
        ],
        "correct_answer": "N2O"
    },
    {
        "question": "Correct statement(s) about hypophosphorous acid is/are",
        "options": [
            "It contains one P = O bond",
            "It contains 2 P–H bonds",
            "It contains 4 P–OH bonds",
            "I, II, and III"
        ],
        "correct_answer": "I, II, and III"
    },
    {
        "question": "Consider the following reaction: R–Cl + NaI → R–I + NaCl. The above reaction known as",
        "options": [
            "Finkelstein reaction",
            "Wurtz reaction",
            "Swartz reaction",
            "Wurtz-Fittig reaction"
        ],
        "correct_answer": "Finkelstein reaction"
    },
    {
        "question": "Correct IUPAC name of the following compound is",
        "options": [
            "1, 1 – Dimethyl-2-ethoxycyclohexane",
            "1 – Ethoxy-2, 2-dimethylcyclohexane",
            "2 – Ethoxy-1, 1-dimethylcyclohexane",
            "2, 2-Dimethyl-1-ethoxycyclohexane"
        ],
        "correct_answer": "1 – Ethoxy-2, 2-dimethylcyclohexane"
    },
    {
        "question": "Which of the following nucleophiles cannot be introduced in the benzene ring using Sandmeyer reaction?",
        "options": [
            "Cl⁻",
            "Br⁻",
            "CN⁻",
            "I⁻"
        ],
        "correct_answer": "I⁻"
    },
    {
        "question": "Which among the following is a basic amino acid?",
        "options": [
            "Lysine",
            "Phenylalanine",
            "Valine",
            "Leucine"
        ],
        "correct_answer": "Lysine"
    },
    {
        "question": "A magnetic moment of 1.73 BM will be shown by",
        "options": [
            "[CoF6]3−",
            "[Co(NH3)6]3+",
            "[NiCl4]2−",
            "[Fe(CN)6]3−"
    ],
    "correct_answer": "[Co(NH3)6]3+"
    },
    {
        "question": "Statement-I: Propadiene is a non-planar molecule.",
        "options": [
            "Statement-I is correct but statement-II is incorrect",
            "Statement-I is incorrect but statement-II is correct",
            "Both statement-I and statement-II are correct",
            "Both statement-I and statement-II are incorrect"
        ],
        "correct_answer": "Statement-I is correct but statement-II is incorrect"
    },
    {
        "question": "The dispersed phase and dispersion medium in paints respectively are",
        "options": [
            "Liquid and liquid",
            "Liquid and solid",
            "Solid and liquid",
            "Gas and liquid"
        ],
        "correct_answer": "Solid and liquid"
    },
    {
        "question": "An aqueous solution of NaOH contains 0.4 g NaOH in 500 g of water. The freezing point depression of the solution is",
        "options": [
            "0.074 K",
            "-0.074 K",
            "0.15 K",
            "-0.15 K"
        ],
        "correct_answer": "0.15 K"
    },
    {
        "question": "Which of the following pair can form acidic buffer?",
        "options": [
            "CH3COOH + HNO3",
            "NH4OH + HNO3",
            "CH3COOH + NaOH",
            "HNO3 + NaOH"
        ],
        "correct_answer": "CH3COOH + NaOH"
    },
    {
        "question": "Statement I: Rate law for any reaction can be predicted by merely looking at balanced chemical equation. Statement II: Sum of the powers of the concentration of the reactants in the rate law expression is called order of reaction. In the light of above statements choose the correct option among the following.",
        "options": [
            "Statement-I is false but statement-II is true",
            "Statement-I is true but statement-II is false",
            "Both statement-I and II are true",
            "Both statement-I and II are false"
        ],
        "correct_answer": "Statement-I is false but statement-II is true"
    },
    {
        "question": "Statement I: Rate law for any reaction can be predicted by merely looking at balanced chemical equation. Statement II: Sum of the powers of the concentration of the reactants in the rate law expression is called order of reaction. In the light of above statements choose the correct option among the following.",
        "options": [
            "Statement-I is false but statement-II is true",
            "Statement-I is true but statement-II is false",
            "Both statement-I and II are true",
            "Both statement-I and II are false"
        ],
        "correct_answer": "Statement-I is false but statement-II is true"
    },
    {
        "question": "Number of 90° bond angle (s) in PCl5 molecule is",
        "options": [
            "Zero",
            "Two",
            "Five",
            "Six"
        ],
        "correct_answer": "Zero"
    },
    {
        "question": "Correct statements among the following are",
        "options": [
            "I and III only",
            "II and III only",
            "I and II only",
            "I, II and III"
        ],
        "correct_answer": "I and II only"
    },
    {
        "question": "The unit of coefficient of viscosity is",
        "options": [
            "Nm–1",
            "Ns–1",
            "Nsm–2",
            "Nsm–1"
        ],
        "correct_answer": "Nsm–1"
    },
    {
        "question": "The products of which of the following reactions is not correctly matched?",
        "options": [
            "2BeCl + LiAlH4 → 2BeH2 + LiCl + AlCl3",
            "3NH3 + 2H2O + CO → 2NH2COOH + NH3",
            "BeO + C + Cl2 (600-800K) → BeCl2 + CO2",
            "CaCO3 + 2HCl → CaCl2 + H2O + CO2"
        ],
        "correct_answer": "3NH3 + 2H2O + CO → 2NH2COOH + NH3"
    },
    {
        "question": "Which among the following elements contain same number at s-electrons as the number of d-electrons in Co^2+?",
        "options": [
            "Si",
            "Cu",
            "Al",
            "C"
        ],
        "correct_answer": "Cu"
    },
    {
        "question": "n-factor of Cu3P in the following conversion is 2 Cu + P + Cu2HPO4 → Cu3P + H2 + PO3",
        "options": [
            "3",
            "8",
            "11",
            "15"
        ],
        "correct_answer": "8"
    },
    {
        "question": "Compounds [Co(NH3)5(SO4)]Br and [Co(NH3)5Br]SO4 are related as",
        "options": [
            "Linkage isomerism",
            "Coordination isomerism",
            "Ionisation isomerism",
            "Geometrical isomerism"
        ],
          "correct_answer": "Coordination isomerism"
    },
    {
        "question": "Consider the following statements:\n(a) Cinnamaldehyde can be prepared by heating acetaldehyde and benzaldehyde in presence of dilute alkali.\n(b) Acetaldehyde gives positive Tollens’ and Fehling’s test.\n(c) Benzaldehyde undergoes disproportionation reaction in presence of concentrated alkali.\nThe correct statements are",
        "options": [
            "(a) and (b) only",
            "(b) and (c) only",
            "(a) and (c) only",
            "(a), (b), and (c)"
        ],
        "correct_answer": "(a) and (c) only",
    },
    {
        "question": "Molar heat capacity of an adiabatic process is",
        "options": [
            "0",
            "1",
            "3/2",
            "∞"
        ],
        "correct_answer": "∞"
    },
    {
        "question": "Which of the following colloids can be prepared by Bredig’s arc method?",
        "options": [
            "As2S3",
            "Sulphur sol",
            "Gold sol",
            "Fe(OH)3 sol"
        ],
        "correct_answer": "Gold sol"
    },
    {
        "question": "Numbers of σ and π bonds are same in which of the following molecule?",
        "options": [
            "(CN)2",
            "C3O2",
            "C6H6",
            "C2H2"
        ],
        "correct_answer": "C6H6"
    },
    {
        "question": "If Ksp of MgSO4 is 10^-10 mol^2L^-2, then maximum mass of MgSO4 in 2 L solution is",
        "options": [
            "10^-5 g",
            "1.2 × 10^-3 g",
            "2.4 × 10^-3 g",
            "1.44 × 10^-2 g"
        ],
        "correct_answer": "2.4 × 10^-3 g"
    },
    {
        "question": "Complex permanent tissues in plants do not",
        "options": [
            "Store various organic materials",
            "Assimilate food from carbon dioxide",
            "Have dead cells",
            "Have thin-walled cells"
        ],
        "correct_answer": "Have thin-walled cells"
    },
    {
        "question": "Select the incorrect statement regarding monocot stem.",
        "options": [
            "Hypodermis provides mechanical support",
            "Vascular bundles are surrounded by sclerenchymatous sheath",
            "Protoxylem lies towards the periphery and metaxylem towards the centre",
            "Ground tissue is not well-differentiated"
        ],
        "correct_answer": "Hypodermis provides mechanical support"
    },
    {
        "question": "The feature which is true for mango fruit but not for coconut fruit is",
        "options": [
            "Development from monocarpellary ovary",
            "One-seeded",
            "Stony hard endocarp",
            "Edible mesocarp"
        ],
        "correct_answer": "One-seeded"
    },
    {
        "question": "Cell wall is not absent in",
        "options": [
            "Euglena",
            "Amoeba",
            "Mycoplasma",
            "Nostoc"
        ],
        "correct_answer": "Amoeba"
    },
    {
        "question": "In eukaryotic cells, the nucleolus is the site where",
        "options": [
            "Active ribosomal RNA synthesis occurs",
            "Polymerization of amino acids occurs",
            "Replication of DNA occurs",
            "Lipids and steroids are synthesized"
        ],
        "correct_answer": "Active ribosomal RNA synthesis occurs"
    },
    {
        "question": "Solanaceae is",
        "options": [
            "Order of mango",
              "Family of Solanum",
              "Scientific name of potato",
              "Category which includes brinjal and wheat"
          ],
          "correct_answer": "Family of Solanum"
    },
    {
          "question": "A book which contains complete listing and description of the plants growing in a particular area is",
          "options": [
            "Manograph",
            "Herbarium",
            "Catalogue",
            "Manual"
         ],
        "correct_answer": "Catalogue"
    },
    {
      "question": "Select the incorrect statement.",
      "options": [
        "Succinate dehydrogenase is found in matrix of mitochondria : true",
        "In alcoholic fermentation, CO2 is released : true",
        "Acetyl CoA is a 2C compound : true",
        "Fats are first broken down into glycerol and fatty acids before entering the respiratory pathway : false"
      ],
      "correct_answer": "Fats are first broken down into glycerol and fatty acids before entering the respiratory pathway : false"
    },
    {
      "question": "Read the following statements and select the correct option.\nStatement A: Cyanobacteria can be used as a source for single-cell protein.\nStatement B: Single-cell protein is protein-rich biomass which is used as food or feed.",
      "options": [
        "Only statement A is correct : true",
        "Only statement B is correct : true",
        "Both statements A and B are correct : true",
        "Both statements A and B are incorrect : false"
      ],
      "correct_answer": "Both statements A and B are correct : true"
    },
    {
      "question": "State true (T) or false (F) for the following statements and select the correct option.\nA. Natality and immigration contribute to an increase in population density.\nB. Growth pattern is logistic type if resources are limiting.\nA B",
      "options": [
        "T F : false",
        "F T : true",
        "T T : false",
        "F F : false"
      ],
      "correct_answer": "F T : true"
    },
    {
      "question": "In a food chain, energy flow is",
      "options": [
        "Cyclic : false",
        "Unidirectional : true",
        "Bidirectional : false",
        "Always from carnivores to herbivores : false"
      ],
      "correct_answer": "Unidirectional : true"
    },
    {
      "question": "Which among the following is not a moss?",
      "options": [
        "Funaria : true",
        "Sphagnum : true",
        "Selaginella : false",
        "Polytrichum : true"
      ],
      "correct_answer": "Selaginella : false"
    },
    {
      "question": "Isogamous sexual reproduction is found in",
      "options": [
        "Volvox : true",
        "Spirogyra : true",
        "Fucus : false",
        "Both (1) and (2) : true"
      ],
      "correct_answer": "Both (1) and (2) : true"
    },
    {
      "question": "Root endodermis has the ability to actively transport ions in only one direction",
      "options": [
        "Because of the layer of suberin : true",
        "Due to downhill transport : false",
        "Because of apoplastic pathway : false",
        "Because of cytoplasmic streaming : false"
      ],
      "correct_answer": "Because of the layer of suberin : true"
    },
    {
      "question": "Nitrogenase enzyme",
      "options": [
        "Is a Mg-Fe protein : false",
        "Is exclusively present in prokaryotes : true",
        "Require aerobic condition for its functioning : false",
        "Helps in nitrogen and carbon fixation : false"
      ],
      "correct_answer": "Is exclusively present in prokaryotes : true"
    },
    {
      "question": "In Meiosis-I synapsis occurs during",
      "options": [
        "Zygotene : true",
        "Leptotene : false",
        "Pachytene : false",
        "Diplotene : false"
      ],
      "correct_answer": "Zygotene : true"
    },
    {
      "question": "During S phase",
      "options": [
        "DNA replication does not occur : false",
        "Chromosome number is doubled : false",
        "Centriole duplicates in the cytoplasm of animal cells : false",
        "Both DNA content and chromosome number doubles : true"
      ],
      "correct_answer": "Both DNA content and chromosome number doubles : true"
    },
    {
      "question": "Select the incorrect feature of cells present in the meristematic phase of growth.",
      "options": [
        "Possess large conspicuous nuclei : true",
        "Cell wall is thin and cellulosic : true",
        "They are rich in protoplasm : true",
        "The secondary cell wall is with few plasmodesmatal connections : false"
      ],
      "correct_answer": "The secondary cell wall is with few plasmodesmatal connections : false"
    },
    {
      "question": "Streptokinase is",
      "options": [
        "Used as an immunosuppressive agent : false",
        "Competitive inhibitor of the enzyme responsible for synthesis of cholesterol : false",
        "Produced by a bacterium : true",
        "Used for commercial production of ethanol : false"
      ],
      "correct_answer": "Produced by a bacterium : true"
    },
    {
      "question": "Select the diploid structure present in the embryo sac",
      "options": [
        "Antipodal cells : false",
        "Definitive nucleus : false",
        "Zygote : true",
        "Synergid cells : false",
        "Egg cell : false"
      ],
      "correct_answer": "Zygote : true"
    },
    {
      "question": "Embryo formation is present in all plant groups, except",
      "options": [
        "Bryophyte : false",
        "Pteridophyte : false",
        "Angiosperm : false",
        "Algae : true"
      ],
      "correct_answer": "Algae : true"
    },
    {
      "question": "Consider the given stages of translation.\n(A) Binding of next charged tRNA at A site\n(B) Peptide bond formation\n(C) Binding of first charged tRNA at P site\n(D) Movement of ribosome on mRNA\nWhich of the given options is true for the sequential arrangement for stage(s) of translation?",
      "options": [
        "C → A → B → D : false",
        "A → B → C → D : true",
        "B → C → D → A : false",
        "D → C → A → B : false"
      ],
      "correct_answer": "A → B → C → D : true"
    },
    {
      "question": "Aminoacyl synthetase binding loop in tRNA is/has",
      "options": [
        "First loop from 5' end : false",
        "Also called TψC loop : true",
        "Anticodon loop with 7 unpaired bases : false",
        "3 bases that act as anticodon : false"
      ],
      "correct_answer": "Also called TψC loop : true"
    },

    {  
        "question": "The distance between two adjacent base pairs in double helical DNA is approximately",
        "options": [
            "3.4 nm",
            "0.34 nm",
            "2.0 nm",
            "0.2 nm"
        ],
        "correct_answer": "3.4 nm"
    },
    {
        "question": "Select the correct statement for NADPH.",
        "options": [
            "It is called reducing power",
            "It is used as assimilatory power in the Krebs cycle",
            "It is produced during cyclic photophosphorylation",
            "These are not consumed in the C3 cycle"
        ],
        "correct_answer": "It is called reducing power"
    },
    {
        "question": "Aravalli Hill of Rajasthan is",
        "options": [
            "A sacred grove",
            "A biosphere reserve",
            "Comprised of core and buffer zone",
            "Consists of a specific area of active cooperation between reserve management and local people that is called core zone"
        ],
        "correct_answer": "A biosphere reserve"
    },
    {
        "question": "Biological magnification",
        "options": [
            "Includes increased accumulation of toxicants successively at higher trophic level.",
            "Has no effect on metabolism of organisms at various trophic levels",
            "Refers to decrease of BOD in aquatic body.",
            "Is result of accumulation of secondary air pollutants"
        ],
        "correct_answer": "Includes increased accumulation of toxicants successively at higher trophic level."
    },
    {
        "question": "Which of the following statements is not associated with fungi?",
        "options": [
            "Fungi prefer to grow in warm and humid places",
            "They show a great diversity in morphology and habitat",
            "Asexual reproduction takes place by ascospores and basidiospores",
            "Network of hyphae is known as mycelium"
        ],
        "correct_answer": "Asexual reproduction takes place by ascospores and basidiospores"
    },
    {
        "question": "Mark the incorrect statement",
        "options": [
            "Viruses are facultative parasites",
            "Prions are almost equal in size to viruses",
            "Viroids have RNA of low molecular weight",
            "A virus contains either DNA or RNA"
        ],
        "correct_answer": "Prions are almost equal in size to viruses"
    },
    {
        "question": "Viruses that infect plants usually have",
        "options": [
            "dsRNA",
            "ssDNA",
            "dsDNA",
            "ssRNA"
        ],
        "correct_answer": "ssRNA"
    },
    {
        "question": "A male suffering from colourblindness as well as haemophilia, marries a normal vision female whose father was colourblind, then find out probability of colourblind daughter.",
        "options": [
            "50%",
            "25%",
            "100%",
            "75%"
        ],
        "correct_answer": "25%"
    },
    {
        "question": "Birds are different from grasshopper as each somatic cell of the former has",
        "options": [
            "Only one sex chromosome in male individual",
            "Two dissimilar sex chromosomes in female individual",
            "Only one sex chromosome in female individual",
            "Only autosomes in male individual"
        ],
        "correct_answer": "Only one sex chromosome in female individual"
    },
    {
        "question": "Sickle cell anaemia\na. Is an example of point mutation.\nb. Is caused by transversion mutation of the gene which synthesises the alpha chain of haemoglobin.\nc. Involves replacement of amino acid valine by glutamic acid.\nThe correct one(s) is/are",
        "options": [
            "All a, b and c",
            "a only",
            "a and b",
            "b and c"
        ],
        "correct_answer": "a and b"
    },
    {
        "question": "Select the incorrect match from the following.",
        "options": [
            "Late wood – Forms during winter",
            "Heartwood – Comprises dead elements",
            "Alburnum – Darker in colour",
            "Autumn wood – Higher density"
        ],
        "correct_answer": "Heartwood – Comprises dead elements"
    },
    {
        "question": "Read the following features:\n(a) Flower are bisexual and actinomorphic.\n(b) Stamens are epiphyllous.\n(c) Leaves have reticulate venation.\n(d) Gynoecium is syncarpous and ovary is superior.\nWhich of the given features is/are true w.r.t members of family Liliaceae?",
        "options": [
            "(a), (b) and (d)",
            "(b), (c) and (d)",
            "(a) only",
            "(a) and (b) only"
        ],
       "correct_answer": "(a) only"
    },
    {
        "question": "Ribosomes were first observed under the ________ by ________.\nSelect the correct option to fill in the blanks.",
        "options": [
            "Compound microscope Robert Brown",
            "Electron microscope George Palade",
            "Phase contrast microscope Singer",
            "Simple microscope Rudolf Virchow"
        ],
        "correct_answer": "Compound microscope Robert Brown"
    },
    {
        "question": "Which of the following statements about DFC is incorrect?",
        "options": [
            "Detritivores act on detritus",
            "Begins with detritus",
            "Sun is the direct source of energy",
            "Major conduit of energy in terrestrial ecosystem"
        ],
        "correct_answer": "Sun is the direct source of energy"
    },
    {
        "question": "The body temperature changes with the ambient temperature in",
        "options": [
            "Regulators",
            "Conformers",
            "Migrators",
            "Suspend"
        ],
        "correct_answer": "Conformers"
    },
    {
        "question": "Select the incorrect statement w.r.t. transpiration",
        "options": [
            "It is the evaporative loss of water by plants",
            "It supplies water for photosynthesis",
            "It is not affected by canopy structure of plant",
            "It maintains the shape and structure of the plants"
        ],
        "correct_answer": "It is not affected by canopy structure of plant"
    },
    {
        "question": "In haplontic life cycle",
        "options": [
            "Sporophyte is dominant and photosynthetic",
            "Gametophytic phase is represented by multicellular, non-photosynthetic spore",
            "Both phases are multicellular",
            "The haploid spore divide mitotically and form the gametophyte"
        ],
        "correct_answer": "Sporophyte is dominant and photosynthetic"
    },
    {
        "question": "Select the odd one out w.r.t. redifferentiated tissue.",
        "options": [
            "Secondary phloem",
            "Secondary cortex",
            "Cork cambium",
            "Secondary xylem"
        ],
        "correct_answer": "Secondary cortex"
    },
    {
        "question": "During fermentation of dough, cheese making and beverage making, the main gas produced is",
        "options": [
            "Hydrogen",
            "Carbon dioxide",
            "Oxygen",
            "Methane"
        ],
        "correct_answer": "Carbon dioxide"
    },
    {
        "question": "In double fertilization, syngamy is",
        "options": [
            "Fusion of male gamete with two polar nuclei and results in zygote formation",
            "Release of two male gamete into the cytoplasm through pollen tube",
            "Fusion of male gamete with the egg cell",
            "Fusion of polar nuclei located in the central cell"
        ],
        "correct_answer": "Fusion of male gamete with the egg cell"
    },
    {
        "question": "Release of hot waste water in aquatic body",
        "options": [
            "Increases dissolved oxygen",
            "Reduces BOD",
            "Reduces DO content",
            "Increase the number of organisms sensitive to high temperature"
        ],
        "correct_answer": "Increase the number of organisms sensitive to high temperature"
    },
    {
        "question": "Which of the given levels of biodiversity helps in formation of ecotype and plays a key role in speciation?",
        "options": [
            "Genetic diversity",
            "Species diversity",
            "Ecological diversity",
            "Community diversity"
        ],
      "correct_answer": "Genetic diversity"
  },
  {
      "question": "Which of the given genes w.r.t lac operon is constitutive?",
      "options": [
          "Structural gene",
          "Operator gene",
          "Promoter gene",
          "Regulator gene"
      ],
      "correct_answer": "Regulator gene" 
  },
  {
      "question": "Select the incorrect statement w.r.t. lichens",
      "options": [
          "Algal partner is called phycobiont",
          "They can grow easily in SO2 polluted areas",
          "Fungal partner is called mycobiont",
          "Their relationship is called mutualism"
      ],
      "correct_answer": "They can grow easily in SO2 polluted areas"
  },
  {
        "question": "Genes responsible for eye and body colour in Drosophila are present on",
        "options": [
            "Two different autosomes",
            "The same chromosome",
            "An autosome and X-chromosome respectively",
            "Both X and Y-chromosomes"
        ],
        "correct_answer": "An autosome and X-chromosome respectively"
  },
  {
        "question": "The junction through which a nerve impulse is transmitted from one neuron to another is formed by",
        "options": [
            "Pre-synaptic membrane only",
            "Pre-synaptic membrane and synaptic cleft only",
            "Synaptic cleft and neurotransmitters",
            "Pre-synaptic membrane, synaptic cleft, post-synaptic membrane"
        ],
        "correct_answer": "Pre-synaptic membrane, synaptic cleft, post-synaptic membrane"
  },
  {
        "question": "Enzyme Linked lmmuno Sorbent Assay is based on the principle of",
        "options": [
            "Radioactive tagging",
            "Amplification of DNA",
            "Autoradiography",
            "Antigen – antibody interaction"
        ],
        "correct_answer": "Antigen – antibody interaction"
  },
  {
        "question": "Assertion (A): The most commonly used bioreactors are of stirring type.\nReason (R): A bioreactor provides the optimal growth conditions like pH, substrate, salts, vitamins, oxygen, temperature etc for achieving the desired product.\nChoose the correct answer from the following options.",
        "options": [
            "(A) is true but (R) is false",
            "(A) is false but (R) is true",
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true and (R) is not the correct explanation of (A)"
        ],
        "correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)"
  },
  {
        "question": "Choose the odd one w.r.t downstream processing.",
        "options": [
            "Separation of product",
            "Biosynthetic stage",
            "Purification of product",
            "Extraction of product"
        ],
        "correct_answer": "Biosynthetic stage"
  },
  {  
        "question": "Which of the following are not required for the isolation of DNA from bacteria?\n(a) Lysozyme (b) DNase\n(c) Protease (d) Spooling\n(e) Chilled ethanol\nChoose the correct option.",
        "options": [
            "(a), (c), (d), (e)",
            "(b) only",
            "(b), (d), (e)",
            "(d) and (e)"
        ],
        "correct_answer": "(b) only"
  },
  {
        "question": "Different structures evolving for the same function have similarity among them. This is exemplified by",
        "options": [
            "Vertebrate brains",
            "Forelimbs of mammals",
            "Flippers of penguins and dolphins",
            "Thorns of Bougainvillea and tendrils of Cucurbita"
        ],
        "correct_answer": "Forelimbs of mammals"
  },
  {
        "question": "S.L Miller, in 1953 initially created vacuum in his experimental setup to facilitate which condition on early earth?",
        "options": [
            "Lightning",
            "Reducing atmosphere",
            "High temperature",
            "Electric discharge"
        ],
        "correct_answer": "Reducing atmosphere"
  },
  {
        "question": "Select the joint that does not allow any movement.",
        "options": [
          "Fibrous joint",
          "Cartilaginous joint",
          "Saddle joint",
          "Synovial joint"
        ],
        "correct_answer": "Fibrous joint"
  },
  {
      "question": "Complete the analogy and select the correct option w.r.t human limbs.\nCarpals : 8 :: Tarsals : ___",
      "options": [
          "5",
          "8",
          "7",
          "14"
      ],
      "correct_answer": "7"
  },
  {
      "question": "Bees are the pollinators of the given crop species except",
      "options": [
            "Sunflower",
            "Apple",
            "Pear",
            "Wheat"
      ],
      "correct_answer": "Wheat"
  },
  {
        "question": "Read the statements given below and select the correct option.\n(a) Enzymes are denatured at high temperature but in thermophilic organisms they are effective at temperatures 80°-90°C.\n(b) Adenylic acid is composed of adenosine with a glucose phosphates molecule.\n(c) Carbohydrates are the most abundant biomolecules on earth.\n(d) Alanine contains an amino group and an acidic group anywhere in the molecule.\nHow many statements given above are correct?",
        "options": [
          "Four",
          "Three",
          "Two",
          "One"
        ],
       "correct_answer": "Two"
  },
  {
        "question": "Select the option among the following that is associated with exoskeleton of Periplaneta.",
        "options": [
            "D-glucuronic acid",
            "N-acetyl glucosamine",
            "Keratin sulphate",
            "N-acetyl galactosamine"
        ],
        "correct_answer": "N-acetyl glucosamine"
  },
  {
        "question": "Which of the following chemical is characteristic of human and other animal cartilages?",
        "options": [
            "Lipoglycans",
            "Inulin",
            "Chondroitin sulphate",
            "Lipopolysaccharide"
        ],
        "correct_answer": "Chondroitin sulphate"
  },  
  {  
      "question": "Injection against the Naja bite contains preformed antibodies whereas injection that is given at the birth for prevention against tuberculosis contains",
      "options": [
          "Attenuated pathogens",
          "Harvested antibodies",
          "Killed pathogen",
          "Gamma globulin"
      ],
      "correct_answer": "Killed pathogen"
  },
  {
      "question": "Complete the analogy w.r.t. animals and their taxonomic categories.\nIchthyophis : Amphibia :: Eptatretus : _____",
      "options": [
          "Urochordata",
          "Hemichordata",
          "Cephalochordata",
          "Cyclostomata"
      ],
      "correct_answer": "Cyclostomata"
  },
  {
      "question": "Choose the correct statement among the following.",
      "options": [
          "Water vascular system is a characteristic feature of sponges.",
          "All mammals are homoiothermous and viviparous.",
          "All gnathostomes are placed in superclass Tetrapoda.",
          "Presence of scales is not an exclusive feature of only reptiles."
      ],
      "correct_answer": "Presence of scales is not an exclusive feature of only reptiles."
  },
  {
      "question": "In all of the following organisms, cell division is itself a mode of reproduction, except",
      "options": [
          "Paramecium",
          "Amoeba",
          "Hydra",
          "Euglena"
      ],
      "correct_answer": "Hydra"
  },
  {
        "question": "Which of the following hormones maintains the endometrium and also plays a role in implantation of fertilized ovum and other events of pregnancy?",
        "options": [
            "Oestrogen",
            "Progesterone",
            "FSH",
            "LH"
        ],
        "correct_answer": "Progesterone"
  },
  {
        "question": "How many of the parts given in the box below are present in the digestive system of both cockroaches and humans?",
        "options": [
            "Three",
            "Six",
            "Five",
            "Four"
        ],
        "correct_answer": "Three"
  },
  {
        "question": "Read the given statements and select the correct one.",
        "options": [
            "The major components of our food are carbohydrates, proteins, vitamins, and fats.",
            "Majority of mammals form two sets of teeth during their life; this type of dentition is called heterodont.",
            "Partially hydrolyzed proteins in the chyme reaching the stomach are acted upon by the proteolytic enzymes.",
            "The digestive wastes, solidified into coherent feces in the rectum, initiate a neural reflex causing an urge or desire for its removal."
        ],
        "correct_answer": "Majority of mammals form two sets of teeth during their life; this type of dentition is called heterodont."
  },
  {
        "question": "Which of the following represents the correct sequence of absorption of fats after digestion?",
        "options": [
            "a → c → d → b",
            "a → c → b → d",
            "d → c → a → b",
            "d → c → b → a"
        ],
        "correct_answer": "a → c → b → d"
  },
  {
        "question": "Select the correct option for the given statements.",
        "options": [
            "Both (A) and (B) are true",
            "Both (A) and (B) are false",
            "(A) is true but (B) is false",
            "(A) is false but (B) is true"
        ],
        "correct_answer": "Both (A) and (B) are true"
  },
  {
        "question": "All of the following are correct about the QRS complex in a standard ECG, except",
        "options": [
            "It represents the depolarization of ventricles",
            "It represents one complete pulse",
            "Its end marks the end of ventricular systole",
            "Ventricular contraction starts shortly after the Q wave."
        ],
        "correct_answer": "It represents one complete pulse"
  },
  {
        "question": "What is the function of valves in the heart?",
        "options": [
            "Bidirectional flow",
            "Allows the flow of blood only in one direction, that is from ventricles to the atria",
            "Unidirectional flow",
            "Promote backward flow of blood"
        ],
        "correct_answer": "Unidirectional flow"
  },
  {
        "question": "Read the statements A and B and select the correct option.",
        "options": [
            "Both statements A and B are correct",
            "Both statements A and B are incorrect",
            "Only statement A is correct",
            "Only statement B is correct"
        ],
        "correct_answer": "Both statements A and B are correct"
  },
  {
        "question": "Choose the correct statement from the following.",
        "options": [
            "The sound waves received by the external ear are directed to the semi-circular canals.",
            "The movements of the tectorial membrane bend the hair cells, pressing them against the basilar membrane.",
            "The vibrations are transmitted by the ear ossicles to the oval window by the ear drum.",
            "The oval window passes the vibrations to the fluid of the cochlea, where they generate waves in the lymphs"
        ],
        "correct_answer": "The movements of the tectorial membrane bend the hair cells, pressing them against the basilar membrane."
  },
  {
        "question": "Choose the odd one w.r.t. bacterial diseases.",
        "options": [
            "Typhoid",
            "Trichomoniasis",
            "Syphilis",
            "Cholera"
        ],
        "correct_answer": "Trichomoniasis"
  },
  {
        "question": "‘Bacillus thuringiensis forms protein crystals during a particular phase of their growth’. These protein crystals can be classified in which of the following categories.",
        "options": [
            "Insecticidal",
            "Nutritive",
            "Yield enhancing",
            "Mineral absorbing"
        ],
        "correct_answer": "Insecticidal"
  },
  {
        "question": "Recognition sequence of EcoR I is",
        "options": [
            "5' GAATTC 3', 3' CTTAAG 5'",
            "5' CCCGGG 3', 3' GGGCCC 5'",
            "5' GATATC 3', 3' CTATAG 5'",
            "5' GAATTC 3', 3' CTTAAG 5'"
        ],
        "correct_answer": "5' GAATTC 3', 3' CTTAAG 5'"
  },
  {
        "question": "Migration of a section of one population to another place and population multiple times is known as",
        "options": [
            "Genetic recombination",
            "Gene flow",
            "Natural selection",
            "Mutation"
        ],
        "correct_answer": "Gene flow"
  },
  {
        "question": "Select the incorrect statement from the following.",
        "options": [
            "Pneumonia is not an occupational respiratory disease.",
            "In mature mammalian erythrocytes, respiration is anaerobic.",
            "Bulk of CO2 released from body tissues into the blood is present as carbamino haemoglobin in RBCs.",
            "One cannot breathe out air which is totally devoid of oxygen."
        ],
        "correct_answer": "Bulk of CO2 released from body tissues into the blood is present as carbamino haemoglobin in RBCs."
  },
  {
        "question": "Select the correct option to complete the analogy.",
        "options": [
            "Simple protein",
            "Oligosaccharide",
            "Amino acid",
            "Nucleic acid"
        ],
        "correct_answer":  "Amino acid"
  },
  {
        "question": "Consider the statements given below.",
        "options": [
            "(a) and (b)",
            "(b) and (c)",
            "(c) and (d)",
            "(a) and (d)"
        ],
        "correct_answer": "(a) and (d)"
  },
  {
        "question": "Notochord is a/an",
        "options": [
            "Mesodermally derived hollow tube",
            "Ectodermally derived tube-like structure",
            "Mesodermally derived rod-like structure",
            "Derived from stomochord in all protochordates"
        ],
        "correct_answer": "Mesodermally derived rod-like structure"
  },
  {
        "question": "How many animals in the given box are bilaterally symmetrical, triploblastic, coelomate in adult stage of life?",
        "options": [
            "4",
            "2",
            "6",
            "5"
        ],
        "correct_answer": "2"
  },
  {
        "question": "Read the following statements (a to e) and choose the option with only correct statements.",
        "options": [
            "Statements (a) and (b) are correct",
            "Statements (c), (d) and (e) are correct",
            "Statements (c) and (e) are correct",
            "Statements (a), (c), (d) and (e) are correct"
       ],
      "correct_answer": "Statements (a), (c), (d) and (e) are correct"
  },
  {
      "question": "Read the given statements and select the option that correctly identifies them as true (T) or false (F).\na. The entire nodal tissue from sino-atrial node to Purkinje fibers has the ability to generate action potentials.\nb. Chordae tendinae in the heart are connections between the cuspid valves and the papillary muscles of the ventricles.\nc. Lymph node is a secondary lymphoid organ and graveyard of RBCs.\nd. RBCs are formed in the red bone marrow in the adults.",
      "options": [
          "T T F T",
          "T T T T",
          "F F F T",
          "F T T F"
    ],
    "correct_answer": "F T T F"
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
      "question": "The ratio of frequencies of fundamental harmonic produced by an open pipe to that of closed pipe having the same length is",
      "options": [
          "1 : 2",
          "2 : 1",
          "1 : 3",
          "3 : 1"
      ],
      "correct_answer":  "2 : 1"
  },
  {
      "question": "Light travels a distance x in time t1 in air and 10x in time t2 in another denser medium. What is the critical angle for this medium?",
      "options": [
          "(1 / 2) * sin^(-1)(t1 / t2)",
          "(1 / 10) * sin^(-1)(t1 / t2)",
          "sin^(-1)(10 / t1)",
          "(1 / 10) * sin^(-1)(t2 / t1)"
      ],
      "correct_answer": "(1 / 10) * sin^(-1)(t2 / t1)"
  },
  {
      "question": "If ∮E dS = 0 over a surface, then",
      "options": [
          "The number of flux lines entering the surface must be equal to the number of flux lines leaving it",
          "The magnitude of electric field on the surface is constant",
          "All the charges must necessarily be inside the surface",
          "The electric field inside the surface is necessarily uniform"
      ],
      "correct_answer": "The number of flux lines entering the surface must be equal to the number of flux lines leaving it"
    },
    {
        "question": "A 12 V, 60 W lamp is connected to the secondary of a step-down transformer, whose primary is connected to ac mains of 220 V. Assuming the transformer to be ideal, what is the current in the primary winding?",
        "options": [
             "0.27 A",
            "2.7 A",
            "3.7 A",
            "0.37 A"
        ],
        "correct_answer": "2.7 A"
    },
    {
      "question": "The minimum wavelength of X-rays produced by an electron accelerated through a potential difference of V volts is proportional to",
      "options": [
          "V",
          "1/V",
          "1/sqrt(V)",
          "V^2"
      ],
      "correct_answer": "1/V"
  },
  {
      "question": "The amount of energy required to form a soap bubble of radius 2 cm from a soap solution is nearly (surface tension of soap solution = 0.03 N m–1)",
      "options": [
          "30.16 × 10^-4 J",
          "5.06 × 10^-4 J",
          "3.01 × 10^-4 J",
          "50.1 × 10^-4 J"
      ],
      "correct_answer": "30.16 × 10^-4 J"
  },
  {
        "question": "The work functions of Caesium (Cs), Potassium (K) and Sodium (Na) are 2.14 eV, 2.30 eV and 2.75 eV respectively. If incident electromagnetic radiation has an incident energy of 2.20 eV, which of these photosensitive surfaces may emit photoelectrons?",
        "options": [
            "Cs only",
            "Both Na and K",
            "K only",
            "Na only"
      ],
      "correct_answer": "k only"
  },
  {
      "question": "The net magnetic flux through any closed surface is",
      "options": [
          "Zero",
          "Positive",
          "Infinity",
          "Negative"
      ],
      "correct_answer": "zero"
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
      "question": "A bullet is fired from a gun at the speed of 280 m s^–1 in the direction 30° above the horizontal. The maximum height attained by the bullet is (g = 9.8 m s^–2, sin30° = 0.5)",
      "options": [
          "2800 m",
          "2000 m",
          "1000 m",
          "3000 m"
      ],
      "correct_answer": "1000 m"
  },
  {
      "question": "An electric dipole is placed at an angle of 30° with an electric field of intensity 2 × 10^5 N C^–1. It experiences a torque equal to 4 N m. Calculate the magnitude of charge on the dipole, if the dipole length is 2 cm.",
      "options": [
          "8 mC",
          "6 mC",
          "4 mC",
          "2 mC"
      ],
      "correct_answer": "2 mc"
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
      "question": "Resistance of a carbon resistor determined from colour codes is (22000 ± 5%) Ω. The colour of third band must be",
      "options": [
          "Red",
          "Green",
          "Orange",
          "Yellow"
      ],
      "correct_answer": "Orange"
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
      "question": "In a series LCR circuit, the inductance L is 10 mH, capacitance C is 1 µF and resistance R is 100 Ω. The frequency at which resonance occurs is",
      "options": [
          "15.9 rad/s",
          "15.9 kHz",
          "1.59 rad/s",
          "1.59 kH"
      ],
      "correct_answer": "15.9 kHz"
  },
  {
        "question": "Choose the best breeding method for animals that have below average growth rate in beef cattle",
        "options": [
            "Out-crossing",
            "Cross-breeding",
            "Interspecific hybridisation",
            "Inbreeding"
        ],
        "correct_answer": "Cross-breeding"
    },
    {
        "question": "True coelom and metamerism evolved for the first time in members of phylum",
        "options": [
            "Annelida",
            "Arthropoda",
            "Aschelminthes",
            "Echinodermata"
        ],
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
        "options": [
            "Ectopic pregnancy",
            "Pregnancy before menarche",
            "Pregnancy after menopause",
            "Normal pregnancy"
        ],
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
        st.title("Mock Test 5 for NEET Examination")
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