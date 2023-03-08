import sys


def form(fileArg, typeArg):
    print("File: " + fileArg)
    try:
        f = open(fileArg, "r+")
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
            lines[i] = '{"name": "' + lines[i] + '"'
            if typeArg != None:
                lines[i] = lines[i] + ', "type": "' + typeArg + '"},'
            else:
                lines[i] = lines[i] + "},"
            return print(lines[i])
    except IOError:
        print("File not found")
        sys.exit(2)
