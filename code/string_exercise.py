# Author: Shuting Chen
# Assignment 05

dna = input("Enter a DNA sequence\n")
rna = dna.replace("T", "U")

print(f'Your DNA length is {len(dna)}\nThere are {dna.count("A")} A(s) in your sequence.\nYour RNA seq: {rna}')
