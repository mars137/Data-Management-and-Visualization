import pandas
import numpy

data = pandas.read_csv('~/Assign_2week/Assign_2.csv', low_memory=False)
print(len(data))
print(len(data.columns))

#often drank alcohol to improve mood/make self feel better
data['S4CQ18A'] = data['S4CQ18A'].convert_objects(convert_numeric=True)
#drank alcohol to improve mood in last 12 months
data['S4CQ18B'] = data['S4CQ18B'].convert_objects(convert_numeric=True)
#drank alcohol to improve mood prior to last 12 months
data['S4CQ18C'] = data['S4CQ18C'].convert_objects(convert_numeric=True)

#ever used medicine/drug on own to improve mood/make self feel better
data['S4CQ19A'] = data['S4CQ19A'].convert_objects(convert_numeric=True)
#used medicine/drug on own to improve mood in last 12 months
data['S4CQ19B'] = data['S4CQ19B'].convert_objects(convert_numeric=True)
#used medicine/drug on own to improve mood prior to last 12 months
data['S4CQ19C'] = data['S4CQ19C'].convert_objects(convert_numeric=True)

#used medicine/drug on own to improve low mood prior to last 12 months
data['S4AQ21A'] = data['S4AQ21A'].convert_objects(convert_numeric=True)
#used medicine/drug on own to improve low mood in last 12 months
data['S4AQ21B'] = data['S4AQ21B'].convert_objects(convert_numeric=True)
#ever used medicine/drug on own to improve low mood/make self feel BETTER
data['S4AQ21C'] = data['S4AQ21C'].convert_objects(convert_numeric=True)

#ever drank alcohol to improve low mood/make self feel better
data['S4AQ20A'] = data['S4AQ20A'].convert_objects(convert_numeric=True)
#drank alcohol to improve mood in last 12 months
data['S4AQ20B'] = data['S4AQ20B'].convert_objects(convert_numeric=True)
#drank alcohol to improve mood prior to last 12 months
data['S4AQ20C'] = data['S4AQ20C'].convert_objects(convert_numeric=True)

#ever drank alcohol to calm down/make self feel better
data['S5Q21A'] = data['S5Q21A'].convert_objects(convert_numeric=True)
#drank alcohol to calm down prior to last 12 months
data['S5Q21B'] = data['S5Q21B'].convert_objects(convert_numeric=True)
#drank alcohol to calm down prior to last 12 months
data['S5Q21C'] = data['S5Q21C'].convert_objects(convert_numeric=True)

#ever used medicine/drug on own to calm down/make self feel better
data['S5Q22A'] = data['S5Q22A'].convert_objects(convert_numeric=True)
#used medicine/drug on own to calm down in last 12 months
data['S5Q22B'] = data['S5Q22B'].convert_objects(convert_numeric=True)
#used medicine/drug on own to calm down prior to last 12 months
data['S5Q22C'] = data['S5Q22C'].convert_objects(convert_numeric=True)



#counts and percentages (i.e. frequency distributions) for each variable
print('counts for S4CQ18A - often drank alcohol to improve mood/make self feel better')
c1 = data['S4CQ18A'].value_counts(sort=False)
print (c1)
print('percentage for S4CQ18A - often drank alcohol to improve mood/make self feel better')
p1 = data['S4CQ18A'].value_counts(sort=False, normalize=True)
print (p1)

print('counts for S4CQ18B - drank alcohol to improve mood in last 12 months')
c2 = data['S4CQ18B'].value_counts(sort=False)
print (c2)
print('percentage for S4CQ18B - drank alcohol to improve mood in last 12 months')
p2 = data['S4CQ18B'].value_counts(sort=False, normalize=True)
print (p2)

print('counts for S4CQ18C - drank alcohol to improve mood prior to last 12 months')
c3 = data['S4CQ18C'].value_counts(sort=False)
print (c3)
print('percentage for S4CQ18C - drank alcohol to improve mood prior to last 12 months')
p3 = data['S4CQ18C'].value_counts(sort=False, normalize=True)
print (p3)

