def isCpgIsland(sequence):
    cpg_count = sequence.count('CG')
    total_count = len(sequence) - 1  # Subtract 1 to avoid counting the last character
    percentage = (cpg_count / total_count) * 100
    return percentage > 10


assert isCpgIsland("ATACATCGGCCGCACGTAATCGCGAATA") is True

assert isCpgIsland("GCGGGCATATAGACTAGCTAGCATTAACGGCAT") is True

assert isCpgIsland("CTAGATGACCATACTATCCAGCAGCTGCAGGAGCTATA") is False

