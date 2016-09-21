

```python
import pandas
```

* interested in understanding the relationship b/t the weather and the number of mosquitos occuring during a particular year
* relationship at a particular site and whether or not it is consistent across sites
* data in csv files
* contains: single location data, rows holds single year info, mosiquito numbers and avg temps and rainfall 

year,temperature,rainfall,mosquitos  
2001,80,157,150  
2002,85,252,2177  
2003,86,154,153  

### Learning objectives
* conduct variable assignment, looping, and conditionals in python
* use an external py library
* read tabular data from a file
* subset and perform analysis on data
* display simple graphs

to get data needed for this unit:

### if you used get clone yesterday to get sio-swc:
  
1. navigate to sio-swc/ 
   * cd Desktop/sio-swc
2. run: git pull at the command line

### if you downloaded the zip file:

1. navigate to the Desktop
2. run: git clone https://github.com/ucsdlib/sio-swc.git


```python
cd /Users/jtdennis/Desktop/sio-swc/mosquitos
```

    /Users/jtdennis/Desktop/sio-swc/mosquitos



```python
pandas.read_csv('A1_mosquito_data.csv')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* read_csv() function belongs to pandas library
* dot notation 



```python
!head A1_mosquito_data.csv
```

    year,temperature,rainfall,mosquitos
    2001,80,157,150
    2002,85,252,217
    2003,86,154,153
    2004,87,159,158
    2005,74,292,243
    2006,75,283,237
    2007,80,214,190
    2008,85,197,181
    2009,74,231,200



```python
data = pandas.read_csv('A1_mosquito_data.csv')
```


```python
print(data)
```

       year  temperature  rainfall  mosquitos
    0  2001           80       157        150
    1  2002           85       252        217
    2  2003           86       154        153
    3  2004           87       159        158
    4  2005           74       292        243
    5  2006           75       283        237
    6  2007           80       214        190
    7  2008           85       197        181
    8  2009           74       231        200
    9  2010           74       207        184



```python
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* Once we have the data we can start playing with it.
* first let's ask what type of thing it is


```python
print(type(data))
```

    <class 'pandas.core.frame.DataFrame'>


* started in a data structure of DataFrame
* there are other data structures (remember numpy arrays from last class)



```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 10 entries, 0 to 9
    Data columns (total 4 columns):
    year           10 non-null int64
    temperature    10 non-null int64
    rainfall       10 non-null int64
    mosquitos      10 non-null int64
    dtypes: int64(4)
    memory usage: 400.0 bytes



* Two rows from 0 to 9
* Four columns 
* we can select an individual column of data using it's name:


```python
print(data['year'])
```

    0    2001
    1    2002
    2    2003
    3    2004
    4    2005
    5    2006
    6    2007
    7    2008
    8    2009
    9    2010
    Name: year, dtype: int64



```python
print(type(data['year']))
```

    <class 'pandas.core.series.Series'>


* or we can select several columns of data at once


```python
print(data[['rainfall', 'temperature']])
```

       rainfall  temperature
    0       157           80
    1       252           85
    2       154           86
    3       159           87
    4       292           74
    5       283           75
    6       214           80
    7       197           85
    8       231           74
    9       207           74


* we can subset rows using slices
* let's get first two rows


```python
print(data[0:2])
```

       year  temperature  rainfall  mosquitos
    0  2001           80       157        150
    1  2002           85       252        217


* remember python uses 0 based indexing
* starts at the first value and goes up to, but doesn't include the second value
* one thing we can't do with this syntax is directly as for data from a single row


```python
data[1]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-28-c805864c0d75> in <module>()
    ----> 1 data[1]
    

    /Users/jtdennis/anaconda/envs/py35/lib/python3.5/site-packages/pandas/core/frame.py in __getitem__(self, key)
       1967             return self._getitem_multilevel(key)
       1968         else:
    -> 1969             return self._getitem_column(key)
       1970 
       1971     def _getitem_column(self, key):


    /Users/jtdennis/anaconda/envs/py35/lib/python3.5/site-packages/pandas/core/frame.py in _getitem_column(self, key)
       1974         # get column
       1975         if self.columns.is_unique:
    -> 1976             return self._get_item_cache(key)
       1977 
       1978         # duplicate columns & possible reduce dimensionality


    /Users/jtdennis/anaconda/envs/py35/lib/python3.5/site-packages/pandas/core/generic.py in _get_item_cache(self, item)
       1089         res = cache.get(item)
       1090         if res is None:
    -> 1091             values = self._data.get(item)
       1092             res = self._box_item_values(item, values)
       1093             cache[item] = res


    /Users/jtdennis/anaconda/envs/py35/lib/python3.5/site-packages/pandas/core/internals.py in get(self, item, fastpath)
       3209 
       3210             if not isnull(item):
    -> 3211                 loc = self.items.get_loc(item)
       3212             else:
       3213                 indexer = np.arange(len(self.items))[isnull(self.items)]


    /Users/jtdennis/anaconda/envs/py35/lib/python3.5/site-packages/pandas/core/index.py in get_loc(self, key, method, tolerance)
       1757                                  'backfill or nearest lookups')
       1758             key = _values_from_object(key)
    -> 1759             return self._engine.get_loc(key)
       1760 
       1761         indexer = self.get_indexer([key], method=method,


    pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:3979)()


    pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:3843)()


    pandas/hashtable.pyx in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12265)()


    pandas/hashtable.pyx in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:12216)()


    KeyError: 1


