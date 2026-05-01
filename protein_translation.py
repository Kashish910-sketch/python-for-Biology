# Protein Translation
# Author: Kashish
# Description: Converts DNA sequence to protein sequence


def translate_dna(dna):

    codon_table = {
        "ATG": "M", "TTT": "F", "TTC": "F",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TAA": "*", "TAG": "*", "TGA": "*"
    }

    protein = ""

    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]

        if len(codon) == 3:
            amino_acid = codon_table.get(codon, "?")
            protein += amino_acid

    return protein


dna = "ATGTTTGTTTAA"

result = translate_dna(dna)

print("Protein:", result)
