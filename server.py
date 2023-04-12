from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

@app.route('/process1', methods=['POST'])
def p1():
   """
   Summary: cslls process1
   Args:
       data (List[int]): the data
   Returns:
       list: result
   """
   data = request.get_json()
   res = jsonify(process1(data))
   res.status_code = 200
   return res

@app.route('/process2', methods=['GET'])
def p2():
   """
   Summary: cslls process2
   Args:
       data (List[int]): the data
   Returns:
       list: result
   """

   data = request.get_json()
   res = jsonify(process2(data))
   res.status_code = 200
   return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)