* this is b/c data[1] is unambiguous
* if we want a single row we can either take a slice that returns a single row


```python
print(data[1:2])
```

       year  temperature  rainfall  mosquitos
    1  2002           85       252        217


* or use the `.iloc` method, which stands for "integer location" since we are looking up the row based on its integer:


```python
print(data.iloc[1])
```

    year           2002
    temperature      85
    rainfall        252
    mosquitos       217
    Name: 1, dtype: int64


* we can also use this syntax to get larger subsets


```python
print(data.iloc[1:3])
```

       year  temperature  rainfall  mosquitos
    1  2002           85       252        217
    2  2003           86       154        153


* we can also subset the data based on the value of other rows:


```python
print(data['temperature'][data['year'] > 2005])
```

    5    75
    6    80
    7    85
    8    74
    9    74
    Name: temperature, dtype: int64


* data frames also know how to perform common math
* mean


```python
print(data.mean())
```

    year           2005.5
    temperature      80.0
    rainfall        214.6
    mosquitos       191.3
    dtype: float64



```python
print(data.max())
```

    year           2010
    temperature      87
    rainfall        292
    mosquitos       243
    dtype: int64



```python
print(data['temperature'].min())
```

    74



```python
print(data['mosquitos'][1:3].std())
```

    45.2548339959



```python
print(data.describe())
```

                 year  temperature    rainfall  mosquitos
    count    10.00000    10.000000   10.000000   10.00000
    mean   2005.50000    80.000000  214.600000  191.30000
    std       3.02765     5.456902   50.317216   33.23335
    min    2001.00000    74.000000  154.000000  150.00000
    25%    2003.25000    74.250000  168.500000  163.75000
    50%    2005.50000    80.000000  210.500000  187.00000
    75%    2007.75000    85.000000  246.750000  212.75000
    max    2010.00000    87.000000  292.000000  243.00000


## Challenge

Import the data from A2_mosquito_data.csv, create a new variable that holds a data frame with only the weather data, and print the means and standard deviations for the weather variables.


```python
data2 = pandas.read_csv('A2_mosquito_data.csv')
data2.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>82</td>
      <td>200</td>
      <td>180</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>70</td>
      <td>227</td>
      <td>194</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>89</td>
      <td>231</td>
      <td>207</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>74</td>
      <td>114</td>
      <td>121</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>78</td>
      <td>147</td>
      <td>140</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather = data2[["temperature","rainfall"]]
print(data2.temperature.mean(), data2.temperature.std(), data2.rainfall.mean(), data2.rainfall.std())
```

    80.3921568627 6.13540033371 207.039215686 56.5603963156


## Loops

* we can loop over the data and perform operations
* remember loop structure:

```python
for item in list:
   do_something
```

* let's look over temperatures and print out their values in degrees Celsius


```python
temps = data['temperature']
for temp_in_f in temps:
    temp_in_c = (temp_in_f - 32) * 5/9
    print(temp_in_c)
```

    26.6666666667
    29.4444444444
    30.0
    30.5555555556
    23.3333333333
    23.8888888889
    26.6666666667
    29.4444444444
    23.3333333333
    23.3333333333


## Conditionals 

* let's review conditionals from yester (if/then/else)

```python
if condition: 
   do_something
```

* So if we want to loop over the temperatures and print out only those temperatures that are > 80


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['temperature'][0]
```




    80




```python
temp = data['temperature'][0]
temp
```




    80




```python
temp = data['temperature'][0]
if temp > 75:
    print("The temperature is greater than 75")
```

    The temperature is greater than 75


* We can also use `==` for equality
* `<=` for less than or equal to
* `>=` for greater than or equal to
* `!=` for not equal to

* we can add conditions with elif and else


```python
temp = data['temperature'][0]
if temp < 80:
    print("the temp is < 80")
elif temp > 80:
    print("the temp is > 80")
else:
    print("the temp is equal to 80")
