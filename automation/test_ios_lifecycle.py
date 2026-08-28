import os
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"

PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]

PCLOUDY_DEVICE = "Apple_iPhone13_Ios_17.2.1"

APP_NAME = os.environ.get(
    "PCLOUDY_APPLICATION_NAME",
    "firebase-ios-app.ipa"
)

BUNDLE_ID = "org.reactjs.native.example.SwagLabsMobileApp"


def test_ios_app_lifecycle():

    print("=" * 50)
    print("Starting iOS Appium lifecycle test")
    print("=" * 50)

    print(f"Device : {PCLOUDY_DEVICE}")
    print(f"Bundle : {BUNDLE_ID}")
    print(f"App    : {APP_NAME}")
    print("=" * 50)

    options = XCUITestOptions()

    # iOS
    options.set_capability("platformName", "iOS")
    options.set_capability("automationName", "XCUITest")

    # pCloudy authentication
    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY
    )

    # pCloudy device
    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    # pCloudy application
    options.set_capability(
        "pCloudy_ApplicationName",
        APP_NAME
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        10
    )

    # iOS application
    options.set_capability(
        "bundleId",
        BUNDLE_ID
    )

    options.set_capability(
        "deviceName",
        "iPhone 13"
    )

    options.set_capability(
        "platformVersion",
        "17.2.1"
    )

    options.set_capability(
        "newCommandTimeout",
        300
    )

    print("Creating pCloudy Appium session...")

    driver = webdriver.Remote(
        command_executor=PCLOUDY_URL,
        options=options
    )

    print("Appium session created successfully")

    try:

        # ----------------------------------------
        # 1. LAUNCH
        # ----------------------------------------

        print("1. Launching application")

        driver.activate_app(BUNDLE_ID)

        time.sleep(5)

        print("Application launched")

        # ----------------------------------------
        # 2. BACKGROUND
        # ----------------------------------------

        print("2. Moving application to background")

        driver.background_app(5)

        print("Application moved to background")

        # ----------------------------------------
        # 3. FOREGROUND
        # ----------------------------------------

        print("3. Bringing application to foreground")

        driver.activate_app(BUNDLE_ID)

        time.sleep(3)

        print("Application returned to foreground")

        # ----------------------------------------
        # 4. TERMINATE
        # ----------------------------------------

        print("4. Terminating application")

        driver.terminate_app(BUNDLE_ID)

        time.sleep(3)

        print("Application terminated")

        # ----------------------------------------
        # 5. RELAUNCH
        # ----------------------------------------

        print("5. Relaunching application")

        driver.activate_app(BUNDLE_ID)

        time.sleep(5)

        print("Application relaunched")

        print("=" * 50)
        print("iOS lifecycle test PASSED")
        print("=" * 50)

    finally:

        print("Closing Appium session")

        driver.quit()

        print("Appium session closed")
