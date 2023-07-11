Here is a new Python programming task.

The human genome consists of 3 billion A, C, G, and T nucleotides. Some parts of the genome are known as "promoter" regions. These regions typically lie upstream of genes and regulate gene expression. Promoter regions typically contain "CpG islands," which have a relatively high number of CG pairs (a C nucleotide followed by a G nucleotide). If 10% or more of the DNA in a region consists of these CG pairs, that region may be classified as a "CpG" island.

Please write a function called "isCpgIsland" that accepts a single argument: a string. This string will contain a DNA sequence. Your function should calculate the percentage of nucleotides in the DNA sequence that are CG pairs. For example, if the DNA sequence were ACGACGAATT, the percentage would be 40. Return a Boolean value that indicates whether the DNA sequence is a CpG island (*greater than* 10%).

Below is a description of a test to verify your code.

For this test, the following code will be executed after your code:

print(isCpgIsland("ATACATCGGCCGCACGTAATCGCGAATA"))

Below is the expected output:

True

Below is a description of a test to verify your code.

For this test, the following code will be executed after your code:

print(isCpgIsland("GCGGGCATATAGACTAGCTAGCATTAACGGCAT"))

Below is the expected output:

True

Below is a description of a test to verify your code.

For this test, the following code will be executed after your code:

print(isCpgIsland("CTAGATGACCATACTATCCAGCAGCTGCAGGAGCTATA"))

Below is the expected output:

False
