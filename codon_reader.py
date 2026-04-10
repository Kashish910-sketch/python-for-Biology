# Codon Reader
# Author: Kashish 
# Description : this codes reads the DNA sequence and prints codons

def read_codons(dna):
  for i in range(0, len(dna), 3):
    codon = dna[i:i+3]

    if len(codon) == 3:
      print(codon)

dna = "ATGCGTACGTTAGC"

print("DNA Sequence:", dna)
print("Codons:")

read_codons(dna) 
    
        
