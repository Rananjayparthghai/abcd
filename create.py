from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return '\nRananjay's practical | 21BCS3357'

if name == 'main':
    app.run(debug=True)
