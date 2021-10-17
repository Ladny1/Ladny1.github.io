import os 
from string import Template

print("Processing")
directory ='images'
date = "2020-10-16-"
with open('painting_page.txt', 'r') as f:
    template = Template(f.read())

    for entry in os.scandir(directory):
        if (entry.path.endswith(".jpg") and entry.is_file()):
            title = entry.name.split(".")[0]
            d = {'title':title,
                      'key':'value',

                      'folder':directory}
            result = template.substitute(d)
            outputfilename = date + title.replace(" ", "-") + ".md"
            text_file = open("out/" +outputfilename, "w")
            n = text_file.write(result)
            text_file.close()