```

    the temp is equal to 80


### Challenge:
>**Import the data from A2_mosquito_data.csv, determine the mean temperate, and loop over the temperature values. For each value print out whether it is greater than the mean, less than the mean, or equal to the mean.**


```python
print(data2['temperature'].head())
print("Mean", data2.temperature.mean())
```

    0    82
    1    70
    2    89
    3    74
    4    78
    Name: temperature, dtype: int64
    Mean 80.3921568627



```python
for temp in data2["temperature"]:
    if temp > data2.temperature.mean():
        print(temp, "is greater than", data2.temperature.mean())
    else:
        print(temp, "is less than", data2.temperature.mean())
```

    82 is greater than 80.3921568627
    70 is less than 80.3921568627
    89 is greater than 80.3921568627
    74 is less than 80.3921568627
    78 is less than 80.3921568627
    85 is greater than 80.3921568627
    86 is greater than 80.3921568627
    75 is less than 80.3921568627
    70 is less than 80.3921568627
    86 is greater than 80.3921568627
    83 is greater than 80.3921568627
    78 is less than 80.3921568627
    87 is greater than 80.3921568627
    76 is less than 80.3921568627
    86 is greater than 80.3921568627
    90 is greater than 80.3921568627
    76 is less than 80.3921568627
    87 is greater than 80.3921568627
    88 is greater than 80.3921568627
    87 is greater than 80.3921568627
    81 is greater than 80.3921568627
    74 is less than 80.3921568627
    85 is greater than 80.3921568627
    71 is less than 80.3921568627
    80 is less than 80.3921568627
    72 is less than 80.3921568627
    76 is less than 80.3921568627
    85 is greater than 80.3921568627
    83 is greater than 80.3921568627
    86 is greater than 80.3921568627
    82 is greater than 80.3921568627
    77 is less than 80.3921568627
    74 is less than 80.3921568627
    70 is less than 80.3921568627
    77 is less than 80.3921568627
    89 is greater than 80.3921568627
    83 is greater than 80.3921568627
    80 is less than 80.3921568627
    86 is greater than 80.3921568627
    72 is less than 80.3921568627
    79 is less than 80.3921568627
    85 is greater than 80.3921568627
    86 is greater than 80.3921568627
    72 is less than 80.3921568627
    78 is less than 80.3921568627
    71 is less than 80.3921568627
    88 is greater than 80.3921568627
    79 is less than 80.3921568627
    73 is less than 80.3921568627
    86 is greater than 80.3921568627
    87 is greater than 80.3921568627


### Plotting


```python
%matplotlib inline
```


```python
from matplotlib import pyplot as plt
```

* couple new things in the import statement above
    1. we can import part of a library using `from library import submodule` syntax
    2. we can use a different name to refer to the by using `as new name` - this called aliasing
* let's make a simple plot showing how the number of mosquitos varies over time


```python
data = pandas.read_csv('A2_mosquito_data.csv')
plt.plot(data['year'], data['mosquitos'])
```




    [<matplotlib.lines.Line2D at 0x10d36ee10>]




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_59_1.png)


* more complicated plots can be created by adding more info
* let's look at how the diff. weather variables vary over time


```python
plt.figure(figsize=(10.0,3.0))

plt.subplot(1,2,1)
plt.plot(data['year'], data['temperature'], 'ro-')
plt.xlabel('Year')
plt.ylabel('Temperature')

plt.subplot(1,2,2)
plt.plot(data['year'], data['rainfall'], 'bs-')
plt.xlabel('year')
plt.ylabel('rain fall')
```




    <matplotlib.text.Text at 0x10d8711d0>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_61_1.png)


### Challenge

>**Using the data in A2_mosquito_data.csv plot the relationship between the number of mosquitos and temperature and the number of mosquitos and rainfall. To change to a scatter plot in matplotlib use plt.scatter() instead of plt.plot(). Don't inlcude the color and shape parameter ('ro-' and 'bs-')**


```python
plt.figure(figsize=(10.0,3.0))

plt.subplot(1,2,1)
plt.scatter(data['temperature'], data2['mosquitos'], c="red")
plt.xlabel('Temp')
plt.ylabel('Mosquitos')

