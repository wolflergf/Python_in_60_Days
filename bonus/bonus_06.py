contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced", "The slicing process was well presented."]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open("./bonus/files/{}".format(filename), "w")
    file.write(content)
