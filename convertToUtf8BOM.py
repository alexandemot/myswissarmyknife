import codecs

BLOCKSIZE = 1048576 # or some other, desired size in bytes

sourcefilename = "txtfile.txt"
targetfilename = "convertedtxtfile.txt"

with codecs.open(sourcefilename, "r") as sourcefile:
	with codecs.open(targetfilename, "w", "utf-8-sig") as targetfile:
		while True:
			contents = sourcefile.read(BLOCKSIZE)
			if not contents:
				break
			targetfile.write(contents)
