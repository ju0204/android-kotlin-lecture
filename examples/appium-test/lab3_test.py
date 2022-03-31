from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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
            textView = self.driver.find_element(AppiumBy.ID, 'textView')
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
        
            



if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\lab3\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '11.0'

    print('Test for English')
    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION, 'en', 'US')
    print('test1:', chw.test_week6_lab3_1())
    print('test2:', chw.test_week6_lab3_2(dog_cat = True))
    print('test3:', chw.test_week6_lab3_2(dog_cat = False))
    del chw
    
    print('Test for Korean')
    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION, 'ko', 'KR')
    print('test1:', chw.test_week6_lab3_1('ko'))
    print('test2:', chw.test_week6_lab3_2(lang='ko', dog_cat = True))
    print('test3:', chw.test_week6_lab3_2(lang='ko', dog_cat = False))

