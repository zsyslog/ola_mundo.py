from flask import Flask, jsonify
from flask import render_template
import os
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
	salutation = choice(salutations)
	return render_template('index_tpl.html', salutation=salutation)

@app.route('/salutation')
def salutation():
	salutation = choice(salutations)
	return jsonify(results=salutation)

salutations = [
	{'saludo': 'ola k ase'},
	{'saludo': 'k pasa Kapo?'},
	{'saludo': 'k suzede?'},
	{'saludo': 'holanda que talka'}
]	

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))

  if port == 5000:
      app.debug = True

  app.run(host='127.0.0.1', port=port)
