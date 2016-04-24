import csv
import json
import re
import copy

r1 = csv.reader(open('donations.csv', 'rb'))
r1.next()	# skip first line

csvfile = open('result.csv', 'wb')
writer = csv.writer(csvfile)

for row in r1:
	writer.writerow(row)

csvfile.close()
csvfile = open('result.csv', 'rb')
jsonfile = open('result.json', 'wb')

d = [
	{
		"name" : "Sanders",
		"party" : "dem",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Clinton",
		"party" : "dem",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Lessig",
		"party" : "dem",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "O'Malley",
		"party" : "dem",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Webb",
		"party" : "dem",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Carson",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Cruz",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Kasich",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Bush",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Perry",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Fiorina",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Rubio",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Paul",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Trump",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	},
	{
		"name" : "Graham",
		"party" : "rep",
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : []
	}
]


fieldnames = ["cmte_id","cand_id","cand_nm","contbr_nm","contbr_city","contbr_st","contbr_zip","contbr_employer","contbr_occupation","contb_receipt_amt","contb_receipt_dt","receipt_desc","memo_cd","memo_text","form_tp","file_num","tran_id","election_tp"]

name_hash = {
	"Sanders, Bernard" 							: ('Sanders', 0),
	"Clinton, Hillary Rodham" 			: ('Clinton', 1),
	"Cruz, Rafael Edward 'Ted'" 		: ('Cruz', 6),
	"Kasich, John R." 							: ('Kasich', 7),
	"Carson, Benjamin S." 					: ('Carson', 5),
	"Webb, James Henry Jr." 				: ('Webb', 4),
	"O'Malley, Martin Joseph" 			: ("O'Malley", 3),
	"Lessig, Lawrence" 							: ("Lessig", 2),
	"Bush, Jeb" 										: ("Bush", 8),
	"Rubio, Marco" 									: ("Rubio", 11),
	"Fiorina, Carly" 								: ("Fiorina", 10),
	"Paul, Rand" 										: ("Paul", 12),
	"Graham, Lindsey O." 						: ("Graham", 14),
	"Trump, Donald J." 							: ("Trump", 13),
	"Perry, James R. (Rick)" 				: ("Perry", 9)
}

def format_name(n):
	return name_hash.get(n)		# returns None on other name

college_hash = {
	"UCLA" 																			: "ucla", 
	"UNIVERSITY OF CALIFORNIA, LOS ANGELES" 		: "ucla",
	"UCB" 																			: "ucb",
	"UNIVERSITY OF CALIFORNIA, BERKELEY" 				: "ucb",
	"UCSB" 																			: "ucsb",
	"UNIVERSITY OF CALIFORNIA, SANTA BARBARA" 	: "ucsb",
	"UCSC" 																			: "ucsc",
	"UNIVERSITY OF CALIFORNIA, SANTA CRUZ" 			: "ucsc",
	"UCR" 																			: "ucr",
	"UNIVERSITY OF CALIFORNIA, RIVERSIDE" 			: "ucr",
	"UCSD" 																			: "ucsd",
	"UNIVERSITY OF CALIFORNIA, SAN DIEGO" 			: "ucsd",
	"UCM" 																			: "ucm",
	"UNIVERSITY OF CALIFORNIA, MERCED" 					: "ucm",
	"UCSF" 																			: "ucsf",
	"UNIVERSITY OF CALIFORNIA, SAN FRANCISCO" 	: "ucsf",
	"UCD" 																			: "ucd",
	"UNIVERSITY OF CALIFORNIA, DAVIS" 					: "ucd"
}

def format_college(c):
	return college_hash.get(c)

job_hash = {
	"STUDENT" 			: "undergraduate",
	"PROFESSOR"			: "professor",
	"FACULTY"			: "faculty",
	"GRADUATE STUDENT"	: "graduate"
}

unique_name_set = set()	

with open('donations.csv', 'rb') as csvfile1:
	reader = csv.DictReader(csvfile1)
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

# format("GRADUTE STUDENT RESEARCHER") --> GRAD
def format_job(input):
	for i in occupation_dict:
		item_list = occupation_dict[i]
		for j in item_list:
			if j == input:
				return i









# def format_job(j):
# 	# student = re.compile('[\w]*STUDENT[\w]*')
# 	# if student.match(j):
# 	# 	return "undergraduate"

# 	return unique_names.format(j)


dict_reader = csv.DictReader(csvfile, fieldnames, delimiter = ',', quotechar = '"')

for row in dict_reader:
	t = format_name( row["cand_nm"] )
	if t is None:
		print row["cand_nm"]
		continue
	ind =  t[1]
	cand = d[ind]


	amt = float(row["contb_receipt_amt"])

	cand["total"] += amt
	# print cand["total"]

	college = format_college( row["contbr_employer"] )
	if college is not None:
		college_arr = cand["colleges"]
		cand["colleges_total"] += amt 

		curr_c = None 
		for c in college_arr:
			if c["name"] == college:
				c["donators"] += 1
				c["total"] += amt
				curr_c = c 
				break

		if curr_c is None:
			new_c = {
				"name" : college,
				"donators" : 1,
				"total" : amt,
				"jobs" : []
			}
			college_arr.append(new_c)
			curr_c = new_c 

		job = format_job( row["contbr_occupation"] )
		if job is not None:

			# handle jobs
			found_job = False 

			for j in curr_c["jobs"]:
				if j["title"] == job:
					j["total"] += amt
					j["donators"] += 1
					found_job = True
					break

			if not found_job:
				j = {
					"title" : job,
					"total" : amt,
					"donators" : 1
				}
				curr_c["jobs"].append(j)


	# handle location
	# loc = cand["locations"]
	# city = row["contbr_city"] 
	# if loc.has_key(city):
	# 	loc[city]["total"] += amt
	# 	loc[city]["donators"] += 1
	# else:
	# 	loc[city] = {
	# 		"total" : amt,
	# 		"donators" : 1 
	# 	}

json.dump(d, jsonfile, indent=4, separators=(',', ': '))
# print(json.dumps(d))




        