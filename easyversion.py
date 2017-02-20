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
        sortname = sorted(mydata[1:], key=operator.itemgetter(0))
        mydata[1:] = sortname
        return template('distable', rows=mydata)


    @route('/origin/age1')
    def age1():
        sortage1 = sorted(mydata[1:], key=operator.itemgetter(1))
        mydata[1:] = sortage1
        return template('distable', rows=mydata)


    @route('/origin/age2')
    def age2():
       sortage2 = sorted(mydata[1:], key=operator.itemgetter(1), reverse=True)
       mydata[1:] = sortage2
       return template('distable', rows=mydata)

    @route('/origin/salary1')
    def salary1():
       sortsalary1 = sorted(mydata[1:], key=operator.itemgetter(2))
       mydata[1:] = sortsalary1
       return template('distable', rows=mydata)

    @route('/origin/salary2')
    def salary2():
      sortsalary2= sorted(mydata[1:], key=operator.itemgetter(2), reverse=True)
      mydata[1:] = sortsalary2
      return template('distable', rows=mydata)

run(host='localhost',port=8457, debug=True)
