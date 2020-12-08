#importing datetime module for now
import datetime
# for timezone()  
import pytz

def get_date_time():
    def convert(num):
        name=str(num)
        if(len(name)==1):
            name='0'+name
        return name
    time_zone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(time_zone)  
        
    date_time_str = convert(current_time.year)+convert(current_time.month)\
        +convert(current_time.day)+convert(current_time.hour)\
            +convert(current_time.minute)+convert(current_time.second)
    # Printing attributes of now().  
    # print ("The attributes of now() are : ")  
        
    # print ("Year : ", end = "")  
    # print (current_time.year)  
        
    # print ("Month : ", end = "")  
    # print (current_time.month)  
        
    # print ("Day : ", end = "")  
    # print (current_time.day)  
        
    # print ("Hour : ", end = "")  
    # print (current_time.hour)  
        
    # print ("Minute : ", end = "")  
    # print (current_time.minute)  
        
    # print ("Second : ", end = "")  
    # print (current_time.second)  
        
    # print ("Microsecond : ", end = "")  
    # print (current_time.microsecond)  
    return date_time_str

# print(get_date_time())