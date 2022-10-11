import calendar
import datetime


#You are given a date. Your task is to find what the day is on that date.
#constraints: 2000 < year < 3000
#Input Format: A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#Output Format: Output the correct day in capital letters.
#Sample Input: 08 05 2015
#Sample Output: WEDNESDAY
#Explanation: The day on August 5th 2015 was WEDNESDAY.
def findDay(date):
    n = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[n])

if __name__ == '__main__':
    date = input("Enter a date in MM DD YYYY format: ")
    print (calendar.TextCalendar(firstweekday=7).formatyear(int(date[6:10])))
    print(findDay(date))    