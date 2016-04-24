import csv
import json
import re

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

def format_job(j):
	# student = re.compile('[\w]*STUDENT[\w]*')
	# if student.match(j):
	# 	return "undergraduate"

	return job_hash.get(j)


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




        