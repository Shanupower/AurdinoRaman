from flask import Flask, render_template
import udp_server  # Import the UDP server to ensure it runs

app = Flask(__name__)

@app.route('/receivedData')
def received_data():
    return render_template('received_data.html', data=udp_server.receivedData)

if __name__ == '__main__':
    app.run(debug=True)
