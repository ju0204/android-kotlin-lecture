from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
        'enforceAppInstall' : 'true'
    }

    def __init__(self, appLocation, platformVersion = '12.0'):
        self.ANDROID_BASE_CAPS['app'] = appLocation
        self.ANDROID_BASE_CAPS['platformVersion'] = platformVersion
        self.driver = webdriver.Remote(
            command_executor=self.EXECUTOR,
            desired_capabilities=self.ANDROID_BASE_CAPS
        )
        self.driver.implicitly_wait(10)
        
        
    def press_home(self):
        self.driver.press_keycode(3) # keycode HOME

           
    def test_week4(self, std_number, click_num):
        try:
            wait = WebDriverWait(self.driver, 10)
            button = wait.until(EC.element_to_be_clickable((By.ID,'button')))
            #button = self.driver.find_element(AppiumBy.ID, 'button')
            if button.text == std_number:
                for i in range(click_num):
                    button.click()
                if button.text == f'TEST {click_num}' or button.text == f'TEST{click_num}':
                    return 'OK'
                else:
                    return '버튼 클릭 번호 오류'
            else:
                return '학번 오류'
        except:
            return '버튼 ID button 오류'
            



if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\MyApplication\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '11.0'

    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION)
    r = chw.test_week4('2012345', 3)   # 학번과 클릭 수
    print(r)