print('counts for S4CQ19A - ever used medicine/drug on own to improve mood/make self feel better')
c4 = data['S4CQ19A'].value_counts(sort=False)
print (c4)
print('percentage for S4CQ19A - ever used medicine/drug on own to improve mood/make self feel better')
p4 = data['S4CQ19A'].value_counts(sort=False, normalize=True)
print (p4)

print('counts for S4CQ19B - used medicine/drug on own to improve mood in last 12 months')
c5 = data['S4CQ19B'].value_counts(sort=False)
print (c5)
print('percentage for S4CQ19B - used medicine/drug on own to improve mood in last 12 months')
p5 = data['S4CQ19B'].value_counts(sort=False, normalize=True)
print (p5)

print('counts for S4CQ19C - used medicine/drug on own to improve mood prior to last 12 months')
c6 = data['S4CQ19C'].value_counts(sort=False)
print (c6)
print('percentage for S4CQ19C - used medicine/drug on own to improve mood prior to last 12 months')
p6 = data['S4CQ19C'].value_counts(sort=False, normalize=True)
print (p6)

print('counts for S4AQ21A - ever used medicine/drug on own to improve low mood/make self feel better')
c7 = data['S4AQ21A'].value_counts(sort=False)
print (c7)
print('percentage for S4AQ21A - ever used medicine/drug on own to improve low mood/make self feel better')
p7 = data['S4AQ21A'].value_counts(sort=False, normalize=True)
print (p7)

print('counts for S4AQ21B - used medicine/drug on own to improve low mood in last 12 months')
c8 = data['S4AQ21B'].value_counts(sort=False)
print (c8)
print('percentage for S4AQ21B - used medicine/drug on own to improve low mood in last 12 months')
p8 = data['S4AQ21B'].value_counts(sort=False, normalize=True)
print (p8)

print('counts for S4AQ21C - used medicine/drug on own to improve low mood prior to last 12 months')
c9 = data['S4AQ21C'].value_counts(sort=False)
print (c9)
print('percentage for S4AQ21C - used medicine/drug on own to improve low mood prior to last 12 months')
p9 = data['S4AQ21C'].value_counts(sort=False, normalize=True)
print (p9)

print('counts for S4AQ20A - ever drank alcohol to improve low mood/make self feel better')
c10 = data['S4AQ20A'].value_counts(sort=False)
print (c10)
print('percentage for S4AQ20A - ever drank alcohol to improve low mood/make self feel better')
p10 = data['S4AQ20A'].value_counts(sort=False, normalize=True)
print (p10)

print('counts for S4AQ20B - drank alcohol to improve mood in last 12 months')
c11 = data['S4AQ20B'].value_counts(sort=False)
print (c11)
print('percentage for S4AQ20B - drank alcohol to improve mood in last 12 months')
p11 = data['S4AQ20B'].value_counts(sort=False, normalize=True)
print (p11)

print('counts for S4AQ20C - drank alcohol to improve mood prior to last 12 months')
c12 = data['S4AQ20C'].value_counts(sort=False)
print (c12)
print('percentage for S4AQ20C - drank alcohol to improve mood prior to last 12 months')
p12 = data['S4AQ20C'].value_counts(sort=False, normalize=True)
print (p12)

print('counts for S5Q21A - ever drank alcohol to calm down/make self feel better')
c13 = data['S5Q21A'].value_counts(sort=False)
print (c13)
print('percentage for S5Q21A - ever drank alcohol to calm down/make self feel better')
p13 = data['S5Q21A'].value_counts(sort=False, normalize=True)
print (p13)

print('counts for S5Q21B - drank alcohol to calm down prior to last 12 months')
c14 = data['S5Q21B'].value_counts(sort=False)
print (c14)
print('percentage for S5Q21B - DRANK ALCOHOL TO CALM DOWN PRIOR TO LAST 12 MONTHS')
p14 = data['S5Q21B'].value_counts(sort=False, normalize=True)
print (p14)

