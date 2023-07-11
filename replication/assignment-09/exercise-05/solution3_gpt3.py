def isCpgIsland(sequence):
    cg_count = 0
    total_count = 0

    for i in range(len(sequence) - 1):
        if sequence[i:i+2] == 'CG':
            cg_count += 1
        total_count += 1

    cg_percentage = (cg_count / total_count) * 100

    print(f"{cg_percentage=}, {cg_count=}, {total_count=}")
    return cg_percentage >= 10


assert isCpgIsland("ATACATCGGCCGCACGTAATCGCGAATA") is True
assert isCpgIsland("GCGGGCATATAGACTAGCTAGCATTAACGGCAT") is True
assert isCpgIsland("CTAGATGACCATACTATCCAGCAGCTGCAGGAGCTATA") is False
