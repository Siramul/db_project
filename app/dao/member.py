class MemberDAO:
    def __init__(self):
        c1 = [1, 2, '1, 2']
        c2 = [1, 3, '1, 3']
        c3 = [1, 4, '1, 4']
        c4 = [2, 1, '2, 1']
        c5 = [2, 3, '2, 3']
        c6 = [2, 4, '2, 4']
        c7 = [3, 1, '3, 1']
        c8 = [3, 2, '3, 2']
        c9 = [3, 4, '3, 4']
        c10= [4, 1, '4, 1']


        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)
        self.data.append(c5)
        self.data.append(c6)
        self.data.append(c7)
        self.data.append(c8)
        self.data.append(c9)
        self.data.append(c10)

    def get_all_members(self):
            return self.data
