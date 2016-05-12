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
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Clinton",
		"party" : "dem",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Lessig",
		"party" : "dem",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "O'Malley",
		"party" : "dem",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Webb",
		"party" : "dem",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Carson",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Cruz",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Kasich",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Bush",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Perry",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Fiorina",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Rubio",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Paul",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Trump",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Graham",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Huckabee",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Christie",
		"party" : "rep",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Other",
		"party" : "mixed",
		"donators" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
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
	"Perry, James R. (Rick)" 				: ("Perry", 9),
	"Huckabee, Mike"								: ("Huckabee", 15),
	"Christie, Christopher J."			: ("Christie", 16)
}

def format_name(n):
	return name_hash.get(n)		# returns None on other name


college_hash = {
	"UCLA" 																			: "ucla", 
	"UNIVERSITY OF CALIFORNIA, LOS ANGELES" 		: "ucla",
	"UNIVERSITY OF CALIFORNIA LOS ANGELES" 			: "ucla",
	"UNIVERSITY OF CALIFORNIA LOS ANGELES H"		: "ucla",
	"UNIVERSITY OF CALIFORNIA- LOS ANGELES"			: "ucla",

	"UCB" 																			: "ucb",
	"UNIVERSITY OF CALIFORNIA, BERKELEY" 				: "ucb",
	"UNIVERSITY OF CALIFORNIA BERKELEY" 				: "ucb",
	"UNIV. OF CALIFORNIA, BERKELEY"							: "ucb",
	"UNIV.OF CALIFORNIA,BERKELEY"								: "ucb",
	"UNIVERSITY OF CALIFORNIA, BERKLEY SCHO"		: "ucb",
	"UNIVERSITY OF CALIFORNIA AT BERKELELY"			: "ucb",
	"UNIVERSITY OF CALIFORNIA; BERKELEY; SC"		: "ucb",
	"UNIVERSITY OF CALIFORNIA - BER"						: "ucb",
	"UNIVERSITY OF CALIFORNIA BERKELEY ALL" 		: "ucb",

	"UCSB" 																			: "ucsb",
	"UNIVERSITY OF CALIFORNIA, SANTA BARBARA" 	: "ucsb",
	"UNIVERSITY OF CALIFORNIA SANTA BARBARA" 		: "ucsb",
	"UNIVERSITY OF CALFORNIA SANTA BARBARA"			: "ucsb",
	"UNIVERSISTY OF CALIFORNIA, SANTA BARBA"		: "ucsb",
	"UNIVESITY OF CALIFORNIA, SANTA BARBARA"		: "ucsb",
	"THE UNIVERSITY OF CALIFORNIA AT SANTA"			: "ucsb",
	"UNIVERSITY OF CALIFORNIA, SANTA BARBAR"		: "ucsb",
	"UNIVERSITY OF CALIFORNIA - SANTA BARBA"		: "ucsb",
	"UNIVERSITY OF CALIFORNIA- SANTA BARBAR"		: "ucsb",

	"UCSC" 																			: "ucsc",
	"UNIVERSITY OF CA, SANTA CRUZ" 							: "ucsc",
	"UNIV. CAL. SANTA CRUZ"											: "ucsc", 
	"UNIVERSITY OF CALIFORNIA, SANTA CRUZ" 			: "ucsc",
	"UNIVERSITY OF CALIFORNIA SANTA CRUZ" 			: "ucsc",
	"UNIV. OF CALIFORNIA, SANTA CRUZ"						: "ucsc", 
	"UNIVERSITY CALIFORNIA SANTA CRUZ"					: "ucsc",
	"UNIV CALIFORNIA SANTA CRUZ"								: "ucsc",
	"THE UNIVERSITY OF CA AT SANTA CRUZ"				: "ucsc",

	"UCR" 																			: "ucr",
	"UNIVERSITY OF CALIFORNIA, RIVERSIDE" 			: "ucr",
	"UNIVERSITY OF CALIFORNIA RIVERSIDE" 				: "ucr",
	"UNIVERSITY OF CALIFORNIA AT RIVERSIDE"			: "ucr",

	"UCSD" 																			: "ucsd",
	"UNIVERSITY OF CALIFORNIA, SAN DIEGO" 			: "ucsd",
	"UNIVERSITY OF CALIFORNIA SAN DIEGO" 				: "ucsd",
	"UNIVERSITY OF CALIFORNIA SAN DIEGO HEA" 		: "ucsd",
	"UNIVERSITY OF CALIFRONIA- SAN DIEGO"				: "ucsd",
	"UNIV OF CALIF SAN DIEGO"										: "ucsd",
	"UNIV. OF SAN DIEGO/US COMM'N ON CIVIL"			: "ucsd",
	"UNIV CALIF SAN DIEGO"											: "ucsd",
	"UNIVERSITY OF CALIFORNIA -SAN DIEGO"				: "ucsd",
	"UNIV. CALIFORNIA AT SAN DIEGO"							: "ucsd",

	"UCM" 																			: "ucm",
	"UNIVERSITY OF CALIFORNIA, MERCED" 					: "ucm",
	"UNIVERSITY OF CALIFORNIA MERCED" 					: "ucm",

	"UCSF" 																			: "ucsf",
	"UNIVERSITY OF CALIFORNIA, SAN FRANCISCO" 	: "ucsf",
	"UNIVERSITY OF CALIFORNIA SAN FRANCISCO" 		: "ucsf",
	"UNIVERSITY OF CALIFORNIA, SAN FRANCISC"		: "ucsf",
	"UNIVERSITY OF CALIFORNIA SAN FRANCISC"			: "ucsf",
	"UNIVERSITY OF CALIFORNIA SF"								: "ucsf",
	"UNIVERSITY OF CALIFONIA, SAN FRANCISCO"		: "ucsf",
	"UNIVERSITY OF CALIFORNIA-SAN FRANCISCO"		: "ucsf",

	"UCD" 																			: "ucd",
	"UNIVERSITY OF CALIFORNIA, DAVIS" 					: "ucd",
	"UNIV. OF CALIF. DAVIS"											: "ucd",
	"UNIVERSITY OF CALIFORNIA DAVIS" 						: "ucd",
	"UNIVERSITY CA DAVIS POLICE"								: "ucd",
	"UNIV. OF CALIFORNIA-DAVIS"									: "ucd",
	"UNIV. OF CALIF. SCH. OF MEDICINE"					: "ucd",
	"UNIVERSITY OF CALIFORNIA-DAVIS"						: "ucd",
	"UNIVERSITY OF CALIFORNIA AT DAVIS"					: "ucd",
	"UNIVERSITY OF CALIFORNIA DAVIS MEDICAL"		: "ucd",

	"UNIVERSITY OF CALIFORNIA, IRVINE" 					: "uci",
	"UNIVERSITY OF CALIFORNIA IRVINE" 					: "uci",
	"UNIVERSITY OF CALIFORNIA-IRVINE"						: "uci",
	"UCI" 																			: "uci",
	"UNIVERSITY OF CALIFORNIA AT IRVINE"				: "uci",
	"UNIVERSITY OF CALIF., IRVINE"							: "uci",
	"UNIVERSITY OF CALIFORNIA, IRVINE, NURS"		: "uci"
}

