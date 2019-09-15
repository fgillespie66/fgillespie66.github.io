import requests
import datetime
import sqlite3


dhke_db = '__HOME__/epione.db'

delim = "\n"
#MAX_READINGS = 5 # After 14 lines of information, no more lines will be displayed on the screen (overflow)


# values:
	# name: name of person form is for
	# loc: 
	# disaster
	# status
	

def request_handler(request): 
	if request['method'] == 'GET': # return all updates in your area
		conn = sqlite3.connect(epione_db)  # connect to that database (will create if it doesn't already exist)
		dis = request['values']['disaster']
		sql_query = '''SELECT * FROM epione_table WHERE disaster=dis ORDER BY dt DESC''';
		return(sql_query)
	elif request['method'] == 'POST':
		c = conn.cursor()  # make cursor into database (allows us to execute commands)

		# get user from the request
		disaster = request['values']['disaster']
		name = request['values']['user']
		loc = request['values']['loc']
		status = request['values']['status']

		dt = datetime.datetime.now()

		c.execute('''CREATE TABLE IF NOT EXISTS epione_table (disaster text, dt timestamp, name text, loc text, status text);''') # run a CREATE TABLE command
		c.execute('''INSERT into epione_table VALUES (?, ?, ?,?, ?);''', (disaster, dt, name, loc, status))
		conn.commit() # commit commands
		conn.close() # close connection to database
	
		return

