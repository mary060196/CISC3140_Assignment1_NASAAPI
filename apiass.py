from flask import Flask, render_template, request
import urllib.request
import json
import webbrowser

app = Flask(__name__, template_folder=r'./templates') # Relative path to reach the templates folder

@app.route('/')
@app.route('/EPIC_API/')
def hello():
    return render_template('intro.html')

@app.route('/EPIC_API/results', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		mykey = request.form['API_KEY']
		# Connect to the endpoint:
		EPIC_Image_url = 'https://api.nasa.gov/EPIC/api/natural/date/2019-06-27?api_key='
		# Call the webservice to fetch the data, and catch any exceptions:
		try:
			EPIC_Image_url_obj = urllib.request.urlopen (EPIC_Image_url + mykey)
		except urllib.error.HTTPError as e:
			print(e.code)
			print(e.read())
			return render_template('intro.html', error = True) # Pass 'True' TO the variable 'error'
		else:
			# Read the object:
			objread = EPIC_Image_url_obj.read()
			# Decode JSON to python data structure:
			decoded = json.loads(objread .decode('utf-8'))
			#Create a new url string referring to the image itself:
			newurl = 'https://epic.gsfc.nasa.gov/archive/natural/2019/06/27/png/' + decoded[8]['image'] + '.png'
			# ( We choose the 9th photo (index 8) made on June 27, 2019.) 
			return render_template('index.html', my_url=newurl, deco = decoded[8])

if __name__ == "__main__":
    webbrowser.open_new("http://localhost:5000/EPIC_API")
    app.run('localhost', 5000, True, use_reloader=False)