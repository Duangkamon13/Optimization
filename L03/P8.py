"""
Write a function named codon.
The function takes 2 arguments:
a file name of a codon table (as string)
and a file name of a DNA sequence, reads the two files,
uses a codon table to decipher the DNA sequence to a protein,
and returns a list of the deciphered sequence of amino acids.
The codon table file is a simple text file,
written in a simple format:
each line contains one codon and its corresponding amino acid
with a "=" in between.
(Note: fun gene data can be downloaded from
NCBI GenBank, looking for download "FASTA")
"""

def read_codons(fname):
    d = {}
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if '=' in line:
                k, v = line.split('=')
                d[k] = v
    return d

def codon(codon_table, gene):
    """
    Reads a DNA sequence and translates it into a list of amino acids
    using a codon table.
    """
    cod_tab = read_codons(codon_table)

    # Read DNA sequence first, skipping the first line (header)
    dna = ""
    with open(gene, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            dna += line.strip()  # ลบช่องว่างและ \n

    # Translate each 3-letter set in DNA sequence to an amino acid
    polypep = []

    # Iterate through the DNA sequence in non-overlapping groups of 3
    for i in range(0, len(dna), 3):
        current_codon = dna[i:i+3]
        if len(current_codon) < 3:
            continue  # ข้าม codon สุดท้ายที่ไม่ครบ 3 bases
        amino_acid = cod_tab.get(current_codon)
        if amino_acid:
            polypep.append(amino_acid)
        else:
            polypep.append("unknown")  # กรณี codon ไม่เจอในตาราง

    return polypep

if __name__ == '__main__':
    res = codon('codons.txt', 'homo_sapiens_mitochondrion.txt')
    print(res)
    print(len(res))
