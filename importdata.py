import csv
import json
from bottle import run, route, template, request

with open('data.csv') as csvfile:
    mydata = list(csv.reader(csvfile, delimiter=';'))
    #mydata=map(list, zip(*mydata))
    @route('/new')
    def index():
        # return {'data':mydata}
     return template('disp_table',rows=mydata)


@route('/new')
def add_new():
    return template('disp_table',rows=mydata)


run(host='localhost', port=8090, debug=True)