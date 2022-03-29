from flask import Flask
myapp_obj = Flask(__name__)
name = 'Lisa'
city_names = ["Paris", "London", "Rome", "Tahiti"]
#<a> defines hyperlinks, href is where to add the https link
@myapp_obj.route("/")
def home():
	return f'''
	<html>
	<head>
		<title>Home Page</title>
	</head>
	<body>
		<h1>Welcome, ''' + name + '''</h1>
		<a href = "https://www.google.com">not google</a> 
		<ul>
			''' + helper(city_names) + '''
		</ul>
	</body>
	</html>
	'''
def helper(list):
	temp = ""
	for n in range(len(list)):
		temp = temp + list[n] + "\n"
	return temp

myapp_obj.run()