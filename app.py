from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    # http://localhost:5000
    # It will run web server on local machine
    # http://localhost:80or localhost
    # app.run(
    #     host="0.0.0.0",
    #     port=80,
    #     debug=True
    #     )
    # resp = """
    # <!Doctype html>
    # <html>
    #     <head> </head>
    #     <body> 
    #         <h1 style='color:red'>
    #             Welcome to Flask Powered Web Page!
    #         </h1>
    #     </body>
    # </html>
    # """