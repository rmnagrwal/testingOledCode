"""

@author: Raman Agarwal
        Electrical Engineering Student
        Indian Institute of Technology, Delhi
"""

'''
This file is to ask user if he/she don't want to proceed in the natural way, 
i.e. if area, divice number and conversion factor are to be given manually.
Naturally if this code is not executed, area, device number and conversion factor 
are automatically extracted from the file name.
'''



def change(area1, devNo1, cf1, manual_input):
    """
    This function ask if user want to manuall give values of
    device area, device number and power conversion factor.
    If user selects no, simply the values passed to the function are returned.
    """
    
    toExecute=True
    #If you don't want to execute this, just make toExecute = False.

    askDeviceNumber = True
    # If you don't want to ask device number,
    #  make askDeviceNumber=False, 
    # it will always set device number to 0.
    
    if toExecute and manual_input:
        starLine="**********************************************************************************************"
        print(starLine+starLine)
        choice = str(input("Do you want to manually enter device area, device number and conversion factor? <Enter Y for Yes or N for No> "))
        if choice == "Y" or choice=="y" or choice == "yes" or choice == "Yes" or choice == "YES":
            area2 = float(input("Enter device area in cm^2> "))
            if askDeviceNumber:
                deviceNumber =  int(input("Enter the device number > "))
            else:
                deviceNumber=0
            conversionFactor = float(input("Enter conversion factor > "))
            return area2, deviceNumber, conversionFactor
    return area1, devNo1, cf1


#print(change(0.254,8,458))


