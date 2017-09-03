import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

import sys

print(sys.argv)

gff_fh = open(sys.argv[1])

gene_lengths = []
for line in gff_fh:
    # print(line)
    if line.startswith("#"):
        continue
    split_line = line.split()
    if split_line[2] == "gene":
        # print(split_line)
        cur_gene_length = int(split_line[4]) - int(split_line[3])
        # print(cur_gene_length)
        gene_lengths.append(cur_gene_length)

# print(gene_lengths)

plt.hist(gene_lengths, bins=100)
plt.savefig(sys.argv[2])
