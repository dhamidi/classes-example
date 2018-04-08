import shelve

class Database:
    def __init__(self, filename):
        """Create a new database that stores its data in the file named filename.
        """
        self.filename = filename

    def add_item(self, item):
        """Adds item to this database.

        Items needs to be dictionary.
        """

        if type(item) != dict:
            raise TypeError("item needs to be a dictionary, got %s" % repr(item))

        with shelve.open(self.filename) as db:
            all_items = db.get('items', [])
            all_items.append(item)
            db['items'] = all_items

    def list_items(self):
        with shelve.open(self.filename) as db:
            return db.get('items', [])