plt.subplot(1,2,2)
plt.scatter(data['rainfall'], data['mosquitos'])
plt.xlabel('Rainfall')
plt.ylabel('Moquitos')
```




    <matplotlib.text.Text at 0x10dc18908>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_63_1.png)


## Modularization and Doc

* relationship b/t the weather and the number of mosquitos so that we can control mosiquitos
* relationships across sites

** learning objectives**

* write code for ppl, not computers
* break programs into chunks 
* write functions
* document code


```python
import pandas as pd
```


```python
data = pd.read_csv('A2_mosquito_data.csv')
```


```python
print(data)
```

        year  temperature  rainfall  mosquitos
    0   1960           82       200        180
    1   1961           70       227        194
    2   1962           89       231        207
    3   1963           74       114        121
    4   1964           78       147        140
    5   1965           85       151        148
    6   1966           86       172        162
    7   1967           75       106        112
    8   1968           70       276        230
    9   1969           86       165        162
    10  1970           83       222        198
    11  1971           78       297        247
    12  1972           87       288        248
    13  1973           76       286        239
    14  1974           86       231        202
    15  1975           90       284        243
    16  1976           76       190        175
    17  1977           87       257        225
    18  1978           88       128        133
    19  1979           87       218        199
    20  1980           81       206        184
    21  1981           74       175        160
    22  1982           85       202        187
    23  1983           71       130        126
    24  1984           80       225        200
    25  1985           72       196        173
    26  1986           76       261        222
    27  1987           85       111        121
    28  1988           83       247        210
    29  1989           86       137        142
    30  1990           82       159        152
    31  1991           77       172        160
    32  1992           74       280        231
    33  1993           70       291        238
    34  1994           77       126        125
    35  1995           89       191        178
    36  1996           83       298        248
    37  1997           80       282        237
    38  1998           86       219        195
    39  1999           72       143        134
    40  2000           79       262        221
    41  2001           85       189        175
    42  2002           86       205        186
    43  2003           72       195        173
    44  2004           78       148        146
    45  2005           71       262        219
    46  2006           88       255        226
    47  2007           79       262        221
    48  2008           73       198        176
    49  2009           86       215        187
    50  2010           87       127        129


* write code for people not computers
* use meaniful variable names


```python
import pandas as pd

data = pd.read_csv('A2_mosquito_data.csv')
print(data.head())
```

       year  temperature  rainfall  mosquitos
    0  1960           82       200        180
    1  1961           70       227        194
    2  1962           89       231        207
    3  1963           74       114        121
    4  1964           78       147        140


* let's go ahead and conduct a regression on the data
* we will use `statsmodels` library to conduct the regression

## More pandas 

* Let's exlore using pandas some more
* We can get attributes of the data frame, like it's columns


```python
data = pandas.read_csv("A1_mosquito_data.csv", sep=",")
```


```python
data.columns
```




    Index(['year', 'temperature', 'rainfall', 'mosquitos'], dtype='object')




```python
%matplotlib inline
```

* we can plot a single variable using the dot notation to plot from a dataframe objtect


```python
data['temperature'].plot(color="black", marker="*")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10dc633c8>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_77_1.png)


* we can also set the index of the data frame


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>



* pandas has a concept of row index that you can set to what you want
* in this case, let's set our row index to `year`
* by default it will read in as the integer index


```python
data.set_index('year')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* we can save that setting by overwriting our data


```python
data = data.set_index('year')
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['temperature'].plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10dd587b8>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_86_1.png)


* ah what happened to the x axes labels?  
* our index is not the right data type


```python
data.index
```




    Int64Index([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], dtype='int64', name='year')



* lets fix and rerun the plot making our index into a string


```python
data.index = data.index.map(str)
```


```python
data['temperature'].plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10e013da0>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_91_1.png)


* one attribute of data frames is `dtypes` - tells us what our data types are


```python
data.dtypes
```




    temperature    int64
    rainfall       int64
    mosquitos      int64
    dtype: object



## subsetting and filtering
* Subsetting and filtering data frames
* let's see only temp greater than 80


```python
data[data["temperature"] > 80]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data["temperature"] > 80]["rainfall"]
```




    2002    252
    2003    154
    2004    159
    2008    197
    Name: rainfall, dtype: int64




```python
type(data)
```




    pandas.core.frame.DataFrame



* let's grab mosiquitos where rainfall is less than 200

### Challenge

>Select the mosiquitos where rainfall is less than 200


```python
data[data['rainfall'] < 200]['mosquitos']
```




    2001    150
    2003    153
    2004    158
    2008    181
    Name: mosquitos, dtype: int64



* this is equivalent statement:


```python
data['mosquitos'][data['rainfall'] < 200]
```




    2001    150
    2003    153
    2004    158
    2008    181
    Name: mosquitos, dtype: int64



* we can also get the max of that returned object


```python
data[data['rainfall'] < 200]['mosquitos'].max()
```




    181



**NOTE** - we can walk through this step by step

* we can also assign it to a variable for later


```python
mosquitos_with_low_rainfall = data['mosquitos'][data['rainfall'] < 200]
```


```python
type(mosquitos_with_low_rainfall)
```




    pandas.core.series.Series




```python
mosquitos_with_low_rainfall
```




    2001    150
    2003    153
    2004    158
    2008    181
    Name: mosquitos, dtype: int64




```python
mosquitos_with_low_rainfall.index
```




    Index(['2001', '2003', '2004', '2008'], dtype='object')




```python
data.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10e111160>




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_111_1.png)


