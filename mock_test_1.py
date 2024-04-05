import streamlit as st  # type: ignore
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
        "question": "Given below are two statements: Assertion (A): The cell walls of diatoms are indestructible Reason (R): In diatoms, cell walls are embedded with silica",
        "options": [
            "Both (A) and (R) are true and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
            "(A) is true but (R) is false.",
            "Both (A) and (R) are false"
        ],
        "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
    },
    {
        "question": "Which one of the following is wrongly matched?",
        "options": [
            "Spirogyra - Motile gametes",
            "Sargassum - Chlorophyll C",
            "Basidiomycetes - Puffballs",
            "Nostoc - Water blooms"
        ],
        "correct_answer": "Basidiomycetes - Puffballs"
    },
    {
        "question": "Identify the fungi which do not belong to the group of other fungi among the following",
        "options": [
            "Sac-fungi",
            "Puffballs",
            "Mushrooms",
            "Bracket Fungi"
        ],
        "correct_answer": "Puffballs"
    },
    {
        "question": "Identify the incorrect statement regarding green algae?",
        "options": [
            "They contain chl a, chl b as well as carotenoids.",
            "The chloroplasts may be discoid, plate-like, reticulate, cup-shaped, spiral or ribbon-shaped in different species.",
            "Most members have one or more storage bodies called pyrenoids located outside the chloroplasts.",
            "They usually have a rigid cell wall made of an inner layer of cellulose and an outer layer of pectose."
        ],
        "correct_answer": "They usually have a rigid cell wall made of an inner layer of cellulose and an outer layer of pectose."
    },
    {
        "question": "How many of the following statements regarding fungi are true? I. Asexual reproduction is common by the formation of spores. II. Their bodies consist of hyphae that many be interconnected to form mycelium. III. They secrete digestive enzymes onto organic matter and then absorb the products of the digestion. IV. Fungi can break down almost any carbon containing product. V. Fungi do not enter symbiotic relationships.",
        "options": [
            "2",
            "3",
            "4",
            "5"
        ],
        "correct_answer": "4"
    },
    {
        "question": "Though Cycas has two cotyledons, it is not included in the dicot because they",
        "options": [
            "have a naked ovule",
            "have megaspore",
            "appear as palm tree",
            "have compound leaves"
        ],
        "correct_answer": "have compound leaves"
    },
    {
        "question": "Consider the following statements regarding brown algae: I. The pigments are chl a, c and xanthophylls, fucoxanthin II. Storage food is laminarin and mannitol III. The cellulosic cell wall is covered with algin IV. They have a centrally located vacuole V. Their photosynthetic organs are called as fronds - leaf like structures VI. They have pear shaped biflagellate zoospores VII. They have two unequal laterally attached flagella. The number of correct statements is",
        "options": [
            "5",
            "6",
            "7",
            "4"
        ],
        "correct_answer": "5"
    },
    {
        "question": "Organisms with soap box like body (a) Are chief producers in the ocean (b) Have silica impregnated cell membrane (c) Are called flagellated golden protists (d) Lack chlorophyll a Choose the incorrect ones",
        "options": [
            "(a), (b), and (c)",
            "(b), (c), and (d)",
            "(a) only",
            "(b) and (d) only"
        ],
        "correct_answer": "(a), (b), and (c)"
    },
    {
        "question": "Select the wrong statement: Organisms with soap box like body (a) Are chief producers in the ocean (b) Have silica impregnated cell membrane (c) Are called flagellated golden protists (d) Lack chlorophyll a Choose the incorrect ones",
        "options": [
            "(a), (b), and (c)",
            "(b), (c), and (d)",
            "(a) only",
            "(b) and (d) only"
        ],
        "correct_answer": "(a), (b), and (c)"
    },
    {
        "question": "Which of the following statement is true about the difference between Cycas and Pinus?",
        "options": [
            "Pinus has coralloid roots associated with N2-fixing cyanobacteria, whereas Cycas has roots with fungal association in the form of mycorrhiza",
            "Cycas is heterosporous, whereas Pinus is homosporous",
            "Male cones and female megasporophylls are borne on different trees in Cycas, whereas they are borne on the same tree in Pinus",
            "Stems of Cycas are branched, whereas Pinus has unbranched stems"
        ],
        "correct_answer": "Cycas is heterosporous, whereas Pinus is homosporous"
    },
    {
        "question": "Given below are two statements: Assertion (A): Ascomycetes are commonly known as sac-fungi Reason (R): Sexual spores of ascomycetes are produced endogenously in sac-like asci",
        "options": [
            "Both (A) and (R) are true and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
            "(A) is true but (R) is false.",
            "Both (A) and (R) are false"
        ],
        "correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
    },
    {
        "question": "Kingdom Protista was proposed by Ernst Haeckel in 1866 as ‘the kingdom of primitive forms’. This kingdom forms a link between the kingdom Fungi, Plantae, and Animalia. Select the option which is incorrectly matched for slime moulds and their plant, animal or fungi like features:",
        "options": [
            "Naked plasmodium - Animal like feature",
            "Spore with true wall - Plant like feature",
            "Formation of fruiting body - Fungi like feature",
            "Formation of plasmodium - Protozoan like feature"
        ],
        "correct_answer": "Formation of plasmodium - Protozoan like feature"
    },
    {
        "question": "The terms that can be applied to all gymnosperms include:",
        "options": [
            "Naked seeds, Homosporous, Dominant independent sporophyte",
            "Seeds enclosed in ovary wall, Heterosporous, Dominant independent sporophyte",
            "Naked seeds, Heterosporous, Dominant independent sporophyte",
            "Naked seeds, Heterosporous, Dominant independent gametophyte"
        ],
        "correct_answer": "Naked seeds, Heterosporous, Dominant independent sporophyte"
    },
    {
        "question": "Read the following five statements (I to V) and select the option with all correct statements. I. Mosses and lichens are the first organisms to colonise bare rock. II. Selaginella is a homosporous pteridophyte. III. Coralloid roots in Cycas have VAM. IV. Main plant body in bryophytes is gametophytic, whereas in pteridophytes it is sporophytic. V. In gymnosperms, male and female gametophytes are present within sporangia located on sporophytes.",
        "options": [
            "I, III and IV",
            "II, III and IV",
            "I, IV and V",
            "II, III and V"
        ],
        "correct_answer": "II, III and IV"
    },
    {
        "question": "Fungus used in genetic studies is",
        "options": [
            "Rhizopus",
            "Mucor",
            "Neurospora",
            "Claviceps"
        ],
        "correct_answer": "Neurospora"
    },
    {
        "question": "Match the organisms in column I with habitats in column II. Column I Column II (a) Halophiles (i) Hot springs (b) Thermoacidophiles (ii) Aquatic environment (c) Methanogens (iii) Guts of ruminants (d) Cyanobacteria (iv) Salty areas Select the correct answer from the options given below: Options: (a) (b) (c) (d)",
        "options": [
            "(iv) (i) (iii) (ii)",
            "(i) (ii) (iii) (iv)",
            "(iii) (iv) (i) (i)",
            "(ii) (iv) (iii) (i)"
        ],
        "correct_answer": "(iii) (iv) (i) (i)"
    },
    {
        "question": "All the following statements regarding Basidiomycetes are correct except:",
        "options": [
            "The mycelium is branched and septate",
            "Asexual spores and vegetative reproduction are generally not found",
            "Sex organs are absent",
            "Basidiospores are exogenously produced on the basidium"
        ],
        "correct_answer": "Asexual spores and vegetative reproduction are generally not found"
    },
    {
        "question": "In all the classes of fungi, common feature will be:",
        "options": [
            "Morphology of the mycelium",
            "Mode of spore formation",
            "Fruiting bodies",
            "Mode of nutrition"
        ],
        "correct_answer": "Mode of nutrition"
    },
    {
        "question": "Identify the organism which causes white spots seen on mustard leaves and select the statement not true for it:",
        "options": [
            "Dikaryophase is the dominant phase of its life",
            "Asexually reproduce by endogenously produced spores",
            "Cell wall is made up of chitin and polysaccharides",
            "It produces sexual spores"
        ],
        "correct_answer": "Dikaryophase is the dominant phase of its life"
    },
    {
        "question": "Consider the following statements about the different classes of algae: I: The members of Chlorophyceae have a rigid cell wall made of an inner layer of cellulose and an outer layer of pectose II: The members of Rhodophyceae do not have a flagellum III: Members of Phaeophyceae store food as floridean starch which is very similar to amylopectin and glycogen in structure",
        "options": [
            "Only I and III are correct",
            "Only I and II are correct",
            "Only II and III are correct",
            "All I, II and III are correct"
        ],
        "correct_answer": "Only I and III are correct"
    },
    {
        "question": "In which of the following class of fungi, sex organs are absent and plasmogamy is brought about by fusion of two vegetative or somatic cells of different strains or genotypes?",
        "options": [
            "Ascomycetes",
            "Phycomycetes",
            "Basidiomycetes",
            "Deuteromycetes"
        ],
        "correct_answer": "Deuteromycetes"
    },
    {
        "question": "Kingdom Protista has brought together Chlamydomonas, Chlorella with Paramoecium and Amoeba. On what basis were these organisms separated under previous classification systems?",
        "options": [
            "Cell wall",
            "Cell type",
            "Body organisation",
            "Mode of nutrition"
        ],
        "correct_answer": "Cell type"
    },
    {
        "question": "Select the incorrect statement about artificial system of classification of Linnaeus",
        "options": [
            "It is called artificial system because it is based on only one or two characters",
            "It was based on androecium structure",
            "It is also called sexual system as he chiefly used characters of stamens",
            "It divides flowering and non-flowering plants into two categories"
        ],
        "correct_answer": "It was based on androecium structure"
    },
    {
        "question": "Bryophytes depend on water as it is required for",
        "options": [
            "vegetative propagation",
            "filling archegonium for fertilization",
            "transfer of male gamete during fertilization",
            "fertilization of homosporous plants"
        ],
        "correct_answer": "transfer of male gamete during fertilization"
    },
    {
        "question": "If you are asked to classify the various algae into distinct groups, which of the following character would you choose?",
        "options": [
            "Types of pigments present in the cell",
            "Nature of stored food material in the cell",
            "Structural organization of thallus",
            "Chemical composition of the cell wall"
        ],
        "correct_answer": "Structural organization of thallus"
    },
    {
        "question": "Given below are two statements: Assertion (A): Vegetative reproduction by fragmentation is common in basidiomycetes Reason (R): In club fungi, sexual spores are not formed during sexual reproduction",
        "options": [
            "Both (A) and (R) are true and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
            "(A) is true but (R) is false.",
            "Both (A) and (R) are false"
        ],
        "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
    },
    {
        "question": "Pick up the wrong statement.",
        "options": [
            "Cell wall is absent in Animalia.",
            "Protista have photosynthetic and heterotrophic modes of nutrition",
            "Some fungi are edible",
            "Nuclear membrane is present in Monera."
        ],
        "correct_answer": "Nuclear membrane is present in Monera."
    },
    {
        "question": "Identify the incorrect statement regarding algae:",
        "options": [
            "At least a half of the total carbon dioxide fixation on earth is carried out by algae through photosynthesis.",
            "Around 70 species of freshwater algae can be used as food.",
            "Certain marine brown and red algae produce large amounts of hydrocolloids (water holding substances), e.g., algin (brown algae) and carrageen (red algae) which are used commercially.",
            "Agar, obtained from Gelidium and Gracilaria are used to grow microbes and in preparations of ice-creams and jellies."
        ],
        "correct_answer": "Agar, obtained from Gelidium and Gracilaria are used to grow microbes and in preparations of ice-creams and jellies."
    },
    {
        "question": "Identify the incorrectly matched pair:",
        "options": [
            "Chlamydomonas: Microscopic unicellular algae",
            "Volvox: Colonial algae",
            "Ulothrix: Filamentous algae",
            "Fucus: Isogamous algae"
        ],
        "correct_answer": "Fucus: Isogamous algae"
    },
    {
        "question": "Unlike plants, the cell walls of most fungi contains",
        "options": [
            "Chitin",
            "Peptidoglycans",
            "Teichoic acid",
            "Cellulose"
        ],
        "correct_answer": "Chitin"
    },
    {
        "question": "Given below are two statements: Assertion (A): Main plant body of bryophyte is called gametophyte Reason (R): Bryophyte possess root like, leaf like and stem like structures",
        "options": [
            "Both (A) and (R) are true and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
            "(A) is true but (R) is false.",
            "Both (A) and (R) are false."
        ],
        "correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
    },
    {
        "question": "Which of the following is true regarding the classes of Bryophytes?",
        "options": [
            "The thallus of mosses is dorsiventral and closely appressed to the surface",
            "In the life cycle of liverworts, the predominant gametophytic stage is divided into two stages - the protonema and the leafy stage",
            "The sporophyte in liverworts is more elaborate than in mosses",
            "Asexual reproduction in liverworts takes place by fragmentation of thalli, or by the formation of specialised structures called gemmae"
        ],
        "correct_answer": "The sporophyte in liverworts is more elaborate than in mosses"
    },
    {
        "question": "Identify the incorrect statement among the following:",
        "options": [
            "Liverworts are considered the most primitive group of bryophytes.",
            "The plant body of mosses is usually more differentiated than that of liverworts.",
            "In the moss plant, the sporophyte is more elaborate than in the liverwort plant.",
            "The sporophyte of a liverwort is usually more elaborate than that of mosses."
        ],
        "correct_answer": "The sporophyte of a liverwort is usually more elaborate than that of mosses."
    },
    {
        "question": "Which one of the following is not a characteristic of bryophytes?",
        "options": [
            "They show alternation of generation",
            "They are known as amphibians of plant kingdom",
            "Antheridia and archegonia are produced on separate gametophytic plant",
            "Sporophytes are partially or wholly dependent on gametophytes for their nutrition"
        ],
        "correct_answer": "Antheridia and archegonia are produced on separate gametophytic plant"
    },
    {
        "question": "Which one of the following is not a characteristic feature of red algae?",
        "options": [
            "Mainly marine, some fresh water forms",
            "Stored food material is floridean starch",
            "Cell walls are made up of cellulose",
            "Most of the red algae are multicellular"
        ],
        "correct_answer": "Cell walls are made up of cellulose"
    },
    {
        "question": "Which of the following is a common feature of green algae and bryophytes?",
        "options": [
            "Both have cell wall made up of cellulose",
            "Both have vascular tissues for conduction of water and food materials",
            "Both store food materials in the form of starch",
            "Both produce seeds as reproductive organs"
        ],
        "correct_answer": "Both store food materials in the form of starch"
    },
    {
        "question": "Consider the following statements:\tI. Pteridophytes are the first terrestrial plants to possessvascular bundles.\tII. Main plant body in pteridophytes is sporophyte whichis differentiated into true stem and leaves.\tIII. Genera like Selaginella and Salvinia are heterosporous.\tWhich of the above statements are true?",
        "options": [
            "I and II only",
            "I and III only",
            "II and III only",
            "I, II and III"
        ],
        "correct_answer": "I and III only"
    },
    {
        "question": "Which of the following statements is correct?",
        "options": [
            "Lichens do not grow in polluted areas.",
            "Algal component of lichens is called mycobiont.",
            "Fungal component of lichens is called phycobiont.",
            "Lichens are not good pollution indicators."
        ],
        "correct_answer": "Lichens are not good pollution indicators."
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
        "question": "Which statement is wrong for viruses?",
        "options": [
            "All are parasites",
            "All of them have helical symmetry",
            "They have the ability to synthesize nucleic acids and proteins",
            "Antibiotics have no effect on them"
        ],
        "correct_answer": "All of them have helical symmetry"
    },

    {
	"question": "The lowest category of plants that is characterized on the basis of both vegetative and reproductive features is",
	"options": [
		"Genus",
		"Species",
		"Class",
		"Family"
	],
"correct_answer": "Species"
},
{
"question": "Mad cow disease in cattle and Cr Jacob disease in humans are due to infection by__________________ .",
"options": [
"Bacterium",
"Virus",
"Viroid",
"Prion"
],
"correct_answer": "Prion"
},
{
"question": "Cr-Jacob disease (CJD) in humans is caused by:",
"options": [
"An agent which consists of abnormally folded protein and is smaller in size to viruses",
"An agent having DNA",
"An agent which consists of abnormally folded protein and is similar in size to viruses",
"The same agent which causes potato spindle tuber disease"
],
"correct_answer": "An agent which consists of abnormally folded protein and is smaller in size to viruses"
},
{
"question": "Given below are two statements:\nAssertion (A): Sporozoans lack locomotory structures\nReason (R): Sporozoans are parasites\n1. Both (A) and (R) are true and (R) is the correct explanation of (A).\n2. Both (A) and (R) are true but (R) is not the correct explanation of (A).\n3. (A) is true but (R) is false.\n4. Both (A) and (R) are false.",
"options": [
"Both (A) and (R) are true and (R) is the correct explanation of (A).",
"Both (A) and (R) are true but (R) is not the correct explanation of (A).",
"(A) is true but (R) is false.",
"Both (A) and (R) are false."
],
"correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
},
{
"question": "The biological names are generally in ____(i)____and printed in italics to indicate their _____(ii)______origin.\nSelect the correct option to fill in the blanks (i) and (ii)",
"options": [
"English - Latin",
"Latin - Latin",
"Greek - Greek",
"Latin - Greek"
],
"correct_answer": "Latin - Latin"
},
{
    "question": "Consider the following statements:\tI. Pteridophytes are the first terrestrial plants to possessvascular bundles.\tII. Main plant body in pteridophytes is sporophyte whichis differentiated into true stem and leaves.\tIII. Genera like Selaginella and Salvinia are heterosporous.\tWhich of the above statements are true?",
    "options": [
        "I and II only",
        "I and III only",
        "II and III only",
        "I, II and III"
    ],
    "correct_answer": "I and III only"
},
{
    "question": "Which of the following statements is correct?",
    "options": [
        "Lichens do not grow in polluted areas.",
        "Algal component of lichens is called mycobiont.",
        "Fungal component of lichens is called phycobiont.",
        "Lichens are not good pollution indicators."
    ],
    "correct_answer": "Lichens are not good pollution indicators."
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
    "question": "Which statement is wrong for viruses?",
    "options": [
        "All are parasites",
        "All of them have helical symmetry",
        "They have the ability to synthesize nucleic acids and proteins",
        "Antibiotics have no effect on them"
    ],
    "correct_answer": "All of them have helical symmetry"
},
{
    "question": "The lowest category of plants that is characterized on the basis of both vegetative and reproductive features is",
    "options": [
        "Genus",
        "Species",
        "Class",
        "Family"
    ],
    "correct_answer": "Species"
},
{
    "question": "Mad cow disease in cattle and Cr Jacob disease in humans are due to infection by__________________ .",
    "options": [
        "Bacterium",
        "Virus",
        "Viroid",
        "Prion"
    ],
    "correct_answer": "Prion"
},
{
    "question": "Cr-Jacob disease (CJD) in humans is caused by:",
    "options": [
        "An agent which consists of abnormally folded protein and is smaller in size to viruses",
        "An agent having DNA",
        "An agent which consists of abnormally folded protein and is similar in size to viruses",
        "The same agent which causes potato spindle tuber disease"
    ],
    "correct_answer": "An agent which consists of abnormally folded protein and is smaller in size to viruses"
},
{
    "question": "Given below are two statements:\nAssertion (A): Sporozoans lack locomotory structures\nReason (R): Sporozoans are parasites\n1. Both (A) and (R) are true and (R) is the correct explanation of (A).\n2. Both (A) and (R) are true but (R) is not the correct explanation of (A).\n3. (A) is true but (R) is false.\n4. Both (A) and (R) are false.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
},
{
    "question": "The biological names are generally in ____(i)____and printed in italics to indicate their _____(ii)______origin.\nSelect the correct option to fill in the blanks (i) and (ii)",
    "options": [
        "English - Latin",
        "Latin - Latin",
        "Greek - Greek",
        "Latin - Greek"
    ],
    "correct_answer": "Latin - Latin"
},

