import os
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions


# ============================================================
# Configuration
# ============================================================

PCLOUDY_URL = "https://device.pcloudy.com/appiumcloud/wd/hub"

PCLOUDY_EMAIL = os.environ["PCLOUDY_EMAIL"]
PCLOUDY_ACCESS_KEY = os.environ["PCLOUDY_ACCESS_KEY"]

PCLOUDY_DEVICE = os.environ.get(
    "PCLOUDY_DEVICE",
    "Apple_iPhone13_Ios_17.2.1"
)

APP_NAME = os.environ.get(
    "PCLOUDY_APPLICATION_NAME",
    "firebase-ios-app.ipa"
)

BUNDLE_ID = os.environ.get(
    "IOS_BUNDLE_ID",
    "org.reactjs.native.example.SwagLabsMobileApp"
)


# ============================================================
# Test
# ============================================================

def test_ios_app_lifecycle():

    print("=" * 50)
    print("Starting iOS Appium lifecycle test")
    print("=" * 50)

    print(f"Device : {PCLOUDY_DEVICE}")
    print(f"Bundle : {BUNDLE_ID}")
    print(f"App    : {APP_NAME}")

    print("=" * 50)

    options = XCUITestOptions()

    # ========================================================
    # iOS capabilities
    # ========================================================

    options.set_capability(
        "platformName",
        "iOS"
    )

    options.set_capability(
        "appium:automationName",
        "XCUITest"
    )

    # ========================================================
    # pCloudy authentication
    # ========================================================

    options.set_capability(
        "pCloudy_Username",
        PCLOUDY_EMAIL
    )

    options.set_capability(
        "pCloudy_ApiKey",
        PCLOUDY_ACCESS_KEY
    )

    # ========================================================
    # IMPORTANT:
    # Use ONLY pCloudy_DeviceFullName for device selection.
    #
    # Do NOT add:
    # deviceName
    # platformVersion
    # pCloudy_DeviceVersion
    # pCloudy_DeviceManufacturer
    # pCloudy_MinVersion
    # ========================================================

    options.set_capability(
        "pCloudy_DeviceFullName",
        PCLOUDY_DEVICE
    )

    # ========================================================
    # pCloudy application
    # ========================================================

    options.set_capability(
        "pCloudy_ApplicationName",
        APP_NAME
    )

    options.set_capability(
        "pCloudy_DurationInMinutes",
        10
    )

    # ========================================================
    # iOS application
    # ========================================================

    options.set_capability(
        "appium:bundleId",
        BUNDLE_ID
    )

    options.set_capability(
        "appium:newCommandTimeout",
        300
    )

    # ========================================================
    # Create Appium session
    # ========================================================

    print("Creating pCloudy Appium session...")

    driver = webdriver.Remote(
        command_executor=PCLOUDY_URL,
        options=options
    )

    print("Appium session created successfully")

    try:

        # ====================================================
        # 1. LAUNCH
        # ====================================================

        print("")
        print("1. LAUNCH APPLICATION")

        driver.activate_app(BUNDLE_ID)

        time.sleep(5)

        print("Current package:", driver.current_package)

        print("RESULT: Application launched successfully")

        # ====================================================
        # 2. WAIT
        # ====================================================

        print("")
        print("2. WAITING FOR APPLICATION")

        time.sleep(5)

        print("RESULT: Application remained active")

        # ====================================================
        # 3. BACKGROUND
        # ====================================================

        print("")
        print("3. BACKGROUNDING APPLICATION")

        driver.background_app(5)

        print("Appium background_app command executed")

        print("RESULT: Background operation completed successfully")

        # ====================================================
        # 4. FOREGROUND
        # ====================================================

        print("")
        print("4. BRINGING APPLICATION TO FOREGROUND")

        driver.activate_app(BUNDLE_ID)

        time.sleep(5)

        print(
            "Package after foreground:",
            driver.current_package
        )

        print(
            "RESULT: Application successfully returned to foreground"
        )

        # ====================================================
        # 5. TERMINATE
        # ====================================================

        print("")
        print("5. TERMINATING APPLICATION")

        driver.terminate_app(BUNDLE_ID)

        time.sleep(3)

        print("Appium terminate_app command executed")

        print("RESULT: Application terminated successfully")

        # ====================================================
        # 6. RELAUNCH
        # ====================================================

        print("")
        print("6. RELAUNCHING APPLICATION")

        driver.activate_app(BUNDLE_ID)

        time.sleep(8)

        print(
            "Package after relaunch:",
            driver.current_package
        )

        if driver.current_package != BUNDLE_ID:
            raise AssertionError(
                f"Application did not relaunch correctly. "
                f"Expected: {BUNDLE_ID}, "
                f"Got: {driver.current_package}"
            )

        print("RESULT: Application relaunched successfully")

        # ====================================================
        # PASS
        # ====================================================

        print("")
        print("=" * 50)
        print("APP LIFECYCLE TEST PASSED")
        print("=" * 50)

    finally:

        # ====================================================
        # Close Appium session
        # ====================================================

        print("")
        print("Closing Appium session")

        driver.quit()

        print("Appium session closed")
