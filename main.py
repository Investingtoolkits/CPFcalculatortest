# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pywebio.input import *
from pywebio.output import *
import pandas as pd
import os

age = input("How old are you?", type=NUMBER)
put_text('Age = %r' % age)

yearsto55 = 55 - age
# 'Years to 55 = ' is the hard text to print out. $r is the input variable i receive to print out.
# so im printing out the calculated number of yearsto55.
put_text('Years to 55 = %r' % yearsto55)

targetyear = 2022 + yearsto55
put_text('Target Year = %r' %targetyear)

pd.set_option('display.max_rows', None)

list_FRS = [(2016,161000),
            (2017,166000),
            (2018,171000)]
df_fixed = pd.DataFrame(list_FRS, columns=["Year","FRS"])

#test printing out the table
#print(df_fixed)

#try to use the append function to add to the table above
x =2018

new_row = {"Year": x+1,"FRS":186000 }
df_fixed=df_fixed.append(new_row,ignore_index=True)
#print(df_fixed)

#this will print out 2019. i want to use this in the above formula.
#Sprint(df_fixed.loc[3,"Year"])

#now with this formula i can take the year from the previous table and increase by one, means i can also take the FRS and multiply by a %
new_row = {"Year": (df_fixed.loc[3,"Year"])+1,"FRS":192000 }
df_fixed=df_fixed.append(new_row,ignore_index=True)
#print(df_fixed)

#next is how to get the last number from the table. function to get number of rows.
#then a for loop to create new rows

#output is the number of rows in the table
length = len(df_fixed)
#print(length)

test_row = {"Year": (df_fixed.loc[length -1,"Year"])+1,"FRS": (df_fixed.loc[length -1,"FRS"])*1.035}

#how to use pandas.concat (append function will be remove in future)
df_fixed=df_fixed.append(test_row,ignore_index=True)
#print(df_fixed)

## loop 30 times, each time take the last row in the table
# increment of 1 to the year and take the last number in FRS x by 1.035, i.e 3.5%
# then append this row to dp_fixed. then it will loop again. now the length of table will be increase by 1.

for i in range(0, 100):
    length = len(df_fixed)
    test_row = {"Year": (df_fixed.loc[length -1,"Year"])+1,"FRS": (df_fixed.loc[length -1,"FRS"])*1.035}
    df_fixed = df_fixed.append(test_row, ignore_index=True)

#how to round up to interger or nearest 100 and the year to no decimal, use round but there is still a trailing.0 -kiv
#Number of decimal places to round to (default: 0). If decimals is negative, it specifies the number of positions to the left of the decimal point.
df_fixed['FRS']=df_fixed['FRS'].round(decimals=-2)
df_fixed['Year']=df_fixed['Year'].round(decimals=0)
#print(df_fixed)

#add brs and ers column
df_fixed['BRS']= df_fixed['FRS'] / 2
df_fixed['ERS']= df_fixed['FRS'] / 2 * 3
#reorder the columns, .astype(int) is to print all the numbers in integer,no decimal, previously all ends with .0)
df_fixed=df_fixed[['Year','BRS','FRS','ERS']].astype(int)

#basically from top to this point, i just copy from my original script, change the print function to put function (i.e display for pywebio)
put_html(df_fixed.to_html(border=0))

#returns the row at age 55.
put_text('Year and Retirement Sums when you are 55')

put_html(df_fixed.loc[df_fixed['Year'] == targetyear].to_html(border=0))

#when i keep this print line here, the program still works, just that now it is displayed in this IDE console
#print(df_fixed.loc[df_fixed['Year'] == targetyear])

#var port = process.env.PORT || 5000;
#app.listen(process.env.PORT || 3000, function(){
#  console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
#});
if _ _name_ _=="_ _main_ _":
            port= int(os.environ.get("PORT", 5000))
            app.run(host="0.0.0.0",port =port)
