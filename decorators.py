from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    tiempo=time.asctime()
    return render_template('index.html',realtime=tiempo)
if __name__=="__main__":
  app.run(debug = True, port=5000)
