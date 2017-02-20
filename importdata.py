import csv

with open('data.csv') as csvfile:
    mydata = list(csv.reader(csvfile, delimiter=';'))
    #mydata=map(list, zip(*mydata))

    from bottle import run, route, template
    @route('/')
    def index():
        # return {'data':mydata}
         return template('disp_table', rows=mydata)
    run(debug=True,reloader=True)

