
class Scanner:

    filename = "example.md"

    def __init__(self, filepath):
        self.filename = filepath
        return

    def scan(self):
        file = open(file=self.filename, mode='r')
        text = file.read()
        file.close()
        return text
      
    def save(self, outputfile, output):
        file = open(file=outputfile, mode='w')
        file.write(output)
        file.close()
        return

