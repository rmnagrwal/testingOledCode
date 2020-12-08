from matplotlib import pyplot as plt


import platform


platform_type1 = platform.system()
#This to to check wether the system is windows or lunix so that the connector used in specifying file paths can be choosed appropriately.
if platform_type1 == 'Windows':
    connector1= '/' #This is the connector used in windows
elif platform_type1 == 'Linux':
    connector1= '/' #this connector is used in lunix platform




def plotlineargraph(outGraphsfolder,format1,x1,y1, x1label='',y1label='',title1='Untitled',s_name ='',x2='not_given',y2='not_given',y2label='',y1scale=-1,y2scale=-1,  y1err=None):
    #this fuction is to plot linear graphs given x values and y values.
    #this funcion can also plot error bars
    plt.errorbar(x1,y1, yerr=y1err, ecolor='red' , barsabove=True)
    plt.xlabel(x1label)
    plt.ylabel(y1label)
    #plt.title(title)
    #plt.legend()
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.tight_layout()
    #plt.ticklabel_format(style='plain')
    # print('outGraphsfolder ' +outGraphsfolder)
    # print('connector1 '+ connector1)
    # print('s_name '+ s_name)
    # print('title1 '+title1)
    plt.savefig(outGraphsfolder+'' + connector1 + ''+s_name+'_'+title1+format1)
    plt.close()


def plotlineargraph2(outGraphsfolder,format1,x1,y1,x1label='',y1label='',title1='Untitled',s_name ='',x2='not_given',y2='not_given',y2label='',y1scale=-1,y2scale=-1):
    #this function is to plot two liner graphs in one fig for comparison.
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x1, y1, 'g-')
    ax2.plot(x2, y2, 'b-')
    if y1scale!=-1:
        ax1.set_yscale(y1scale)
    if y2scale!=-1:
        ax2.set_yscale(y2scale)

    ax1.set_xlabel(x1label)
    ax1.set_ylabel(y1label, color='g')
    ax2.set_ylabel(y2label, color='b')
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.tight_layout()
    #plt.ticklabel_format(style='plain')
    plt.savefig(outGraphsfolder+'' + connector1 + ''+s_name+'_'+title1+format1)
    plt.close()                                                                                   