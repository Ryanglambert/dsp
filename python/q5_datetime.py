# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
from datetime import datetime as dt
print dt.strptime(date_stop, "%m-%d-%Y").toordinal() - dt.strptime(date_start, "%m-%d-%Y").toordinal()

####b)  
date_start = '12312013'  
date_stop = '05282015'  
print dt.strptime(date_stop, "%m%d%Y").toordinal() - dt.strptime(date_start, "%m%d%Y").toordinal()

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
print dt.strptime(date_stop, "%d-%b-%Y").toordinal() - dt.strptime(date_start, "%d-%b-%Y").toordinal()


