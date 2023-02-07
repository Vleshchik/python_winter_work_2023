dna = input() #GGCTAACCTTACTGGCTGACGTGACTGCATG
rna = []
d = {'G':'C', 'C':'G', 'T':'A', 'A':'T'}
for i in dna:
    for j in i:
        if j in d:
            rna.append(d[j])
print(''.join(rna))