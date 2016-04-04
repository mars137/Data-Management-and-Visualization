import pandas
import numpy

data = pandas.read_csv('/home/Coursera/DataAalysis/CourseData.csv', low_memory=False)

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

#setting variables you will be working with to numeric
data['DYSDX12'] = data['DYSDX12'].convert_objects(convert_numeric=True)
data['AGE'] = data['AGE'].convert_objects(convert_numeric=True)
data['S4CQ18A'] = data['S4CQ18A'].convert_objects(convert_numeric=True)
data['S4CQ19A'] = data['S4CQ19A'].convert_objects(convert_numeric=True)
data['S4CQ18B'] = data['S4CQ18B'].convert_objects(convert_numeric=True)

#subset data for age >=18 and age <=25 and patients with dysthemia in last 12 months
sub1=data[(data['AGE']>=18) & (data['AGE']<=25) & (data['DYSDX12']==1)]

#make a copy of my new subsetted data
sub2 = sub1.copy()


print 'counts for original S4CQ18A'
c1 = sub2['S4CQ18A'].value_counts(sort=False, dropna=False)
print(c1)

# recode missing values to python missing (NaN)
sub2['S4CQ18A']=sub2['S4CQ18A'].replace(9, numpy.nan)
sub2['S4CQ19A']=sub2['S4CQ19A'].replace(9, numpy.nan)
sub2['S4CQ18B']=sub2['S4CQ18B'].replace(9, numpy.nan)

#if you want to include a count of missing add ,dropna=False after sort=False
print 'counts for S4CQ18A with 9 set to NAN and number of missing requested'
c2 = sub2['S4CQ18A'].value_counts(sort=False, dropna=False)
print(c2)
#if you want to include a count of missing add ,dropna=False after sort=False
print 'counts for S4CQ19A with 9 set to NAN and number of missing requested'
c2 = sub2['S4CQ19A'].value_counts(sort=False, dropna=False)
print(c2)
#if you want to include a count of missing add ,dropna=False after sort=False
print 'counts for S4CQ18B with 9 set to NAN and number of missing requested'
c2 = sub2['S4CQ18B'].value_counts(sort=False, dropna=False)
print(c2)

sub2.describe()
#to check the structure of the data columns
def rstr(df): return df.shape, df.apply(lambda x: [x.unique()])
print(rstr(sub2))

#recode junk values such as p, +AAc-, 2, 9, 1, es, +by5zZA- values as missing
sub2['S5Q22C']=sub2['S5Q22C'].replace('p', numpy.nan)
sub2['S5Q22C']=sub2['S5Q22C'].replace('+AAc-', numpy.nan)
sub2['S5Q22C']=sub2['S5Q22C'].replace('es', numpy.nan)
sub2['S5Q22C']=sub2['S5Q22C'].replace('+by5zZA-', numpy.nan)

#subsetting data which contains only 3 columns
sub3 = sub2[['AGE','S4CQ18A','S4CQ19A','S4CQ18B']]

# check coding
chk3 = sub3['S4CQ18A'].value_counts(sort=False, dropna=False)
print(chk3)
ds3= sub3["S4CQ18A"].describe()

#examining frequency distributions for age
print 'counts for AGE'
c3 = sub3['AGE'].value_counts(sort=False)
print(c3)

print 'percentages for AGE'
p3 = sub3['AGE'].value_counts(sort=False, normalize=True)
print (p3)


# quartile split (use qcut function & ask for 4 groups - gives you quartile split)
print 'AGE - 4 categories - quartiles'
sub3['AGEGROUP4']=pandas.qcut(sub3.AGE, 4, labels=["1=0%tile","2=25%tile","3=50%tile","4=75%tile"])
c4 = sub3['AGEGROUP4'].value_counts(sort=False, dropna=True)
print(c4)

# categorize quantitative variable based on customized splits using cut function
# splits into 3 groups (18-20, 21-22, 23-25) - remember that Python starts counting from 0, not 1
sub3['AGEGROUP3'] = pandas.cut(sub3.AGE, [17, 20, 22, 25])
c5 = sub3['AGEGROUP3'].value_counts(sort=False, dropna=True)
print(c5)


#frequency distribution for AGEGROUP3
print 'counts for AGEGROUP3'
c10 = sub3['AGEGROUP3'].value_counts(sort=False)
print(c10)

print 'percentages for AGEGROUP3'
p10 = sub3['AGEGROUP3'].value_counts(sort=False, normalize=True)
print (p10)