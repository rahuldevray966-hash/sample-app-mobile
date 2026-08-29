import os

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"

PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]

PCLOUDY_DEVICE = os.getenv(
    "PCLOUDY_DEVICE",
    "Apple_iPhone17_Ios_26.5.1"
)

PCLOUDY_APPLICATION_NAME = os.getenv(
    "PCLOUDY_APPLICATION_NAME",
    "firebase-ios-app.ipa"
)

IOS_BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "org.reactjs.native.example.SwagLabsMobileApp"
)


@pytest.mark.ios
def test_ios_session():

    print("=" * 60)
    print("iOS pCloudy Appium Session Test")
    print("=" * 60)

    print(f"Device      : {PCLOUDY_DEVICE}")
    print(f"Application : {PCLOUDY_APPLICATION_NAME}")
    print(f"Bundle ID   : {IOS_BUNDLE_ID}")
    print("=" * 60)

    options = XCUITestOptions()

    # ==========================================
    # Standard Appium / iOS
    # ==========================================

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
        IOS_BUNDLE_ID
    )

    # ==========================================
    # pCloudy
    # ==========================================

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
        PCLOUDY_APPLICATION_NAME
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        15
    )

    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    # ==========================================
    # Timeouts
    # ==========================================

    options.set_capability(
        "appium:newCommandTimeout",
        300
    )

    options.set_capability(
        "appium:wdaLaunchTimeout",
        90000
    )

    options.set_capability(
        "appium:wdaConnectionTimeout",
        90000
    )

    print("")
    print("Creating pCloudy Appium session...")
    print("Please wait...")

    driver = None

    try:

        driver = webdriver.Remote(
            command_executor=PCLOUDY_URL,
            options=options
        )

        print("")
        print("=" * 60)
        print("SUCCESS: pCloudy Appium session created")
        print("=" * 60)

        print(f"Session ID: {driver.session_id}")

        print("")
        print("iOS application session is working.")

    finally:

        if driver:

            print("")
            print("Closing Appium session...")

            try:
                driver.quit()
                print("Appium session closed successfully.")
            except Exception as exc:
                print(f"Warning while closing session: {exc}")
