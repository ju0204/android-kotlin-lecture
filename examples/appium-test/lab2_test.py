from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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


    def test_lab2(self, filepath, filepath2):
        try:
            self.driver.save_screenshot(filepath)
            #swipe(startX, startY, endX, endY, duration)
            self.driver.swipe(150, 600, 150, 100, 100)
            self.driver.swipe(150, 600, 150, 100, 100)
            return self.driver.save_screenshot(filepath2)
        except:
            return False



if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\MyApplication\app\build\intermediates\apk\debug\app-debug.apk'
    ANDROID_VERSION = '12.0'

    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION)
    r = chw.test_lab2('screeshot.png', 'screenshot2.png')
    print(r)

