import datetime

#Return current date and time
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Return date in specified format
exam_st_date = (11, 12, 2014)
print("The exam will start on : %i / %i / %i") %exam_st_date