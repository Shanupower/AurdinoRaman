### Requirements

```bash
pip install flask
```

OR

```bash
pip3 install flask
```

### Sending Data

You can use a tool like Postman to send a POST request to `http://127.0.0.1:5000/sendData` with form data containing a field named `data`.

### Sending Data using Example Using `curl`

Alternatively, you can use `curl` from the command line to send data:

```bash
curl -X POST -F "data=your_data_here" http://127.0.0.1:5000/sendData
```

### Accessing the data

You can Visit this website to see the resulted webpage http://127.0.0.1:5000/receivedData
