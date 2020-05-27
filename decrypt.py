fo=open("enc.txt","rb")
image =fo.read()
fo.close()
image=bytearray(image)
key=int(input("enter a key "))
for index,value in enumerate(image):
    image[index]=value^key


fo=open("dec.txt","wb")
fo.write(image)
fo.close()