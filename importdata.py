import csv
import operator
from bottle import run, route, template, request

with open('data.csv') as csvfile:
    mydata = list(csv.reader(csvfile, delimiter=';'))
    sort = mydata

@route('/origin')
def origin():
    return template('disp_table',rows=mydata)

@route('/origin',method='POST')
def origin():
        x=str(request.forms.get('submit'))

        if x == '1':
         sort = sorted(mydata[1:], key=operator.itemgetter(0))
        else:
            if x == '2':
                sort = sorted(mydata[1:], key=operator.itemgetter(1))
            else:
                if x == '3':
                    sort = sorted(mydata[1:], key=operator.itemgetter(1), reverse=True)
                else:
                    if x == '4':
                       sort = sorted(mydata[1:], key=operator.itemgetter(2))
                    else:
                        if x == '5':
                             sort = sorted(mydata[1:], key=operator.itemgetter(2), reverse=True)

        mydata[1:]=sort

        return {'return somthing'+\
                x}
run(port=8453, debug=True)

