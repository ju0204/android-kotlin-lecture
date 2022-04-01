from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CheckHW():
    MAIN_ACTIVITY = '.MainActivity'
    EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
    ANDROID_BASE_CAPS = {
        'app': 'app-debug.apk',  # path to the app package
        'automationName': 'UIAutomator2',
        'platformName': 'Android',
        'platformVersion': '12.0',  # platform version of emulator or device where app will be tested
        'deviceName': 'Android Emulator',
        'allowTestPackages': 'true',  # add -t flags to adb command when install the app package
        'enforceAppInstall' : 'true',
        'language' : 'ko',
        'locale' : 'KR'
    }

    def __init__(self, appLocation, platformVersion = '12.0', language = 'en', locale = 'US'):
        self.ANDROID_BASE_CAPS['app'] = appLocation
        self.ANDROID_BASE_CAPS['platformVersion'] = platformVersion
        self.ANDROID_BASE_CAPS['language'] = language
        self.ANDROID_BASE_CAPS['locale'] = locale
        
        self.driver = webdriver.Remote(
            command_executor=self.EXECUTOR,
            desired_capabilities=self.ANDROID_BASE_CAPS
        )
        self.driver.implicitly_wait(10)
 

    def test_week6_lab3_1(self, lang='en'):
        textview_text = {'en':'Android Programming', 'ko':'안드로이드 프로그래밍'}
        
        try:
            wait = WebDriverWait(self.driver, 10)
            textView = wait.until(EC.visibility_of_element_located((By.ID, 'textView')))
            # textView = self.driver.find_element(AppiumBy.ID, 'textView')
        except:
            return '텍스트뷰 ID가 textView가 아님'
            
        if textView.text == textview_text[lang]:
            return 'OK'
        else:
            return f'텍스트뷰의 내용이 {textview_text[lang]}이 아님'
            
    
    def test_week6_lab3_2(self, lang='en', dog_cat = True):
        dog_text = {'en':'dog', 'ko':'개'}
        cat_text = {'en':'cat', 'ko':'고양이'}
        
        try:
            textView = self.driver.find_element(AppiumBy.ID, 'textView')
        except:
            return '텍스트뷰 ID가 textView가 아님'
        
        try:
            radioDog = self.driver.find_element(AppiumBy.ID, 'radioDog')
        except:
            return 'ID radioDog 없음'
            
        try:
            radioCat = self.driver.find_element(AppiumBy.ID, 'radioCat')
        except:
            return 'ID radioCat 없음'
            
        try:            
            button = self.driver.find_element(AppiumBy.ID, 'button')
        except:
            return '버튼 ID가 button이 아님'
        
        if dog_cat:
            radioDog.click()
        else:
            radioCat.click()
        button.click()
        
        time.sleep(0.5)
        
       
        if dog_cat:
            if textView.text == dog_text[lang]:
                return 'OK'
            else:
                return f'텍스트뷰 내용이 {dog_text[lang]}이 아님'
        else:
            if textView.text == cat_text[lang]:
                return 'OK'
            else:
                return f'텍스트뷰 내용이 {cat_text[lang]}이 아님'
        
            


def test_week6_lab3(appLocation, android_version):
    print('Test for English')
    chw = CheckHW(appLocation, android_version, 'en', 'US')
    r = [chw.test_week6_lab3_1(),
         chw.test_week6_lab3_2(dog_cat = True),
         chw.test_week6_lab3_2(dog_cat = False)]
    print('test1,2,3:', r)
    del chw
    
    print('Test for Korean')
    chw = CheckHW(appLocation, android_version, 'ko', 'KR')
    rk = [chw.test_week6_lab3_1('ko'),
          chw.test_week6_lab3_2(lang='ko', dog_cat = True),
          chw.test_week6_lab3_2(lang='ko', dog_cat = False)]
    print('test4,5,6:', rk)
    
    score = sum([15 for x in r if x == 'OK']) + sum([15 for x in rk if x == 'OK'])
    if score == 15 * 6:
        score = 100
    
    return (score, ','.join(r) + ',' + ','.join(rk))


if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\lab3\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '12.0'

    score, result = test_week6_lab3(DEF_APP_LOCATION, ANDROID_VERSION)
    print(score, result)

