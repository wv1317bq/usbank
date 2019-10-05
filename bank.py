
from datetime import datetime, date
from dateutil.parser import parse
import pandas as pd
import time


bill = {}

d0 = "11-02-2019"
d1 = "10-10-2019"
d2 = "12-10-2019"


a_datetime = datetime.strptime("11-10-2019", '%d-%m-%Y')
b_datetime = datetime.strptime("15-10-2019", '%d-%m-%Y')
c_datetime = datetime.strptime("12-10-2019", '%d-%m-%Y')

bill["date"] = [a_datetime, b_datetime, c_datetime]
bill["card"] = ["discover", "firefly", "usbank"]
bill["amount"] = [10.23, 45.00, 19.00]


CurrentDate = datetime.today();
##dateTimeDifference = bill["date"][0] - CurrentDate;

for i in (0,1,2):
    print("########################################")
    ##dateTimeDifference =  - CurrentDate;
    for billkey, billvalue in bill.items():
        if billkey == "date":
            dateTimeDifference = (billvalue[i] - CurrentDate).days;
            if dateTimeDifference < 7:
                print("Bill is due in less than 5 days. Please make the payment soon")
            else:
                print("Due date in ", dateTimeDifference, " days");
            time.sleep(1)
        else:
            print(str(billkey) + ': ' + str(billvalue[i]))
            time.sleep(1)


    time.sleep(2)
print("########################################")


## print(dateTimeDifference)







