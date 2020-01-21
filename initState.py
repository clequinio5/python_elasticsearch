from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import time

# curl -X POST "192.168.0.112:9200/cvs/_update_by_query?pretty" -H 'Content-Type: application/json' -d'{"script": {"source": "ctx._source[\u0027cvtheque\u0027]=params.update_cvtheque","params":{"update_cvtheque":{"comment":"","state":"vivier"}},"lang": "painless"},"query":{"bool":{"must_not":{"exists":{ "field": "cvtheque" }}}}}'

url = 'http://192.168.0.112:9200/cvs/_update_by_query?pretty'

while (True):

	time.sleep(5)

	data = {"script": {"source": "ctx._source[\u0027cvtheque\u0027]=params.update_cvtheque","params":{"update_cvtheque":{"comment":"","state":"vivier"}},"lang": "painless"},"query":{"bool":{"must_not":{"exists":{ "field": "cvtheque" }}}}}
	
	request = Request(url, data=json.dumps(data).encode('utf8'), headers={'content-type': 'application/json'})
	resp = json.loads(urlopen(request).read().decode())
	
	print(resp)

		
		
		
	