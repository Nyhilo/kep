# Module imports
from sys import argv as args

# Local imports


# Parsing objects
class Kep:
    @classmethod
    def list(self, subfolder = "./"):
        pass

    @classmethod
    def open(self, assetname, location):
        pass

    @classmethod
    def read(self, location, assetname = null):
        if assetname == null:
            assetname = location.split('/').[-1]
            location = location.split('/')[:-1].join('/')



if __name__ == '__main__':

    # Equivalent to `kep list`
    if len(args) == 1:
        Kep.list()

    # Single argument tasks
    if len(args) == 2:
        if args[1].lower() == "list"
            Kep.list()

        #...

        # Defaults to kep open args[1] ./
        Kep.Open(args[1], "./")

    # Two argument tasks
    if len(args) == 3:
        # Built-in tasks
        if args[1].lower() == "list":
            Kep.list(args[2])

        if args[1].lower() == "read":
            Kep.read(args[2])

        #...

        # Default to kep open args[1] args[2]
        Kep.Open(args[1], args[2])
