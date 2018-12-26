import re


outfile = open("kokotinec.side","a")

with open("start.txt") as start:
    outfile.write(start.read())

with open ("list.txt") as list:
    for line in list:
        print (line)
        name = line.split("=")[-1].replace("\n","")
        namef = f"tests/{name}.side"
        print (name, namef)

        with open ("template.side") as template:
            #print(template.read())
            output = re.sub("TEMPLATE_VALUE",line.replace("\n",""),template.read())
            output = re.sub("NAME_PLACEHOLDER",name,output)
            #print(output)


            outfile.write(output)
            #outfile.write("},{")

    with open ("end.txt") as end:
        outfile.write(end.read())