{
    "question": "Choose the correct statements:\na. Bones support and protect softer tissues and organs\nb. Weight-bearing function is served by limb bones\nc. Ligament is the site of production of blood cells.\nd. Adipose tissue is specialized to store fats.\ne. Tendons attach one bone to another.\nChoose the most appropriate answer from the options given below:",
    "options": [
        "(a), (b), and (d) only",
        "(b), (c), and (e) only",
        "(a), (c), and (d) only",
        "(a), (b), and (e) only"
    ],
    "correct_answer": "(a), (b), and (d) only"
},
{
    "question": "Read the following statements carefully and choose the option with only incorrect statements.\na. All multicellular animals exhibit the same pattern of organization of cells.\nb. Organ level of organization is exhibited by members of Platyhelminthes and other higher phyla where tissues are grouped together to form organs.\nc. Organ systems in different groups of animals exhibit various patterns of complexities.\nd. In all multicellular animals which have organ level of body organization, a complete digestive system has two openings, mouth and anus.",
    "options": [
        "(a) and (b)",
        "(b) and (c)",
        "(a), (b), and (c)",
        "(a) and (d)"
    ],
    "correct_answer": "(a) and (b)"
},
{
    "question": "Read the following statements A and B (about chordates) and choose the correct answer from the given options:\nA:Protochordates are exclusively marine and havenotochord present only in larval tail.\nB:In all vertebrates, notochord is replaced by a bony vertebral column in the adult.",
    "options": [
        "Both statements A and B are correct",
        "Both statements A and B are incorrect",
        "Only statement A is correct",
        "Only statement B is correct"
    ],
    "correct_answer": "Both statements A and B are incorrect"
},
{
    "question": "If a teacher wants to demonstrate that some invertebrates possess a closed circulatory system, the teacher should dissect a",
    "options": [
        "Asterias",
        "Pheretima",
        "Pinctada",
        "Aplysia"
    ],
    "correct_answer": "Pheretima"
},
{
    "question": "Match the following diseases with the causative organism and select the correct option:\n\tColumn I\t\t\t\t\tColumn II\n\tGregarious, polyphagous pest\t\t\tAsterias\n\tAdult with radial symmetry and larva withbilateral symmetry\tScorpion\n\tBook lungs\t\t\t\t\tCtenoplana\t\t\tBioluminescence\t\t\t\tLocusta\n\t(a)\t(b)\t(c)\t(d)\n(1)\t(iv)\t(i)\t(ii)\t(iii)\n(2)\t(iii)\t(ii)\t(i)\t(iv)\n(3)\t(ii)\t(i)\t(iii)\t(iv)\n(4)\t(i)\t(iii)\t(ii)\t(iv)",
    "options": [
        "(iii) (iv) (i) (ii)",
        "(iv) (ii) (iii) (i)",
        "(i) (iv) (iii) (ii)",
        "(ii) (iii) (iv) (i)"
    ],
    "correct_answer": "(ii) (iii) (iv) (i)"
},
{
    "question": "A marine cartilaginous fish that can produce electric current is:",
    "options": [
        "Pristis",
        "Torpedo",
        "Trygon",
        "Scoliodon"
    ],
    "correct_answer": "Torpedo"
},
{
    "question": "Which of the following statements is not true about a frog?",
    "options": [
        "The body colour offers it protective colouration",
        "Summer sleep of frog is called aestivation",
        "Tail is present in the lifecycle of frog",
        "Mouth is bounded by a pair of lips"
    ],
    "correct_answer": "Tail is present in the lifecycle of frog"
},
{
    "question": "Which insect is useful for us?",
    "options": [
        "Periplaneta",
        "Musca",
        "Bombyx",
        "Mosquitoes"
    ],
    "correct_answer": "Bombyx"
},
{
    "question": "Match the following columns and select the correct option.\n\tColumn I\t\t\tColumn II\n(a)6 - 15 pairs of gill slits\t(i)\tTrygon\n(b)Heterocercal caudal fin\t(ii)\tCyclostomes\n(c)Air Bladder\t\t(iii)\tChondrichthyes\n(d)Poison sting\t\t(iv)\tOsteichthyes\nOptions:\t(a)\t(b)\t(c)\t(d)",
    "options": [
        "iii ii iv i",
        "iv ii iii i",
        "i iv iii ii",
        "ii iii iv i"
    ],
    "correct_answer": "ii iii iv i"
},
{
    "question": "Like other animals with bilateral symmetry, flatworms have:",
    "options": [
        "an internal body cavity",
        "segmented bodies",
        "three germ layers",
        "specialized circulatory and respiratory organs"
    ],
    "correct_answer": "three germ layers"
},

