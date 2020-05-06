import os
import re
path = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(path):
    if file.endswith(".fasta"):
        outname = file[:-6] + "_Opsins_7sites.fas"
        output = open(outname, "w")
        print(file)
        sequence_data = {}
        f = open(file, "r")
        for key in f:
            if key.startswith(">"):
                seq_id = key.rstrip()
                sequence_data[seq_id] = next(f).rstrip()
                if re.search("[^G][A-Z][SAC]K[STALIMR][GSACPNV][STACP]", sequence_data[seq_id]):
                    output.write(seq_id + "\n")
                    output.write(sequence_data[seq_id] + "\n")
                    print(key + " is an Opsin, written to outfile.")

        output.close()
