import csv

r1 = csv.reader(open('sanders.csv', 'rb'))
r1.next()	# skip first line

# r2 = csv.reader(open('clinton.csv', 'rb'))
# r2.next()

csvfile = open('result.csv', 'wb')
writer = csv.writer(csvfile)

for row in r1:
	writer.writerow(row)

# for row in r2:
# 	writer.writerow(row)

csvfile.close()
csvfile = open('result.csv', 'rb')
jsonfile = open('result.json', 'wb')

d = {
	'dem' : {
		'Sanders' : {
			"total" : 0,
			"colleges" : {
				"ucla" : {

				}

			},
			"locations" : {
				# add keys if they don't exist!

			}
		}
	},
	'rep' : { 
		'Trump' : {
			"total" : 0
		}
	}
	
}


fieldnames = ["cmte_id","cand_id","cand_nm","contbr_nm","contbr_city","contbr_st","contbr_zip","contbr_employer","contbr_occupation","contb_receipt_amt","contb_receipt_dt","receipt_desc","memo_cd","memo_text","form_tp","file_num","tran_id","election_tp"]

name_hash = {
	"Sanders, Bernard" : ('dem', 'Sanders'),
	"Clinton, Hillary Rodham" : ('dem', 'Sanders')
}

def format_name(n):
	return name_hash[n]



# dictReader = csv.DictReader(csvfile, fieldnames, delimiter = ',', quotechar = '"')
dictReader = csv.DictReader(csvfile, fieldnames, delimiter = ',', quotechar = '"')

curr_name = 0; 

for row in dictReader:
	t = format_name( row["cand_nm"] )
	cand = d[t[0]][t[1]]

	amt = int(row["contb_receipt_amt"])

	cand["total"] += amt
	print cand["total"]
    # for key in row:
    # 	print key
        # d[key].append(row[key])
        # print "%s : %s " % (key, row[key])