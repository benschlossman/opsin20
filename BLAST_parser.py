import os
from Bio import SeqIO
path = os.path.dirname(os.path.abspath(__file__))
species = os.path.basename(path)
outname = species + "_blast_sequences.fas"
output = open(outname, "w")
for file in os.listdir(path):
    if file.endswith(".out"):
		f = open(file,"r")
		seq_data = file[:-4]  # remove '.out' so seq is now fasta file name
		lines = f.readlines()
		clean = {}
		print(file)
		for x in lines:  # reading through each line of .out file
			result1 = (x.split('\t')[1])   # append result1 with sequence name
			result2 = (x.split('\t')[10])   # append result2 with sequence e-score
			if "." in result2:
				print(result1 + " not added; contains decimal.")
			else:
				result2 = result2.split('-')[1]  # split at '-', then take string after '-'.
				if result2[0] == "0":
					result2 = result2[1:]
				if result1 not in clean and int(result2) >= 7:  # if statement to not add duplicate sequence names and e value above Ne-07 in first place
					clean[result1] = result2  # if no dupe, then add to dictionary with result1 as key, result2 as value
					# print(result1 + " added to sequence dictionary.")

		fasta_dict = SeqIO.index(seq_data, "fasta")  # reads/indexes in the corresponding fasta file
		for key in clean:
			output.write(fasta_dict.get_raw(key).decode())  # write raw sequence data of keys (corresponding to sequence IDs in fasta) to output file
			print(key + " written to output file.")

		f.close()
