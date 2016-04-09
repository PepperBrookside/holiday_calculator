import datetime

wkdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

# Holiday1 for set dates (e.g. Halloween or Christmas)
class Holiday1(object):
    def __init__(self, name, month, date, year):
        self.name = name
        self.month = month
        self.date = date
        self.year = year

    def holiday(self):
        return datetime.date(self.year, self.month, self.date)

    def listing(self):
        w = wkdays[self.holiday().weekday()]
        m = months[self.holiday().month - 1]
        d = self.date
        print("{}: {}, {} {} \n".format(self.name, w, m, d))

# Holiday2 for movable dates (e.g. Labor Day, Thanksgiving)
class Holiday2(object):
    def __init__(self, name, month, wkday, wknum, year):
        # Monday = 0, Thursday = 3, Sunday = 6
        self.name = name
        self.month = month
        self.wkday = wkday
        self.wknum = wknum
        self.year = year

    def holiday(self):
        dates = [x for x in range(1 + (self.wknum - 1)*7, 8 + (self.wknum - 1)*7)]
        for y in dates:
            if datetime.date(self.year, self.month, y).weekday() == self.wkday:
                return datetime.date(self.year, self.month, y)
            else:
                pass

    def listing(self):
        w = wkdays[self.holiday().weekday()]
        m = months[self.holiday().month - 1]
        d = self.holiday().day
        print("{}: {}, {} {} \n".format(self.name, w, m, d))

# This function was found on the Wikipedia page for Computus and is used to find the date for Easter
# The function is credited to http://www.merlyn.demon.co.uk/estralgs.txt, however that address is no longer active
def IanTaylorEasterJscr(year):
    a = year % 19
    b = year >> 2
    c = b // 25 + 1
    d = (c * 3) >> 2
    e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
    e += (29578 - a - e * 32) >> 10
    e -= ((year % 7) + b - d + e + 2) % 7
    d = e >> 5
    day = e - d * 31
    month = d + 3
    m = months[month - 1]
    print("Easter: Sunday, {} {} \n".format(m, day))

# Memorial day is the last Monday of May
def mem(year):
    mem1 = Holiday2("Memorial Day", 5, 0, 4, year)
    mem2 = mem1.holiday()
    mem3 = mem2.day
    if mem3 < 25:
        mem3 += 7
        mem1.listing()
    else:
        mem1.listing()

def operation():
    year = input("Please enter a year. ")
    year = int(year)
    nyd = Holiday1("New Year's Day", 1, 1, year)
    nyd.listing()
    mlk = Holiday2("Martin Luther King, Jr. Day", 1, 0, 3, year)
    mlk.listing()
    grn = Holiday1("Groundhog Day", 2, 2, year)
    grn.listing()
    val = Holiday1("St. Valentine's Day", 2, 14, year)
    val.listing()
    pres = Holiday2("President's Day", 2, 0, 3, year)
    pres.listing()
    zp = Holiday1("Zack's Birthday", 3, 9, year)
    zp.listing()
    stp = Holiday1("St. Patrick's Day", 3, 17, year)
    stp.listing()
    IanTaylorEasterJscr(year)
    af = Holiday1("April Fool's Day", 4, 1, year)
    af.listing()
    fcb = Holiday2("Free Comic Book Day", 5, 5, 1, year)
    fcb.listing()
    cdm = Holiday1("Cinco de Mayo", 5, 5, year)
    cdm.listing()
    mom = Holiday2("Mother's Day", 5, 6, 2, year)
    mom.listing()
    mem(year)
    jim = Holiday1("Jimmy's Birthday", 6, 5, year)
    jim.listing()
    dad = Holiday2("Father's Day", 6, 6, 3, year)
    dad.listing()
    ind = Holiday1("Independence Day", 7, 4, year)
    ind.listing()
    lab = Holiday2("Labor Day", 9, 0, 1, year)
    lab.listing()
    col = Holiday2("Columbus Day", 10, 0, 2, year)
    col.listing()
    hal = Holiday1("Halloween", 10, 31, year)
    hal.listing()
    vet = Holiday1("Veteran's Day", 11, 11, year)
    vet.listing()
    tg = Holiday2("Thanksgiving", 11, 3, 4, year)
    tg.listing()
    christmas = Holiday1("Christmas", 12, 25, year)
    christmas.listing()

operation()