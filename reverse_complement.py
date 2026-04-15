def reverse_complement(dna):
    
    complement =""
    
    for base in dna:
        
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
            
    reverse = complement[::-1]
    
    return reverse
    
dna = "ATGCGTAC"

result = reverse_complement(dna)

print("Reverse Complement:", result)
