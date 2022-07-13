class Data:
    def __init__(self, s):
        self.d = s[0:2]
        self.m = s[3:5]
        self.a = s[6:10]

    def data(self):
        return self.d, self.m, self.a

class Periodo:
    def __init__(self, s):
        di = Data(s[0:10])
        df = Data(s[13:24])
        self.di, self.mi, self.ai = di.data()
        self.df, self.mf, self.af = df.data()

    def periodo(self):
        return self.di, self.mi, self.ai, self.df, self.mf, self.af

    def data_inicial(self):
        return f'{self.ai}-{self.mi}-{self.di}'

    def data_final(self):
        return f'{self.af}-{self.mf}-{self.df}'

def main():
    d = Data('08-05-2002')
    p = Periodo('08/05/2002 - 09/06/2002')
    # d, m, a = d.data()
    # print(d)
    # print(m)
    # print(a)
    # d1, m1, a1, d2, m2, a2 = p.periodo()
    # print(d1, m1, a1, d2, m2, a2)
    print(p.data_inicial())

if __name__ == '__main__':
    main()