class morse:
	def __init__(self, message):
		self.message = message
		self.translation = '   '
		self.alpha = 'abcdefghijklmnopqrstuvwxyz'
		self.code = [ '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
		for x in range(len(self.message)):
			self.message.lower
			if self.message[x].isalpha():
				self.alpha[x] = self.code[x]
				return self.translation.append(self.code)
			else: 
				self.code[x] = self.message[x]
				self.translation = self.translation.append(self.code)

       

