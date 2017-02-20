import csv
import operator
from bottle import run, route, template

with open('data.csv') as csvfile:
    mydata = list(csv.reader(csvfile, delimiter=';'))

    @route('/origin')
    def origin():
        return template('distable', rows=mydata)



    @route('/origin/name')
    def name():
        sort = sorted(mydata[1:], key=operator.itemgetter(0))
        mydata[1:] = sort
        return template('distable', rows=mydata)


    @route('/origin/age1')
    def age1():
        sort= sorted(mydata[1:], key=operator.itemgetter(1))
        mydata[1:] = sort
        return template('distable', rows=mydata)


    @route('/origin/age2')
    def age2():
       sort= sorted(mydata[1:], key=operator.itemgetter(1), reverse=True)
       mydata[1:] = sort
       return template('distable', rows=mydata)

    @route('/origin/salary1')
    def salary1():
       sort = sorted(mydata[1:], key=operator.itemgetter(2))
       mydata[1:] = sort
       return template('distable', rows=mydata)

    @route('/origin/salary2')
    def salary2():
      sort= sorted(mydata[1:], key=operator.itemgetter(2), reverse=True)
      mydata[1:] = sort
      return template('distable', rows=mydata)

run(host='localhost',port=8457, debug=True)
