import os, sys


with open(os.path.join(sys.path[0], "my_file.txt"), "w") as f:
    f.write("New text. ")

    f.close()



    