city_hash = {
	"DAVIS" : "ucd",
	"LOS ANGELES" : "ucla",
	"SANTA CRUZ" : "ucsc", 
	"BERKELEY" : "ucb",
	"RIVERSIDE" : "ucr", 
	"MERCED" : "ucm",
	"SAN DIEGO" : "ucsd",
	"IRVINE" : "uci",
	"SAN FRANCISCO" : "ucsf",
	"SANTA BARBARA" : "ucsb",
	"LA JOLLA" : "ucsd",
	"SANTA MONICA" : "ucla",
	"SACRAMENTO" : "ucd",
	"NORTH HOLLYWOOD": "ucla",
	"CARLSBAD" : "ucsd",
	"OAKLAND" : "ucb",
	"ALAMEDA" : "ucb",
	"SAN LEANDRO" : "ucb",
	"ALBANY" : "ucb", 
	"SEBASTOPOL" : "ucb",
	"CASTRO VALLEY" : "ucsf",
	"DANA POINT" : "ucsd",
	"ORANGEVALE" : "ucd",
	"WALNUT CREEK" : "ucb",
	"FAIRFIELD" : "ucd",
	"LAKE FOREST" : "uci",
	"TARZANA" : "ucla",
	"VENICE" : "ucla",
	"BISHOP" : "ucla",
	"ALISO VIEJO" : "uci",
	"DEL MAR" : "ucsd",
	"FRESNO" : "ucsf",
	"GOLETA" : "ucsb",
	"GILROY" : "ucsc",
	"BUENA PARK" : "ucla",
	"CAMPBELL" : "ucsc",
	"RENO" : "ucsf",
	"CORONA" : "ucr",
	"COSTA MESA" : "uci",
	"TUSTIN" : "uci",
	"CYPRESS" : "uci",
	"TEMECULA" : "ucsd",
	"CORONA DEL MAR" : "uci",
	"LAGUNA BEACH" : "uci",
	"SANTA ANA" : "uci",
	"ORANGE" :"uci",
	"WEST HOLLYWOOD" : "ucla",
	"CULVER CITY" : "ucla",
	"SHERMAN OAKS" : "ucla",
	"PACIFIC PALISADES" : "ucla",
	"FAIRFAX" : "ucb",
	"SAUSALITO" : "ucb",
	"TIBURON" : "ucb",
	"NEWPORT BEACH" : "uci",
	"ANTIOCH" : "ucb",
	"SOQUEL" : "ucsc",
	"CARPINTERIA" : "ucsb",
	"GUALALA" : "ucd",
	"VALLEY VILLAGE" : "ucla",
	"SAN RAFAEL" : "ucb",
	"MILL VALLEY" : "ucb"


}

