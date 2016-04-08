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
          
  The class above is used for holidays with a set date on the calender, like Christmas or Halloween. 
  
  MORE TO WRITE.
