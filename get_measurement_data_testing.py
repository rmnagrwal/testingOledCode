import pandas as pd
from get_connector import get_connector
from read_csv1 import read_csv1
from read_txt1 import read_txt1
import glob
import os
import platform


# platform_type1 = platform.system()
#This to to check wether the system is windows or lunix so that the connector used in specifying file paths can be choosed appropriately.
connector1 = get_connector()
connector_length = len(connector1)
# if platform_type1 == 'Windows':
#     connector1= '/'
#     connector_length = 1
# elif platform_type1 == 'Linux':
#     connector1= '/'
#     connector_length = 1


def get_measurement_data(csv_path,txt_path):

    column_name_for_biasing_data_table = ['%Vdevice','IdeviceAVG', 'IdeviceSTD' ,'IdetectorAVG' , 'IdetectorSTD']
    column_name_for_wavelength_counts_table = ['wavelength', 'counts']

    def get_header(csv_file, keyword1 = 'FMDL'):
        #get_header is a function to to search first occurence of 
        #keyword1 and considering the very next line as the 
        #header for a table 
        #returns line number of header line. 
        
        file1 = open(csv_file,'r')
        lines1 = file1.readlines()
        file1.close()
        j=0
        while j<len(lines1) :
            #print(lines1[j])
            #print(lines1[j][1:5])
            if lines1[j][1:5]=='FMDL':
                break
            else:
                j+=1
            #print(j+1)
        return j+1



    # def get_file_locs(directory):

    #     ##returns the file path for latest csv and txt files
    #     list_of_csv_files = glob.glob( directory+'' + connector1 + '*.csv') # * means all if need specific format then *.csv
    #     #print(list_of_csv_files)
    #     i=0
    #     while i<len(list_of_csv_files):
    #         filename1 = list_of_csv_files[i][( len(directory)+connector_length-1 ) :]
    #         #print(filename1[0:10])
    #         if len(filename1) >10:
    #             if filename1[0:10]=='processed-':
    #                 list_of_csv_files.remove(list_of_csv_files[i])
    #             else:
    #                 i=i+1
    #         else:
    #             i=i+1
    #     #print(list_of_csv_files)


    #     latest_csv_file = max(list_of_csv_files, key=os.path.getctime)
    #     #print (latest_csv_file)

    #     list_of_txt_files = glob.glob( directory+'' + connector1 + '*.txt') # * means all if need specific format then *.csv
    #     i=0
    #     while i<len(list_of_txt_files):
    #         filename1 = list_of_txt_files[i][( len(directory)+connector_length-1 ) :]
    #         if len(filename1) >10:
    #             if filename1[0:10]=='processed-':
    #                 list_of_txt_files.remove(list_of_txt_files[i])
    #             else:
    #                 i=i+1
    #         else:
    #             i=i+1
        
    #     latest_txt_file = max(list_of_txt_files, key=os.path.getctime)
    #     #print (latest_txt_file)
        

    #     return (latest_csv_file, latest_txt_file)

    '''def get_file_info(filepath1):


        return (area1, div_no, s_name1)
    '''

    '''def get_file_locs(directory):
        
        return ('F:' + connector1 + 'OLED calculations' + connector1 + 'jan17' + connector1 + 'new_program' + connector1 + 'test_input' + connector1 + 'data1.csv' , 'F:' + connector1 + 'OLED calculations' + connector1 + 'jan17' + connector1 + 'new_program' + connector1 + 'test_input' + connector1 + 'nineVoltage.txt' )

    '''
    def get_file_info(filepath1, directory ):
        div_area_lookup_table = {1:0.1521, 2:0.0707, 3:0.0452, 4:0.0707, 5:0.0452, 6:0.0707, 7:0.1521, 8:0.1521, 9:4.4 }

        ##returns device info from the file name i.e. device area, device number and starting name

        '''j = len(filepath1)-1
        print(filepath1)
        while j >= 0 :
            if filepath1[j-1:j+1] == '\':
                filename1 = filepath1[j+1:-4]
                break
            j=j+1'''

        for i in range(len(csv_path)-connector_length,0,-1):
            if csv_path[i:i+connector_length] == connector1:
                filename1=csv_path[i+connector_length:-4]
                break
        
        # filename1 = filepath1[ ( len(directory)+connector_length ) : -4]
        # print(filename1)
        for i in range(len(filename1)):
            if filename1[i:i+2] == '-d':
                #print('ok')
                #print(filename1, i)
                div_no = int(filename1[i+2] )
                #print(div_no)
        s_name1 = filename1
        #s_name1 = 'processed-'+s_name1 # we no longer want 'propcessed' in file names
        div_area= div_area_lookup_table[div_no] #in cm2        


        return ( div_area, div_no, s_name1)

    
    ###this to get the file path for latest csv and txt files
    # biasing_file_path, spectrum_file_path = get_file_locs(directory)
    biasing_file_path, spectrum_file_path = csv_path, txt_path

    directory=""
    for i in range(len(csv_path)-connector_length,0,-1):
        if csv_path[i:i+connector_length] == connector1:
            directory=csv_path[:i-1]
            break
    # print("-----------------------------------------------------------------------------------------")
    # print('csv_path '+csv_path )
    # print('directory ' +directory)
    # print("-----------------------------------------------------------------------------------------")



    ###tis is to get device info from the file name i.e. device area, device number and starting name
    (area1, div_no, s_name1) =  get_file_info(biasing_file_path, directory)

    ###to get biasing data in form of pandas datafrme
    biasing_data_table = read_csv1(filepath1=biasing_file_path, header1= get_header(biasing_file_path) , datatype1=float, column_name= column_name_for_biasing_data_table )
    #print(biasing_data_table)

    ###this is to get wavelength counts data in pandas dataframe
    wavelength_counts_table = read_txt1(filepath=spectrum_file_path, column_name= column_name_for_wavelength_counts_table)

    return (biasing_data_table, wavelength_counts_table, area1, div_no, s_name1 )