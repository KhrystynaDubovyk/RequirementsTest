import os 
import pandoc
from markdown import markdown
import pdfkit
import re
#Split all .md in one
directory = '../Guide_index/' 
flist = [os.path.join(pdir,f) for pdir, dirs, files in os.walk(directory) for f in files]
for i in flist:
	print i 
	f1 = open("guidline.md", 'a+')
	f2 = open( i, 'r')
	f1_out=[]
	f2_out=[]
	res=[]
	f1_out=f1.read()
	f2_out=f2.read()
	res=f1_out+f2_out
	f1.write(res)
	f1.close()
	f2.close()
#Rebase link
md = open("guidline.md", 'r+')
for line in md:
    line = re.sub(r'(\.\./+.+\.md)','', line)
    print line 
    f=open("guidlineresult.md", 'a')
    f.write(line)
       
f.close()    
md.close()
