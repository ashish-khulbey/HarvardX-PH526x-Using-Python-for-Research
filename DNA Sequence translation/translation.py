def read_seq(inputfile):
  """Read and return a input sequence"""
  with open(inputfile, "r") as f:
    seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
  return seq

inputfile = "dna.txt"
# f = open(inputfile, "r")
# seq = f.read()

def translate(seq):
  """Translate a string containing a nucleotide sequence into a 
  string containing the corresponding sequence of amino acids . 
  Nucleotides are translated in triplets using the table dictionary; 
  each amino acid 4 is encoded with a string of length 1. """

  table = {
  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
  'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
  'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
  }

  protein = ""
  if len(seq) % 3 == 0:
    for i in range(0, len(seq), 3): 
      codon = seq[i : i+3]
      protein += table[codon]

  return protein

dna = read_seq("dna.txt")
prt = read_seq("protein.txt")
protein = translate(dna[20:938-3])  #NBCI CDS--tells what is actual seq for conversion
#last value of protein is underscore(_) so not needed--which means end of protein
print(prt == protein)