### Functions

* review: 

```python
def function_name(inputs):
    do stuff
    return output
```

* general form

**EXAMPLE: function that returns the value of a number squared**


```python
def square(x):
    x_squared = x ** 2
    return x_squared

print('Four sqared is', square(4))
print('Five squared is', square(5))
```

    Four sqared is 16
    Five squared is 25



```python
#we can also return the desired value directly
def square(x):
    return x ** 2

print(square(3))
```

    9


* remember if we want to use the results of a function later we need to store it


```python
two_squared = square(2)
print(two_squared)
```

    4


## Challenge 

>“Adding” two strings produces their concatenation: 'a' + 'b' is 'ab'. Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:

>print(fence('name', '*'))

>\*name\*



```python
def fence(original, wrapper):
    return wrapper + original + wrapper
fence("hello", "**")
```




    '**hello**'



## Challenge
>If the variable s refers to a string, then s[0] is the string’s first character and s[-1] is its last. Write a function called outer that returns a string made up of just the first and last characters of its input. A call to your function should look like this:

>print(outer('helium'))  
>hm


```python
def outer(input_string):
    return input_string[0] + input_string[-1]

print(outer('helium'))
```

    hm


What does the following piece of code display when run - and why?

```python
f = 0
k = 0

def f2k(f):
  k = ((f-32)*(5.0/9.0)) + 273.15
  return k

f2k(8)
f2k(41)
f2k(32)

print(k)
```



```python
f = 0
k = 0

def f2k(f):
  k = ((f-32)*(5.0/9.0)) + 273.15
  return k

print(f2k(8))
print(f2k(41))
print(f2k(32))

print(k)
#k is 0 because the k inside the function f2k doesn’t 
#know about the k defined outside the function.

```

    259.81666666666666
    278.15
    273.15
    0


* Each time a function is called, a new stack frame is created on the **call stack** to hold its parameters and local variables.

## Challenge - function 

1. Write a function called fahr_to_celsius that converts temperature from Fahrenheit to Celcius and use it to replace

>```python
>data['temperature'] = (data['temperature'] - 32) * 5 / 9.0
>```
>
> in our program.


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius

print(fahr_to_celsius(32))
```

    0.0


*Walk through someone’s result. When discussing talk about different names. E.g., fahr_to_celcius is better than temp_to_celcius since it is explicit both the input and the output. Talk about the fact that even though this doesn’t save us any lines of code it’s still easier to read.*

## Functions

Documenting our functions. Using function with pandas objects.


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
fahr_to_celsius(32)
```




    0.0




```python
fahr_to_celsius(212)
```




    100.0



* 
* let's comment our function


```python
#this is a comment
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
"this is a string"
```




    'this is a string'




```python
#doesn't work
"a multiline 
string
"
```


      File "<ipython-input-94-316711d988ad>", line 2
        "a multiline
                     ^
    SyntaxError: EOL while scanning string literal



* a triple quote (single or double) will let us do a multi lined string


```python
multiline_string = ''' line one
line 2
one more
'''
```


```python
print(multiline_string)
```

     line one
    line 2
    one more
    



```python
#when we see the literal string we see the new line character
multiline_string
```




    ' line one\nline 2\none more\n'




```python
def fahr_to_celsius(temp_fahr):
    """Convert Fahrenheit to Celsiuss
    
    Return Celsius conversion of input
    """
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
# use a question after the function to get python help
fahr_to_celsius?
```

## Challenge - documenting

Revise a function you wrote for one of the previous exercises to try to make the code more readable. Then, collaborate with one of your neighbors to critique each other’s functions and discuss how your function implementations could be further improved to make them more readable.



```python
def fence(original, wrapper):
    return wrapper + original + wrapper
fence("hello", "**")
```




    '**hello**'




```python
def fence(original, wrapper):
    """Returns a string with a wrapper
    Args: 
        param1 (str): String we want wrapped
        param2 (str): The wrapper for param1
        
    Example:
    >>> fence("hello", "++")
    ++hello++
    """
    return wrapper + original + wrapper
```


```python
fence?
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>



* now we have the have the function we can apply it to our data frame
* let's see how that looks and then save to the data frame itself 


```python
fahr_to_celsius(data['temperature'])
```




    2001    26.666667
    2002    29.444444
    2003    30.000000
    2004    30.555556
    2005    23.333333
    2006    23.888889
    2007    26.666667
    2008    29.444444
    2009    23.333333
    2010    23.333333
    Name: temperature, dtype: float64




```python
data["temperature_c"] = fahr_to_celsius(data['temperature'])
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
      <td>26.666667</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
      <td>29.444444</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
      <td>30.555556</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
      <td>23.333333</td>
    </tr>
  </tbody>
</table>
</div>



