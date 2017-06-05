import os,sys

def printFile(fileName):
	filePrint = os.getcwd()+'\\'+'Output\\'+fileName
	os.startfile(filePrint, "print")

if __name__=='__main__':
	printFile(sys.argv[1])
