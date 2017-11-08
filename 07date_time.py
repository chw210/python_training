from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today();
    print "Today's date is ", today
    print "Date Components: ", today.day, today.month, today.year
    print "Today's Weekday #: ", today.weekday()
    #today = datetime.now()
    #print " The current time is ", today
    wd = today.weekday()
    days = ["monday", "tuesday", "wednesday"]
    print "Today is day number %d" % wd
    print "which is a " + days[wd]

if __name__ == "__main__":
    main()