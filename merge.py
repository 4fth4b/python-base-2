dict1={'car':'honda','model':'city','year':2019}
dict2={'bike':'honda','state':'kerala','country':'india'}
dict3={}
for i in dict1:
    if i not in dict3:
        dict3[i]=dict1[i]
for i in dict2:
    if i not in dict3:
        dict3[i]=dict2[i]    
print(dict3)