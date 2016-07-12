from abc import ABCMeta, abstractmethod

class Planet(object):
	"""One of the planets found in the Solar System.
	
	Attributes:
		mass: planetary mass in cm
		radius: planetary radius in cm
		period: orbital period in years
		semi_major: semi-major axis of the orbit in AU
		eccentricty: eccentricity of the orbit
	"""
	
	__metaclass__ = ABCMeta

	type = "None"
	ref = "None"

	def __init__(self, mass, radius, period, semi_major, eccentricity):
		self.mass = mass
		self.radius = radius
		self.period = period
		self.semi_major = semi_major
		self.eccentricity = eccentricity

	def __setattr__(self, name, value):
		if self.__dict__.has_key("locked"):
			raise NameError("Class is locked. \
					Can't add {} attribute!".format(name))
		if self.__dict__.has_key(name):
			raise NameError("Can't rebind {}".format(name))
		self.__dict__[name] = value

	def density(self):
		"""Return average density of planet."""
		return self.mass / (4.188790 * self.radius**3)

	@abstractmethod
	def planet_name(self):
		"""Return planet name."""
		pass


class Mercury(Planet):
	"""Mercury, closest planet to the Sun."""

	type = "Terrestrial"
	ref = "http://www.astro.wisc.edu/~dolan/constants.html"

	def __init__(self):
		self.mass = 3.303E+26
		self.radius = 2.439E+08
		self.period = 2.4085E-01
		self.semi_major = 3.87096E-01
		self.eccentricity = 0.205622
		self.locked = 1


class Venus(Planet):
	"""Venus, second planet from the Sun."""

	type = "Terrestrial"
	ref = "http://www.astro.wisc.edu/~dolan/constants.html"

	def __init__(self):
		self.mass = 4.870E+27
		self.radius = 6.050E+08
		self.period = 6.1521E-01
		self.semi_major = 7.23342E-01
		self.eccentricity = 0.006783
		self.locked = 1
