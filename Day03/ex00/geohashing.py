import sys, antigravity

class ArgError(Exception):
	def __init__(self) -> None:
		super().__init__("required 3 argments")

class ArgError(Exception):
	def __init__(self) -> None:
		super().__init__("required 3 argments")


if __name__ == '__main__':

	if len(sys.argv) != 4:
		raise ArgError

	latitude = float(sys.argv[1])
	longitude = float(sys.argv[2])
	datedow = sys.argv[3].encode()

	antigravity.geohash(latitude, longitude, datedow)