{
    "question": "Which one of the following animals is correctly matched with its one characteristic and the taxon?\n\t Animal\t\tCharacteristic\t\tTaxon\n1.\tMillipede\tVentral nerve cord\tArachnids\n2.    \tSea Anemone\tTriploblastic\t\tCnidaria\n3.\tSilverfish\tPectoral and pelvicfins\tChordata\n4.\tDuckbilledplatypus\tOviparous\t\tMammalian",
    "options": [
        "Only II",
        "Only I and II",
        "Only II and III",
        "Only III"
    ],
    "correct_answer": "Only II"
},
{
    "question": "The structure present in all adult vertebrates is:",
    "options": [
        "Notochord",
        "Dorsal tubular nerve cord",
        "Pharyngeal gill slits",
        "All of the above"
    ],
    "correct_answer": "All of the above"
},
{
    "question": "Monkey, gorilla, gibbon, tiger, cat and dog do not belong to the same:",
    "options": [
        "Phylum",
        "Order",
        "Class",
        "Kingdom"
    ],
    "correct_answer": "Order"
},
{
    "question": "Given below are two statements:\nAssertion (A): Frog is a ureotelic animal.\nReason (R): They excrete nitrogenous waste in form of urea.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
},
{
    "question": "For female frog, which of the following is false?\nI. One pair ovaries is situated near kidneys\nII. Ovary has functional connection with kidney\nIII. Convoluted, tubular, ciliated and glandular oviductarises from ovary and opens into cloaca\nIV. Oviduct and ureter open separately into the cloaca\nV. A female frog can lay 2500-3000 ova at a time",
    "options": [
        "I and II",
        "only II",
        "I and IV",
        "IV and V"
    ],
    "correct_answer": "IV and V"
},
{
    "question": "Given below are two statements:\nAssertion (A): All vertebrates possess notochord during embryonic period only.\nReason (R): In all adult vertebrates, notochord is replaced by bony vertebral column.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are false."
},
{
    "question": "Identify the correct statements regarding the members of Phylum Aschelminthes:\nI. Their body is circular in cross-section\nII. Alimentary canal is complete\nIII. Males, are often, longer than females",
    "options": [
        "Only II",
        "Only I and II",
        "Only II and III",
        "Only III"
    ],
    "correct_answer": "Only II"
},
{
    "question": "The larvae in echinoderms are:\nI. Radially symmetrical\t\tII. Free swimming",
    "options": [
        "Only I",
        "Only II",
        "Both I and II",
        "Neither I nor II"
    ],
    "correct_answer": "Both I and II"
},
{
    "question": "Select the Taxon mentioned that represents both marine and fresh water species:",
    "options": [
        "Echinoderms",
        "Ctenophora",
        "Cephalochordata",
        "Cnidaria"
    ],
    "correct_answer": "Cnidaria"
},

