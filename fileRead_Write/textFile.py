# reading a text file
readFile = open("textRead.txt","r")
lines = readFile.readlines()

newList = []
for readLine in lines:
    newList.append(readLine.strip())

print(newList)



#writing to a text file
writeFile = open("textWrite.txt","w")
writeFile.write("Hello!\n")
writeFile.write("my name is niya\n")
writeFile.write("I am learning how to write to a file")

writeFile.close()