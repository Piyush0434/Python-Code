f=open("poem.txt")
d=f.read()
if("Twinkle" in d):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")

f.close()