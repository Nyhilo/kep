# Module imports
from sys import argv as args
from datetime import datetime

# Local imports

# Parsing objects0
class file:
    _date_format = "%Y-%m-%d %H:%M:%S"

    def __init__(title,
                 date_created=None,
                 date_modified=None,
                 tags=[],
                 files=[]):
        self.title = title
        self.date_created = date_created
        self.date_modified = date_modified
        self.tags = tags
        self.files = files

    def get_default_header(self):
        header = ""

        if self.title:
            header += f"Title: {title}\n"

        if self.date_created is not None:
            d = date_created.strftime(self._date_format)
            header += f"Date Created: {d}\n"

        if self.date_modified is not None:
            d = date_modified.strftime(self._date_format)
            header += f"Date Modified: {d}\n"

        if len(self.tags) > 0:
            t = " ".join(self.tags)
            header += f"Tags: {t}\n"

        if len(self.files) > 0:
            t = " ".join(self.files)
            header += f"Files: {t}\n"

        header += "-----\n\n"

        return header


class Kep:
    @classmethod
    def list(self, subfolder="./"):
        pass

    @classmethod
    def open(self, assetname, location):
        pass

    @classmethod
    def read(self, location, assetname=None):
        if assetname is None:
            assetname = location.split('/')[-1]
            location = location.split('/')[:-1].join('/')



if __name__ == '__main__':

    # Equivalent to `kep list`
    if len(args) == 1:
        Kep.list()

    # Single argument tasks
    if len(args) == 2:
        if args[1].lower() == "list":
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
