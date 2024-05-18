from flask import Flask, request, render_template

app = Flask(__name__)

# Global variable to store the received data
receivedData = ""

@app.route('/sendData', methods=['POST'])
def send_data():
    global receivedData
    receivedData = request.form['data']
    return "Data received and stored."

@app.route('/receivedData')
def received_data():
    global receivedData
    return render_template('received_data.html', data=receivedData)

if __name__ == '__main__':
    app.run(debug=True)
