
import os
import time
import csv
import pandas as pd
pdir = '~/Zillow/_to_ssend(April)'
paths_to_file = []


for d, dirs, files in os.walk(pdir):
	pass
	#print(d)
	#print(dirs)
	#print(files)
#print(files)


for file in files:
	#print(file)
	#print(os.path.join(pdir, file))
	paths_to_file.append(os.path.join(pdir, file))


for file in paths_to_file:
	pass
	#print(file)



lines = []
for file in paths_to_file:
	with open(file, 'r+') as csvfile:
		reader = csv.reader(csvfile)		
		#i=0
		for current_line in reader:
			pass
			if current_line[10] == 'url':
				pass
			else:
				lines.append(current_line)
	


file_name = "%s_%s.csv" % (str(time.strftime("%Y-%m-%d")),str(time.strftime("%H%M%S")))
columns = ["address", "city", "state", "zip", "price", "sqft", "bedrooms",
           "bathrooms", "days_on_zillow", "sale_type", "url", "zestimate",
            "zRange", "builtIn", "builtBy", "comName", "parking", "school", 
            "parking_details", "lastSold", "priceSqft"]
pd.DataFrame(lines, columns = columns).to_csv(file_name, index = False)





# for i in os.walk(pdir):
# 	print(i)
# 	contdir.append(i)


# for i in contdir:
# 	print(i)





# import os


# tree = os.walk("~/Zillow")


# print(tree)


# for d in tree:
# 	print(d)


# for path, dirs, files in os.walk("~/Zillow"):
# 	print("ss")
# 	for fname in files:
# 		print("ss")
# 		print(os.path.join(path, fname))




# filepath = "to_send(April)/2018-04-14_231058_93737.csv"

	# with open(filepath, 'r+') as csvfile:
	# 	reader = csv.reader(csvfile)
	# 	lines = []
	# 	i=0

	# 	for current_line in reader:
	# 		pass
	# 		#print(current_line)
	# 		# i+=1
	# 		# if i == 5:
	# 		# 	break

