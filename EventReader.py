import Evtx.Evtx as evtx
import Evtx.Views as e_views
import re

def freq(str): 
  
    # break the string into list of words  
    str = str.split()          
    str2 = [] 
  
    # loop till string values present in list str 
    for i in str:              
  
        # checking for the duplicacy 
        if i not in str2: 
  
            # insert value in str2 
            str2.append(i)  
              
    for i in range(0, len(str2)): 
  
        # count the frequency of each word(present  
        # in str2) in str and print 
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))

def main():
    with evtx.Evtx("/Users/dburget/Downloads/Security.evtx") as log:
        s = ""
        user = ""
        for record in log.records():
            s = record.xml()
            result = re.search('<Data Name="TargetUserName">(.*)</Data>', s)
            if result is not None:
                user = user + " " + result.group(1)
    freq(user)
        sgdf
if __name__=="__main__": 
    main()             # call main function 