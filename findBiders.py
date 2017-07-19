import sys
import csv

input_file = sys.argv[-1]
hLA = []
peptide = []
numInfo = []
count = 0

file = list(csv.reader(open(input_file,'r'), delimiter='\n'))
numrows = len(file)

for i in range(0, numrows-1):
	if len(file[i]) != 0:
		if file[i][0][4:5] == '0':
			if file[i][0][-1] == 'B':
				count = count + 1
				hLA.append(file[i][0][9:18])
				peptide.append(file[i][0][22:31])
				numInfo.append(file[i][0][127:])

with open("final_binders.txt","w") as txt_file:
	txt_file.write("------------------------------------------------------" + "\n")
	txt_file.write("  HLA         Peptide       Affinity(nM)    %Rank" + "\n")
	txt_file.write("------------------------------------------------------" + "\n")
	for j in range(1, count):
		txt_file.write(hLA[j] + "    " + peptide[j] + "       " + numInfo[j] + "\n")
