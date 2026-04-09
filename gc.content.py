# GC content Calculator
# Author = Kashish
# Description = Calculate GC Content of DNA

dna = "ATGCGTACGTTAGC"

g = dna.count("G")
c = dna.count("C")

gc_content = (g + c) / len(dna) * 100 

print = ("DNA:", dna)
print = ("GC Content:", gc_content)
