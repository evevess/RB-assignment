import csv

from bottle import run, route, template
@route('/hello')
def hello():
    return "Hello World!"


with open('data.csv') as csvfile:
    mydata = list(csv.reader(csvfile, delimiter=';'))

    sort = mydata

@route('/hello')
def original():
    return template('disp_table', rows=sort)


@route('/sorting')
def sorting():
    return template('disp_table', rows=mydata)


run(port=8403, debug=True, update=True)


