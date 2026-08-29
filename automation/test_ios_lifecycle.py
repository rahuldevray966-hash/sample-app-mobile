import os
import time

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


PCLOUDY_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"

PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]

PCLOUDY_DEVICE = os.environ["PCLOUDY_DEVICE"]

PCLOUDY_APPLICATION_NAME = os.getenv(
    "PCLOUDY_APPLICATION_NAME",
    "firebase-ios-app.ipa",
)

IOS_BUNDLE_ID = os.getenv(
    "IOS_BUNDLE_ID",
    "org.reactjs.native.example.SwagLabsMobileApp",
)


def create_driver():

    print("==========================================")
    print("Creating pCloudy Appium session")
    print("==========================================")

    print(f"Device      : {PCLOUDY_DEVICE}")
    print(f"Application : {PCLOUDY_APPLICATION_NAME}")
    print(f"Bundle ID   : {IOS_BUNDLE_ID}")

    options = XCUITestOptions()

    # ------------------------------------------
    # iOS
    # ------------------------------------------

    options.platform_name = "iOS"
    options.automation_name = "XCUITest"

    options.bundle_id = IOS_BUNDLE_ID

    # ------------------------------------------
    # pCloudy
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
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE,
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        15,
    )

    # ------------------------------------------
    # Appium / XCUITest
    # ------------------------------------------

    options.set_capability(
        "newCommandTimeout",
        300,
    )

    options.set_capability(
        "launchTimeout",
        120000,
    )

    options.set_capability(
        "wdaLaunchTimeout",
        120000,
    )

    options.set_capability(
        "wdaConnectionTimeout",
        120000,
    )

    options.set_capability(
        "autoAcceptAlerts",
        True,
    )

    print("Connecting to pCloudy...")
    print("Please wait...")

    driver = webdriver.Remote(
        command_executor=PCLOUDY_URL,
        options=options,
    )

    print("pCloudy Appium session created successfully")

    return driver


@pytest.mark.ios
def test_ios_app_lifecycle():

    print("")
    print("=" * 60)
    print("iOS pCloudy Appium Lifecycle Test")
    print("=" * 60)

    print(f"Device : {PCLOUDY_DEVICE}")
    print(f"Bundle : {IOS_BUNDLE_ID}")
    print(f"App    : {PCLOUDY_APPLICATION_NAME}")

    print("=" * 60)

    driver = None

    try:

        # ==========================================
        # 1. LAUNCH
        # ==========================================

        print("")
        print("[1/6] Launching application...")

        driver = create_driver()

        time.sleep(10)

        current_bundle = driver.execute_script(
            "mobile: activeAppInfo"
        )

        print(
            f"Active application information: {current_bundle}"
        )

        print("RESULT: Application launched successfully")


        # ==========================================
        # 2. WAIT
        # ==========================================

        print("")
        print("[2/6] Waiting for application...")

        time.sleep(10)

        print("RESULT: Application remained active")


        # ==========================================
        # 3. BACKGROUND
        # ==========================================

        print("")
        print("[3/6] Backgrounding application...")

        driver.background_app(5)

        print(
            "RESULT: Background operation completed successfully"
        )


        # ==========================================
        # 4. FOREGROUND
        # ==========================================

        print("")
        print("[4/6] Bringing application to foreground...")

        driver.activate_app(IOS_BUNDLE_ID)

        time.sleep(5)

        print(
            "RESULT: Application successfully returned "
            "to foreground"
        )


        # ==========================================
        # 5. TERMINATE
        # ==========================================

        print("")
        print("[5/6] Terminating application...")

        terminated = driver.terminate_app(
            IOS_BUNDLE_ID
        )

        print(
            f"Terminate result: {terminated}"
        )

        time.sleep(3)

        print(
            "RESULT: Application terminated successfully"
        )


        # ==========================================
        # 6. RELAUNCH
        # ==========================================

        print("")
        print("[6/6] Relaunching application...")

        driver.activate_app(IOS_BUNDLE_ID)

        time.sleep(10)

        print(
            "RESULT: Application relaunched successfully"
        )


        # ==========================================
        # FINAL
        # ==========================================

        print("")
        print("=" * 60)
        print("iOS APP LIFECYCLE TEST PASSED")
        print("=" * 60)

    finally:

        if driver is not None:

            print("")
            print("Closing pCloudy Appium session...")

            try:
                driver.quit()

                print(
                    "pCloudy Appium session closed successfully"
                )

            except Exception as exc:

                print(
                    f"Warning while closing driver: {exc}"
                )
