
def count_kmer(kmer, sequence):
    count = 0
    k = len(kmer)
    
    for i in range(len(sequence) - k + 1):
       substring = sequence[i:i+k] 
       if substring == kmer:        
        count = count + 1 
    return count

r = count_kmer('ACTAT', 'ACAACTATGCATACTATCGGGAACTATC')
print(r)
r = count_kmer('AC', 'ACAACTATGCATACTATCGGGAACTATC')
print(r)
r = count_kmer('ATA', 'CGATATATCCATAG')
print(r)