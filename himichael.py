def main():
    print(suckcock())

    my_dick = penis(10)
    print('me:', my_dick.get_cock())

    your_moms_dick = penis(1)
    print('your mom:', your_moms_dick.get_cock())

def suckcock():
    return 'cum'

class penis:
    def __init__(self, length):
        self.length = length
        self.hairy = True

    def shave(self):
        self.hairy = False

    def bush(self):
        self.hairy = True

    def get_cock(self):
        dick = '8'
        for i in range(self.length):
            dick += '='
        dick += 'D'

        return dick

if __name__ == '__main__':
    main()