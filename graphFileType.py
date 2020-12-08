#This function is to get the foemat in which graps have to be saved.

def getFormat(x):
    # x is a boolean
    # if x is true getFormat() wii ask format.
    # if x is false getFormat() will simply return pdf format.
    # functions returns a string. For example ".pdf"
    if(x):
        n = int(input("In which format you want graphs to be saved:\n1 -> PDF\n2 -> PNG\nEnter an integer > "))
        if(n==2):
            return '.png'
        return '.pdf'
    else:
        return '.pdf'


if __name__ == "__main__" :
    print(getFormat(False))
    print(getFormat(True))