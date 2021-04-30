#사용자로부터 이름,전화번호,성별 입력 받은 후 출력하는 프로그램

class Info:
    def __init__(self, name, sex, number):
        self.name = name
        self.sex = sex
        self.number = number

    def getSex(self):
        return self.sex

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def print(self):
        print("이름은", self.name, ", 전화번호는", self.number, ", 성별은", self.sex, "입니다.")


u_l = []
while(1):
    for u in u_l:
        u.print()
    print()
    name = input("이름을 입력하세요 : ")
    if (name == "그만"):
        break
    number = input("전화번호를 입력하세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if (sex != "male" and sex != "female"):
        sex = "unknown"
    u_l.append(Info(name, sex, number)) 


for u in u_l:
    u.print()


