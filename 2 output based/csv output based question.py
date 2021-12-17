import csv
def addCsvFile(Name,Hobby):
    f=open("D:\\12th File handle\\hobby.csv","a")
    newFileWriter=csv.writer(f)
    newFileWriter.writerow([Name,Hobby])
    f.close()
def readCsvFile():
    newFile=open("D:\\12th File handle\\hobby.csv","r") 
    newFilereader=csv.reader(newFile)
    for row in newFilereader:
        print(row[0],"@",row[1])
    newFile.close()    
addCsvFile("Pratik","Cricket")
addCsvFile("Sunaina","Badminton")
addCsvFile("Manish","Painting")
readCsvFile()        

