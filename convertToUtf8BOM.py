
import codecs
import glob


BLOCKSIZE = 1048576 # or some other, desired size in bytes

pyfiles = glob.glob('*.txt')


for eachitem in pyfiles:

	sourcefilename = eachitem
	targetfilename = "converted_"+eachitem

	with codecs.open(sourcefilename, "r") as sourcefile:
		with codecs.open(targetfilename, "w", "utf-8-sig") as targetfile:
			while True:
				contents = sourcefile.read(BLOCKSIZE)
				if not contents:
					break
				targetfile.write(contents)
