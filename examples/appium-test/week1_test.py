from androguard.core.bytecodes.apk import APK
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 테스트할 APK 파일의 위치
APP_LOCATION = r'C:\Users\jyheo\AndroidStudioProjects\MyApplication\app\build\intermediates\apk\debug\app-debug.apk'

ANDROID_BASE_CAPS = {
    'app': APP_LOCATION,
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '12.0',  # 오류 발생시 본인의 안드로이드 버전으로 바꿔야 합니다.
    'deviceName': 'Android Emulator',
    'allowTestPackages': 'true'
}

EXECUTOR = 'http://127.0.0.1:4723/wd/hub'


class CheckHW():
    PACKAGE = 'com.example.myapplication'
    MAIN_ACTIVITY = '.MainActivity'

    def __init__(self):
        apk = APK(APP_LOCATION)
        self.PACKAGE = apk.get_package()

        self.driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=ANDROID_BASE_CAPS
        )
        self.driver.implicitly_wait(10)

    def __del__(self):
        self.driver.remove_app(self.PACKAGE)  # remove app
        self.driver.quit()

    def test_myapp(self):
        txtview = self.driver.find_element(AppiumBy.ID, 'txtView')
        return txtview.text == 'Hello World!'


chw = CheckHW()
r = chw.test_myapp()
print(r)
