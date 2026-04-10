# Mutation Finder
# Author: Kashish
# Description: Compares two DNA sequences and finds mutations

def find_mutation(dna1, dna2):
    
    for i in range(len(dna1)):
        
        if dna1[i] != dna2[i]:
            print("Mutation at position", i+1, ":", dna1[i], "→", dna2[i])


dna1 = "ATGCGTAC"
dna2 = "ATGAGTAC"

print("DNA 1:", dna1)
print("DNA 2:", dna2)

print("\nMutations found:")

find_mutation(dna1, dna2)
