<h2>Geopy-Page</h2>
<p>Takes a list of addresses and outputs an HTML table with latitude and longitude information.</p>

<h3>Make it Work</h3>
<strong>Install Python</strong>
http://www.python.org/download/

<strong>Install pip</strong>
http://www.pip-installer.org/en/latest/installing.html

<strong>Use pip to install Geopy</strong>
'''
pip install geopy
'''

<strong>Add your addresses</strong>
'''python
addresses = [
	"600 Civic Center Dr, Detroit, MI",
	"2100 Woodward Ave, Detroit, MI",
	"2000 Brush St #200, Detroit, MI"
]
'''

<strong>Run it</strong>
'''
python geopy-page.py
'''