<h2>geopy-page</h2>
<p>geopy-page uses the <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CDMQFjAA&url=http%3A%2F%2Fcode.google.com%2Fp%2Fgeopy%2F&ei=TW0BUbLZNZKTqwG25YCIDA&usg=AFQjCNFKsHikLRahjbXkYt_eanbjuXRu9A&sig2=P4O2alk5Qe2PSObUOJsyBw&bvm=bv.41248874,d.aWM">geopy library</a> to turn a list of addresses into an HTML file with latitude and longitude information.</p>

<h3>Make it Work</h3>
<strong>Install Python</strong><br />
http://www.python.org/download/

<strong>Install pip</strong><br />
http://www.pip-installer.org/en/latest/installing.html

<strong>Use pip to install geopy</strong><br />
```
pip install geopy
```

<strong>Add your addresses</strong><br />
```python
addresses = [
	"600 Civic Center Dr, Detroit, MI",
	"2100 Woodward Ave, Detroit, MI",
	"2000 Brush St #200, Detroit, MI"
]
```

<strong>Run it</strong><br />
```
python geopy-page.py
```

<hr>
<p>Special thanks to <a href="http://bootstrapcdn.com">BootstrapCDN.com</a> for hosting the Twitter Bootstrap stylesheet and making the output nice.</p>