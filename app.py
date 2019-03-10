from flask import Flask, render_template, request
app = Flask(__name__)
server = app.server
import sqlite3
def getData():
	conn=sqlite3.connect('E:\\MyProgress\\Curie Labs\\webserver\\sensorsData.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM cur_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
	conn.close()
	return time, temp, hum
@app.route("/")
def index():
	time, temp, hum = getData()
	templateData = {
		'time': time,
		'temp': temp,
		'hum': hum
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run_server(debug=True)
