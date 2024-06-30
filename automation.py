from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core.os_manager import ChromeType
import time

phoneLists = ["+251910900050",
"+251967055519",
"+251923363130",
"+251911547782",
"+251941791054"
"+251921233248",
"+251911766134",
"+251911176275",
"+251967055519",
"+251923363119",
"+251911547719",
"+251941791050",
"+251921233250",
"+251910547782",
"+251911791054",
"+251920233248",
"+251911966134",
"+251911177275"]


# PATH = r'.\chromedriver.exe'
# chrome_options = ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# # driver = webdriver.Chrome(options=chrome_options)

# # #Docker
# # chrome_options = ChromeOptions()
# # chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--headless")
# # driver = webdriver.Chrome(options=chrome_options)



# # s= Service(Service(ChromeDriverManager()))
# # options = ChromeOptions()
# # options.add_argument("--headless")
# # options.add_argument("--no-sandbox")
# # options.add_argument('--disable-dev-shm-usage')

# # Set the language preference to English
# chrome_prefs = {
#     "intl.accept_languages": "en,en_US"
# }
# chrome_options.add_experimental_option("prefs", chrome_prefs)


# #driver = webdriver.Chrome( service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)

# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=chrome_options)


# # PATH = r'C:\Users\slave\OneDrive\Desktop\Gits\HabibiProject\chromedriver.exe'
# # driver = webdriver.Chrome()

chrome_options = ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--lang=en-US")

driver = webdriver.Chrome(options = chrome_options)


namesStart = []
results = {}


def searchAutomation ():
    driver.switch_to.new_window('tab')
    print("Automation Started")
    driver.get('https://en-gb.facebook.com/')
    
    search = driver.find_element(By.CLASS_NAME, "_6ltj")
    
    search.click()
 



def searchByPhone ( phoneNum,numberofPhone ):
            newFoundNames = []
            x = phoneNum
            try:
                print("Search by phone", x)
                searchAutomation()

                #If facebook directly opens the last forgotten account page from previous session
                # this snippet makes sure to click not you
                try:
                    time.sleep(10)
                    notYou = driver.find_element(By.LINK_TEXT, "Not you?")

                    if(notYou):
                        notYou.click()
                        searchAutomation()
                        # print("Not you clicked!")
                except Exception as e:
                    # print("Not you is not found")
                    pass

                driver.implicitly_wait(5)


                #Finding the email input and sending the number to search for accounts
                identifyEmail = driver.find_element(By.ID, "identify_email")
                driver.implicitly_wait(5)
                identifyEmail.send_keys(x)
                identifyEmail.send_keys(Keys.RETURN)
                # print("Searching with number ",x)

                #Collecting this is my account urls to open them individually
                try:
                    time.sleep(5)
                    foundAccountLists = driver.find_elements(By.LINK_TEXT,"This is my account")
                    accountLinks = []
                
                    # print("Accounts", len(foundAccountLists))  
                    for a in foundAccountLists:
                        accountLinks.append(a.get_attribute("href"))
                        #print("Tags " , a.get_attribute('href'))
                    
                    #print("Length of accounts tag", len(accountLinks))

                    if(len(accountLinks) > 1):
                        
                        for a in accountLinks:
                            driver.get(a)
                            # print("Page Title: ", driver.title)

                            # print("Tag ", a)
                            driver.implicitly_wait(10)
                            try:
                                tryAnother = driver.find_element(By.LINK_TEXT, "Try another way")
                                if (tryAnother):
                                    tryAnother.click()
                                    print("Try Another clicked")
                                
                                
                                driver.implicitly_wait(10)
                                search2 = driver.find_element(By.ID, "globalContainer")
                                
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[2]")))
                                search3 = search2.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
                                # print("If part",search3)
                                for e in search3:
                                        # print("Target word with try another",e.text[0], e.text[5])
                                        newFoundNames.append(e.text[0]+e.text[5])
                                        
                                        
                                    
                            except Exception as e:
                                    driver.implicitly_wait(10)
                                    search2 = driver.find_element(By.ID, "globalContainer")
                                    search3 = search2.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
                                    for e in search3:
                                        newFoundNames.append(e.text[0]+e.text[5])
                                        
                                        # print("Target word without try another",e.text[0], e.text[5])
                                        # print(newFoundNames)
                                        


                    else:
                        driver.implicitly_wait(10)
                        search2 = driver.find_element(By.ID, "globalContainer")
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[2]")))
                        search3 = search2.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
                        # print("Else Part", search3)
                        for e in search3:  
                                # print("Target word without multiple accounrs found" ,e.text[0], e.text[5])                              
                                newFoundNames.append(e.text[0]+e.text[5])
                                
                                
                        
                except Exception as e:
                    # print("Try another way not found",e)
                    namesStart.append('0')
                
                #print("Found Names: " , newFoundNames )
            except Exception as e:
                print("Error Founnd",e)
                #namesStart.append('0')
            print("HEllo" , newFoundNames)
            results[x] = newFoundNames
            # finally:
            #      if(numberofPhone == 0):
            #         driver.quit()
                
        
def automate(phone,numberofPhone):
        if(numberofPhone != 0):
            print("Welcome to our AutoSearch Application!")
            searchByPhone(phone,numberofPhone)
            print("Automation Finished!")
            
            print("Found Target Names" , results)
            return results
        else:
            driver.close()
            driver.quit()


#Find number with matching last digits with the input 
def matching_last (lastNum):
     wantedNums = []
     for i in phoneLists:
        if(i[11]+i[12] == lastNum):
           wantedNums.append(i)
     return wantedNums

#Match the letters with the first letter of name and surname
def matching_letters (arr:dict, name:str):
    newResult = {}
    finalResult = []
    nameArray = name.split(' ')
    nameStart = nameArray[0][0] + nameArray[1][0]
    
    #making a key-name value phone number pair of dictionary
    for key, value in arr.items():
        newResult["name"]=name
        for i in value:
          if (i ==nameStart):
               newResult["phone"]=key
    #appending to an array for easier functionality
    #finalResult.append(newResult)
    return newResult
 

#function to search numbers from data
def search_last (phoneLast:str, name:str):
     phoneNumbers = matching_last(phoneLast)
     print(phoneNumbers)
     
     index = len(phoneNumbers)
     if(len(phoneNumbers)  == 0):
         return -1
     
     else:
         for i in phoneNumbers:
             result = automate(i,index)
             index = index -1
         pass
    
     finalResult  = matching_letters(result, name)
     print("Final result in phone", finalResult)
     return finalResult

        

# automate("+251967055519", "1")

  

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# import selenium



# # s= Service(ChromeDriverManager())
# # options = ChromeOptions()
# # options.add_argument("--headless=new")
# chrome_options = webdriver.ChromeOptions()
# #chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# #chrome_options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=chrome_options)
# # PATH = r'C:\Users\slave\OneDrive\Desktop\Gits\HabibiProject\chromedriver.exe'
# # driver = webdriver.Chrome()


# def searchAutomation ():
#     driver.switch_to.new_window('tab')
#     print(selenium.__version__)
#     print("Automation Started")
#     driver.get('http://www.facebook.com')
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, "a[href='https://www.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzE2OTEyNzE5LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&ars=facebook_login']")
#     print("Page title was '{}'".format(driver.title))

# try:
#     searchAutomation()

# finally:
#     driver.quit()