{
    "question": "Identify the incorrectly matched pair:\n\tAnimals\t\t\t\t\tFeature present in both\n1.\tBalanoglossus and Pinctada\tOpen circulatory system\n2.\tBranchiostoma and Ascidia\tPersistent notochord\n3.\tAplysia and Pheretima\t\tTrue coelom\n4.\tGorgonia and Pennatula\t\tCnidoblasts",
    "options": [
        "Open circulatory system",
        "Persistent notochord",
        "True coelom",
        "Cnidoblasts"
    ],
    "correct_answer": "Cnidoblasts"
},
{
    "question": "Given below are two statements:\nAssertion (A): Frog maintain ecological balances.\nReason (R): Frog serves as an important link of food chain and food web in ecosystem.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
},
{
    "question": "Which of the following features is not present in the phylum–Arthropoda?",
    "options": [
        "Metameric segmentation",
        "Parapodia",
        "Jointed appendages",
        "Chitinous exoskeleton"
    ],
    "correct_answer": "Parapodia"
},
{
    "question": "Given below are two statements:\nAssertion (A): Platyhelminthes have two openings to the outside of body that serve as mouth and anus respectively.\nReason (R): A complete digestive system has two openings to outside of body where anterior opening usually acts as anus.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
},
{
    "question": "The water vascular system in Antedon:",
    "options": [
        "Functions in locomotion, feeding and gas exchange",
        "Is bilateral in organisation, even though the animal is radially symmetrical",
        "Moves water through the animals body during suspension feeding",
        "Is analogous to the gastrovascular cavity of flatworms"
    ],
    "correct_answer": "Functions in locomotion, feeding and gas exchange"
},
{
    "question": "Which of the following is a common feature between Pheretima and Ascaris?",
    "options": [
        "Presence of true coelom",
        "Presence of metameres",
        "Absence of pharynx",
        "Presence of bilateral symmetry"
    ],
    "correct_answer": "Presence of true coelom"
},
{
    "question": "Given below are two statements:\nI Amphibians and reptiles have a 3-chambered heart with two atria and a single ventricle, and are oviparous in nature\nII Crocodiles possess a 4 chambered heart with two ventricles and two atria and are viviparous in nature\nSelect the most appropriate option:",
    "options": [
        "I is correct but II is incorrect.",
        "I is incorrect but II is correct.",
        "Both I and II are correct.",
        "Both I and II are incorrect."
    ],
    "correct_answer": "Both I and II are incorrect."
},
{
    "question": "Match each item in Column I with one item in Column II regarding taxonomic categories of humans and chose your answer from the codes given below:\nColumn I\tColumn II\nI.Family\t1. Primata\nII. Order\t2. Hominidae\nIII. Class\t3. Chordata\nIV. Phylum\t4. Mammalia\nCodes:\n\tI\tII\tIII\tIV",
    "options": [
        "1\t2\t3\t4",
        "2\t1\t4\t3",
        "2\t1\t3\t4",
        "1\t2\t4\t3"
    ],
    "correct_answer": "2\t1\t4\t3"
},
{
    "question": "Which of the following characteristics is not shared by birds and mammals?",
    "options": [
        "Breathing using lungs",
        "Viviparity",
        "Warm-blooded nature",
        "Ossified endoskeleton"
    ],
    "correct_answer": "Viviparity"
},
{
    "question": "Which one of the following categories of animals, is correctly described with no single exception in it?",
    "options": [
        "All bony fishes have four pairs of gills and an operculum on each side",
        "All sponges are marine and have collared cells",
        "All mammals are viviparous and possess a diaphragm for breathing",
        "All reptiles possess scales, have a three-chambered heart, and are cold blood (poikilothermal)"
    ],
    "correct_answer": "All mammals are viviparous and possess a diaphragm for breathing"
},
{
    "question": "Identify the incorrect statement:",
    "options": [
        "Metamerism appeared for the first time in annelida",
        "Arthropods have jointed appendages and chitinous exoskeleton",
        "Reptiles are endotherms",
        "Forelimbs of birds are modified into wings"
    ],
    "correct_answer": "Reptiles are endotherms"
},
{
    "question": "The unique mammalian characteristics are:",
    "options": [
        "pinna, monocondylic skull and mammary glands",
        "hairs, tympanic membrane and mammary glands",
        "hairs, pinna and mammary glands",
        "hairs, pinna and indirect development"
    ],
    "correct_answer": "hairs, pinna and mammary glands"
},

