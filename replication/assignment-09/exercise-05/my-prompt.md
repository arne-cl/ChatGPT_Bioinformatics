Write a Python function called `isCpgIsland` that accepts a single argument: a string. This string will contain a DNA sequence. Your function should calculate the percentage of nucleotides in the DNA sequence that are CG pairs. For example, if the DNA sequence were ACGACGAATT, the percentage would be 40. Return a Boolean value that indicates whether the DNA sequence is a CpG island (i.e. the value must be greater than 10%).

Background information: the human genome consists of 3 billion A, C, G, and T nucleotides. Some parts of the genome are known as "promoter" regions. These regions typically lie upstream of genes and regulate gene expression. Promoter regions typically contain "CpG islands," which have a relatively high number of CG pairs (a C nucleotide followed by a G nucleotide). If 10% or more of the DNA in a region consists of these CG pairs, that region may be classified as a "CpG" island.


Example 1
Input: print(isCpgIsland("ATACATCGGCCGCACGTAATCGCGAATA"))
Expected output: True

Example 2
Input: print(isCpgIsland("GCGGGCATATAGACTAGCTAGCATTAACGGCAT"))
Expected output: True

Example 3
Input: print(isCpgIsland("CTAGATGACCATACTATCCAGCAGCTGCAGGAGCTATA"))
Expected output: False
