fo=open("raja.txt","rb")
text=fo.read()
fo.close()
text=bytearray(text)
key=int(input("enter a key"))
for index,value in enumerate(text):
    text[index]=value^key


fo=open("enc.txt","wb")
fo.write(text)
fo.close()