{
    "question": "The fertilization and development is:",
    "options": [
        "internal and indirect in Ctenophora",
        "internal and indirect in Porifera",
        "external and direct in Aschelminthes",
        "external and direct in Echinodermata"
    ],
    "correct_answer": "external and direct in Echinodermata"
},
{
    "question": "Octopus has:",
    "options": [
        "Tetrameric radial symmetry",
        "Hexameric radial symmetry",
        "Octomeric radial symmetry",
        "Bilateral symmetry"
    ],
    "correct_answer": "Bilateral symmetry"
},
{
    "question": "Which of the following is considered as the most anterior part of Balanoglossus?",
    "options": [
        "Proboscis",
        "Collar",
        "Trunk",
        "Stomochord"
    ],
    "correct_answer": "Proboscis"
},
{
    "question": "In which of the following animals, the digestive tract has additional chambers like crop and gizzard?",
    "options": [
        "Pavo, Psittacula, Corvus",
        "Corvus, Columba, Chameleon",
        "Bufo, Balaenoptera, Bangarus",
        "Catla, Columba, Crocodilus"
    ],
    "correct_answer": "Catla, Columba, Crocodilus"
},
{
    "question": "At which of the following categories, number of similar characters amongst the organisms will be less?",
    "options": [
        "Division",
        "Family",
        "Order",
        "Genus"
    ],
    "correct_answer": "Genus"
},
{
    "question": "The characteristics of class Reptilia are:",
    "options": [
        "Body covered with moist skin which is devoid of scales, the ear is represented by a tympanum, alimentary canal, urinary and reproductive tracts open into a common cloaca",
        "Freshwater animals with a bony endoskeleton and air bladder to regulate buoyancy",
        "Marine animals with cartilaginous endoskeletons, bodies covered with placoid scales",
        "Body covered with dry and cornified skin, scales over the body are epidermal, they do not have external ears"
    ],
    "correct_answer": "Body covered with dry and cornified skin, scales over the body are epidermal, they do not have external ears"
},
{
    "question": "Which of the following taxonomic categories contains organisms least similar to one another?",
    "options": [
        "Class",
        "Genus",
        "Family",
        "Species"
    ],
    "correct_answer": "Species"
},
{
    "question": "How many of the animals given in the box below are triploblastic, have a true coelom but lack segmentation? Antedon, Laccifer, Limulus, Aplysia, Dentalium, Ancylostoma, Hirudinaria, Sepia, Ophiura, Nereis",
    "options": [
        "4",
        "5",
        "6",
        "7"
    ],
    "correct_answer": "4"
},
{
    "question": "What is the molality of Na+ in a solution containing 3.00 g NaCl (M=58.4), 9.00 g glucose(M=180.0), and 168 g H2O (M=18.0)?",
    "options": [
        "5.50 × 10^-3 m",
        "0.285 m",
        "0.306 m",
        "0.777 m"
    ],
    "correct_answer": "0.285 m"
},
{
    "question": "Match List I with List II\nList I(IUPAC Name) List II(atomic number)\nA. Unnilennium I. 120\nB. Ununpentium II. 111\nC. unbinilium III. 115\nD. Unununnium IV. 109\n V. 110\nChoose the correct answer from the options given below:",
    "options": [
        "A ‐ IV, B ‐ II, C ‐ I, D ‐ III",
        "A ‐ V, B ‐ II, C ‐ IV, D ‐ III",
        "A ‐ IV, B ‐ III, C ‐ I, D ‐ II",
        "A ‐ IV, B ‐ II, C ‐ I, D ‐ V"
    ],
    "correct_answer": "A ‐ IV, B ‐ II, C ‐ I, D ‐ V"
},
{
    "question": "Which of the following statements regarding the ionization energy of gas-phase atoms is correct?",
    "options": [
        "The first ionization energy of a group 1 element is always greater than the first ionization energy of the group 2 element in the same row of the periodic table.",
        "In the second row of the periodic table, the first ionization energy is directly proportional to the atomic radius.",
        "Among the elements from Al (Z = 13) to Ar (Z = 18), the first ionization energy increases monotonically with atomic number.",
        "Among the elements of group 16, the first ionization energy decreases monotonically with atomic number."
    ],
    "correct_answer": "Among the elements of group 16, the first ionization energy decreases monotonically with atomic number."
},
{
    "question": "The correct order of increasing C — O bond length of CO, CO3^2- and CO2 is:",
    "options": [
        "CO3^2- < CO2 < CO",
        "CO2 < CO3^2- < CO",
        "CO < CO3^2- < CO2",
        "CO < CO2 < CO3^2-"
    ],
    "correct_answer": "CO3^2- < CO2 < CO"
},
{
    "question": "138 g of ethyl alcohol is mixed with 72 g of water. The ratio of mole fraction of alcohol to water is:",
    "options": [
        "3 : 4",
        "1 : 2",
        "1 : 4",
        "1 : 1"
    ],
    "correct_answer": "1 : 2"
},
{
    "question": "Consider the electronic configuration of the following elements:\nA : 1s2 2s2 2p6 3s1\nB : 2s2 2s2 2p6 3s2 3p5\nC : 1s2 2s2 2p6 3s2 3p2\nD : 1s2 2s2 2p5\nThe element having a maximum difference between the first and second ionization energy is:",
    "options": [
        "A",
        "C",
        "B",
        "D"
    ],
    "correct_answer": "B"
},

{
    "question": "Which pair of symbols represents nuclei with the same number of neutrons?",
    "options": [
	"56Co and 58Co",
	"57Mn and 57Fe",
	"57Fe and 58Ni",
	"57Co and 58Ni"
    ],
    "correct_answer": "57Fe and 58Ni"
},

{
    "question": "If 28 g of Fe reacts with 24 g of S to produce FeS, what would be the limiting reagent and how many grams of excess reagent would be present in the vessel at the end of         the reaction, respectively?\nFe + S −→ FeS",
    "options": [
"Fe and 10 g",
"Fe and 8 g",
"S and 15 g",
"S and 10 g"
],
"correct_answer": "S and 10 g"
},

{
"question": "Europium element belongs to:",
"options": [
"s – block element",
"p – block element",
"d – block element",
"f – block element"
],
"correct_answer": "f – block element"
},

{
"question": "Assertion (A): Irrespective of the source, a given compound always contains the same elements in the same proportion.\nReason (R): This law is referred to as the law of multiple proportions.",
"options": [
"Both (A) and (R) are true and (R) is the correct explanation of (A).",
"Both (A) and (R) are true but (R) is not the correct explanation of (A).",
"(A) is true but (R) is false.",
"Both (A) and (R) are false."
],
"correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
},

{
"question": "The volume of oxygen gas (O2) needed to completely burn 1 L of propane gas (C3H8) (both O2 & propane measured at 0°C and 1 atm) will be:",
"options": [
"7 L",
"6 L",
"5 L",
"10 L"
],
"correct_answer": "5 L"
},

{
"question": "Round off 0.1545 up to three significant figures:",
"options": [
"0.153",
"0.154",
"0.16",
"0.150"
],
"correct_answer": "0.154"
},

{
"question": "Assertion (A): Angular momentum of the electron in the orbit which has four subshells is.\nReason (R): Angular momentum of the electron is quantized.",
"options": [
"Both (A) and (R) are true and (R) is the correct explanation of (A).",
"Both (A) and (R) are true but (R) is not the correct explanation of (A).",
"(A) is true but (R) is false.",
"(A) is false but (R) is true."
],
"correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
},

