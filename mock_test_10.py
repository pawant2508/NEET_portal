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
       
        "question": "Endarch condition of xylem is seen in",
        "options": {
            "Dicot root",
            "Monocot root",
            "Dicot stem",
            "Monocot leaf"
        },
        "correct_answer": "Monocot root"
    },
    {
        
        "question": "Read the following statements and select the correct option.\nA. Vascular cambium is completely secondary in origin in dicot roots. \nB. Casparian strips are seen in monocot root and stem.",
        "options": {
            "Only statement A is correct",
            "Only statement B is correct",
            "Both statements A and B are correct",
            "Both statements A and B are incorrect"
        },
        "correct_answer": "Both statements A and B are incorrect"
    },
    {
        
        "question": "Inclusion bodies",
        "options": {
            "Do not lie freely in the cytoplasm of prokaryotes",
            "Help in photosynthesis as it contains pigments",
            "Store reserve material in prokaryotes",
            "Are membrane bound"
        },
        "correct_answer": "Store reserve material in prokaryotes"
    },
    {
        
        "question": "Select the odd one w.r.t cell organelles and their functions.",
        "options": {
            "RER – Helps in secretory protein synthesis",
            "Golgi apparatus – Important site for glycosylation",
            "Lysosome – Enzymes are active at basic pH",
            "Vacuole – Maintains high concentration of ions"
        },
        "correct_answer": "Vacuole – Maintains high concentration of ions"
    },
    {
        
        "question": "APC (Anaphase promoting complex) ensures",
        "options": {
            "Attachment of spindle fibres to kinetochores",
            "Separation of sister chromatids",
            "Formation of spindle fibres",
            "Both (1) and (2)"
        },
        "correct_answer": "Separation of sister chromatids"
    },
    {
        
        "question": "The homologous chromosomes separate but sister chromatids remain associated at their centromeres during which of the following stages of the cell cycle?",
        "options": {
            "Metaphase I",
            "Anaphase II",
            "Prophase I",
            "Anaphase I"
        },
        "correct_answer": "Anaphase II"
    },
    {
        
        "question": "Select the incorrect match.",
        "options": {
            "Leptotene – Compaction of chromatin",
            "Zygotene – Synapsis occurs",
            "Pachytene – Short lived as compared to zygotene",
            "Diplotene – Dissolution of the synaptonemal complex"
        },
        "correct_answer": "Pachytene – Short lived as compared to zygotene"
    },
    {
        
        "question": "Select the incorrect statement.",
        "options": {
            "For a solution, s is always negative",
            "For a solution at atmospheric pressure w is equal to s",
            "More the solute molecules, the lower is the solute potential",
            "The greater the concentration of water in a system, less is its water potential"
        },
        "correct_answer": "For a solution at atmospheric pressure w is equal to s"
    },
    {
        
        "question": "Facilitated diffusion does not involve",
        "options": {
            "Cell membrane",
            "Movement of molecules along the concentration gradient",
            "Transporters",
            "Uphill transport of molecules"
        },
        "correct_answer": "Uphill transport of molecules"
    },
    {
        
        "question": "Biological nitrogen fixation forms _____ from N2.",
        "options": {
            "NO2",
            "NO3",
            "NH3",
            "NH4+"
        },
        "correct_answer": "NH3"
    },
    {
        
        "question": "Which of the following nutrients is a component of several enzymes like nitrogenase and nitrate reductase?",
        "options": {
            "Boron",
            "Magnesium",
            "Molybdenum",
            "Zinc"
        },
        "correct_answer": "Molybdenum"
    },
    {
        
        "question": "The primary CO2 acceptor during the carbon fixation in C4 plants present in the mesophyll cells of leaf is",
        "options": {
            "3C compound",
            "Oxaloacetic acid",
            "5C compound called RuBP",
            "Malic acid"
        },
        "correct_answer":  "Oxaloacetic acid"
    },
    {
        
        "question": "Which of the following is not related to cyclic photophosphorylation?",
        "options": {
            "PS I",
            "Oxygen evolution",
            "Cyclic flow of electrons",
            "ATP synthesis"
        },
        "correct_answer": "Oxygen evolution"
    },
    {
     
      "question": "During which of the following conversions, substrate level phosphorylation takes place in Krebs cycle?",
      "options": {
        "Isocitrate   Ketoglutaric acid",
        "Succinyl CoA  Succinic acid",
        "Succinic acid  Fumaric acid",
        "Malic acid  Oxaloacetic acid"
      },
      "correct_answer": "Succinyl CoA  Succinic acid"
    },
    {
      
      "question": "Cytochrome c oxidase complex containing cytochromes a and a3, and two copper centres is referred to",
      "options": {
        "Complex I",
        "Complex II",
        "Complex III",
        "Complex IV"
      },
      "correct_answer":  "Complex IV"
    },
    {
      
      "question": "Which of the following is redifferentiated tissue?",
      "options": {
        "Cork cambium",
        "Wound cambium",
        "Interfascicular cambium",
        "Secondary cortex"
      },
      "correct_answer": "Wound cambium"
    },
    {
      
      "question": "Select the incorrect match.",
      "options": {
        "Auxin  Causes apical dominance",
        "Gibberellin  Promotes bolting",
        "Cytokinin  Promotes senescence",
        "Abscisic acid  Stress hormone"
      },
      "correct_answer": "Cytokinin  Promotes senescence"
    },
    {
      
      "question": "Select the odd one w.r.t heterogametes.",
      "options": {
        "Volvox",
        "Fucus",
        "Human",
        "Spirogyra"
      },
      "correct_answer":  "Human"
    },
    {
      
      "question": "Select the incorrect statement.",
      "options": {
        "The most vital event of sexual reproduction is perhaps fusion of gametes",
        "Majority of plants show internal fertilization",
        "Meiocyte of fruit fly has 8 chromosomes",
        "Papaya and date palm are monoecious plants"
      },
      "correct_answer":  "Meiocyte of fruit fly has 8 chromosomes"
    },
    {
      
      "question": "Select the incorrect match w.r.t. ploidy level of structures found in angiosperms.",
      "options": {
        "Nucellus – 2n",
        "MMC – 2n",
        "Functional megaspore – n",
        "Female gametophyte – 2n"
      },
      "correct_answer": "Female gametophyte – 2n"
    },
    {
      
      "question": "Transfer of pollen grains from anther to the stigma of a different plant brings genetically different types of pollen grains to the stigma in",
      "options": {
        "Autogamy",
        "Xenogamy",
        "Cleistogamy",
        "Geitonogamy"
      },
      "correct_answer": "Xenogamy"
    },
    {
      
      "question": "In few species, the thalamus also contributes to the fruit formation. All the given species show the same, except",
      "options": {
        "Cashew",
        "Strawberry",
        "Apple",
        "Banana"
      },
      "correct_answer": "Apple"
    },
    {
      
      "question": "Both males and females bear the same number of chromosomes. Above statement does not hold true for",
      "options": {
        "Humans",
        "Drosophila",
        "Birds",
        "Grasshopper"
      },
      "correct_answer": "Drosophila"
    },
    {
      
      "question": "Select the incorrect match.",
      "options": [
        "Thalassemia – Autosomal recessive disorder",
        "Phenylketonuria – Autosomal dominant disorder",
        "Sickle cell anaemia – Defect caused by substitution of glutamic acid by valine at 6th position",
        "Colour blindness – Sex linked recessive disorder"
      ],
      "correct_answer": "Phenylketonuria – Autosomal dominant disorder"
    },
    {
      
      "question": "Select the odd statement w.r.t. structure of DNA.",
      "options": [
        "A nitrogenous base is linked to the OH of 1C pentose sugar through a N-glycosidic linkage to form a nucleoside",
        "Cytosine is common for both RNA and DNA",
        "Two nucleotides are linked through 3-5 phosphodiester linkage to form a dinucleotide",
        "Phosphoester bond joins sugar to base"
      ],
      "correct_answer": "Phosphoester bond joins sugar to base"
    },
    {
      
      "question": "Select the incorrect statement about replication.",
      "options": [
        "DNA polymerase cannot initiate the process of replication",
        "Okazaki fragments are joined by DNA ligase",
        "On template strand with polarity 3 to 5 the replication is discontinuous",
        "Replication does not initiate randomly at any place"
      ],
      "correct_answer": "DNA polymerase cannot initiate the process of replication"
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
      
        "question": "If there is mutation in regulatory gene of lac operon then there will be no synthesis of",
        "options": [
          "Repressor protein",
          "β galactosidase",
          "Permease",
          "Transacetylase"
        ],
        "correct_answer": "Repressor protein"
      },
      {
        
        "question": "The ability to generate a whole plant from any cell/explant is called",
        "options": [
          "Totipotency",
          "Apical meristem culture",
          "Somaclones",
          "Somatic hybrids"
        ],
        "correct_answer":  "Totipotency"
      },
      {
        
        "question": "Resistance to yellow mosaic virus in mung bean was created through",
        "options": [
          "Conventional breeding",
          "Mutation breeding",
          "Genetic engineering",
          "Tissue culture"
        ],
        "correct_answer": "Mutation breeding"
      },
      {
        
        "question": "Fungus Trichoderma polysporum produces____, which is an immunosuppressive agent. Fill in the blank with correct option.",
        "options": [
          "Streptokinase",
          "Cyclosporin A",
          "Statins",
          "Lipids"
        ],
        "correct_answer": "Cyclosporin A"
      },
      {
        
        "question": "LAB converts milk into curd which improves the nutritional quality of milk as it increases content of",
        "options": [
          "Vitamin B5",
          "Vitamin B12",
          "Vitamin A",
          "Vitamin C"
        ],
        "correct_answer": "Vitamin A"
      },
      {
        
        "question": "Commensalism is a type of interspecific interaction where one species is benefited and the other remains unharmed (neither benefited nor harmed). This is exemplified by",
        "options": [
          "Fungi and roots of higher plants",
          "Barnacles growing on back of whale",
          "Sea anemone and hermit crab",
          " Dogs and ticks"
        ],
        "correct_answer": "Barnacles growing on back of whale"
      },
      {
        
        "question": "Majority of animals and nearly all plants cannot maintain a constant internal environment, their body temperature changes with the ambient temperature. They are called",
        "options": [
          "Conformers",
          "Regulators",
          "Partial regulators",
          "Suspenders"
        ],
        "correct_answer": "Conformers"
      },
      {
          
          "question": "The rate of production of organic matter during photosynthesis is called",
          "options": [
              "Gross primary productivity",
              "Secondary productivity",
              "Net primary productivity",
              "Both (1) and (3)"
          ],
          "correct_answer": "Both (1) and (3)"
      },
      {
          
          "question": "The most important cause driving animals and plants to extinction is",
          "options": [
              "Overexploitation",
              "Habitat loss and fragmentation",
              "Co-extinction",
              "Alien species invasion"
          ],
          "correct_answer": "Habitat loss and fragmentation"
      },
      {
          
          "question": "Select the incorrect match.",
          "options": [
              "Primary producer – Grass",
              "Secondary consumer – Man",
              "Primary consumer – Goat",
              "Tertiary consumer – Rabbit"
          ],
          "correct_answer": "Secondary consumer – Man"
      },
      {
          
          "question": "Select the odd one w.r.t ex-situ conservation strategy.",
          "options": [
              " Botanical garden",
              " Wildlife safari parks",
              "Biodiversity hot spots",
              "Zoological park"
          ],
          "correct_answer": "Biodiversity hot spots"
      },
      {
          
          "question": "Montreal protocol was signed in 1987 to",
          "options": [
              " Prevent cutting of forests",
              " Lay the road with polyblend only",
              " Control emission of ozone depleting substances",
              " Prevent killing of animals"
          ],
          "correct_answer": " Control emission of ozone depleting substances"
      },
      {
          
          "question": "Slash and burn agriculture is commonly called",
          "options": [
              "Chipko movement",
              "Joint forest management",
              "Jhum cultivation",
              " Reforestation"
          ],
          "correct_answer": "Jhum cultivation"
      },
      {
          
          "question": "The component of xylem which is living, is",
          "options": [
              "Xylem fibre",
              "Xylem parenchyma",
              "Tracheid",
              "Vessel"
          ],
          "correct_answer": "Xylem parenchyma"
      },
      {
          
          "question": "Bivalents align themselves at equatorial or metaphasic plate in",
          "options": [
              "Metaphase I",
              "Anaphase I",
              "Anaphase II",
              "Telophase I"
          ],
          "correct_answer": "Metaphase I"
      },
      {
          
          "question": "All of the following enzymes of Krebs cycle are found in mitochondrial matrix, except",
          "options": [
              "Citrate synthase",
              "Malate dehydrogenase",
              "Succinate dehydrogenase",
              "Fumarase"
          ],
          "correct_answer": "Malate dehydrogenase"
      },
      {
     
          "question": "All viruses do not contain",
          "options": [
              "Genetic material",
              "Protein capsid",
              "Capsomeres",
              "Envelope"
          ],
          "correct_answer": "Envelope"
      },
      {
        
        "question": "Match column-I with column-II and choose the correct option.",
        "options": {
          "a(i), b(iii), c(ii)",
          "a(i), b(ii), c(iii)",
          "a(iii), b(ii), c(i)",
          "a(iii), b(i), c(ii)"
        },
        "correct_answer": "a(i), b(ii), c(iii)"
      },
      {
        
        "question": "How many of the following STIs given in a box below have bacterium as their causative agent?\nGenital herpes, Trichomoniasis, Genital warts, Syphilis, Gonorrhoea, AIDS",
        "options": {
          "Two",
          "Three",
          "Four",
          "Five"
        },
        "correct_answer": "Four"
      },
      {
        
        "question": "Select the option that is correct for the type of contraceptive devices with their examples.",
        "options": {
          "Progestasert and CuT are hormone-releasing IUDs.",
          "Cu7, Multiload 375 and LNG-20 are copper releasing IUDs.",
          "Non-medicated IUDs include LNG-20, Lippes loop and CuT.",
          "Mala D and Mala N are examples of combined oral contraceptive pills"
        },
        "correct_answer": "Cu7, Multiload 375 and LNG-20 are copper releasing IUDs."
      },
      {
        
        "question": "Which of the following statement about human sperm is correct?",
        "options": {
          "The neck region possesses numerous mitochondria.",
          "For normal fertility, at least 40% of total sperms must have normal shape, size and vigorous motility.",
          "The sperm  lysins present in the acrosome of sperm’s head dissolve the egg envelope so as to facilitate fertilisation.",
          "Sperm head contains an elongated diploid nucleus."
        },
        "correct_answer": "The sperm  lysins present in the acrosome of sperm’s head dissolve the egg envelope so as to facilitate fertilisation."
      },
      {
       
        "question": "Choose the correct option to complete the analogy w.r.t. presence of glands.\nMale reproductive system: Cowper’s glands : : Female reproductive system : _______",
        "options": {
          "Bulbourethral glands",
          "Bartholin’s glands",
          "Seminal vesicles",
          "Prostate gland"
        },
        "correct_answer": "Bartholin’s glands"
      },
      {
        
        "question": "Psilophyton did not give rise to which of the following plants?",
        "options": {
          "Sphenopsids",
          "Conifers",
          "Bryophytes",
          "Ferns"
        },
        "correct_answer": "Conifers"
      },
      {
        
        "question": "Select the incorrect statement w.r.t evolution of man.",
        "options": {
          "Dryopithecus and Ramapithecus were hairy and walked like gorillas and chimpanzees.",
          "Ramapithecus was more man-like while Dryopithecus was more ape-like.",
          "The brain capacity of Homo habilis was 1450 cc.",
          "Pre-historic cave art developed about 18,000 years ago."
        },
        "correct_answer": "The brain capacity of Homo habilis was 1450 cc."
      },
      {
        
        "question": "In humans, Plasmodium reaches the liver through blood as A . The parasite in the hepatocyte reproduces B , bursting the cell and releasing into the blood. Fill the blanks A and B correctly with a suitable option.",
        "options": {
          "Merozoites Sexually",
          "Trophozoites Asexually",
          "Sporozoites Sexually",
          "Sporozoites Asexually"
        },
        "correct_answer": "Sporozoites Asexually"
      },
      {
        
        "question": "Select the incorrect match w.r.t. pathogens listed in column A and corresponding diseases in column B.",
        "options": {
          "Haemophilus influenzae – Pneumonia",
          "Salmonella typhi – Typhoid",
          "Wuchereria malayi – Ascariasis",
          "Epidermophyton – Ringworm"
        },
        "correct_answer": "Wuchereria malayi – Ascariasis"
      },
      {
        
        "question": "Read the following given statements w.r.t lymphoid organs.\nStatement A: Bone marrow and thymus are primary lymphoid organs.\nStatement B: The thymus is quite small at the time of birth but keeps increasing in size with age.\nChoose the correct option.",
        "options": {
          "Only statement A is correct.",
          "Only statement B is correct.",
          "Both statements A and B are correct.",
          "Both statements A and B are incorrect."
        },
        "correct_answer": "Both statements A and B are correct."
      },
      {
         
          "question": "Which of the following statements is correct w.r.t. cancer?",
          "options": [
              "Transformation of cancerous cells into non-neoplastic cells may be induced by oncogenes.",
              "Malignant tumors are mass of non-proliferating cells called neoplastic or tumor cells.",
              "Benign tumors normally remain confined to their original location and do not spread to other parts of the body.",
              "Malignant tumors do not possess the property of metastasis."
          ],
          "correct_answer": "Benign tumors normally remain confined to their original location and do not spread to other parts of the body."
      },
      {
         
          "question": "Choose the mismatch w.r.t. drugs.",
          "options": [
              "Opioid – Binds to specific opioid receptors present principally in cardiovascular system of the body",
              "Cannabinoid – Binds to cannabinoid receptor present principally in human brain",
              "Coca alkaloid – Interferes with the transport of the neuro-transmitter dopamine",
              "Barbiturates – Help patients to cope with mental illness like depression, insomnia, etc."
          ],
          "correct_answer": "Opioid – Binds to specific opioid receptors present principally in cardiovascular system of the body"
      },
      {
          
          "question": "Comprehend the following given statements w.r.t MOET.\nA: MOET is a programme for herd improvement.\nB: Cow is administered hormones with LH-like activity.\nChoose the correct option.",
          "options": [
              "Both statements A and B are correct",
              "Both statements A and B are incorrect",
              "Only statement B is correct",
              "Only statement A is correct"
          ],
          "correct_answer": "Only statement A is correct"
      },
      {
          
          "question": "Fisheries include rearing, catching and selling of fishes, crustaceans and molluscs. Which of the following is not a marine fish?",
          "options": [
              "Hilsa",
              "Shellfish",
              "Pomfret",
              "ackerel"
          ],
          "correct_answer": "Shellfish"
      },
      {
          
          "question": "Choose the incorrect match.",
          "options": [
              "Interspecific hybridization– Results in hybrids e.g. mule whose parents are mare and male donkey",
              "Out-breeding – Hisardale is a result of one of its techniques",
              "Cross-breeding– Best technique to overcome inbreeding depression in less time",
              "Inbreeding – Pure lines with increased homozygosity are generated"
          ],
          "correct_answer": "Cross-breeding– Best technique to overcome inbreeding depression in less time"
      },
      {
         
          "question": "If a foreign gene is inserted at ClaI site in pBR322, then",
          "options": [
              "Non-recombinants so produced will be tets",
              "Non-recombinants so produced will be amps",
              "Recombinants so produced will be ampR but tets",
              "Recombinants so produced will be ampR as well as tetR."
          ],
          "correct_answer": "Recombinants so produced will be ampR as well as tetR."
      },
      {
          
          "question": "Select the incorrect match.",
          "options": [
              "Lysozyme – Degrades bacterial cell wall",
              "Cellulase – Degrades plant cell wall",
              "Micro-injection – rDNA is directly injected into the nucleus of an animal cell",
              "Chitinase – Degrades algal cell wall"
          ],
          "correct_answer": "Micro-injection – rDNA is directly injected into the nucleus of an animal cell"
      },
      {
         
          "question": "Read the following statements w.r.t bioreactor.\nStatement A: The stirrer of a stirred-tank bioreactor facilitates the even mixing and oxygen availability throughout the bioreactor.\nStatement B: A bioreactor does not exhibit the optimal conditions for achieving desired product.\nChoose the correct option.",
          "options": [
              "Only statement A is correct.",
              "Only statement B is correct.",
              "Both statements A and B are correct.",
              "Both statements A and B are incorrect."
          ],
          "correct_answer": "Only statement A is correct."
      },
      {
          
          "question": "Match column-I with column-II and choose the correct option.\nColumn-I Column-II\na. Probe (i) Antigen-antibody interaction\nb. ELISA (ii) ssDNA/RNA tagged with radioactive molecule\nc. α-1-antitrypsin (iii) Produced human protein-enriched milk\nd. First transgenic cow, Rosie (iv) Used to treat emphysema",
          "options": [
              "a(i), b(ii), c(iii), d(iv)",
              "a(iv), b(iii), c(ii), d(l)",
              "a(ii), b(i), c(iii), d(iv)",
              "a(ii), b(i), c(iv), d(iii)"
          ],
          "correct_answer": "a(ii), b(i), c(iv), d(iii)"
      },
      {
         
          "question": "Select the correct statement among the following given options.",
          "options": [
              "A nematode, Meloidogyne incognita infects the stems of tobacco plants and causes an increase in yield.",
              "RNAi involves silencing of a specific mRNA due to a complementary dsDNA molecule that binds to and prevents translation of the mRNA.",
              "Bt toxin protein exists as an inactive protoxin but once an insect ingests the inactive toxin, it is converted into an active form due to the alkaline pH of midgut which solubilises the crystals.",
              "Proteins encoded by the genes cryIAc and cryIIAb control the corn borer."
          ],
          "correct_answer": "Bt toxin protein exists as an inactive protoxin but once an insect ingests the inactive toxin, it is converted into an active form due to the alkaline pH of midgut which solubilises the crystals."
      },
      {
          
          "question": "Select the incorrect match from the options given below: Organisms Characteristic features",
          "options": {
              "Fasciola – Suckers are present.",
              "Ctenoplana – Body bears eight external rows of ciliated comb plates, which help in locomotion.",
              "Obelia – Polyps produce medusae sexually and medusae form the polyps asexually.",
              "Spongilla – Fertilisation is internal and development is indirect having a larval stage which is morphologically distinct from the adult."
          },
          "correct_answer": "Obelia – Polyps produce medusae sexually and medusae form the polyps asexually."
      },
      {
          
          "question": "Hemichordates have a rudimentary structure in the collar region called",
          "options": {
              "Vertebral column",
              "Trunk",
              "Proboscis gland",
              "Stomochord"
          },
          "correct_answer": "Stomochord"
      },
{
    "question": "The parts of human brain that helps in regulation of sexual behaviour, expression of excitement, pleasure, rage, fear etc. are:",
    "options": [
        "Corpora quadrigemina and hippocampus",
        "Brain stem and epithalamus",
        "Corpus callosum and thalamus",
        "Limbic system and hypothalamus"
    ],
    "correct_answer": "Limbic system and hypothalamus"
},

{
    "question": "Vital capacity of lung is _________.",
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
    "question": "Which of the following statements is incorrect?",
    "options": [
        "The viroids were discovered by D.J lvanowsky.",
        "W.M. Stanley showed that viruses could be crystallized.",
        "The term 'contagium vivum fluidum' was coined by MW Beijerinck.",
        "Mosaic disease in tobacco and AIDS in human beings are caused by viruses."
    ],
    "correct_answer": "The term 'contagium vivum fluidum' was coined by MW Beijerinck."
},

{
  "question": "The number of σ bonds, π bonds and lone pair of electrons in pyridine, respectively are:",
  "options": [
    "12, 3, 0",
    "11, 3, 1",
    "12, 2, 1",
    "11, 2, 0"
  ],
  "correct_answer": "12, 3, 0"
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
        st.title("Mock Test 10 for NEET Examination")
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