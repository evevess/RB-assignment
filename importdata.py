# import csv
#
# with open('data.csv') as csvfile:
#     mydata = list(csv.reader(csvfile, delimiter=';'))
#     #mydata=map(list, zip(*mydata))

from bottle import run, route, template,request
    # @route('/')
    # def index():
    #     # return {'data':mydata}
    #  return template('creat_checkbox')
@route('/new')
def add_new():
    return template('creat_checkbox')

    @route('/new', method='POST')
    def add_new():
        p = request.forms.get()

    run(host='localhost',debug=True)