* yay we added a new column on our dataframe
* let's plot using that var and save our plot to the disk


```python
%matplotlib inline
```


```python
import matplotlib.pyplot as plt
```


```python
plt.plot?
```


```python
plt.plot(data['temperature_c'], data['mosquitos'], ".")
plt.savefig('A1_mosquito_data_mosquitos_vs_tempC.png')
```


![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_154_0.png)



```python
!ls *png
```

    A1_mosquito_data_mosquitos_vs_tempC.png A3_mosquito_data_mosquitos_vs_tempC.png
    A2_mosquito_data_mosquitos_vs_tempC.png B1_mosquito_data_mosquitos_vs_tempC.png


* ok, we've successfully added a column to our data frame and plotted values
* then we saved that image to the file system
* but remember: we have a number of files in that directory


```python
!ls -l *csv
```

    -rw-r--r--  1 jtdennis  2113415076  196 Feb  6  2016 A1_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  852 Feb  6  2016 A2_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  827 Feb  6  2016 A3_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  823 Feb  6  2016 B1_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  852 Feb  6  2016 B2_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  217 Sep 20 14:11 a4.csv


* what we want is to be able to read each of those files, plot and save the fig out
* problem is we don't want to have to specify the file name manually
* let's see if we can manipulate our csv filenames 


```python
a = "A1_mosquitos_data.csv"
```


```python
a
```




    'A1_mosquitos_data.csv'



* remember how we sliced off parts of strings last week
* we can reuse that here


```python
a[0:-3] + "png"
```




    'A1_mosquitos_data.png'



* we can also concatenate our last part -- that tells us what we plotted


```python
a[0:-4] + "_mosquitos_vs_tempC.png"
```




    'A1_mosquitos_data_mosquitos_vs_tempC.png'



* we can do string replacement using the replace method


```python
a.replace(".csv", ".png")
```




    'A1_mosquitos_data.png'



**Let's put it all together with our conversion and plotting above into a couple of functions**


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
%matplotlib inline
```

* It is often good to write out what you want the function to do step by step


```python
def create_mosquitos_vs_tempC_plot(filename):
    # write out process here
    #load data
    #conert celsius
    #create the plot
    #save the plot
    pass
    
```

* Then just write out those operations 


```python
def create_mosquitos_vs_tempC_plot(filename):
  # write processing here
    # load data
    print("Loading", filename)
    mosquitos_data = pandas.read_csv(filename)
    # convert celsius
    mosquitos_data["temperature_C"] = fahr_to_celsius(mosquitos_data["temperature"])
    # create the plot
    print("Plotting", filename)
    plt.plot(mosquitos_data["temperature_C"], mosquitos_data["mosquitos"], ".")
    # save the plot
    filename_png = filename[0:-4] + "_mosquitos_vs_tempC.png"
    plt.savefig(filename_png)
    print("Saving", filename_png)
    return filename_png
```


```python
name_of_png = create_mosquitos_vs_tempC_plot('A2_mosquito_data.csv')
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_174_1.png)


* yay, we sucessfully created a function that takes a filename, reads in data, does a conversion, plots and then saves plot to the file


```python
print(name_of_png)
```

    A2_mosquito_data_mosquitos_vs_tempC.png



```python
create_mosquitos_vs_tempC_plot("B1_mosquito_data.csv")
```

    Loading B1_mosquito_data.csv
    Plotting B1_mosquito_data.csv
    Saving B1_mosquito_data_mosquitos_vs_tempC.png





    'B1_mosquito_data_mosquitos_vs_tempC.png'




![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_177_2.png)



```python
!ls *png
```

    A1_mosquito_data_mosquitos_vs_tempC.png A3_mosquito_data_mosquitos_vs_tempC.png
    A2_mosquito_data_mosquitos_vs_tempC.png B1_mosquito_data_mosquitos_vs_tempC.png


* **now, how about instead of returning the new plot filename, let's return the data frame**
* we just need to change the return value


```python
def create_mosquitos_vs_tempC_plot(filename):
  # write processing here
    # load data
    print("Loading", filename)
    mosquitos_data = pandas.read_csv(filename)
    # convert celsius
    mosquitos_data["temperature_C"] = fahr_to_celsius(mosquitos_data["temperature"])
    # create the plot
    print("Plotting", filename)
    plt.plot(mosquitos_data["temperature_C"], mosquitos_data["mosquitos"], ".")
    # save the plot
    filename_png = filename[0:-4] + "_mosquitos_vs_tempC.png"
    plt.savefig(filename_png)
    print("Saving", filename_png)
    return mosquitos_data
```


