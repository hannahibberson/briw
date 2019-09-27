from json import JSONEncoder

class MyEncoder(JSONEncoder):
	def default(self, o):
		try:
			return o.__dict__
		except:
			return o.decode('utf-8')


		