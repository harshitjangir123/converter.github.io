from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def convert():
    # Get inputs from the user
    temp = request.json['temp']
    from_unit = request.json['from_unit']
    to_unit = request.json['to_unit']

    # Convert temperature from one unit to another
    if from_unit == "C" and to_unit == "F":
        result = (temp * 1.8) + 32
    elif from_unit == "F" and to_unit == "C":
        result = (temp - 32) / 1.8
    elif from_unit == "C" and to_unit == "K":
        result = temp + 273.15
    elif from_unit == "K" and to_unit == "C":
        result = temp - 273.15
    elif from_unit == "F" and to_unit == "K":
        result = (temp + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "F":
        result = (temp * 9/5) - 459.67
    else:
        result = temp

    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
