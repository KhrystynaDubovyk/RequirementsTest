import os 
import re
#Split all .md in one
directory = '../Guide_index/' 
filelist = sorted([os.path.join(pdir, f) for pdir, dirs, files in os.walk(directory) for f in files])
for i in filelist:
    print i
    f = open('guidline.md', 'a')
    f.write((open(i, 'r')).read())
    f.close()
#Conver link
temp = open("guidline.md", 'r+')
for line in temp:
    line = re.sub(r'(\.\./+.+\.md)','', line)
    f = open("guidlineresult.md", 'a')
    f.write(line)
f.close()    
temp.close()

