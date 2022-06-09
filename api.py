try:
	import http.client

except ImportError:
	print("Import error")

### api
def conv(text):
	conn = http.client.HTTPSConnection("bionic-reading1.p.rapidapi.com")

	payload = "content="+text+".&response_type=html&request_type=html&fixation=1&saccade=10"

	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'X-RapidAPI-Host': "bionic-reading1.p.rapidapi.com",
		'X-RapidAPI-Key': "API-KEY"
		}

	conn.request("POST", "/convert", payload, headers)

	res = conn.getresponse()

	data = res.read()
	data = data.decode("utf-8")
	print("Done")
	return data
