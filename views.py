from flask import render_template
from app import app

from systeminfo import systeminfo

@app.route('/')
def index():
	returnDict = {} 
	returnDict['systeminfo'] = systeminfo.main()
	returnDict['title'] = 'Home'
	return render_template("index.html", **returnDict)
