import pandas as pd

from rectangular_devices_change import change

def get_calculated_data(biasing_data_table, wavelength_counts_table, conversion_factor_spectrum_table , responsivity_table, area1, div_no, manual_input = False):


    if div_no==4:
        p_correction_factor=10.15 #calculated correction factor with detector in holder and on top of device is 10.15
    else:
        p_correction_factor=496
    
    area1, div_no, p_correction_factor = change(area1, div_no, p_correction_factor, manual_input )


    Area1=area1/10000 #area in m2
    start_index = 5


    
    nrow_cf_spectrum_table = conversion_factor_spectrum_table.shape[0]
    nrow_biasing_data_table = biasing_data_table.shape[0]
    nrow_wavelength_counts_table = wavelength_counts_table.shape[0]
    
        
    pi=3.14
    qe=6240000000000000 #conveision factor g5
    cons_for_photons_per_w_s = (10**17)/19.87851

    modified_wavelength_counts = pd.DataFrame([[0,0] for i in range( nrow_cf_spectrum_table )], columns = ['wavelength', 'counts'])
    calculated_result = pd.DataFrame(biasing_data_table['%Vdevice'].values, columns = ['Bias Voltage(Volts)'])
    #print(calculated_result)

    j=0
    for i in range(nrow_cf_spectrum_table):
        while wavelength_counts_table['wavelength'].loc[j] < ( conversion_factor_spectrum_table['wavelength'].loc[i]-2.5 ):
            j=j+1
        n_wavelength_entries=0
        while wavelength_counts_table['wavelength'].loc[j] < ( conversion_factor_spectrum_table['wavelength'].loc[i]+2.5 ):
            modified_wavelength_counts['wavelength'].loc[i] += wavelength_counts_table['wavelength'].loc[j]
            modified_wavelength_counts['counts'].loc[i] += wavelength_counts_table['counts'].loc[j]
            j += 1
            n_wavelength_entries += 1

        modified_wavelength_counts['wavelength'].loc[i] = modified_wavelength_counts['wavelength'].loc[i]/n_wavelength_entries
        modified_wavelength_counts['counts'].loc[i] = modified_wavelength_counts['counts'].loc[i]/n_wavelength_entries




    max_wl_index = start_index
    max_intensity=wavelength_counts_table['counts'].loc[start_index]
    for i in range(start_index,nrow_wavelength_counts_table):
        if max_intensity < wavelength_counts_table['counts'].loc[i]:
           max_intensity = wavelength_counts_table['counts'].loc[i]
           max_wl_index = i
    max_wl = wavelength_counts_table['wavelength'].loc[max_wl_index]


    print('maximun intensity wavelength is '+str(max_wl)+'nm')
    j=1
    while max_wl > responsivity_table['wavelength'].loc[j] :
        j=j+1

    max_wl = int( max_wl )
    last_digit=int(str(max_wl)[-1])
    if last_digit==0:
        if max_wl == responsivity_table['wavelength'].loc[j] :
            responsivity = responsivity_table['responsivity'].loc[j]
        else:
            responsivity = responsivity_table['responsivity'].loc[j-1]
    else:
        responsivity = responsivity_table['responsivity'].loc[j-1] + (( responsivity_table['responsivity'].loc[j] - responsivity_table['responsivity'].loc[j-1] )/( responsivity_table['wavelength'].loc[j] - responsivity_table['wavelength'].loc[j-1] ))*last_digit




    calculated_result['Current density (mA/cm2)']= biasing_data_table['IdeviceAVG']*(1000/area1)
    calculated_result['Current density error']= biasing_data_table['IdeviceSTD']*(1000/area1)

    calculated_result['Power corrected (mW)']= biasing_data_table['IdetectorAVG']*((1000*p_correction_factor)/responsivity)
    calculated_result['Power corrected error']= biasing_data_table['IdetectorSTD']*((1000*p_correction_factor)/responsivity)
    


    counts_sum = modified_wavelength_counts['counts'].sum()
    
    sum_conv_fac_mod_spec=0
    sum_conv_fac_mod_spec = pd.Series(conversion_factor_spectrum_table['conversion_factor']*modified_wavelength_counts['counts']).sum()
    cf_lm_w = sum_conv_fac_mod_spec/(counts_sum*1000)
    cf_cd_mw = cf_lm_w/pi

    
    cons_for_luminance = cf_cd_mw/Area1

    calculated_result['Luminance [cd/m2]']= calculated_result['Power corrected (mW)']*cons_for_luminance
    calculated_result['Luminance error']= calculated_result['Power corrected error']*cons_for_luminance


    const_for_lum_power_eff = (cf_lm_w*1000)/area1

    calculated_result['Luminosity [lm/w]']= (calculated_result['Power corrected (mW)']*const_for_lum_power_eff)/(calculated_result['Bias Voltage(Volts)']*calculated_result['Current density (mA/cm2)'])
    calculated_result['Luminosity error']= (const_for_lum_power_eff/calculated_result['Bias Voltage(Volts)'])*( (calculated_result['Power corrected error']/calculated_result['Current density (mA/cm2)'])-((calculated_result['Power corrected (mW)']*calculated_result['Current density error'])/(calculated_result['Current density (mA/cm2)']**2))  )


    photons_per_watt_sec = pd.Series(list(map(lambda x: x*cons_for_photons_per_w_s, modified_wavelength_counts['wavelength'].values )))

    sum_of_counts_photons_cf=0
    sum_of_counts_photons_cf = pd.Series(photons_per_watt_sec*modified_wavelength_counts['counts']).sum()

    const_for_qe = (sum_of_counts_photons_cf)/(1000*counts_sum*area1*qe)

    calculated_result['Quantum Eff.[0-1]'] = (calculated_result['Power corrected (mW)']*const_for_qe)/calculated_result['Current density (mA/cm2)']
    calculated_result['Quantum Eff.error'] = const_for_qe*( (calculated_result['Power corrected error']/calculated_result['Current density (mA/cm2)'])-((calculated_result['Power corrected (mW)']*calculated_result['Current density error'])/(calculated_result['Current density (mA/cm2)']**2))  )


    calculated_result['Current Eff.[cd/A]'] = calculated_result['Luminance [cd/m2]']/(calculated_result['Current density (mA/cm2)']*10)
    calculated_result['Current Eff.error'] = 0.1*( (calculated_result['Luminance error']/calculated_result['Current density (mA/cm2)'])-((calculated_result['Luminance [cd/m2]']*calculated_result['Current density error'])/(calculated_result['Current density (mA/cm2)']**2))  )


    calculated_result['Radience [mW/m2]'] = calculated_result['Power corrected (mW)']/Area1
    calculated_result['Radience error'] = calculated_result['Power corrected error']/Area1

    #print(calculated_result)


    return ( calculated_result, modified_wavelength_counts )