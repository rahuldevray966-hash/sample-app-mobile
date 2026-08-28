import os
import time

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"

PCLOUDY_EMAIL = os.getenv("PCLOUDY_EMAIL")
PCLOUDY_ACCESS_KEY = os.getenv("PCLOUDY_ACCESS_KEY")

PCLOUDY_DEVICE = os.getenv(
    "PCLOUDY_DEVICE",
    "Apple_iPhone17_Ios_26.5.1",
)

PCLOUDY_APPLICATION_NAME = os.getenv(
    "PCLOUDY_APPLICATION_NAME",
    "firebase-ios-app.ipa",
)

IOS_BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "org.reactjs.native.example.SwagLabsMobileApp",
)


def create_driver():
    """
    Create an Appium session on pCloudy iOS real device.
    """

    if not PCLOUDY_EMAIL:
        raise RuntimeError("PCLOUDY_EMAIL is missing")

    if not PCLOUDY_ACCESS_KEY:
        raise RuntimeError("PCLOUDY_ACCESS_KEY is missing")

    print("Creating pCloudy Appium session...")
    print(f"Device      : {PCLOUDY_DEVICE}")
    print(f"Application : {PCLOUDY_APPLICATION_NAME}")
    print(f"Bundle ID   : {IOS_BUNDLE_ID}")

    options = XCUITestOptions()

    # ------------------------------------------
    # Standard iOS capabilities
    # ------------------------------------------

    options.platform_name = "iOS"
    options.automation_name = "XCUITest"

    options.bundle_id = IOS_BUNDLE_ID

    # ------------------------------------------
    # pCloudy capabilities
    # ------------------------------------------

    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL,
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY,
    )

    options.set_capability(
        "pCloudy_ApplicationName",
        PCLOUDY_APPLICATION_NAME,
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        15,
    )

    # IMPORTANT:
    #
    # Use ONLY DeviceFullName for device selection.
    #
    # Do NOT send:
    # pCloudy_DeviceVersion
    # pCloudy_DeviceManufacturer
    # deviceName
    #
    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE,
    )

    # ------------------------------------------
    # Useful Appium/XCUITest settings
    # ------------------------------------------

    options.set_capability(
        "newCommandTimeout",
        300,
    )

    options.set_capability(
        "launchTimeout",
        90000,
    )

    options.set_capability(
        "wdaLaunchTimeout",
        90000,
    )

    options.set_capability(
        "wdaConnectionTimeout",
        90000,
    )

    options.set_capability(
        "autoAcceptAlerts",
        True,
    )

    print("Creating pCloudy session...")

    driver = webdriver.Remote(
        command_executor=PCLOUDY_URL,
        options=options,
    )

    return driver


@pytest.mark.ios
def test_ios_app_lifecycle():

    print("=" * 50)
    print("Starting iOS Appium lifecycle test")
    print("=" * 50)

    print(f"Device : {PCLOUDY_DEVICE}")
    print(f"Bundle : {IOS_BUNDLE_ID}")
    print(f"App    : {PCLOUDY_APPLICATION_NAME}")

    print("=" * 50)

    driver = None

    try:

        # ------------------------------------------
        # 1. Launch
        # ------------------------------------------

        print("\n[1/6] Launching application...")

        driver = create_driver()

        time.sleep(10)

        print("Application launched successfully.")

        # ------------------------------------------
        # 2. Wait
        # ------------------------------------------

        print("\n[2/6] Waiting...")

        time.sleep(10)

        print("Wait completed.")

        # ------------------------------------------
        # 3. Background
        # ------------------------------------------

        print("\n[3/6] Moving application to background...")

        driver.background_app(5)

        print("Background operation completed.")

        # ------------------------------------------
        # 4. Foreground
        # ------------------------------------------

        print("\n[4/6] Bringing application to foreground...")

        driver.activate_app(IOS_BUNDLE_ID)

        time.sleep(5)

        print("Foreground operation completed.")

        # ------------------------------------------
        # 5. Terminate
        # ------------------------------------------

        print("\n[5/6] Terminating application...")

        terminated = driver.terminate_app(IOS_BUNDLE_ID)

        print(f"Terminate result: {terminated}")

        time.sleep(3)

        # ------------------------------------------
        # 6. Relaunch
        # ------------------------------------------

        print("\n[6/6] Relaunching application...")

        driver.activate_app(IOS_BUNDLE_ID)

        time.sleep(10)

        print("Application relaunched successfully.")

        print("\n" + "=" * 50)
        print("iOS Appium lifecycle test PASSED")
        print("=" * 50)

    finally:

        if driver is not None:

            print("\nClosing Appium session...")

            try:
                driver.quit()
            except Exception as exc:
                print(f"Warning while closing driver: {exc}")
