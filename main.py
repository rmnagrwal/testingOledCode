#the required libraries are 'matplotlib', 'pandas', 'os', 'glob'


from read_csv1 import read_csv1
from read_txt1 import read_txt1
from get_connector import get_connector
from get_measurement_data import get_measurement_data
from get_calculated_data import get_calculated_data
from plotgraph1 import plotlineargraph
from plotgraph1 import plotlineargraph2
import sys
import platform

'''
read_csv1 is a function to read csv files
read_txt1 is a function to read space saaperated text files
get_measurement_data takes a directory as input. This is the directory where the two required measurement files(1. file containing biasing data i.e. biasing voltage, current and detector current with their respective errors 2. the wavelength-counts file from the detector) are saved.
get_measurement_data will scan the directories and select the latest csv file for biasing data and latest txt file for wavelength-counts
get_calculated_data is a function that takes the measurement data and gives back the required calculated data
plotlineargraph1 and plotlineargraph2 are functions to plot graphs(line graphs) using matplotlib

'''
dashLine="------------------------------------------------------------------------------------------------------------"
print(dashLine+dashLine)

# platform_type1 = platform.system()
#This to to check wether the system is windows or lunix so that the connector used in specifying file paths can be choosed appropriately.
connector1 = get_connector()
# if platform_type1 == 'Windows':
#     connector1= '\\' #This is the connector used in windows
# elif platform_type1 == 'Linux':
    # connector1= '/' #this connector is used in lunix platform



#reading the two required standard files
conversion_factor_spectrum_table = read_txt1(filepath='standard_data' + connector1 + 'conversion_factor_spectrum_[lmwatt].txt',column_name=['wavelength','conversion_factor'])
responsivity_table = read_txt1(filepath='standard_data' + connector1 + 'responsivity_table.txt', column_name=['wavelength','responsivity'])
#both the files must be saved in a folder named 'standard_data' in the folder containing this code.
#name of the files must also be 1. conversion_factor_spectrum_[lmwatt].txt 2. responsivity_table.txt'(this one is specific for the device we are using)
#both are space saperated txt files



#the input_directory1 is the only required input from command by the program
input_directory1= list(sys.argv)[1]
# while calling the program from command line it shoul be called as : python main.py "input_xyz"
# example : python main.py "C:/Users/Raman Agarwal/OneDrive - IIT Delhi/Github/OledCalculation/test_input"
#here main.py is the pythom code to be run and input_xyz is the input directory path. This input directory path should be passesd while callig to run the program


#calling get_measurement_data.
(biasing_data_table, wavelength_counts_table, area1, div_no, s_name1 ) = get_measurement_data(input_directory1)


#output_directory1 is same as input directory. All processed files would be saved there with the same stating name of the biasing data csv file with a prefix processed
output_directory1 = input_directory1


#calling get_calculated_data
(calculated_data_table, modified_wavelength_counts) = get_calculated_data(biasing_data_table, wavelength_counts_table, conversion_factor_spectrum_table , responsivity_table, area1, div_no)




#ploting the required graphs
plotlineargraph(output_directory1, modified_wavelength_counts['wavelength'],                       modified_wavelength_counts['counts'] ,                  'wavelength[nm]',          'Intensity[arb. units]',            'Electroluminescense(Modified Data)',      s_name1)
plotlineargraph(output_directory1, wavelength_counts_table['wavelength'],                          wavelength_counts_table['counts'] ,                     'wavelength[nm]',          'Intensity[arb. units]',             'Electroluminescense(Raw data)',          s_name1)
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'] ,                  calculated_data_table['Current density (mA/cm2)'] ,      'bias voltage [Volts]',   'current density [mA/cm2]',          'Current Density vs Bias Voltage',        s_name1, y1err= calculated_data_table['Current density error'] )
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'] ,                  calculated_data_table['Luminance [cd/m2]'] ,             'bias voltage [Volts]',   'Luminance [cd/m2]',                 'Luminance vs Bias Voltage',              s_name1, y1err= calculated_data_table['Luminance error'] )
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'].values[2:] ,       calculated_data_table['Luminosity [lm/w]'].values[2:] ,  'bias voltage [Volts]',   'Luminious power efficieny [lm/W]',  'Luminous power efficieny vs bias voltage',s_name1, y1err=calculated_data_table['Luminosity error'].values[2:])
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'].values[2:] ,       calculated_data_table['Quantum Eff.[0-1]'].values[2:],  'bias voltage [Volts]',     'quantum efficiency [0-1]',          'Quantum efficiency vs bias voltage',     s_name1, y1err= calculated_data_table['Quantum Eff.error'].values[2:])
plotlineargraph(output_directory1, calculated_data_table['Current density (mA/cm2)'].values[2:] ,  calculated_data_table['Quantum Eff.[0-1]'].values[2:] , 'current density [mA/cm2]', 'quantum efficiency [0-1]',          'Quantum efficiency vs current density',  s_name1, y1err=calculated_data_table['Quantum Eff.error'].values[2:])
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'].values[2:] ,       calculated_data_table['Current Eff.[cd/A]'].values[2:], 'bias voltage [Volts]',     'Current efficiency [cd/A]',         'Current efficiency vs bias voltage',     s_name1, y1err= calculated_data_table['Current Eff.error'].values[2:])
plotlineargraph(output_directory1, calculated_data_table['Bias Voltage(Volts)'] ,                  calculated_data_table['Radience [mW/m2]'] ,             'bias voltage [Volts]',     'radience [mW/m2]',                  'radience[m2] vs bias voltage',           s_name1, y1err=calculated_data_table['Radience error'] )
plotlineargraph2(output_directory1, conversion_factor_spectrum_table['wavelength'],                conversion_factor_spectrum_table['conversion_factor'] , 'Wavelength[nm]',           'Conversion factor [lm/w]',          'standard and experimental spectrum',     s_name1, modified_wavelength_counts['wavelength'], modified_wavelength_counts['counts'] , 'counts[arb. units]' )
plotlineargraph2(output_directory1, calculated_data_table['Bias Voltage(Volts)'] ,                 calculated_data_table['Current density (mA/cm2)'] ,     'Bias voltage [Volts]',     'current density [mA/cm2]',          'JVLgraph',                              s_name1, calculated_data_table['Bias Voltage(Volts)'] , calculated_data_table['Luminance [cd/m2]'] , 'Luminance [cd/m2]' )
plotlineargraph2(output_directory1, calculated_data_table['Bias Voltage(Volts)'] ,                 calculated_data_table['Current density (mA/cm2)'] ,     'Bias voltage [Volts]',     'current density [mA/cm2] [in log]', 'JVLgraph(log)',                         s_name1, calculated_data_table['Bias Voltage(Volts)'] , calculated_data_table['Luminance [cd/m2]'] , 'Luminance [cd/m2]', 'log' )


#saving the pandas dataframes in csv format
calculated_data_table.to_csv(output_directory1+ connector1 +s_name1+ 'calculated_data_table.csv')
modified_wavelength_counts.to_csv(output_directory1+ connector1 +s_name1+ 'modified_wavelength_counts.csv')

print(dashLine+"Completed!!!!"+dashLine)
