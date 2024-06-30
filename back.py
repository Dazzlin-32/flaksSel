import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from phoneNumbers import search_last

app = Flask(__name__)
CORS(app)



@app.route('/')
def get_current_time():
    return {'time': time.time()}

@app.route('/data', methods = ['POST'])
def fetching_data():
    if (request.method == 'POST'):
        
        name = request.form.get('name')
        phone = request.form.get('phone')
        print(name , phone)
        if(phone != 0):
            result = callAutomation(name, phone)
            print(result)
            
    return jsonify(result)


def callAutomation(name, phone):
    print("Automation Called!", name , phone)
    if(phone != 0):
        result = search_last(str(phone), name)
        print("REsult in python", result)
        return result
    else:
        return "Error"

if __name__ == '__main__':
    app.run()
        
