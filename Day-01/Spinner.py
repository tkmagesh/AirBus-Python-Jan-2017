class Spinner:
	def __init__(self):
		self.__counter = 0

	def inc(self):
		self.__counter += 1

	def get_value(self):
		return self.__counter


spinner = Spinner()

spinner.inc()
print(spinner.get_value())
spinner.inc()
print(spinner.get_value())
spinner.inc()
print(spinner.get_value())

spinner.__counter = 10000
spinner.inc()
print(spinner.get_value())