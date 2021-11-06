import re
import sys

def myfunc (infile , outfile, search1):

    fi =  open(infile).readlines()
    fo =  open(outfile, 'w')

    for n, l in enumerate(fi):

        if re.findall(search1 , str(l)):
            print("wegqegq")
            len = 3
            for x in range(len(str(l))):
                if str(l)[x] == "[":
                    sect = str(l)[x]+str(l)[x]
                for x in range(n):
                    if re.findall(sect , str(fi[n-x-1])) and len > 0:
                        fo.write(str(fi[n-x-1]))
                        l = l-1
            
            fo.write(str(l)+" -----")   
    fo.close()
    infile.close()

    return

infile = sys.argv[0]
outfile = sys.argv[1]
search1 = "ERROR"
myfunc(infile, outfile, search1)