```python
mosquito_data_A2 = create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_181_1.png)


* we can then save that new data out as csv


```python
mosquito_data_A2.to_csv("A2_mosquito_data_C.csv")
```


```python
mosquito_data_A2.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>82</td>
      <td>200</td>
      <td>180</td>
      <td>27.777778</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>70</td>
      <td>227</td>
      <td>194</td>
      <td>21.111111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>89</td>
      <td>231</td>
      <td>207</td>
      <td>31.666667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>74</td>
      <td>114</td>
      <td>121</td>
      <td>23.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>78</td>
      <td>147</td>
      <td>140</td>
      <td>25.555556</td>
    </tr>
  </tbody>
</table>
</div>




```python
!head A2_mosquito_data_C.csv
```

    ,year,temperature,rainfall,mosquitos,temperature_C
    0,1960,82,200,180,27.77777777777778
    1,1961,70,227,194,21.11111111111111
    2,1962,89,231,207,31.666666666666668
    3,1963,74,114,121,23.333333333333332
    4,1964,78,147,140,25.555555555555557
    5,1965,85,151,148,29.444444444444443
    6,1966,86,172,162,30.0
    7,1967,75,106,112,23.88888888888889
    8,1968,70,276,230,21.11111111111111


### Making a module

* Let's write a script! 
* We will turn our functions into a script and use in panadas like our `import` modules
* open a text editor, nano cd to the mosquitos dir! 
* `cd ~/Desktop/sio-swc/mosquitos/`
* nano `analyze.py`



```python
!ls *py
```

    analyze.py            run_analyze_script.py



```python
cd ~/workshops/lecture-notes/intermed-py/
```

    /Users/jtdennis/workshops/lecture-notes/intermed-py



```python
!cat analyze.py
```

    import pandas
    import matplotlib.pyplot as plt
    
    def fahr_to_celsius(temp_fahr):
        """Convert Fahrenheit to Celsiuss
        
        Return Celsius conversion of input
        """
        temp_celsius = (temp_fahr- 32) * 5/9
        return temp_celsius
    
    def create_mosquitos_vs_tempC_plot(filename):
        """Create a png plot of mosquitos vs temp C
        
        Parameters
        ----------
        filename : string
            name of csv data file
        Returns
        -------
        mosquito_data : DataFrame
            Table with temp C column
        """
        
        # write processing here
        # load data
        print("Loading", filename)
        mosquitos_data = pandas.read_csv(filename)
        # convert celsius
        mosquitos_data["temperature_C"] = fahr_to_celsius(mosquitos_data["temperature"])
        # create the plot
        print("Plotting", filename)
        plt.plot(mosquitos_data["temperature_C"], mosquitos_data["mosquitos"], ".")
        # save the plot
        filename_png = filename[0:-4] + "_mosquitos_vs_tempC.png"
        plt.savefig(filename_png)
        print("Saving", filename_png)
        return mosquitos_data


```python
%matplotlib inline
```


```python
import analyze
```


```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_192_1.png)



```python
print(data)
```

        year  temperature  rainfall  mosquitos  temperature_C
    0   1960           82       200        180      27.777778
    1   1961           70       227        194      21.111111
    2   1962           89       231        207      31.666667
    3   1963           74       114        121      23.333333
    4   1964           78       147        140      25.555556
    5   1965           85       151        148      29.444444
    6   1966           86       172        162      30.000000
    7   1967           75       106        112      23.888889
    8   1968           70       276        230      21.111111
    9   1969           86       165        162      30.000000
    10  1970           83       222        198      28.333333
    11  1971           78       297        247      25.555556
    12  1972           87       288        248      30.555556
    13  1973           76       286        239      24.444444
    14  1974           86       231        202      30.000000
    15  1975           90       284        243      32.222222
    16  1976           76       190        175      24.444444
    17  1977           87       257        225      30.555556
    18  1978           88       128        133      31.111111
    19  1979           87       218        199      30.555556
    20  1980           81       206        184      27.222222
    21  1981           74       175        160      23.333333
    22  1982           85       202        187      29.444444
    23  1983           71       130        126      21.666667
    24  1984           80       225        200      26.666667
    25  1985           72       196        173      22.222222
    26  1986           76       261        222      24.444444
    27  1987           85       111        121      29.444444
    28  1988           83       247        210      28.333333
    29  1989           86       137        142      30.000000
    30  1990           82       159        152      27.777778
    31  1991           77       172        160      25.000000
    32  1992           74       280        231      23.333333
    33  1993           70       291        238      21.111111
    34  1994           77       126        125      25.000000
    35  1995           89       191        178      31.666667
    36  1996           83       298        248      28.333333
    37  1997           80       282        237      26.666667
    38  1998           86       219        195      30.000000
    39  1999           72       143        134      22.222222
    40  2000           79       262        221      26.111111
    41  2001           85       189        175      29.444444
    42  2002           86       205        186      30.000000
    43  2003           72       195        173      22.222222
    44  2004           78       148        146      25.555556
    45  2005           71       262        219      21.666667
    46  2006           88       255        226      31.111111
    47  2007           79       262        221      26.111111
    48  2008           73       198        176      22.777778
    49  2009           86       215        187      30.000000
    50  2010           87       127        129      30.555556


* notice that we added out earlier version of the plotting function to the file -- the one that returned the file
* edit the file and return mosquitos_data instead
* let's rerun the function call


```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_195_1.png)



