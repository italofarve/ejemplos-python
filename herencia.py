class Parent():

	def __init__(self, name, band):
		print("Parent Constructor Called")
		self.name = name
		self.band = band

	def show_info(self):
		print("Name - "+self.name)
		print("Band - "+self.band)


class Child(Parent):

	def __init__(self, name, band, best_selling_single):
		print("Child Constructor Called")
		Parent.__init__(self, name, band)
		self.best_selling_single = best_selling_single

	def show_info(self):
		print("Name - "+self.name)
		print("Band - "+self.band)
		print("Best selling single - "+str(self.best_selling_single))


james_taylor = Parent("James Taylor", "Kool and the Gang")
freddie_mercury = Child("Freddie Mercury", "Queen", "Another One Bites the Dust")

print "\n"
print "Imprimiendo datos:"
freddie_mercury.show_info()
print "================================================"
print james_taylor.name
print james_taylor.band