def format_college(e, c):
	r = college_hash.get(e)
	if r is not None:
		return r
	elif e == "UNIV OF CA" or e == "THE REGENTS OF THE UNIVERSITY OF CALIF" or e == "APPLE, INC.; UNIV OF CALIFORNIA" or e == "UNIVERSITY OF CALIFORNIA OFFICE OF THE" or e == "UNIVERSITY OF CALIFORNIA REGENTS" or e == "UNIV OF CALIF" or e == "UNIVERISTY OF CALIFORNIA" or e == "UNIVERSITY OF CALIFORNIA" or e == "UNIVERSITY OF CA" or e == "UNIV OF CALIFORNIA" or e == "UNIV. OF CALIFORNIA" or e == "UNIV. OF CA" or e == "UNIVERSITY  OF CALIFORNIA":
		r2 = city_hash.get(c) 
		if r2 is None:
			unknown_cities_set.add(c)
			return "na"
		else:
			return r2
	else:
		return None

job_hash = {
	"STUDENT" 					: "undergraduate",
	"PROFESSOR"					: "professor",
	"FACULTY"						: "faculty",
	"GRADUATE STUDENT"	: "graduate"
}

unique_name_set = set()	

possible_colleges_set = set()
unknown_cities_set = set()

with open('donations.csv', 'rb') as csvfile1:
	reader = csv.DictReader(csvfile1)
	for row in reader:
		if (format_college(row["contbr_employer"], row["contbr_city"]) is not None):
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

dict_reader = csv.DictReader(csvfile, fieldnames, delimiter = ',', quotechar = '"')

for row in dict_reader:
	t = format_name( row["cand_nm"] )
	if t is None:
		# print row["cand_nm"]
		# continue
		t = ("Other", 17)
	ind =  t[1]
	cand = d[ind]


	amt = float(row["contb_receipt_amt"])

	cand["total"] += amt
	cand["donators"] += 1
	# print cand["total"]

	college = format_college( row["contbr_employer"], row["contbr_city"] )
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
				"total" : amt

			}
			college_arr.append(new_c)
			curr_c = new_c 

		job = format_job( row["contbr_occupation"] )
		if job is not None:

			# handle jobs
			found_job = False 
			coll_name = curr_c["name"]

			for j in cand["jobs"]:
				if j["title"] == job:
					j["total"] += amt
					j["donators"] += 1
					found_job = True

					if j["colleges"].has_key(coll_name):
						j["colleges"][coll_name]["donators"] += 1
						j["colleges"][coll_name]["total"] += amt

					else:
						j["colleges"][coll_name] = {
							"total" : amt,
							"donators" : 1
						}


					break

			if not found_job:
				j = {
					"title" : job,
					"total" : amt,
					"donators" : 1,
					"colleges" : {}
				}

				j["colleges"][coll_name] = {
					"donators" : 1,
					"total" : amt
				}

				cand["jobs"].append(j)

	else:

		searchObj1 = re.search( r'UNIVERSITY', row["contbr_employer"], re.M|re.I)
		searchObj2 = re.search( r'UNIV', row["contbr_employer"], re.M|re.I)
		searchObj3 = re.search( r'CA', row["contbr_employer"], re.M|re.I)
		searchObj4 = re.search( r'CALIF', row["contbr_employer"], re.M|re.I)
		searchObj5 = re.search( r'CALIFORNIA', row["contbr_employer"], re.M|re.I)
		if (searchObj1 or searchObj2) and (searchObj3 or searchObj4 or searchObj5):
			possible_colleges_set.add(row["contbr_employer"])
			# print row["contbr_employer"]

print "UNKNOWN CITIES: "
for item in unknown_cities_set:
	print item 
print len(unknown_cities_set)

# for item in possible_colleges_set:
# 	print item 
# print len(possible_colleges_set)
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




        