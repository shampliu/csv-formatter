import csv
import json

r1 = csv.reader(open('donations.csv', 'rb'))
r1.next()	# skip first line

csvfile = open('result.csv', 'wb')
writer = csv.writer(csvfile)

for row in r1:
	writer.writerow(row)

csvfile.close()
csvfile = open('result.csv', 'rb')
jsonfile = open('result.json', 'wb')

d = {
	'dem' : {
		'Sanders' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Clinton' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Lessig' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		"O'Malley" : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Webb' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		}
	},
	'rep' : { 
		'Carson' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Cruz' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Kasich' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Bush' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Perry' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Fiorina' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Rubio' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Paul' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Trump' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		},
		'Graham' : {
			"total" : 0,
			"colleges" : { },
			"locations" : { }
		}

	}
	
}


fieldnames = ["cmte_id","cand_id","cand_nm","contbr_nm","contbr_city","contbr_st","contbr_zip","contbr_employer","contbr_occupation","contb_receipt_amt","contb_receipt_dt","receipt_desc","memo_cd","memo_text","form_tp","file_num","tran_id","election_tp"]

name_hash = {
	"Sanders, Bernard" 					: ('dem', 'Sanders'),
	"Clinton, Hillary Rodham" 			: ('dem', 'Clinton'),
	"Cruz, Rafael Edward 'Ted'" 		: ('rep', 'Cruz'),
	"Kasich, John R." 					: ('rep', 'Kasich'),
	"Carson, Benjamin S." 				: ('rep', 'Carson'),
	"Webb, James Henry Jr." 			: ('dem', 'Webb'),
	"O'Malley, Martin Joseph" 			: ('dem', "O'Malley"),
	"Lessig, Lawrence" 					: ('dem', "Lessig"),
	"Bush, Jeb" 						: ('rep', "Bush"),
	"Rubio, Marco" 						: ('rep', "Rubio"),
	"Fiorina, Carly" 					: ('rep', "Fiorina"),
	"Paul, Rand" 						: ('rep', "Paul"),
	"Graham, Lindsey O." 				: ('rep', "Graham"),
	"Trump, Donald J." 					: ('rep', "Trump"),
	"Perry, James R. (Rick)" 			: ('rep', "Perry")


}

def format_name(n):
	return name_hash.get(n)		# returns None on other name

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

job_hash = {
	"STUDENT" 			: "student",
	"PROFESSOR"			: "professor",
	"FACULTY"			: "faculty"
}

def format_job(j):
	return job_hash.get(j)


dict_reader = csv.DictReader(csvfile, fieldnames, delimiter = ',', quotechar = '"')

for row in dict_reader:
	t = format_name( row["cand_nm"] )
	if t is None:
		continue 
	cand = d[t[0]][t[1]]

	amt = float(row["contb_receipt_amt"])

	cand["total"] += amt
	print cand["total"]

	college = format_college( row["contbr_employer"] )
	if college is not None:
		c = cand["colleges"]

		if c.has_key(college):
			c[college]["donators"] += 1
			c[college]["total"] += amt
		else:
			c[college] = {
				"donators" : 1,
				"total" : amt,
				"jobs" : {

				 }

			}

		j = format_job( row["contbr_occupation"] )
		if j is not None:

			# handle jobs
			if c[college]["jobs"].has_key(j):
				c[college]["jobs"][j]["total"] += amt
				c[college]["jobs"][j]["donators"] += 1
			else:
				c[college]["jobs"][j] = {
					"total" : amt,
					"donators" : 1
				}


	# handle location
	loc = cand["locations"]
	city = row["contbr_city"] 
	if loc.has_key(city):
		loc[city]["total"] += amt
		loc[city]["donators"] += 1
	else:
		loc[city] = {
			"total" : amt,
			"donators" : 1 
		}

json.dump(d, jsonfile, indent=4, separators=(',', ': '))
print(json.dumps(d))




        