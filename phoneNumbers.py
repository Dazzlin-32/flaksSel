from automation import search_last

def callSearch(phoneLast:str, name:str):
    search_last(phoneLast,name )





# phoneLists = ["+251910900050",
# "+251967055519",
# "+251923363130",
# "+251911547782",
# "+251941791054"
# "+251921233248",
# "+251911766134",
# "+251911176275",
# "+251967055519",
# "+251923363119",
# "+251911547719",
# "+251941791050",
# "+251921233250",
# "+251910547782",
# "+251911791054",
# "+251920233248",
# "+251911966134",
# "+251911177275"]

# startLetters = []
# #Find number with matching last digits with the input 
# def matching_last (lastNum):
#      wantedNums = []
#      for i in phoneLists:
#         if(i[11]+i[12] == lastNum):
#            wantedNums.append(i)
#      return wantedNums


# #Match the letters with the first letter of name and surname
# def matching_letters (arr:dict, name:str):
#     newResult = {}
#     finalResult = []
#     nameArray = name.split(' ')
#     nameStart = nameArray[0][0] + nameArray[1][0]
    
#     #making a key-name value phone number pair of dictionary
#     for key, value in arr.items():
#         newResult["name"]=name
#         for i in value:
#           if (i ==nameStart):
#                newResult["phone"]=key
#     #appending to an array for easier functionality
#     #finalResult.append(newResult)
#     return newResult
#     pass


# def search_last (phoneLast:str, name:str):
#      phoneNumbers = matching_last(phoneLast)
#      print(phoneNumbers)
     
#      index = len(phoneNumbers)
#      if(len(phoneNumbers)  == 0):
#          return -1
     
#      else:
#          for i in phoneNumbers:
#              result = automate(i,index)
#              index = index -1
#          pass
    
#      finalResult  = matching_letters(result, name)
#      print("Final result in phone", finalResult)
#      return finalResult

# #search_last("19","Habib Ahmed")
# # # def nameSearch(letterSearch,response):
     
# # #      for x in response:
# # #           if(x == letterSearch):
               
# # def findIndex(letterSearch: str, response: list ):
# #      try:
# #          return response.index(letterSearch)
# #      except Exception as e:
# #           return -1


     

# # def firstLetters (name: str):
# #      arr = name
# #      arr = arr.split(' ')
# #      return (arr[0][0]+arr[1][0])


# # def search_last (phoneLast, name):
# #      newPhoneList = []
# #      newNames = []
# #      resultDic = {
# #           'Name' : name,
# #           'Possible Values': []
# #      }
     
# #      for i in range(len(phoneLists)):
# #                stringP = str(phoneLists[i][11]+phoneLists[i][12])
# #                if(phoneLast == stringP):
# #                     newPhoneList.append(phoneLists[i])
# #      numberofPhone = len(newPhoneList)
# #      print (len(newPhoneList))
# #      for x in newPhoneList:
# #           response = automate(x, numberofPhone)
# #           numberofPhone = numberofPhone - 1     
# #           newNames.append(response)
# #      print(len(newPhoneList) , " Matching numbers :" , newPhoneList)
# #      print("Responses are : " , response)
# #      letterSearch = firstLetters(name)
# #      index = findIndex(letterSearch, response)
# #      if( index == -1):
# #          resultDic["Possible Values"] = "No accounts Found"
# #      else:
# #          resultDic["Possible Values"] = response[index] 

# #      return resultDic
# # search_last ("50", "Habib Ahmed")