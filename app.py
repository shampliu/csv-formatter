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
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Clinton",
		"party" : "dem",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Lessig",
		"party" : "dem",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "O'Malley",
		"party" : "dem",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Webb",
		"party" : "dem",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Carson",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Cruz",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Kasich",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Bush",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Perry",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Fiorina",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Rubio",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Paul",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Trump",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Graham",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Huckabee",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Christie",
		"party" : "rep",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
		"colleges" : [],
		"locations" : [],
		"jobs" : []
	},
	{
		"name" : "Other",
		"party" : "mixed",
		"contributions" : 0,
		"total" : 0,
		"colleges_total" : 0,
		"colleges_contributions" : 0,
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
grad_re = re.compile('GRAD(UATE)?|DOCTORAL|PHD')
research_re = re.compile("BOOK|RESEARCH|LAB|BIO(LOGIST)?|HISTORIAN|ECONOMIST|ARCHIVIST")
retired_re = re.compile("RETIRE(D)?")
legal_re = re.compile("ATTORNEY|LAWYER")
other_re = re.compile("[a-z][0-9]")


# occupation_match_set = ("GRAD", "UNDERGRAD",  "LEGAL", "PROFESSOR", "TECH", "ADMINISTRATIVE", "FACULTY", "ARTS",
# 	"HEALTH", "RESEARCH", "RETIRED", "OTHER")

# occupation_match_dict = {
# 	"PROFESSOR": professor_re,
# 	"TECH": tech_re,
# 	"ADMINISTRATIVE": admin_re,
# 	"FACULTY": faculty_re,
# 	"ARTS": arts_re,
# 	"HEALTH": health_re,
# 	"GRAD": grad_re,
# 	"UNDERGRAD": undergrad_re,
# 	"RESEARCH": research_re,
# 	"RETIRED": retired_re,
# 	"LEGAL": legal_re,
# 	"OTHER": other_re
# }

# occupation_dict = {
# }

occupation_dict2 = {
	"FACULTY": [
		"PROFESSOR",
		"FACULTY ADVISER",
		"FACULTY, DISTINGUISHED SCIENTIST",
		"PROFESSOR OF ASTROPHYSICS",
		"PROFESSOR PHYSICIAN",
		"PROFESSOR AND ADMINISTRATOR",
		"EDUCATOR",
		"ASSISTANT PROFESSOR, NURSING",
		"PROFFESSOR",
		"INSTRUCTOR",
		"PROFESSOR OF COMPUTER SCIENCE",
		"PROFESSOR, PHYSICIAN",
		"LAW PROFESSOR",
		"PROFESSOR EMERITA",
		"UNIVERSITY PROFESSOR",
		"COLLEGE PROFESSOR",
		"UNIV PROF",
		"PROFESSOR OF HISTORY",
		"TEACHER",
		"PROFESSOR OF ANTHROPOLOGY",
		"ASSOCIATE CLINICAL PROFESSOR",
		"PROFESSOR/ARTIST",
		"COLLEGE LECTURER",
		"PROFESSOR OF PHYSICS",
		"LAW PROFESSOR AND DEAN",
		"PROFESSOR EMERITUS",
		"PROFESSOR OF NURSING",
		"ASSOCIATE PROFESSOR",
		"LECTURER",
		"UNIVERSITY INSTRUCTOR",
		"PROFESSOR OF NEUROSURGERY",
		"PROFESSOR/PHYSICIAN",
		"ASSISTANT PROFESSOR",
		"PROFESSOR AND DEAN",
		"PROFESSOR/ PHYSICIAN",
		"PSYCHOLOIGST/PROFESSOR",
		"SCIENTIST/ PROFESSOR",
		"PROFESSOR OF ECONOMICS",
		"PROFESSOR",
		"PHYSICIAN/PROFESSOR",
		"PROFESSOR OF CHEMISTRY",
		"PROFESSOR OF LAW/CIVIL RIGHTS COMMISSI",
		"WRITER, PROFESSOR",
		"PSYCHOLOGIST/CLINICAL PROFESSOR",
		"PROFESSOR OF LAW",
		"EDUCATION",
		"FACULTY", 
		"DISTINGUISHED VISITOR/FACULTY ADVISOR",
		"PROFESSOR OF EPIDEMIOLOGY AND ENVIRNOM",
		"STAFF"
	],
	"TECH": [
		"TECH",
		"COMPUTER PROFESSIONAL",
		"WEB DEVELOPER",
		"DATA ARCHIVIST",
		"ELECTRICAL ENGINEER",
		"RESEARCH AND DEVELOPMENT ENGINEER",
		"APP DEVELOPER",
		"SOFTWARE ENGINEER",
		"COMPUTER PROGRAMMER",
		"DATABASE PROGRAMMER",
		"ENGINEER",
		"IT MANAGER",
		"COMPUTER SCIENCE RESEARCHER",
		"ITS",
		"PROGRAMMER/ANALYST",
		"COMPUTER SCIENTIST",
		"SOFTWARE DEVELOPER",
		"COMPUTING RESOURCE MANAGER",
		"INFORMATION TECHNOLOGY",
		"SOFTWARE SYSTEMS ARCHITECT",
		"IT MANAGEMENT",
		"IT DIRECTOR",
		"PROGRAMMER",
		"SYSTEMS ENGINEER",
		"TECH ASST",
		"TECHNOLOGY TRANSFER MANAGER"
	],
	"ADMINISTRATIVE": [
		"ACADEMIC OFFICER",
		"ADMINISTRATIVE",
		"ADMINISTRATIVE ASSISTANT",
		"CHIEF ADMINISTRATIVE OFFICER",
		"ADMIN ASSIST",
		"ADMINISTRATIVE SPECIALIST",
		"LIBRARY ADMINISTRATOR",
		"EDUCATION ADMINISTRATOR",
		"HIGHER EDUCATION ADMINISTRATOR",
		"ADMIN ADDIST",
		"OFFICE ADMINISTRATOR",
		"RESEARCH ADMINISTRATOR",
		"ADMINISTRATOR",
		"SYSTEM ADMINISTRATOR",
		"ADMIN",
		"EDUCATIONAL ADMINISTRATION",
		"ADMINISTRATION",
		"ADMINISTRATIVE OFFICER",
		"FINANCIAL AID OFFICER",
		"OFFICE MANAGER",
		"HR",
		"HUMAN RESOURCES",
		"FINANCIAL OFFICER",
		"EXTERNAL AFFAIRS",
		"ASSISTANT DEAN",
		"CHIEF SUSTAINABILITY OFFICER",
		"STUDENT AFFAIRS",
		"STUDENT AFFAIRS ADVISOR",
		"UNIVERSITY MANAGER",
		"ADMIN ASSIT",
		"VICE CHANCELLOR, PLANNING & BUDGET, ME",
		"ASSOCIATE VICE CHANCELLER DEVELOPMENT",
		"PROJECT MANAGER",
		"CONTRACTS MANAGER",
		"POSTSECONDARY PROJECT DIRECTOR",
		"PRESIDENT",
		"DIVISION MANAGER",
		"PROJECT DIRECTOR",
		"DIRECTOR",
		"MANAGER",
		"PUBLIC AFFAIRS HEAD",
		"SR. EXECUTIVE ASSISTANT",
		"SENIOR STRATEGY OFFICER",
		"GIS COORDINATOR",
		"ACCESSIBLE TECHNOLOGY INITIATIVE PROGR",
		"DIRECTOR, UCSD RETIREMENT RESOURCE CEN",
		"DIRECTOR OF INTERNATIONAL RELATIONS",
		"CAREER RESOURCES COORDINATOR, CAREER C",
		"OUTREACH COORDINATOR",
		"EXECUTIVE DIRECTOR, EMERGING INITIATIV",
		"FACILITIES/PURCHASING MANAGER"
	],
	"DATA" : [
		"ACCOUNTANT",
		"SENIOR ALALYST",
		"DATA ARCHIVIST",
		"SOFTWARE ANALYST",
		"PERSONNEL ANALYST",
		"ADMIN ANALYST",
		"COLLECTION ANALYST",
		"RESEARCH ANALYST",
		"ENVIRONMENTAL PHILOSOPHER",
		"ADMINISTRATIVE ANALYST",
		"LEGAL ANALYST",
		"ADMIN. ANALYST",
		"CLINICAL APPLICATION ANALYST",
		"ANALYST",
		"PROGRAMMER ANALYST",
		"HUMAN RESOURCES ANALYST",
		"FINANCIAL ANALYST",
		"BUDGET RESEARCH ANALYST",
		"DATA ANALYST",
		"BUSINESS ANALYST",
		"ASSISTANT STATISTICIAN",
		"MATH SPECIALIST",
		"STATISTICIAN",
		"ECONOMIST",
		"FINANCIAL ASSISTANT",
		"FINANCE",
		"HUMAN RESOURCES ANALYIST",
		"DATA ENTRY"
	],
	"ARTS": [
		"MUSICAN",
		"ARTISTIC DIRECTOR",
		"GRAPHIC DESIGNER",
		"ARTS",
		"FILM TECHNINCIAN",
		"DIGITAL MEDIA ADMINISTRATOR"
	],
	"HEALTH": [
		"RADIATION ONCOLOGIST",
		"CLINICAL LAB SCIENTIST",
		"PHYSICIAN ASSISTANT",
		"OPHTHALMOLOGY",
		"INTEGRATIVE ONCOLOGY SPECIALIST",
		"FACULTY PHYSICIAN",
		"DIETITIAN",
		"DERMATOLOGIST",
		"NURSE PRACTITIONER",
		"ANESTHESIA TECHNICIAN",
		"EPIDEMIOLOGIST",
		"PSYCHOLOGIST",
		"CLINICAL SOCIAL WORKER",
		"SURGEON",
		"ED PHYSICIAN",
		"FAMILY PHYSICIAN",
		"VETERINARIAN",
		"SOCIOLOGIST",
		"HEALTH CARE",
		"CLERICAL",
		"PSYCHIATRIST",
		"MD, GENETICIST",
		"MD",
		"DOCTOR",
		"NEUROSURGEON",
		"NURSE",
		"PEDIATRICIAN",
		"RN",
		"VETERINIARIAN",
		"PHYSICIAN ANESTHESIOLOGIST",
		"DENTAL HYGIENE",
		"PHYSICIAN",
		"EYE DOCTOR",
		"PUBLIC HEALTH DENTIST",
		"REGISTERED NURSE",
		"R.N.",
		"RN - PART TIME",
		"SURGICAL TECH",
		"HOSPITAL CEO"
	],
	"GRAD": [
		"GRAD",
		"MD/PHD STUDENT",
		"POST-DOCTORAL SCHOLAR",
		"GRADUATE STUDENT RESEARCH",
		"GRAD STUDENT",
		"PHD STUDENT",
		"DOCTORAL CANDIDATE",
		"GRADUATE STUDENT",
		"CHEMISTRY GRADUATE STUDENT",
		"GRADUATE STUDENT INSTRUCTOR",
		"DOCTORAL STUDENT",
		"GRADUATE STUDENT RESEARCHER",
		"POSTDOCTORAL RESEARCHER",
		"MEDICAL STUDENT",
		"TEACHING ASSOCIATE/DOCTORATE STUDENT",
		"PH.D. STUDENT",
		"TEACHING ASSISTANT"
	],
	"UNDERGRAD": [
		"UNDERGRAD",
		"WORKSITE AND STUDENT",
		"STUDENT WORKER",
		"STUDENT/ATHLETIC TRAINER",
		"STUDENT",
		"STUDENT/ LABORER",
		"STUDENT RESEARCHER"
	],
	"RESEARCH": [
		"RESEARCH FACULTY",
		"INSTITUTIONAL RESEARCH",
		"NEUROSCIENTIST/ NEUROLOGIST",
		"LABORATORY TECHNICIAN",
		"SCIENTIST",
		"LAB TECH RESEARCH",
		"RESEARCH SOCIOLOGIST",
		"RESEARCH SCIENTIST",
		"RESEARCH", 
		"LVN/RESEARCH COORDINATOR",
		"RESEARCH ASSISTANT",
		"SOCIAL WORK RESEARCH",
		"RESEARCH",
		"LAB MANAGER",
		"MICROBIOLOGIST",
		"MEDICAL INFORMATICS RESEARCH",
		"BIOINFORMATICS",
		"EDUCATION, RESEARCH",
		"BIOLOGIST",
		"RESEARCHER",
		"DEMOGRAPHER/RESEARCHER",
		"HEALTH RESEARCHER",
		"POSTDOC",
		"RESEARCH DEMOGRAPHER",
		"LAB ASST.",
		"CANCER RESEARCHER",
		"SPECIALIST RESEARCHER",
		"SEISMOLOGIST",
		"PHYSICIST",
		"GEOLOGIST",
		"ANTHOPOLOGIST",
		"MATHEMATICIAN"
	],
	"RETIRED": [
		"RETIRED BIOLOGIST",
		"RETIRED PROFESSOR OF MUSIC",
		"RETIRED PROFESSOR",
		"MICROBIOLOGIST, RETIRED",
		"SEMI-RETIRED TEACHER",
		"RETIRED PROFESSOR, DEAN",
		"RETIRED HUMAN RESOURCES MANAGER",
		"RETIRED",
		"RETIRED REGISTERED NURSE",
		"RETIRED OFFICE MANAGER",
		"RETIRED DEPARTMENT MANAGER"
	],
	"LEGAL": [
		"LEGAL",
		"ATTORNEY",
		"LAWYER",
		"LAW ENFORCEMENT",
		"POLICE DISPATCHER"
	],
	"OTHER": [
		"REFUSED",
		"INTERN",
		"KAYAKING INSTRUCTOR",
		"ATHLETICS PROFESSIONAL",
		"JOURNAL EDITOR",
		"ACADEMIC",
		"EDITOR, ACADEMIC JOURNAL",
		"ACADEMIC SERVICES SPECIALIST",
		"PROPOSAL WRITER",
		"ARCHITECT",
		"EDITOR ACADEMIC JOURNAL",
		"ACADEMIC COORDINATOR",
		"HISTOTECHNOLOGIST I",
		"INSTRUCTIONAL TECHNOLOGIST",
		"AUDITOR",
		"HISTOLOGY TECH",
		"LIBRARIAN",
		"CONTRACT OFFICER",
		"LIBRARY SUPERVISOR",
		"OFFICE ASSISTANT",
		"LAW LIBRARIAN",
		"EXTENSION SPECIALIST",
		"BUS DRIVER",
		"LABORER",
		"HISTORIAN",
		"ARCHIVIST",
		"BOOK CONSERVATOR",
		"CONFERENCE SALES COORDINATOR",
		"POWER PLANT OPERATOR",
		"AHT II",
		"PURCHASING SPECIALIST",
		"CRA",
		"CLIMATE ACTION MANAGER",
		"INVESTIGATOR",
		"PUBLISHER",
		"COMPLIANCE CONSULTANT",
		"SPECIALIST",
		"ADVANCEMENT",
		"CONTRACT WORKER",
		"FUNDRAISING & COMMUNICATIONS",
		"SEN. MHP",
		"CURATOR",
		"CPHT",
		"SIGN LANGUAGE INTERPRETER",
		"ACADEMI",
		"SUPERVISOR",
		"FUNDRAISER",
		"SENIOR SPECIALIST"

	]

}

# for key in occupation_match_dict:
# 	occupation_dict[key] = []

# final_name_set = unique_name_set.copy()

# counta = 0
# for item in unique_name_set:
# 	match = False
# 	for m in occupation_match_dict:
# 		if (re.search(occupation_match_dict[m], item) != None):
# 			match = True
# 			counta += 1
# 			occupation_dict[m].append(item)
# 			final_name_set.discard(item)
# 	if not match:
# 		occupation_dict["OTHER"].append(item)
# 		final_name_set.discard(item)

# format("GRADUTE STUDENT RESEARCHER") --> GRAD
def format_job(input):
	for i in occupation_dict2:
		item_list = occupation_dict2[i]
		# print item_list
		for j in item_list:
			if j == input:
				return i

	print input 

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
	cand["contributions"] += 1
	# print cand["total"]

	college = format_college( row["contbr_employer"], row["contbr_city"] )
	if college is not None:
		college_arr = cand["colleges"]
		cand["colleges_total"] += amt 
		cand["colleges_contributions"] += 1

		curr_c = None 
		for c in college_arr:
			if c["name"] == college:
				c["contributions"] += 1
				c["total"] += amt
				curr_c = c 
				break

		if curr_c is None:
			new_c = {
				"name" : college,
				"contributions" : 1,
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
					j["contributions"] += 1
					found_job = True

					if j["colleges"].has_key(coll_name):
						j["colleges"][coll_name]["contributions"] += 1
						j["colleges"][coll_name]["total"] += amt

					else:
						j["colleges"][coll_name] = {
							"total" : amt,
							"contributions" : 1
						}


					break

			if not found_job:
				j = {
					"title" : job,
					"total" : amt,
					"contributions" : 1,
					"colleges" : {}
				}

				j["colleges"][coll_name] = {
					"contributions" : 1,
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

# print "UNKNOWN CITIES: "
# for item in unknown_cities_set:
	# print item 
# print len(unknown_cities_set)

for da in d:
	da["colleges"] = sorted(da["colleges"], key=lambda c: c["name"])

# for item in possible_colleges_set:
# 	print item 
# print len(possible_colleges_set)
	# handle location
	# loc = cand["locations"]
	# city = row["contbr_city"] 
	# if loc.has_key(city):
	# 	loc[city]["total"] += amt
	# 	loc[city]["contributions"] += 1
	# else:
	# 	loc[city] = {
	# 		"total" : amt,
	# 		"contributions" : 1 
	# 	}

json.dump(d, jsonfile, indent=4, separators=(',', ': '))
# print(json.dumps(d))




        