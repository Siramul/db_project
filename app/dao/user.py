class UserDAO:
    def __init__(self):
        u1 = [1, 'Joe', 'Amador', '7879388245', 'joe.martin@upr.edu', 'joe_martin', 'password']
        u2 = [2, 'Diego', 'Amador', '7872349283', 'diego.amador@upr.edu', 'Diego_Amador', 'password']
        u3 = [3, 'Manuel', 'Martinez', '7874628792', 'manuel.martinez@upr.edu', 'manuel_martinez', 'password']
        u4 = [4, 'Luis', 'Santiago', '7877658935', 'luis.santiago@upr.edu', 'luis_santiago', 'password']

        self.data = []
        self.data.append(u1)
        self.data.append(u2)
        self.data.append(u3)
        self.data.append(u4)

    def get_all_users(self):
        return self.data

    def get_user_by_uid(self, u_id):
        for r in self.data:
            if u_id == r[0]:
                return r
        return None

    def get_user_by_fname(self, fname):
        for r in self.data:
            if fname == r[1]:
                return r
        return None

    def get_user_by_lname(self, lname):
        for r in self.data:
            if lname == r[2]:
                return r
        return None

    def get_user_by_phone(self, phone):
        for r in self.data:
            if phone == r[3]:
                return r
        return None

    def get_user_by_email(self, email):
        for r in self.data:
            if email == r[4]:
                return r
        return None

    def get_user_by_username(self, username):
        for r in self.data:
            if username == r[5]:
                return r
        return None

    def get_user_by_password(self, password):
        for r in self.data:
            if password == r[6]:
                return r
        return None

