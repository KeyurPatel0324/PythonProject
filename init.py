from Development.init import app
from flask import request


@app.route('/handler/monthly',methods = ['POST','GET'])
def monthly():
    try:
        data = request.get_data()
        data = {'allotedwater': {'ratio': '1:5', 'appartment': 3}, 'add_guest': [{'ag': 2}]}
        from Development.BL import monthly
        monobj = monthly.monthlycost()
        data1 = monobj.MonthlyData(data)
        return data
    except BaseException as e:
        raise e


