Here is a new Python programming task.

Please write a function called "findVowelStartWords" that accepts two arguments. The first argument will be the name of a text file that contains part of a classic biology paper. The second argument will be the name of a text file that your function will need to create.

Your function should read the specified input file and use the "re" module to identify any multi-letter words that start with an upper-case vowel. Your function should write each of these words to the output file on a separate line (not including any white space before or after the word). For simplicity, focus on words that are preceded and followed by a space character (don't worry about words at the beginning of a line or that are followed by a punctuation mark).

Below is a description of a test to verify your code.

For this test, the following code will be executed after your code:

import os

findVowelStartWords("Gurdon.txt", "Gurdon_Output.txt")
findVowelStartWords("Kornberg.txt", "Kornberg_Output.txt")
findVowelStartWords("Mendel.txt", "Mendel_Output.txt")

def checkOutputFile(outputFilePath):
if os.path.exists(outputFilePath):
with open(outputFilePath) as outputFile:
print("{}:".format(outputFilePath))
for line in outputFile:
print(" " + line.rstrip("\n"))
print("")
else:
print("No output file exists at {}.".format(outputFilePath))

checkOutputFile("Gurdon_Output.txt")
checkOutputFile("Kornberg_Output.txt")
checkOutputFile("Mendel_Output.txt")

Below is the expected output:

Gurdon_Output.txt:
Intestinal
Embryology
ONE
It

Kornberg_Output.txt:
Arthur
University
Acta
Acta
In
ATP
Enzymatic
Enzyme
Escheriehia
Edsall

Mendel_Output.txt:
IN
OF

Below is a description of a data file that is available for testing.

File name: Mendel.txt

File contents:

EXPERIMENTS IN PLANT HYBRIDIZATION (1865)

GREGOR MENDEL

Read at the February 8th, and March 8th, 1865, meetings
of the Brünn Natural History Society

INTRODUCTORY REMARKS

EXPERIENCE OF ARTIFICIAL FERTILIZATION, such as is effected with ornamental plants in order to obtain new variations in color, has led to the experiments which will here be discussed. The striking regularity with which the same hybrid forms always reappeared whenever fertilization took place between the same species induced further experiments to be undertaken, the object of which was to follow up the developments of the hybrids in their progeny.

To this object numerous careful observers, such as Kölreuter, Gärtner, Herbert, Lecoq, Wichura and others, have devoted a part of their lives with inexhaustible perseverance. Gärtner especially in his work Die Bastarderzeugung im Pflanzenreiche [The Production of Hybrids in the Vegetable Kingdom], has recorded very valuable observations; and quite recently Wichura published the results of some profound investigations into the hybrids of the Willow. That, so far, no generally applicable law governing the formation and development of hybrids has been successfully formulated can hardly be wondered at by anyone who is acquainted with the extent of the task, and can appreciate the difficulties with which experiments of this class have to contend. A final decision can only be arrived at when we shall have before us the results of detailed experiments made on plants belonging to the most diverse orders.

Those who survey the work done in this department will arrive at the conviction that among all the numerous experiments made, not one has been carried out to such an extent and in such a way as to make it possible to determine the number of different forms under which the offspring of the hybrids appear, or to arrange these forms with certainty according to their separate generations, or definitely to ascertain their statistical relations.

It requires indeed some courage to undertake a labor of such far-reaching extent; this appears, however, to be the only right way by which we can finally reach the solution of a question the importance of which cannot be overestimated in connection with the history of the evolution of organic forms.

The paper now presented records the results of such a detailed experiment. This experiment was practically confined to a small plant group, and is now, after eight years’ pursuit, concluded in all essentials. Whether the plan upon which the separate experiments were conducted and carried out was the best suited to attain the desired end is left to the friendly decision of the reader.

[See full text here: http://tetrad.ucsf.edu/classicpapers.]

Below is a description of a data file that is available for testing.

File name: Kornberg.txt

File contents:

The early history of DNA polymerase: a commentary by Arthur Kornberg

Department of Biochemistry, Stanford University School of Medicine, Stanford, CA (U.S.A.)

on 'Enzymic synthesis of deoxyribonucleic acid' by A. Kornberg, I.R. Lehman, M.J. Bessman and E.S. Simms Biochim. Biophys. Acta 21 (1956) 197-198

The brief publication [1] in Biochimica et Biophysica Acta (BBA) entitled "Enzymic Synthesis of Deoxyribonucleic Acid", submitted May 2, 1956, was the first such report of DNA synthesis, aside from an abstract which appeared in Federation Proceedings in March of that year [2]. In the BBA paper, we (see photograph, p. 55) showed that the incorporation of [a4C]thymidine into an acid-soluble, DNase-sensitive, alkali-stable product depended on partially purified enzyme fractions, ATP and DNA which was converted to an 'active primer'. We expressed the brash hope of assembling 'genetically specific DNA'.

Two years later, we submitted two papers to the Journal of Biological Chemistry describing the 2000-fold purification of DNA polymerase and the enzymatic synthesis of the four deoxyribonucleoside triphosphates which the enzyme assembled into long chains. The papers were titled: 'The Enzymatic Synthesis of DNA. I. Preparation of Substrates and Partial Purification of an Enzyme from Escheriehia coli. II. General Properties of the Reaction.' The papers were not accepted because of the term 'DNA' in the title. The consensus among the many referees after a protracted review was that the papers would be acceptable if we used the term "polydeoxyribonucleotide" to identify the synthetic product; the use of 'DNA' could be justified only with a demonstration of genetic activity. To us this seemed unreasonable, because few if any DNA papers in the Journal had been required to fulfill this criterion. Fortunately, with accession of John Edsall to the editorship, the papers were accepted with DNA in the title [3,4].

[Full text available here: http://tetrad.ucsf.edu/classicpapers.]

Below is a description of a data file that is available for testing.

File name: Gurdon.txt

File contents:

The Developmental Capacity of Nuclei taken from Intestinal Epithelium Cells of Feeding Tadpoles

by J. B. GURDON

From the Embryology Laboratory, Department of Zoology, Oxford

WITH ONE PLATE

An important problem in embryology is whether the differentiation of cells depends upon a stable restriction of the genetic information contained in their nuclei. The technique of nuclear transplantation has shown to what extent the nuclei of differentiating cells can promote the formation of different cell types (e.g. King & Briggs, 1956; Gurdon, 1960c). Yet no experiments have so far been published on the transplantation of nuclei from fully differentiated normal cells. This is partly because it is difficult to obtain meaningful results from such experiments. The small amount of cytoplasm in differentiated cells renders their nuclei susceptible to damage through exposure to the saline medium, and this makes it difficult to assess the significance of the abnormalities resulting from their transplantation. It is, however, very desirable to know the developmental capacity of such nuclei, since any nuclear changes which are necessarily involved in cellular differentiation must have already taken place in cells of this kind.

The experiments described below are some attempts to transplant nuclei from fully differentiated cells. Many of these nuclei gave abnormal results after transplantation, and several different kinds of experiments have been carried out to determine the cause and significance of these abnormalities.

The donor cells used for these experiments were intestinal epithelium cells of feeding tadpoles. This is the final stage of differentiation of many of the endoderm cells whose nuclei have already been studied by means of nuclear transplantation experiments in Xenopus. The results to be described here may therefore be regarded as an extension of those previously obtained from differentiating endoderm cells (Gurdon, 1960c).

[See full text here: http://tetrad.ucsf.edu/classicpapers.]
