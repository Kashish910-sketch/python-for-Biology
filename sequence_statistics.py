# Sequence Statistics
# Author: Kashish
# Description: Calculates DNA statistics

def sequence_stats(dna):
    
   length = len(dna)
   a = dna.count("A")
   t = dna.count("T")
   g = dna.count("G")
   c = dna.count("C")   

   gc = g + c / length * 100 
   
   print("Length: ", length)
   print("A:", a)
   print("T:", t)
   print("G:", g)
   print("C:", c)
   print("GC Content:", gc)
   
dna = "ATGCGTACGTTAGC"
 
print("DNA:", dna)
print("\nStatistics:")
 
sequence_stats(dna)
