def readFile(filename):
    with open(filename, "r") as file:
        return file.read()
    
def writeFile(filename, data):
    with open(filename, "w") as file:
        file.write(data)

if __name__ == "__main__":
    data = readFile("input.csv")
    print("teste", data)