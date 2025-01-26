from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
  data = json.load(f)


@app.route('/')
def hello_world():
  return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref')  # get the parameter from url
  if pref:
    for student in data:  # iterate dataset
      if student[
          'pref'] == pref:  # select only the students with a given meal preference
        result.append(student)  # add match student to the result
    return jsonify(result)  # return filtered set if parameter is supplied
  return jsonify(data)  # return entire dataset if no parameter supplied


@app.route('/students/<int:key>')
def get_student(id):
  for student in data:
    if student['id'] == id:
      return jsonify(student)


@app.route('/stats')
def get_stats():
  chicken = 0
  fish = 0
  vegetarian = 0
  for student in data:
    if student['pref'] == "Chicken":
      chicken += 1
    elif student['pref'] == "Fish":
      fish += 1
    else:
      vegetarian += 1


app.run(host='0.0.0.0', port=8080)
