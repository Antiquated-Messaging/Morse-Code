class morse:
	def __init__(self, message):
		self.message = message
<<<<<<< HEAD
		self.translation = '   '
=======
		self.translation = ''
>>>>>>> 42097cb0b4ae11a3ff01451049172a8c7ac5b94b
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

       

