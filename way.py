class Way:
    def __init__(self, id, name, connected_nodes):
        self.id = id
        self.name = name
        self.connected_nodes = connected_nodes

    def __repr__(self):
        return f"Way({self.name})"

    def __str__(self):
        return str(self.__dict__)