{
"question": "Which species has the largest ionic radius?",
"options": [
"S2−",
"Cl−",
"K+",
"Ca2+"
],
"correct_answer": "Ca2+"
},

{
"question": "A monochromatic infrared range finder of power 1mW emits photons with wavelength 1000 nm in 0.1 second. The number of photons emitted in 0.1 second is- (Given: h = 6.626 × 10−34J s, c = 3 × 108m s−1, Avogadro number = 6.022 × 1023)",
"options": [
"30 × 10^37",
"5 × 10^14",
"30 × 10^34",
"5 × 10^11"
],
"correct_answer": "5 × 10^14"
},

{
"question": "Assertion (A): Removal of the s-electron is relatively more difficult than the removal of the p-electron of the same main shell.\nReason (R): s-electrons are closer to the nucleus than p-electrons of the same shell and hence, are more strongly attracted by a nucleus.",
"options": [
"Both (A) and (R) are true and (R) is the correct explanation of (A).",
"Both (A) and (R) are true but (R) is not the correct explanation of (A).",
"(A) is true but (R) is false.",
"Both (A) and (R) are false."
],
"correct_answer": "Both (A) and (R) are true and (R) is the correct explanation of (A)."
},

{
"question": "ψ2 = 0 represents:",
"options": [
"a node",
"an orbital",
"angular wave function",
"wave function"
],
"correct_answer": "a node"
},

{
"question": "Match the types of series given in Column I with the wavelength range given in Column II and choose the correct option.\nColumn 1\t\tColumn 2\nA. Lyman\t\t1. Ultraviolet\nB. Paschen\t\t2. Infrared\nC. Balmer\t\t3. Visible\nD. p-fund",
"options": [
"A-1, B-2, C-3, D-2",
"A-3, B-3, C-2, D-1",
"A-1, B-1, C-2, D-3",
"A-2, B-3, C-2, D-1"
],
"correct_answer": "A-1, B-2, C-3, D-2"
},

{
"question": "The wavelength of a spectral line emitted by a hydrogen atom in the Lyman series is 16/15R cm. What is the value of n2? (R = Rydberg constant)",
"options": [
"2",
"3",
"4",
"1"
],
"correct_answer": "2"
},

{
"question": "If the concentration of glucose (C6H12O6) in the blood is 0.9 g L^-1, then the molarity of glucose in the blood is",
"options": [
"5 M",
"50 M",
"0.005 M",
"0.05 M"
],
"correct_answer": "0.05 M"
},

{
"question": "The volume occupied by ten molecules of water (density 1g cm^-3) is :",
"options": [
"18 cm^3",
"22400 cm^3",
"6.02310^-23 cm^3",
"3.010^-22 cm^3"
],
"correct_answer": "6.023*10^-23 cm^3"
},

{
"question": "Which property decreases from left to right across the periodic table and increases from top to bottom?",
"options": [
"Atomic radius.",
"Electronegativity.",
"Ionization energy.",
"Melting point."
],
"correct_answer": "Atomic radius."
},

{
"question": "Match List-I with List-II:\nList-I\t\t\tList-II\n(quantum number)\t\t(Orbital)\n(A) n = 2, l= 1\t\t( I) 2s\n(B) n = 3, l= 2\t\t( II) 3s\n(C) n = 3, l= 0\t\t(III) 2p\n(D) n = 2, l= 0\t\t(IV) 3d\nChoose the correct answer from the options given below:\t(A)\t(B)\t(C)\t(D)",
"options": [
"(III)\t(IV)\t(I)\t(II)",
"(IV)\t(III)\t(I)\t(II)",
"(IV)\t(III)\t(II)\t(I)",
"(III)\t(IV)\t(II)\t(I)"
],
"correct_answer": "(IV)\t(III)\t(II)\t(I)"
},

{
"question": "The mole fraction of NaOH in the aqueous solution is 0.001. The molarity of NaOH solution will be (For dilute solution molality and molarity are approx. same)",
"options": [
"0.056 M",
"55.55 M",
"0.001 M",
"Data is insufficient"
],
"correct_answer": "0.001 M"
},

{
"question": "The empirical formula of a compound that contains 40.9 percent carbon, 4.58 percent hydrogen, and 54.52 percent oxygen and has a molar mass of 88 g/mol is:",
"options": [
"C3H40",
"CH4O3",
"C3H2O3",
"C3H4O3"
],
"correct_answer": "C3H4O3"
},

{
"question": "Which characteristics of an atomic orbital are most closely associated with the magnetic quantum number ml ?",
"options": [
"Size",
"Shape",
"Occupancy",
"Orientation"
],
"correct_answer": "Orientation"
},

{
"question": "The total number of semi-metals among the following is: Si, Sb, Ge, Ga, As, Sn, Se",
"options": [
"5",
"4",
"3",
"2"
],
"correct_answer": "5"
},

{
"question": "How many H atoms are in 3.4 g of C12H22O11?",
"options": [
"6.0 × 10^23",
"1.3 × 10^23",
"3.8 × 10^22",
"6.0 × 10^21"
],
"correct_answer": "6.0 × 10^23"
},

{
"question": "Which set of quantum numbers (n, l, ml, ms) is not permitted by the rules of quantum mechanics?",
"options": [
"1, 0, 0, +1/2",
"2, 1, -1, −1/2",
"3, 3, 1, -−1/2",
"4, 3, 2, +1/2"
],
"correct_answer": "3, 3, 1, -−1/2"
},

{
"question": "The ratio of masses of oxygen and nitrogen in a particular gaseous mixture is 1:4. The ratio of a number of their molecules is:",
"options": [
"7:32",
"1:8",
"3:16",
"1:4"
],
"correct_answer": "3:16"
},

{
"question": "Match the following :",
"options": [
"(a) CO (i) Basic",
"(b) BaO (ii) Neutral",
"(c) Al2O3 (iii) Acidic",
"(d) Cl2O7 (iv) Amphoteric"
],
"correct_answer": "(a) (ii), (b) (i), (c) (iv), (d) (iii)"
},

{
"question": "When the atoms: Ba, Cs, Mg, and Na are arranged in order of increasing size, the correct order is:",
"options": [
"Cs < Na < Mg < Ba",
"Mg < Na < Ba < Cs",
"Mg < Ba < Na < Cs",
"Ba < Mg < Na < Cs"
],
"correct_answer": "Mg < Na < Ba < Cs"
},

{
"question": "How many sulphur atoms are there in 3.00 g of iron pyrite, FeS2 (M = 120.0)?",
"options": [
"27.53 × 10^21",
"1.51 × 10^22",
"3.01 × 10^22",
"6.02 × 10^23"
],
"correct_answer": "1.51 × 10^22"
},

{
"question": "Helium can be singly ionized by losing one electron to become the cation. Which of the following statements is true concerning this helium cation?",
"options": [
"The line spectrum of this helium cation will resemble the line spectrum of a hydrogen atom.",
"The line spectrum of this helium cation will resemble the line spectrum of a lithium cation.",
"The line spectrum of this helium cation will remain the same as for unionized helium.",
"The line spectrum of this helium cation will resemble the line spectrum of a hydrogen ion."
],
"correct_answer": "The line spectrum of this helium cation will resemble the line spectrum of a hydrogen atom."
},

{
"question": "Find the incorrect statement.",
"options": [
"Valence electron and valency are the same for group 1.",
"p-block elements are metals, nonmetals, and metalloids.",
"Noble gases have 8 valence electrons except He.",
"The smallest atom in the periodic table is Ne."
],
"correct_answer": "The smallest atom in the periodic table is Ne."
},

{
"question": "Which of the following compounds has the least tendency to form hydrogen bonds between molecules?",
"options": [
"NH3",
"H2NOH",
"HF",
"CH3F"
],
"correct_answer": "CH3F"
},

