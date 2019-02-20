import glob

pyfiles = glob.glob('*.txt')

print(pyfiles)

thistxtfile = pyfiles[0]

import zipfile

fileunderwork = zipfile.ZipFile('temp.zip', 'w')
fileunderwork.write(thistxtfile, compress_type=zipfile.ZIP_DEFLATED)
fileunderwork.close()
