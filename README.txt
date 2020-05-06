BLAST_parser.py
*************************************
Python script that reads through a local BLAST output file, finding all sequence ID's that
scored more than or equal to an e-value of 1e-07, then exports the corresponding sequence
from your database file into a new output file.

Scripted with advice from Jake Ireland


OpsinFinder_7sites.py
*************************************
Finds all sequences in a sequence database that possess 7 sites of retinal binding domain 
pattern available on PROSITE for visual photopigments (PROSITE accession: PS00238) and
writes those sequences to a new file. File must be FASTA, with entire protein sequence
on one line.


*.phy
*************************************
The 6 alignment files for each of our databases, having been trimmed with
trimAl v1.2 (-gt 0.45)


*.tree
*************************************
The 8 uncollapsed phylogenies we reconstructed:
	_GTRG: GTR+G Model
	_LGFR8: LG+F+R8 Model
	_Pb: PhyloBayes MPI v1.8
	_IQTREE: IQ-TREE v1.6.12
	
	
REAout_IQTREE_annotate.pdf
*************************************
Additional annotation of fully expanded REAout IQ-TREE LG+F+R8
This is the original database of Ramirez et al. 2016 with improved outgroups,
with the identical model and tree reconstruction software.