print('counts for S5Q21C - drank alcohol to calm down prior to last 12 months')
c15 = data['S5Q21C'].value_counts(sort=False)
print (c15)
print('percentage for S5Q21C - drank alcohol to calm down prior to last 12 months')
p15 = data['S5Q21C'].value_counts(sort=False, normalize=True)
print (p15)

print('counts for S5Q22A - ever used medicine/drug on own to calm down/make self feel better')
c16 = data['S5Q22A'].value_counts(sort=False)
print (c16)
print('counts for S5Q22A - ever used medicine/drug on own to calm down/make self feel better')
p16 = data['S5Q22A'].value_counts(sort=False, normalize=True)
print (p16)

print('counts for S5Q22B - used medicine/drug on own to calm down in last 12 months')
c17 = data['S5Q22B'].value_counts(sort=False)
print (c17)
print('percentage for S5Q22B - used medicine/drug on own to calm down in last 12 months')
p17 = data['S5Q22B'].value_counts(sort=False, normalize=True)
print (p17)

print('counts for S5Q22C - used medicine/drug on own to calm down prior to last 12 months')
c18 = data['S5Q22C'].value_counts(sort=False)
print (c18)
print('percentage for S5Q22C - used medicine/drug on own to calm down prior to last 12 months')
p18 = data['S5Q22C'].value_counts(sort=False, normalize=True)
print (p18)

# freqeuncy disributions using the 'bygroup' function
ct1= data.groupby('S4CQ18A').size()
print ct1
pt1 = data.groupby('S4CQ18A').size() * 100 / len(data)
print pt1

ct2= data.groupby('S4CQ18B').size()
print ct2
pt2 = data.groupby('S4CQ18B').size() * 100 / len(data)
print pt2

ct3= data.groupby('S4CQ18C').size()
print ct3
pt3 = data.groupby('S4CQ18C').size() * 100 / len(data)
print pt3

ct4= data.groupby('S4CQ19C').size()
print ct4
pt4 = data.groupby('S4CQ19C').size() * 100 / len(data)
print pt4

ct5= data.groupby('S4CQ19C').size()
print ct5
pt5 = data.groupby('S4CQ19C').size() * 100 / len(data)
print pt5

ct6= data.groupby('S4CQ19C').size()
print ct6
pt6 = data.groupby('S4CQ19C').size() * 100 / len(data)
print pt6

ct7= data.groupby('S4AQ21A').size()
print ct7
pt7 = data.groupby('S4AQ21A').size() * 100 / len(data)
print pt7

ct8= data.groupby('S4AQ21B').size()
print ct8
pt8 = data.groupby('S4AQ21B').size() * 100 / len(data)
print pt8

ct9= data.groupby('S4AQ21C').size()
print ct9
pt9 = data.groupby('S4AQ21C').size() * 100 / len(data)
print pt9

ct10= data.groupby('S4AQ20A').size()
print ct10
pt10 = data.groupby('S4AQ20A').size() * 100 / len(data)
print pt10

ct11= data.groupby('S4AQ20B').size()
print ct11
pt11 = data.groupby('S4AQ20B').size() * 100 / len(data)
print pt11

ct12= data.groupby('S4AQ20C').size()
print ct12
pt12 = data.groupby('S4AQ20C').size() * 100 / len(data)
print pt12

ct13= data.groupby('S5Q21A').size()
print ct13
pt13 = data.groupby('S5Q21A').size() * 100 / len(data)
print pt13

ct14= data.groupby('S5Q21B').size()
print ct14
pt14 = data.groupby('S5Q21B').size() * 100 / len(data)
print pt14

ct15= data.groupby('S5Q21C').size()
print ct15
pt15 = data.groupby('S5Q21C').size() * 100 / len(data)
print pt15

ct16= data.groupby('S5Q22A').size()
print ct16
pt16 = data.groupby('S5Q22A').size() * 100 / len(data)
print pt16

ct17= data.groupby('S5Q22B').size()
print ct17
pt17 = data.groupby('S5Q22B').size() * 100 / len(data)
print pt17

ct18= data.groupby('S5Q22C').size()
print ct18
pt18 = data.groupby('S5Q22C').size() * 100 / len(data)
print pt18 
