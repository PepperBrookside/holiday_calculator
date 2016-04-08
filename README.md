# holiday_calculator
This a relatively simple program that asks the user for a year. Based on the year given for input, the program will print out the day of the week and date of the month of each holiday listed inside the code.

# How it works
  There are two main foundations behind the inner workings of this program, one is the datetime module which helps us create the date objects we need for each holiday listed inside for every year in the Gregorian calender between 1 and 9999. The second is our two main holiday classes we use to find each date, based on data provided by each object. The data typed into the arguments of each argument are used in a datetime date function to create an idealized object which we then use to run in a function to print out the weekday, the month and the day. (e.g. "Christmas: Sunday, December 25")
  
# Example code: Holiday1
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
          
  The class above is used for holidays with a set date on the calender, like Christmas or Halloween. the arguments used are name, which is entered as a string, month, date and year, however are entered as integers. If we created an object for Christmas 2016, it would be entered as Holiday1("Christmas", 12, 25, 2016). Using the months and wkdays[short for weekdays] lists created earlier in the code, if we called the listing function in our object it would print out "Christmas: Sunday, December 25"
  
# Example code: Holiday2
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
            
  The Holiday2 class is used for holidays with a movable date based on a day of the week, such as Labor Day or Thanksgiving. It works similar to the our first class, but uses a different set of arguments, and uses an extra set of instructions for our holiday function. The wkday and wknum arguments are for weekday and week number respectively, wkday should be an integer that is equal to the position on of the wkdays list. (Monday = 0, Thursday = 3, Sunday = 6]. Since Thanksgiving is held on the fourth Thursday of November, if we wanted to create an object based on Thanksgiving 2016 we would write Holiday2("Thanksgiving", 11, 3, 4, 2016). With this data, the holiday function runs through all the dates in the fourth week in November (22-28), when it finds one that is on a Thursday, the function returns the date. The listing funtion then prints "Thanksgiving: Thursday, November 24"
  
# Why This Was Made

  I'm a beginning programmer, and thought this would be a good exercise in understanding class-based and date-based objects. This also was based on a thought I had about calculating the date for Easter, as well as some past thoughts about some Holidays ("When will Halloween be held on the weekend again?", "How early will Memorial Day be this year?"). It's just a simple little project to get my hands dirty.

# Contribution Requests
  With the exception of Easter, all the holidays listed in the code are easy to calculate, since we have a 10 Millenia long Gregorian calander on hand. What I would like is a way to convert dates from the Hebrew calender to the Gregorian calander, so we can list the dates for Jewish Holidays (First Night of Hanukkah, Passover, Yom Kippur). Any users are free to add any other Holidays of signifigance as they so please. 
  
# Attribution: IanTaylorEasterJscr function
  The IanTaylorEasterJscr function included in this program is used to find the date for Easter, it was found on the Wikipedia page for Compututs. The function is credited to http://www.merlyn.demon.co.uk/estralgs.txt, however that address is no longer active.
  
# License: MIT

Copyright (c) 2016 Zack Parr

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