```python
print(data)
```

        year  temperature  rainfall  mosquitos  temperature_C
    0   1960           82       200        180      27.777778
    1   1961           70       227        194      21.111111
    2   1962           89       231        207      31.666667
    3   1963           74       114        121      23.333333
    4   1964           78       147        140      25.555556
    5   1965           85       151        148      29.444444
    6   1966           86       172        162      30.000000
    7   1967           75       106        112      23.888889
    8   1968           70       276        230      21.111111
    9   1969           86       165        162      30.000000
    10  1970           83       222        198      28.333333
    11  1971           78       297        247      25.555556
    12  1972           87       288        248      30.555556
    13  1973           76       286        239      24.444444
    14  1974           86       231        202      30.000000
    15  1975           90       284        243      32.222222
    16  1976           76       190        175      24.444444
    17  1977           87       257        225      30.555556
    18  1978           88       128        133      31.111111
    19  1979           87       218        199      30.555556
    20  1980           81       206        184      27.222222
    21  1981           74       175        160      23.333333
    22  1982           85       202        187      29.444444
    23  1983           71       130        126      21.666667
    24  1984           80       225        200      26.666667
    25  1985           72       196        173      22.222222
    26  1986           76       261        222      24.444444
    27  1987           85       111        121      29.444444
    28  1988           83       247        210      28.333333
    29  1989           86       137        142      30.000000
    30  1990           82       159        152      27.777778
    31  1991           77       172        160      25.000000
    32  1992           74       280        231      23.333333
    33  1993           70       291        238      21.111111
    34  1994           77       126        125      25.000000
    35  1995           89       191        178      31.666667
    36  1996           83       298        248      28.333333
    37  1997           80       282        237      26.666667
    38  1998           86       219        195      30.000000
    39  1999           72       143        134      22.222222
    40  2000           79       262        221      26.111111
    41  2001           85       189        175      29.444444
    42  2002           86       205        186      30.000000
    43  2003           72       195        173      22.222222
    44  2004           78       148        146      25.555556
    45  2005           71       262        219      21.666667
    46  2006           88       255        226      31.111111
    47  2007           79       262        221      26.111111
    48  2008           73       198        176      22.777778
    49  2009           86       215        187      30.000000
    50  2010           87       127        129      30.555556


* doesn't work! 
* in juypter we have to explicitly 'reload' the module and this requies importing it from the importlib
* there's also `autoreload` extension 



```python
#only use if using jupyter text editor
from importlib import reload
reload(analyze)
```




    <module 'analyze' from '/Users/jtdennis/workshops/lecture-notes/intermed-py/analyze.py'>




```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data_files/Analyzing%20Mosquito%20Data_199_1.png)



```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>82</td>
      <td>200</td>
      <td>180</td>
      <td>27.777778</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>70</td>
      <td>227</td>
      <td>194</td>
      <td>21.111111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>89</td>
      <td>231</td>
      <td>207</td>
      <td>31.666667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>74</td>
      <td>114</td>
      <td>121</td>
      <td>23.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>78</td>
      <td>147</td>
      <td>140</td>
      <td>25.555556</td>
    </tr>
  </tbody>
</table>
</div>




```python
!ls *.png
```

    A1_mosquito_data_mosquitos_vs_tempC.png A2_mosquito_data_mosquitos_vs_tempC.png B1_mosquito_data_mosquitos_vs_tempC.png


**Last step -create a Python script that let's us run the above script from the command line**

1. Open another ext file
2. Call it run_analyze_script
3. Add the below to the file (using the cat command to print the file to the notebook)


```python
!cat run_analyze_script.py
```

    import analyze
    import sys 
    
    #filename = "a2_mosquito_data.csv"
    #argv[0] our script filename
    filename = sys.argv[1]
    
    analyze2.create_mosquitos_vs_tempC_plot(filename)


A note about the above: 

`sys.argv[1]` is the second element of the command line arguements - in this case the script filename is the first. So:
>python scriptname.py filename.csv 

sys.argv[0] is scriptname.py  
sys.argv[1] is filename.csv 

1. Lastly open a terminal console (cmd in win)
2. Go to the same directory of the file 
3. Type: `python run_analyze_script.py B1_mosquito_data.csv` in the command line and enter

* Yay! good job. 


```python

```
