import sqlite3 as lite
import sys
import re

months = {
	'Jan' : 1,
	'Feb' : 2,
	'Mar' : 3,
	'Apr' : 4,
	'May' : 5,
	'Jun' : 6,
	'Jul' : 7,
	'Aug' : 8,
	'Sep' : 9,
	'Oct' : 10,
	'Nov' : 11,
	'Dec' : 12
}

#open and readfile
def readTextFile():
	with open ('tempLog.txt','r') as textfile:
		for line in textfile:
			#print line

			#format line
			#line = "T=17.6, H=59.1, 27-Dec-2015, 10.15.03"
			pattern = "T=(\d+\.\d),\ H=(\d+.\d),\ (\d+)-(\w{3})-(\d{4}),\ (\d+).(\d+).\d+"
			result = re.search(pattern, line)

			values = []
			for x in range(1,8):
				if x==4:
					values.append(months[result.group(x)])
				else:
					values.append(result.group(x))


			final = ','.join((map(str,values)))
			cur.execute("INSERT INTO DHT_readings VALUES (" + final + ")")


#create db
with lite.connect('ambient.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS DHT_readings")
    cur.execute("CREATE TABLE DHT_readings (temp INT, hum INT, day INT, month INT, year INT, hour INT, minute INT)"
    )
    readTextFile()  


#commit