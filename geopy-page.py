from geopy import geocoders
import time

g = geocoders.Google()
count = 0

# Update this list of address to your needs
addresses = [
"600 Civic Center Dr, Detroit, MI",
"2100 Woodward Ave, Detroit, MI",
"2000 Brush St #200, Detroit, MI",
"2345123 sdsgasv"
]

# open file and page header
text_file = open("output.html", "w")
text_file.write("""
<!doctype html>
<html lang=\"en\">
<head>
	<meta charset=\"UTF-8\">
	<title>Addresses</title>
	<link href=\"http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css\" rel=\"stylesheet\">
</head>
<body>
	<table class=\"table table-striped\">
		<tr><th>#</th><th>Address</th><th>Latitude</th><th>Longitude</th></tr>
""")

# find lat and long and output as table row
for a in addresses:
	count = count + 1
	# print "%d" % count
	try:
		place, (lat, lng) = g.geocode(a)
		text_file.write("\t\t<tr><td>%d</td><td>%s</td><td>%.5f</td><td>%.5f</td></tr>\n" % (count, place, lat, lng))
		time.sleep(.5)
	except:
		text_file.write("\t\t<tr><td>%d</td><td>%s</td><td colspan=\"2\" style=\"color:#AA0000;\">Failed</td></tr>\n" % (count, a))

# close page and file
text_file.write("""\t</table>
</body>
</html>""")
text_file.close()
print "Done."