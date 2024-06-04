import re
import sys


def readFile(filename):
    with open(filename, "r") as file:
        return file.read()
    
def writeFile(filename, data):
    with open(filename, "w") as file:
        file.write(data)

def fromIsoToBrazilianDate(date_match):
    return f"{date_match.group('day')}/{date_match.group('month')}/{date_match.group('year')}"

if __name__ == "__main__":

    try:
        filename = sys.argv[1]
        output_filename = sys.argv[2]
    except IndexError:
        print("No arguments provided, using default filenames")
        filename = "input-example.csv"
        output_filename = "output-example.csv"
    
    data = readFile(filename)

    iso_date_format_rgx = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
    data = re.sub(iso_date_format_rgx, fromIsoToBrazilianDate, data)

    writeFile(output_filename, data)