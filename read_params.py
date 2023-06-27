f=open('parameters','r')
lines=f.readlines()
f.close()
params = {}
currentHex=''
currentParam=''

def h2i(hexLines):
    if (hexLines == ''):
        return 0
    return int(hexLines.replace(' ','').replace(':',''), 16)

def splitPoint(hexLines):
    gen=hexLines.replace(' ','').replace(':','')[2:]
    print("gen", gen)
    gl=len(gen)

    splitt = int(gl/2)


    return (int(gen[:splitt],16), int(gen[splitt:], 16))

ecpoints=["Gener", "pub"]

for line in lines:
    if line[0].isalpha():
        if (currentHex != '' and currentParam != ''):
            print("key:",currentParam)
            if not currentParam in ecpoints:
                params[currentParam]=h2i(currentHex)
            else:
                params[currentParam]=splitPoint(currentHex)
        currentParam = line.strip().replace(':','')[:5]
        currentHex=''
    else:
        currentHex+=line.strip()
print(params)
