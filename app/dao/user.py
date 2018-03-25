class UserDAO:
    def __init__(self):
        U1 = [1,'Joe', 'Martin','7879388245', 'joe.martin@upr.edu','joe_martin','password']
        U2 = [2,'Diego', 'Amador','7872349283', 'diego.amador@upr.edu','Diego_Amador','password']
        U3 = [3,'Manuel', 'Martinez','7874628792', 'manuel.martinez@upr.edu','manuel_martinez','password']
        U4 = [4,'Luis', 'Santiago','7877658935', 'luis.santiago@upr.edu','luis_santiago','password']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def get_all_users(self):
        return self.data

    def get_user_by_id(self, id):
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