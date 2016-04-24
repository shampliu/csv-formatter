import csv
import re
import copy

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

undergrad_re = re.compile('STUDENT')
professor_re = re.compile('COLLEGE|PROF|LECTURER|TEACHER|EDUCATOR|INSTRUCTOR')
tech_re = re.compile('ENGINEER|SOFTWARE|DEVELOPER|DATA|SCIENTIST|ANALYST|COMPUTER|COMPUTING|IT|PROGRAM|TECH|ACADEMIC')
admin_re = re.compile('ADMIN')
faculty_re = re.compile('STAFF|FACULTY|OFFICE|LIBRARIAN|ASSISTANT|AFFAIR|LIBRARY')
arts_re = re.compile('ART|MUSIC[I]*AN|DESIGN')
health_re = re.compile('HEALTH|SURGEON|SURGICAL|PHYSICIAN|MD|SOCIOLOGIST|PSYCHIATRIST|DOCTOR|NURSE|DENTAL|DENTIST|R.N.|RN|CLERICAL|PSYCHO|CLINIC')
grad_re = re.compile('GRAD')
research_re = re.compile("BOOK|RESEARCH|LAB|BIO(LOGIST)?|HISTORIAN|ECONOMIST|ARCHIVIST")
retired_re = re.compile("RETIRE(D)?")
legal_re = re.compile("ATTORNEY|LAWYER")
other_re = re.compile("[a-z][0-9]")


occupation_match_dict = {
	"UNDERGRAD": undergrad_re,
	"PROFESSOR": professor_re,
	"TECH": tech_re,
	"ADMINISTRATIVE": admin_re,
	"FACULTY": faculty_re,
	"ARTS": arts_re,
	"HEALTH": health_re,
	"GRAD": grad_re,
	"RESEARCH": research_re,
	"RETIRED": retired_re,
	"LEGAL": legal_re,
	"OTHER": other_re
}

occupation_dict = {}

for key in occupation_match_dict:
	occupation_dict[key] = []

final_name_set = unique_name_set.copy()
# print(type(final_name_set))

counta = 0
for item in unique_name_set:
	match = False
	for m in occupation_match_dict:
		if (re.search(occupation_match_dict[m], item) != None):
			match = True
			counta += 1
			occupation_dict[m].append(item)
			final_name_set.discard(item)
	if not match:
		occupation_dict["OTHER"].append(item)
		final_name_set.discard(item)

for key in occupation_match_dict:
	print(key)
	items = occupation_dict[key]
	for item in items:
		print(item)
	print("\n\n")

print("counta: ")
print(counta)

print("\n\n\n")

for name in final_name_set:
	print(name)
print(len(final_name_set))
# print("OTHERS\n")
# for name in final_name_set:
# 	print(name)
# print(len(final_name_set))


		# elif re.search('STUDENT', item):
		# 	undergrad_student_variation.add(item)
		# elif re.search('PROFESSOR', item):
		# 	professor_variation.add(item)
		# elif re.search('RESEARCHER', item):
		# 	researcher_variation.add(item)
		# else:
		# 	other_variation.add(item)

# undergrad_student_variation = set()
# grad_student_variation = set()
# professor_variation = set()
# researcher_variation = set()
# other_variation = set()





# def add_to_occupation_dict(match_pattern, specific_title):
# 	occupation[match_pattern] = specific_title

# f


# print("Student variations:")
# for variation in undergrad_student_variation:
# 	print(variation)
# print("\n\n")
# print("grad variations:")
# for variation in grad_student_variation:
# 	print(variation)
# print("\n\n")
# print("Professor variations:")
# for variation in professor_variation:
# 	print(variation)
# print("\n\n")
# print("Researcher variations:")
# for variation in researcher_variation:
# 	print(variation)
# print("\n\n")
# print("other variations:")
# for variation in other_variation:
# 	print(variation)
		


	

# print(len(unique_name_set))





