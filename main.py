from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
from flask import request

app = Flask(__name__)


@app.route("/titanic")
def hello():
	graph = request.args.get('graph')
	tit = pd.read_csv('data/titanic.csv')
	# tit['Age'].hist()
	# plt.figure()
	tit['Age'].plot()

	if graph == '0':
		df = tit.head()
		return df.to_html()
	elif graph == '1':
		my_stringIObytes = io.BytesIO()
		plt.savefig(my_stringIObytes, format='jpg')
		my_stringIObytes.seek(0)
		
		b64 = base64.b64encode(my_stringIObytes.read()).decode('utf8')
		

		html = '<html><body><img src="data:image/png;base64, '+b64+'"/></body></html>'

		return html


if __name__ == "__main__":
	app.run(host='0.0.0.0')
