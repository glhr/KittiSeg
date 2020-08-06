with open("training.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.split("_")[-1].split(".")[0] for x in content]

import glob, os

for img in content:
    for f in glob.glob("thermal/"+img+"*.png"):
        os.remove(f)
	print img
	

