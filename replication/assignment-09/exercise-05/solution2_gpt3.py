def isCpgIsland(sequence):
    cpg_count = sequence.count('CG')
    total_count = len(sequence)
    percentage = (cpg_count / total_count) * 100
    print(f"{sequence=}: {percentage=}")
    return percentage > 10


assert isCpgIsland("ATACATCGGCCGCACGTAATCGCGAATA") is True
assert isCpgIsland("GCGGGCATATAGACTAGCTAGCATTAACGGCAT") is True
assert isCpgIsland("CTAGATGACCATACTATCCAGCAGCTGCAGGAGCTATA") is False
