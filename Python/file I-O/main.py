
#Reading a file 
f = open("f.txt")
data = f.read()
print(data)
f.close()

#Writing a file 
st="Hey Piyush you are amazing"

f = open("myfile.txt","w")

f.write(st)

f.close()