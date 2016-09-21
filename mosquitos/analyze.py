import pandas
import matplotlib.pyplot as plt

def fahr_to_celisus(temp_fahr):
    '''Convert Fahrenheit to Celsisus
    
    Return Celsisus conversion of input
    '''
    temp_celsius = (temp_fahr - 32) * 5/9
    return temp_celsius


def create_mosquitos_vs_tempC_plot(filename):
   '''Create mosiquitos vs TempC plot
   Parameters
   ----------
   filename : string
      name of csv data file    
   Returns 
   -------
   mosquito_data : DataFrame 
   '''
    # load data
   print("loading", filename)
   mosquitos_data = pandas.read_csv(filename)
   # convert celisus
   mosquitos_data["temperature_c"] = fahr_to_celisus(mosquitos_data['temperature'])
   #create the plot
   plt.plot(mosquitos_data["temperature_c"], mosquitos_data['mosquitos'], '.')
   plt.xlabel("Temperature C")
   plt.ylabel("Mosquitos")
   plt.title("Temperature Celsius vs. Mosquitos")
   #save the plot
   filename_png = filename[0:-4] + "_mosquitos_vs_tempC.png"
   plt.savefig(filename_png)
   print("Saving", filename_png)
   return mosquitos_data


