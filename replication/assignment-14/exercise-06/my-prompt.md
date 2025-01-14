Please write a Python function called `findVowelStartWords` that accepts two arguments. The first argument will be the name of an input file. The second argument will be the name of an output file.

Your function should read the specified input file and use the `re` module to identify all multi-letter words that start with an upper-case vowel. Your function should write each of these words to the output file on a separate line. DO NOT include any white space before or after the word. For simplicity, focus on words that are preceded and followed by a space character.

Here's an example input file called `Kornberg.txt`:

```
The early history of DNA polymerase: a commentary by Arthur Kornberg

Department of Biochemistry, Stanford University School of Medicine, Stanford, CA (U.S.A.)

on 'Enzymic synthesis of deoxyribonucleic acid' by A. Kornberg, I.R. Lehman, M.J. Bessman and E.S. Simms Biochim. Biophys. Acta 21 (1956) 197-198

The brief publication [1] in Biochimica et Biophysica Acta (BBA) entitled "Enzymic Synthesis of Deoxyribonucleic Acid", submitted May 2, 1956, was the first such report of DNA synthesis, aside from an abstract which appeared in Federation Proceedings in March of that year [2]. In the BBA paper, we (see photograph, p. 55) showed that the incorporation of [a4C]thymidine into an acid-soluble, DNase-sensitive, alkali-stable product depended on partially purified enzyme fractions, ATP and DNA which was converted to an 'active primer'. We expressed the brash hope of assembling 'genetically specific DNA'.

Two years later, we submitted two papers to the Journal of Biological Chemistry describing the 2000-fold purification of DNA polymerase and the enzymatic synthesis of the four deoxyribonucleoside triphosphates which the enzyme assembled into long chains. The papers were titled: 'The Enzymatic Synthesis of DNA. I. Preparation of Substrates and Partial Purification of an Enzyme from Escheriehia coli. II. General Properties of the Reaction.' The papers were not accepted because of the term 'DNA' in the title. The consensus among the many referees after a protracted review was that the papers would be acceptable if we used the term "polydeoxyribonucleotide" to identify the synthetic product; the use of 'DNA' could be justified only with a demonstration of genetic activity. To us this seemed unreasonable, because few if any DNA papers in the Journal had been required to fulfill this criterion. Fortunately, with accession of John Edsall to the editorship, the papers were accepted with DNA in the title [3,4].
```

I will run your function like this:

```
findVowelStartWords("Kornberg.txt", "Kornberg_Output.txt")
```

Afterwards, `Kornberg_Output.txt` should have the following content:

```
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
```

If there is anything unclear, please ask questions before writing any code.
