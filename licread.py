import base64

f=open("licenza.bin","rb")
licenza=f.read().decode('utf-8')
licenza=base64.b85decode(licenza)
print(str(licenza))
licenza=base64.b64decode(licenza)
licenza=licenza.decode("utf-8")

print (licenza)
f.close()
