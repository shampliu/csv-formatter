import csv

unique_name_set = set()

college_hash = {
	"UCLA" 											: "ucla", 
	"UNIVERSITY OF CALIFORNIA, LOS ANGELES" 		: "ucla",
	"UCB" 											: "ucb",
	"UNIVERSITY OF CALIFORNIA, BERKELEY" 			: "ucb",
	"UCSB" 											: "ucsb",
	"UNIVERSITY OF CALIFORNIA, SANTA BARBARA" 		: "ucsb",
	"UCSC" 											: "ucsc",
	"UNIVERSITY OF CALIFORNIA, SANTA CRUZ" 			: "ucsc",
	"UCR" 											: "ucr",
	"UNIVERSITY OF CALIFORNIA, RIVERSIDE" 			: "ucr",
	"UCSD" 											: "ucsd",
	"UNIVERSITY OF CALIFORNIA, SAN DIEGO" 			: "ucsd",
	"UCM" 											: "ucm",
	"UNIVERSITY OF CALIFORNIA, MERCED" 				: "ucm",
	"UCSF" 											: "ucsf",
	"UNIVERSITY OF CALIFORNIA, SAN FRANCISCO" 		: "ucsf",
	"UCD" 											: "ucd",
	"UNIVERSITY OF CALIFORNIA, DAVIS" 				: "ucd"
}

def format_college(c):
	return college_hash.get(c)

with open('donations.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if (format_college(row["contbr_employer"]) is not None):
			unique_name_set.add(row["contbr_occupation"])


for item in unique_name_set:
	print(item)

print(len(unique_name_set))