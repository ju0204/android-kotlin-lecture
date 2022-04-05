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
 

    def test_lab4(self, number=123, inc=2, dec=1):
        wait = WebDriverWait(self.driver, 10)

        try:
            editText = wait.until(EC.element_to_be_clickable((By.ID, 'editText')))
        except:
            return 'ID가 editText인 에디트텍스트를 찾을 수 없음'

        editText.send_keys(f'{number}')

        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
            button.click()
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'


        # SecondActivity 가 시작됨

        try:
            buttonInc = wait.until(EC.element_to_be_clickable((By.ID, 'buttonInc')))
        except:
            return 'ID가 buttonInc인 버튼을 찾을 수 없음'

        try:
            buttonDec = wait.until(EC.element_to_be_clickable((By.ID, 'buttonDec')))
        except:
            return 'ID가 buttonDec인 버튼을 찾을 수 없음'

        for i in range(inc):
            buttonInc.click()

        for i in range(dec):
            buttonDec.click()

        # 화면을 회전시켜서 Configuration change를 고의로 발생시킴
        self.driver.orientation = 'LANDSCAPE'
        self.driver.orientation = 'PORTRAIT'

        self.driver.back()

        result_number = number + inc - dec

        try:
            editText = wait.until(EC.element_to_be_clickable((By.ID, 'editText')))
        except:
            return 'ID가 editText인 에디트텍스트를 찾을 수 없음'

        if editText.text == f'{result_number}':
            return 100, 'OK'
        else:
            return 0, f'결과 숫자가 틀림, {result_number} 가 아님'
       


if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\Lab4Application\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '12.0'

    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION)
    score, r = chw.test_lab4(1234, 3, 2)
    print(score, r)

