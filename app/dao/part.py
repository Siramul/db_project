class PartDAO:
    def __init__(self):
        P1 = [122, 'Bolt', 0.5, 'blue']
        P2 = [74, 'Wire', 1.5, 'silver']
        P3 = [849, 'wood', 5, 'brow']
        P4 = [757, 'pvc', 5, 'blue']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllParts(self):
        # P1 = [122, 'Bolt', 0.5, 'blue']
        # P2 = [74, 'Wire', 1.5, 'silver']
        # P3 = [849, 'wood', 5, 'brow']
        # result = []
        # result.append(P1)
        # result.append(P2)
        # result.append(P3)
        return self.data

    def getPartById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getSuppliersByPartId(self, id):
        if id == 74:
            return [['123', 'Home Depot']]
        elif id == 122:
            T = []
            T.append(['123', 'Home Depot'])
            T.append(['456', 'National'])
            return T
        else:
            return []

    def searchByColor(self, color):
        result = []
        for r in self.data:
            if color == r[3]:
                result.append(r)
        return result
