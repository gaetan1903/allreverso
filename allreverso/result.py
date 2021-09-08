class CorrectResult:
	def __init__(self, **kwargs):
		self.text = kwargs.get('text')
		self.description = ''
		for desc in kwargs.get('corrections'):
			self.description += desc['shortDescription'] + ': '
			self.description += desc['mistakeText'] + ' --> ' + desc['correctionText']
			self.description += '\n' + desc['longDescription'] + '\n\n'


	def __str__(self):
		return self.text
