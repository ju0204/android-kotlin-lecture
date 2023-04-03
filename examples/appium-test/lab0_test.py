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
        'allowTestPackages': True,  # add -t flags to adb command when install the app package
        'enforceAppInstall' : True,
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


    def test_myapp(self):
        try:
            txtview = self.driver.find_element(AppiumBy.ID, 'txtView')
            if txtview.text == 'Hello World!':
                return 'OK'
            else:
                return 'Incorrect Text'
        except:
            return 'No txtView ID'



if __name__ == '__main__':
    # 테스트할 APK 파일의 위치
    DEF_APP_LOCATION = r'C:\Users\juh02\AndroidStudioProjects\Test\app\build\outputs\apk\debug'
    ANDROID_VERSION = '13'

    chw = CheckHW(DEF_APP_LOCATION, ANDROID_VERSION)
    r = chw.test_myapp()
    print(r)

