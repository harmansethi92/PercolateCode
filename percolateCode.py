import re                                                                                                                       # For Regex
import json                                                                                                                     # For Json
from collections import OrderedDict                                                                                             # For Ordered dictionary                         

array= []                                                                                                                       # List for inputs from file
entry = []                                                                                                                      # List for entries
errors  = []                                                                                                                    # List for errors
for line in open("data.in"):
    array.append(line.strip().split(","))

# Creating Regex to match the given pattern
zipcodetype = r' (\d{5})$'                                                                                                      # For Zipcode with max 5 digits
nametype1 = r'(.+)'                                                                                                             # Name type of Firstname, lastname
nametype2 = r'(\w+)\s(.+)'                                                                                                      # Name type of Firstname lastname
phonetype1 = r' (\d{3}) (\d{3}) (\d{4})$'                                                                                       # Phone type 703 955 0373
phonetype2 = r' \((\d{3})\)-(\d{3})-(\d{4})$'                                                                                   # Phone type (703)-742-0996
colortype      = r' (.+)'                                                                                                       # For Color


for arr in array:
    
         # Case1 : Firstname Lastname, Red, 11237, 703 955 0373
    if (len(arr) == 4) and ( (re.match(nametype2,arr[0])) and (re.match(colortype, arr[1])) and (re.match(zipcodetype, arr[2]) )and  (re.match(phonetype1, arr[3]))) :
        
    
        words = arr[0].split(" ",1)                                                                                             # Splitting the First word of the array
        firstname = words[0].strip()                                                                                            # Creating first name and stripping spaces
        lastname  = words[1].strip()                                                                                            # Creating Second name and stripping spaces
        phone = arr[3].split(" ",3)                                                                                             # Spliting given phone number
        phonenumber = phone[1] + '-' + phone[2] + '-' + phone[3]                                                                # Defining in the form of output we want
        zipcode = arr[2].strip()                                                                                                # Creating zipcode and stripping spaces
        color = arr[1].strip()                                                                                                  # Creating color and stripping spaces
        pythondict = OrderedDict()                                                                                              # creating an ordered dictionary
        pythondict["color"] = color
        pythondict["firstname"] = firstname
        pythondict["lastname"] = lastname
        pythondict["phonenumber"] =  phonenumber
        pythondict["zipcode"] = zipcode
        entry.append(pythondict)                                                                                                # Appending the ordereddictionary in the above entry list
       
        # Case2 : Lastname, Firstname, (703)-742-0996, Blue, 10013
    elif (len(arr) == 5) and ( (re.match(nametype1,arr[0])) and (re.match(nametype1,arr[1])) and (re.match(colortype, arr[3])) and (re.match(zipcodetype, arr[4]) )and  (re.match(phonetype2, arr[2]))) :
            phone = arr[2].split("(",1)                                                                                         # Spliting given phone number
            phone1 = phone[1].split(")",1)
            phone2= arr[2].split("-",2)
            firstname = arr[1].strip()                                                                                          # Creating first name and stripping spaces
            lastname = arr[0].strip()                                                                                           # Creating Second name and stripping spaces
            color = arr[3].strip()                                                                                              # Creating color and stripping spaces
            zipcode = arr[4].strip()                                                                                            # Creating zipcode and stripping spaces
            phonenumber = phone1[0] + '-' + phone2[1] + '-' + phone2[2]                                                         # Defining number in the form of output we want
            pythondict = OrderedDict()                                                                                          # creating an ordered dictionary
            pythondict["color"] = color
            pythondict["firstname"] = firstname
            pythondict["lastname"] = lastname
            pythondict["phonenumber"] =  phonenumber
            pythondict["zipcode"] = zipcode
            entry.append(pythondict)                                                                                            # Appending the ordereddictionary in the above entry list
        
        # Case3 : Firstname, Lastname, 10013, 646 111 0101, Green
    elif (len(arr) == 5) and ( (re.match(nametype1,arr[0])) and (re.match(nametype1,arr[1])) and (re.match(colortype, arr[4])) and (re.match(zipcodetype, arr[2]) ) and  (re.match(phonetype1, arr[3]))) :        
            phone = arr[3].split(" ",3)                                                                                         # Spliting given phone number
            firstname = arr[0].strip()                                                                                          # Creating first name and stripping spaces
            lastname = arr[1].strip()                                                                                           # Creating Second name and stripping spaces
            zipcode = arr[2].strip()                                                                                            # Creating zipcode and stripping spaces
            phonenumber = phone[1] + '-' + phone[2] + '-' + phone[3]                                                            # Defining number in the form of output we want
            color = arr[4].strip()                                                                                              # Creating color and stripping spaces
            pythondict = OrderedDict()                                                                                          # creating an ordered dictionary
            pythondict["color"] = color
            pythondict["firstname"] = firstname
            pythondict["lastname"] = lastname
            pythondict["phonenumber"] =  phonenumber
            pythondict["zipcode"] = zipcode
            entry.append(pythondict)                                                                                            # Appending the ordereddictionary in the above entry list                                                                                         
    else:
            errors.append(array.index(arr))                                                                                     # Appending the line number of errors in errors list above

entries = sorted(entry, key=lambda d:(("lastname" not in d, d.get("lastname")),("firstname" not in d, d.get("firstname"))))     # Sorting the entry list based on lastname and firstname
r = OrderedDict()                                                                                                               # Making an ordered dictionary with entries and errors
r["entries"] = entries
r["errors"] = errors
result = json.dumps(r, indent=2)
print result
    
