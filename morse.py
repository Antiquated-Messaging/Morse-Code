class morse:
	def __init__(self, message, location):
		self.message = message
		self.location = location
		self.translation = ''
		self.alpha = 'abcdefghijklmnopqrstuvwxyz'
		self.code = [ '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
		for x in range(len(self.message)):
			if self.message[x].isalpha():
				self.alpha[x] = self.code[x]
				return self.translation.append(self.code)
			else: 
				self.code[x] = self.message[x]
				self.translation = self.translation.append(self.code)

       



