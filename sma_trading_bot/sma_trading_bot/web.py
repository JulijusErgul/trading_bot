from flask import Flask, render_template_string
from logger import LOG_FILE

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Tradingbot Status</title></head>
<body>
<h2>Tradingbot Logg</h2>
<pre>{{ logs }}</pre>
</body>
</html>
'''

@app.route("/")
def index():
    with open(LOG_FILE, "r") as f:
        logs = f.read()
    return render_template_string(TEMPLATE, logs=logs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