{
"question": "Which one of the following statements is true about the structure of CO3^2− ion?",
"options": [
"It can be explained by considering sp3 hybridization.",
"Out of the three C–O bonds, two are longer and one is shorter.",
"It has three Sigma and three π-bonds.",
"All three C–O bonds are equal in length with a bond order in between 1 and 2."
],
"correct_answer": "All three C–O bonds are equal in length with a bond order in between 1 and 2."
},

{
"question": "The pair with similar geometry(shape) is:",
"options": [
"PCl3, NH4+",
"BeCl2, H2O",
"CH4, CCl4",
"IF5, PF5"
],
"correct_answer": "IF5, PF5"
},

{
"question": "The correct order of stability for the following species is:",
"options": [
"Li2 < He2+ < O2+ < C2",
"C2 < O2+ < Li2 < He2+",
"He2+ < Li2 < C2 < O2+",
"O2+ < C2 < Li2 < He2+"
],
"correct_answer": "O2+ < C2 < Li2 < He2+"
},

{
"question": "Which of the following is the correct order of dipole moment?",
"options": [
"NH3 < BF3 < NF3 < H2O",
"BF3 < NF3 < NH3 < H2O",
"BF3 < NH3 < NF3 < H2O",
"H2O < NF3 < NH3 < BF3"
],
"correct_answer": "H2O < NF3 < NH3 < BF3"
},

{
"question": "How many millimoles of methane, CH4, are present in 6.4 g of this gas?",
"options": [
"0.40",
"4.0",
"40",
"4.0 x 10^2"
],
"correct_answer": "4.0"
},

{
"question": "Match List I with List II",
"options": [
"A ‐ IV, B ‐ III, C ‐ I, D ‐ II",
"A ‐ I, B ‐ II, C ‐ IV, D ‐ III",
"A ‐ II, B ‐ I, C ‐ IV, D ‐ III",
"A ‐ IV, B ‐ II, C ‐ I, D ‐ III"
],
"correct_answer": "A ‐ II, B ‐ I, C ‐ IV, D ‐ III"
},

{
"question": "Given below are two statements\nStatementI: SF6 and NO are examples of the expanded octet and odd electron molecules respectively.\nStatementII: BeCl2 molecules have hybrid orbitals with 50 % s character as well as a linear geometry.\nIn light of the above statements, choose the correctanswer from the options given below",
"options": [
"Both Statement I and Statement II are true.",
"Both Statement I and Statement II are false.",
"Statement I is true but Statement II is false.",
"Statement I is false but Statement II is true."
],
"correct_answer": "Both Statement I and Statement II are false."
},

{
"question": "Among the compounds shown below which one will have a linear structure?\n1. NO2\n2. HOCl\n3. O3\n4. N2O",
"options": [
    "NO2",
    "HOCl",
    "O3",
"N2O"
],
"correct_answer": "N2O"
},
{
"question": "Which molecules/ions are most paramagnetic?\n1. B2\n2. C2\n3. O+2\n4. O−2",
"options": [
"B2",
"C2",
"O+2",
"O−2"
],
"correct_answer": "O−2"
},

{
"question": "The covalent characters of CaCl2, BaCl2, SrCl2 and MgCl2 follow the order :\n1. CaCl2 < BaCl2 < SrCl2 < MgCl2\n2. BaCl2 < SrCl2 < CaCl2 < MgCl2\n3. CaCl2 < BaCl2 < MgCl2 < SrCl2\n4. SrCl2 < MgCl2 < CaCl2 < BaCl2",
"options": [
"CaCl2 < BaCl2 < SrCl2 < MgCl2",
"BaCl2 < SrCl2 < CaCl2 < MgCl2",
"CaCl2 < BaCl2 < MgCl2 < SrCl2",
"SrCl2 < MgCl2 < CaCl2 < BaCl2"
],
"correct_answer": " BaCl2 < SrCl2 < CaCl2 < MgCl2"
},
{
  "question": "The equilibrium concentrations of the species in the reaction A B C D ++ are 2, 3, 10 and 6 mol L–1, respectively at 300 K. ΔGº for the reaction is (R = 2 cal/mol K)",
  "options": [
    "-137.26 cal",
    "-1381.80 cal",
    "-13.73 cal",
    "-1372.60 cal"
  ],
  "correct_answer": "-1372.60 cal"
},
{
"question": "A child riding on a merry-go-round jumps off a wooden horse and starts walking towards the center of the ride. As he moves, the acceleration he feels:\n1. increases, because his tangential speed decreases.\n2. increases, because his radius from the center decreases.\n3. decreases, because his tangential speed increases.\n4. decreases, because his radius from the center decreases.",
"options": [
"increases, because his tangential speed decreases.",
"increases, because his radius from the center decreases.",
"decreases, because his tangential speed increases.",
"decreases, because his radius from the center decreases."
],
"correct_answer": "increases, because his radius from the center decreases."
},

{
  "question": "The reaction that does NOT take place in a blast furnace between 900 K to 1500 K temperature range during extraction of iron is :",
  "options": [
    "FeO + CO → Fe + CO2",
    "C + CO2 → 2CO",
    "CaO + SiO2 → CaSiO3",
    "Fe2O3 + CO → 2FeO + CO2"
  ],
  "correct_answer": "CaO + SiO2 → CaSiO3"
},

{
"question": "The unit of length, fermi is used for the measurement of:\n1. distance of stars\n2. interatomic dimension\n3. height of mountain\n4. nuclear dimension",
"options": [
"distance of stars",
"interatomic dimension",
"height of mountain",
"nuclear dimension"
],
"correct_answer": "interatomic dimension"
},

{
"question": "A particle is in a uniform circular motion with a time period of 4 s and radius √2 m. What is the magnitude of displacement in 3 s?\n1. 4 m\n2. 3 m\n3. 2 m\n4. 1 m",
"options": [
"4 m",
"3 m",
"2 m",
"1 m"
],
"correct_answer": "1 m"
},

{
"question": "A car is moving with speed of 150 km/h and after applying the brake, it will move 27 m before it stops. If the same car is moving with a speed of one-third the reported speed, then it will stop after travelling a distance of:\n1. 4 m\n2. 3 m\n3. 2 m\n4. 1 m",
"options": [
"4 m",
"3 m",
"2 m",
"1 m"
],
"correct_answer": "2 m"
},
{
"question": "A sparrow cruising at 1.5 m/s begins to accelerate at a constant 0.3 m/s2 for 3 s. What is its change in velocity?",
"options": [
"0.9 m/s",
"1.5 m/s",
"1.95 m/s",
"2.4 m/s"
],
"correct_answer": "1.95 m/s"
},

{
"question": "A projectile launched at an angle θ is observed to move at an angle of 45∘ with the vertical (upward) at some point on its trajectory. If the launch angle θ was increased, then the horizontal range:",
"options": [
"decreases",
"increases",
"first increases then decreases",
"first decreases then increases"
],
"correct_answer": "increases"
},

