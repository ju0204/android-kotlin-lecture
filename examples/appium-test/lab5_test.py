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
        'uiautomator2ServerInstallTimeout' : 20000,
        'adbExecTimeout' : 20000
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


    def test_lab5(self):
        wait = WebDriverWait(self.driver, 10)

        # Home fragment
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'
            
        try: 
            tvTitle = self.driver.find_element(AppiumBy.ID, 'tvTitle')
        except:
            return 'ID가 tvTitle인 텍스트뷰를 찾을 수 없음'
        if tvTitle.text != 'Home':
            return 'tvTitle의 내용이 Home이 아님'
            
        button.click()
        time.sleep(1)
        
        # Nav1 fragment
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'
            
        try: 
            tvTitle = self.driver.find_element(AppiumBy.ID, 'tvTitle')
        except:
            return 'ID가 tvTitle인 텍스트뷰를 찾을 수 없음'
        if tvTitle.text != 'Nav1':
            return 'tvTitle의 내용이 Nav1이 아님'
            
        button.click()
        time.sleep(1)
        
        # Nav2 fragment
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'
            
        try: 
            tvTitle = self.driver.find_element(AppiumBy.ID, 'tvTitle')
        except:
            return 'ID가 tvTitle인 텍스트뷰를 찾을 수 없음'
        if tvTitle.text != 'Nav2':
            return 'tvTitle의 내용이 Nav2가 아님'
            
        button.click()
        time.sleep(1)
        
        # Home fragment
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'
            
        button.click()
        time.sleep(1)
        
        # Nav1 fragment
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'ID가 button인 버튼을 찾을 수 없음'
            
        try: 
            textView = self.driver.find_element(AppiumBy.ID, 'textView')
        except:
            return 'ID가 textView인 텍스트뷰를 찾을 수 없음'
        if textView.text != '4':
            return 'textView의 내용이 4가 아님'
        
        self.driver.press_keycode(4)  # Back key
        time.sleep(1)
        
        # Home fragment
        try: 
            tvTitle = self.driver.find_element(AppiumBy.ID, 'tvTitle')
        except:
            return 'ID가 tvTitle인 텍스트뷰를 찾을 수 없음 - Home으로 되돌아가지 않음'
        if tvTitle.text != 'Home':
            return 'tvTitle의 내용이 Home이 아님 - Home으로 되돌아가지 않음'
            
        self.driver.press_keycode(4)  # Back key
        time.sleep(1)
              
        try:
            button = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        except:
            return 'OK'

        return "홈 화면이 나오지 않고, 다시 다른 프래그먼트로 되돌아감."
       


if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\Lab5\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '12.0'
    
    print('''
    1. Appium 서버는 실행 했나요?
    2. 에뮬레이터를 실행하거나 디바이스를 연결 했나요?
    3. 에뮬레이터는 정상적으로 동작 중인가요? 에뮬레이터가 멈춰있다면 cold boot하세요.
    4. DEF_APP_LOCATION은 본인의 app-debug.apk를 제대로 가리키고 있나요?
    5. ANDROID_VERSION은 에뮬레이터나 디바이스의 안드로이드 버전과 일치하나요?
    ''')

    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION)
    r = chw.test_lab5()
    if r == 'OK':
        score = 100
    else:
        score = 0
    print(score, r)

