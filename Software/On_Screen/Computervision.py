import cv2
import pytesseract
import pyautogui
import re
import socket
import numpy as np

class codcv():
    '''
    THIS FUNCTION IMPLEMENTS THE COD COMPUTER VISION FUNCTIONALITY THE FOLLOWING IS INCLUDED
    VARIABLES:
    notspectating - This tells the user whether or not they are notspectating
    startgame - This tells the user whether or not they are in or out of the warzone lobby, pregame lobby excluded.
    dead - This tells the user whether they have died or not
    confirm_kill - This tells the user whether or not they have a confirmed kill (4 consecutive instances of the same reading register on the tesseract)


    Functions:
    '''
    def __init__(self):
        self.spectating = False
        self.startgame = False
        self.killcounter = 0
        self.avgkill = [0,0,0,0]
        self.notspectating = [True,True,True,True,True]
        self.confirm_kill = 0
        self.dead = False
        self.startflag = False
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

    def confirm(self, items):
        return all(x == items[0] for x in items)

    def isspectating(self):
        pyautogui.screenshot('pictures/cod/spectating.png', region = (860, 800, 200, 40))
        speccheck = cv2.imread('pictures/cod/spectating.png')
        speccheck = cv2.cvtColor(speccheck, cv2.COLOR_RGB2GRAY)
        speccheck = cv2.bilateralFilter(speccheck, 11, 30, 30)
        ret, speccheckthreshold = cv2.threshold(speccheck, 160, 255, cv2.THRESH_BINARY)
        speccheckthreshold = cv2.bitwise_not(speccheckthreshold)
        cv2.imwrite('pictures/cod/spectatingthreshold.png', speccheckthreshold)
        custom_config = r'-l eng --oem 3 --psm 8 -c tessedit_char_whitelist="SPECTATING" '
        gameendstring = pytesseract.image_to_string(speccheckthreshold, config = custom_config)
        if 'SPECTATING' in gameendstring:
            self.notspectating.insert(0, False)
            self.spectating = True
        else:
            self.notspectating.insert(0, True)
        if self.confirm(self.notspectating) and self.notspectating[0]:
            self.spectating = False
        self.notspectating.pop()

    def isingame(self):
        if self.startgame == False:
            pyautogui.screenshot('pictures/cod/gamestart.png', region = (110, 750, 300, 80))
            img = cv2.imread('pictures/cod/gamestart.png')
            template = cv2.imread('pictures/cod/gamestarttemplate.png')
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            ret, thresh1 = cv2.threshold(gray_img, 229, 255, cv2.THRESH_BINARY)
            ret, thresh2 = cv2.threshold(gray_template, 229, 255, cv2.THRESH_BINARY)
            result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= 0.9)
            sum = loc[0] + loc[1]
            if sum.size > 0:
                self.startgame = True
                self.startflag = True
        else:
            pyautogui.screenshot('pictures/cod/gameend.png', region = (270, 862, 365, 60))
            gameend = cv2.imread('pictures/cod/gameend.png')
            gamestart = cv2.cvtColor(gameend, cv2.COLOR_RGB2GRAY)
            ret, threshgame = cv2.threshold(gameend, 120, 255, cv2.THRESH_BINARY)
            cv2.imwrite('pictures/cod/gameendthresh.png', threshgame)
            custom_config = r'-l eng --oem 3 --psm 8 -c tessedit_char_whitelist="VERDANSK" '
            gamestring = pytesseract.image_to_string(threshgame, config = custom_config)
            if gamestring == 'VERDANSK\n\x0c':
                self.startgame = False

    def iskill(self):
        pyautogui.screenshot('pictures/cod/Kill.png', region = (1823, 48, 30, 23))
        img = cv2.imread('pictures/cod/Kill.png')
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grayscale = cv2.bilateralFilter(grayscale, 11, 30, 30)
        ret, thresh1 = cv2.threshold(grayscale, 255, 255, cv2.THRESH_TRUNC)
        thresh1 = cv2.bitwise_not(thresh1)
        cv2.imwrite('pictures/cod/Killthresh.png', thresh1)
        custom_config = r'-l eng --oem 3 --psm 7 -c tessedit_char_whitelist="1234567890" '
        killnumber = pytesseract.image_to_string(thresh1, config = custom_config)
        killnumber2 = pytesseract.image_to_string(img, config = custom_config)
        killnumberlist = re.split(r'',killnumber)
        killnumberlist2 = re.split(r'',killnumber2)
        killstring = ''
        if killnumberlist[1] == '\x0c':
            killnumberlist.insert(1, killnumberlist2[1])
        for i in killnumberlist:
            try:
                int(i)
                killstring = killstring + i
            except:
                pass
        if killstring:
            self.killcounter = int(killstring)
        else:
            self.killcounter = -1
        self.avgkill.insert(0, self.killcounter)
        self.avgkill.pop()
        if self.confirm(self.avgkill) and self.killcounter != -1 and abs(self.killcounter)- abs(self.confirm_kill) < 7:
            self.confirm_kill = self.avgkill[0]

    def isdead(self):
        pyautogui.screenshot('pictures/cod/Death.png', region = (900,900,130,50))
        img = cv2.imread('pictures/cod/Death.png')
        template = cv2.imread('pictures/cod/DeathTemplate.png')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_img, 229, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(gray_template, 229, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        sum = loc[0] + loc[1]
        if sum.size > 0:
            self.dead = True
        else:
            self.dead = False
    
class fallguyscv():

    def __init__(self):
        self.win = False
        self.lose = False
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

    def iseliminated(self):
        pyautogui.screenshot('pictures/fallguys/Disqualified.png', region = (315,390,220,230))
        img = cv2.imread('pictures/fallguys/Disqualified.png')
        template = cv2.imread('pictures/fallguys/DisqualifiedTemplate.png')
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_img, 229, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(gray_template, 229, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        sum = loc[0] + loc[1]
        if sum.size > 0:
            self.lose = True
        else:
            self.lose = False
    
    def isqualified(self):
        pyautogui.screenshot('pictures/fallguys/Qualified.png', region = (400,390,220,230))
        img = cv2.imread('pictures/fallguys/Qualified.png')
        template = cv2.imread('pictures/fallguys/QualifiedTemplate.png')
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_img, 229, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(gray_template, 229, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        sum = loc[0] + loc[1]
        if sum.size > 0:
            self.win = True
        else:
            self.win = False

class amonguscv():

    def __init__(self):
        self.imposterwins = 0
        self.imposterloses = 0
        self.crewmatewins = 0
        self.crewmateloses = 0
        self.crack = False
        self.reported = False
        self.imposter = False
        self.crewmate = False
        self.ingame = False
        self.lights = False
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

    def isreported(self):
        pyautogui.screenshot('pictures/amongus/amongusreport.png', region = (550,425,200,250))
        img = cv2.imread('pictures/amongus/amongusreport.png')
        template = cv2.imread('pictures/amongus/amongusTemplate.png')
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(gray_template, 180, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        sum = loc[0] + loc[1]
        if sum.size > 0:
            self.reported = True
        else:
            self.reported = False

    def iscracked(self):
        pyautogui.screenshot('pictures/amongus/amonguscrack.png', region = (1425,400,300,300))
        img = cv2.imread('pictures/amongus/amonguscrack.png')
        template = cv2.imread('pictures/amongus/amonguscrackTemplate.png')
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(gray_template, 180, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh1, thresh2, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)
        sum = loc[0] + loc[1]
        if sum.size > 0:
            self.crack = True
        else:
            self.crack = False

    def whichteam(self):
        pyautogui.screenshot('pictures/amongus/amongusmember.png', region = (345,50,1250,350))
        img = cv2.imread('pictures/amongus/amongusmember.png')
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        custom_config = r'-l eng --oem 3 --psm 7'
        membertype = pytesseract.image_to_string(grayscale, config = custom_config)

        if 'crewmate' in membertype.lower():
            self.crewmate = True
            self.imposter = False
            self.ingame = True
        if 'impostor' in membertype.lower():
            self.imposter = True
            self.crewmate = False
            self.ingame = True
        if 'victory' in membertype.lower():
            if self.ingame:
                if self.crewmate:
                    self.crewmatewins += 1
                else:
                    self.imposterwins += 1
            self.ingame = False
        if 'defeat' in membertype.lower():
            if self.ingame:
                if self.crewmate:
                    self.crewmateloses += 1
                else:
                    self.imposterloses += 1
            self.ingame = False

    def lightstate(self):
        pyautogui.screenshot('pictures/amongus/fixlights.png', region = (25,250,275,280))
        img = cv2.imread('pictures/amongus/fixlights.png')
        mask = cv2.inRange(img, (0, 200, 110), (50, 255,255))
        mask2 = cv2.inRange(img, (0, 0, 110), (100, 60,255))
        lightstring = pytesseract.image_to_string(mask, config= r'-l eng --oem 3 --psm 11')
        lightstring2 = pytesseract.image_to_string(mask2, config= r'-l eng --oem 3 --psm 11')
        cv2.imwrite('pictures/amongus/fixlightsthreshold.png',mask)
        if 'lights' in lightstring.lower() or 'lights' in lightstring2.lower():
            if self.lights:    
                return False
            else:
                self.lights = True
                return True
        else:
            if self.lights:
                self.lights = False
                return True
            else:
                return False

    def maptype(self):
        pic = pyautogui.screenshot('pictures/amongus/map.png', region = (15,60,370,50))
        pic = cv2.imread('pictures/amongus/map.png')
        custom_config = r'-l eng --oem 3 --psm 8'
        mapstring = pytesseract.image_to_string(pic, config = custom_config)
        print(mapstring)
        if 'skeld' in mapstring.lower():
            print('skeld')
        if 'polus' in mapstring.lower():
            print('polus')
        if 'mira' in mapstring.lower():
            print('mira')

class pogostuckcv():

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
        self.percentageint = 0
        self.previousint = 0
        self.furthestpercentageint = 0
        self.furthestpreviousint = 0

    def percentage(self):
        self.previousint = self.percentageint
        pic = pyautogui.screenshot('pictures/pogostuck/percentage.png', region = (390, 5, 75, 40))
        pic = cv2.imread('pictures/pogostuck/percentage.png')
        mask = cv2.inRange(pic, (0, 200, 110), (50, 255,255))
        custom_config = r'-l eng --oem 3 --psm 7 -c tessedit_char_whitelist="1234567890."'
        percentagestring = pytesseract.image_to_string(mask, config = custom_config)
        percentagelist = re.split(r'',percentagestring)
        intstring = ''
        percentageintlist = []
        for i in percentagelist:
            try:
                myint = int(i)
                percentageintlist.insert(myint, i)
                intstring = intstring + i
            except:
                pass
        if percentageintlist:
            self.percentageint = int(intstring)
        print(self.percentageint)

        if self.previousint - self.percentageint > 10:
            print('zap') 
        
    def furthest(self):
        self.furthestpreviousint = self.furthestpercentageint
        pic = pyautogui.screenshot('pictures/pogostuck/furthest.png', region = (500, 5, 75, 40))
        pic = cv2.imread('pictures/pogostuck/furthest.png')
        mask = cv2.inRange(pic, (0, 200, 110), (50, 255,255))
        custom_config = r'-l eng --oem 3 --psm 7 -c tessedit_char_whitelist="1234567890."'
        percentagestring = pytesseract.image_to_string(mask, config = custom_config)
        percentagelist = re.split(r'',percentagestring)
        intstring = ''
        percentageintlist = []
        for i in percentagelist:
            try:
                myint = int(i)
                percentageintlist.insert(myint, i)
                intstring = intstring + i
            except:
                pass
        if percentageintlist:
            self.furthestpercentageint = int(intstring)