{
    "question": "The fruit juggler, dissatisfied with simply dropping fruit, decides to throw an apricot off a cliff. The apricot leaves the top of the cliff at a speed of 35 m/s and at an angle of 50∘ above the horizontal. If the cliff is 310 m tall, how far down range is the fruit when it hits the ground?",
    "options": [
        "180 m",
        "251 m",
        "390 m",
        "1423 m"
    ],
    "correct_answer": "251 m"
},
{
    "question": "A throws a ball towards B who then catches it across the field. B throws the ball back towards A who then catches it. The angle of the throw is 30 for A while it is 60 for B's throw. The ratio of their speeds of throw, VA : VB is:",
    "options": [
        "3",
        "1/3",
        "√3",
        "1"
    ],
    "correct_answer": "√3"
},
{
    "question": "An arrow is shot into the air. When the arrow is in the air, what forces are acting on the arrow? (Ignore air resistance.)",
    "options": [
        "there are no forces.",
        "there is the force of gravity.",
        "there is the force of gravity and an upward normal force.",
        "there is the force of gravity and a forward force."
    ],
    "correct_answer": "there is the force of gravity and an upward normal force."
},
{
    "question": "A 2 kg ball at the end of a 1 m string is spun in a vertical circle. The tension in the string is 52 N when the ball is at the bottom of the circle. What is the ball's speed?",
    "options": [
        "4 m/s",
        "5 m/s",
        "6 m/s",
        "7 m/s"
    ],
    "correct_answer": "6 m/s"
},
{
    "question": "The number of significant figures in the result of (7.1 + 7.3 + 9.1) is:",
    "options": [
        "1",
        "2",
        "3",
        "4"
    ],
    "correct_answer": "3"
},
{
    "question": "In a projectile motion the velocity,",
    "options": [
        "is always perpendicular to the acceleration",
        "is never perpendicular to the acceleration",
        "is perpendicular to the acceleration for one instant only",
        "is perpendicular to the acceleration for two instants"
    ],
    "correct_answer": "is perpendicular to the acceleration for one instant only"
},
{
    "question": "Given below are two statements:\nAssertion (A): A body of mass 1 kg is making 1 rps in a circle of radius 1 m. The centrifugal force acting on it is 4 N.\nReason (R): Centrifugal force is given by F = mv^2/r.",
    "options": [
        "Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "(A) is true but (R) is false.",
        "Both (A) and (R) are false."
    ],
    "correct_answer": "Both (A) and (R) are true but (R) is not the correct explanation of (A)."
},
{
    "question": "A 40 N block is supported by two ropes. One rope is horizontal and the other makes an angle of 30 with the ceiling. The tension in the rope attached to the ceiling is approximately:",
    "options": [
        "80 N",
        "40 N",
        "34.6 N",
        "46.2 N"
    ],
    "correct_answer": "46.2 N"
},
{
    "question": "Consider the following statements and select the correct option.\nStatement (A): The dimensional correctness of an equation is verified using the principle of homogeneity.\nStatement (B): All unitless quantities are dimensionless.",
    "options": [
        "Both statements (A) and (B) are true.",
        "Both statements (A) and (B) are false.",
        "Only statement (A) is true.",
        "Only statement (B) is true."
    ],
    "correct_answer": "Only statement (A) is true."
},
{
    "question": "A ball of mass 2 kg is dropped from a height of 9.8 m and rebounds to a height of 4.9 m. If it remains in contact with the ground for 0.2 s, the average force on the ball exerted by the ground is:",
    "options": [
        "98(√2 + 1) N",
        "49(√2 + 1) N",
        "98(√2 − 1) N",
        "49(√2 − 1) N"
    ],
    "correct_answer": "49(√2 − 1) N"
},
{
    "question": "What force is needed to do 100 Joules of work on a box, while pushing it uphill at an angle of 60 with respect to the horizontal ground?",
    "options": [
        "100 N",
        "87 N",
        "50 N",
        "there is insufficient information to determine the work"
    ],
    "correct_answer": "50 N"
},

{
    "question": "A particle sits on the periphery of the wheel of a car, which is being driven along a straight road at a speed. The radius of the wheel of the car is . The instantaneous acceleration of the particle, as observed by a passenger, is:",
    "options": [
        "4v^2/R",
        "2v^2/R",
        "v^2/R",
        "v^2/2R"
    ],
    "correct_answer": "4v^2/R"
},

{
    "question": "The main scale of a vernier caliper has least count of 1 mm. 20 divisions of the vernier scale coincide with 19 divisions of the main scale. The vernier constant of the caliper is:",
    "options": [
        "0.01 cm",
        "0.01 mm",
        "0.005 cm",
        "0.005 mm"
    ],
    "correct_answer": "0.01 mm"
},
{
    "question": "Two cars having masses m1 and move in circles of radii r1 and r2 respectively. If they complete the circles in equal time, the ratio of their angular speeds w1/w2 will be:",
    "options": [
        "m1/m2",
        "r1/r2",
        "m1r1/m2r2",
        "1"
    ],
    "correct_answer": "m1r1/m2r2"
},
{
    "question": "Which one of the following ratios of physical quantities has the same dimensions as that of pressure?",
    "options": [
        "force/length",
        "energy/area",
        "energy/volume",
        "force/volume"
    ],
    "correct_answer": "force/volume"
},
{
    "question": "A car is traveling around a curved portion of a flat highway at a constant speed v. The curve has a radius R. What is the minimum coefficient of static friction between the tires and the road necessary for the car to make the curve without skidding?",
    "options": [
        "μ = √Rg",
        "μ = Rv^2/mg",
        "μ = v^2/Rg",
        "μ = R2g/v"
    ],
    "correct_answer": "μ = v^2/Rg"
},
{
    "question": "Given below are two statements:\nAssertion (A): Parabolic curve of velocity versus time implies that its acceleration varies linearly with time.\nReason (R): Parabolic curve represent quadratic function and acceleration is the first derivative of velocity so the acceleration versus time graph will be linear.",
    "options": [
        "1Both (A) and (R) are true and (R) is the correct explanation of (A).",
        "2Both (A) and (R) are true but (R) is not the correct explanation of (A).",
        "3(A) is true but (R) is false.",
        "4Both (A) and (R) are false."
    ],
    "correct_answer": "(A) is true but (R) is false."
},
{
    "question": "When a vertically oriented spring scale supports a 180 N block, the spring stretches 0.3 m from rest. Neglecting any other masses associated with the scale, what is the value of the spring constant?",
    "options": [
        "30 N/m",
        "294 N/m",
        "600 N/m",
        "5880 N/m"
    ],
    "correct_answer": "294 N/m"
},
{
    "question": "Swimming is possible on account of:",
    "options": [
        "First law of motion",
        "Second law of motion",
        "Third law of motion",
        "Newton's law of gravitation"
    ],
    "correct_answer": "Third law of motion"
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
    "question": "Which of the following is characteristic feature of cockroach regarding sexual dimorphism?",
    "options": [
        "Presence of anal styles",
        "Presence of sclerites",
        "Presence of anal cerci",
        "Dark brown body colour and anal cerci"
    ],
    "correct_answer": "Presence of anal cerci"
},

{
    "question": "Select the correct statements.",
    "options": [
        "Tetrad formation is seen during Leptotene.",
        "During Anaphase, the centromeres split and chromatids separate.",
        "Terminalization takes place during Pachytene.",
        "Nucleolus, Golgi complex and ER are reformed during Telophase.",
        "Crossing over takes place between sister chromatids of homologous chromosome."
    ],
    "correct_answer": "B and E only"
},

{
    "question": "Which of the following statements are correct?",
    "options": [
        "An excessive loss of body fluid from the body switches off osmoreceptors.",
        "ADH facilitates water reabsorption to prevent diuresis.",
        "ANF causes vasodilation.",
        "ADH causes increase in blood pressure.",
        "ADH is responsible for decrease in GFR."
    ],
    "correct_answer": "A, B and E only"
},

{
    "question": "Which one of the following is NOT an advantage of inbreeding?",
    "options": [
        "It exposes harmful recessive genes but are eliminated by selection.",
        "Elimination of less desirable genes and accumulation of superior genes takes place due to it.",
        "It decreases the productivity of inbred population, after continuous inbreeding.",
        "It decreases homozygosity."
    ],
    "correct_answer": "It decreases the productivity of inbred population, after continuous inbreeding."
},

{
    "question": "The unique mammalian characteristics are:",
    "options": [
        "hairs, pinna and mammary glands",
        "hairs, pinna and indirect development",
        "pinna, monocondylic skull and mammary glands",
        "hairs, tympanic membrane and mammary glands"
    ],
    "correct_answer": "hairs, pinna and mammary glands"
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
        st.write("your score is: ",score)
        st.session_state.Mktst1 = score
    return max(score, 0)  # Ensure score is non-negative

def app():
    # Initialize Firestore client
    db = firestore.client()

    # Check if user is logged in
    if 'username' not in st.session_state or not st.session_state['username']:
        st.error('Please login first.')
        return

    try:
        st.title("Mock Test 1 for NEET Examination")
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