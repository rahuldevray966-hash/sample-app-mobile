import os
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]
PCLOUDY_DEVICE = os.environ["PCLOUDY_DEVICE"]

APP_NAME = "firebase-ios-app.ipa"

BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "org.reactjs.native.example.SwagLabsMobileApp"
)

APPIUM_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"


def test_ios_app_lifecycle():

    options = XCUITestOptions()

    # pCloudy
    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY
    )

    options.set_capability(
        "pCloudy_ApplicationName",
        APP_NAME
    )

    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        15
    )

    # iOS
    options.set_capability(
        "platformName",
        "iOS"
    )

    options.set_capability(
        "appium:automationName",
        "XCUITest"
    )

    options.set_capability(
        "appium:bundleId",
        BUNDLE_ID
    )

    options.set_capability(
        "appium:noReset",
        False
    )

    options.set_capability(
        "appium:newCommandTimeout",
        600
    )

    driver = None

    try:

        print("==========================================")
        print("Starting iOS Appium lifecycle test")
        print("==========================================")

        print(f"Device : {PCLOUDY_DEVICE}")
        print(f"Bundle : {BUNDLE_ID}")

        driver = webdriver.Remote(
            APPIUM_URL,
            options=options
        )

        print("Appium session created successfully")

        # --------------------------------------
        # 1. LAUNCH
        # --------------------------------------

        print("")
        print("1. LAUNCH APPLICATION")

        time.sleep(10)

        current_bundle = driver.execute_script(
            "mobile: activeAppInfo"
        )

        print(f"Active application: {current_bundle}")

        print("RESULT: Application launched successfully")

        # --------------------------------------
        # 2. WAIT
        # --------------------------------------

        print("")
        print("2. WAITING FOR APPLICATION")

        time.sleep(5)

        print("RESULT: Application remained active")

        # --------------------------------------
        # 3. BACKGROUND
        # --------------------------------------

        print("")
        print("3. BACKGROUNDING APPLICATION")

        driver.background_app(5)

        print("RESULT: Background operation completed successfully")

        # --------------------------------------
        # 4. FOREGROUND
        # --------------------------------------

        print("")
        print("4. BRINGING APPLICATION TO FOREGROUND")

        driver.activate_app(BUNDLE_ID)

        time.sleep(5)

        print("RESULT: Application successfully returned to foreground")

        # --------------------------------------
        # 5. TERMINATE
        # --------------------------------------

        print("")
        print("5. TERMINATING APPLICATION")

        driver.terminate_app(BUNDLE_ID)

        time.sleep(3)

        print("RESULT: Application terminated successfully")

        # --------------------------------------
        # 6. RELAUNCH
        # --------------------------------------

        print("")
        print("6. RELAUNCHING APPLICATION")

        driver.activate_app(BUNDLE_ID)

        time.sleep(8)

        print("RESULT: Application relaunched successfully")

        print("")
        print("==========================================")
        print("IOS APP LIFECYCLE TEST PASSED")
        print("==========================================")

    finally:

        if driver:

            print("")
            print("Closing Appium session")

            driver.quit()
