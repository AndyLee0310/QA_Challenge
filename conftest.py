import logging
import pytest
import subprocess

from appium.options.common import AppiumOptions


def get_android_devices():
    try:
        # Run the adb devices command
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        lines = result.stdout.splitlines()
        devices = [line.split()[0] for line in lines if line.endswith('device')]

        if len(devices) == 0:
            return None  # No devices detected
        elif len(devices) == 1:
            logging.info(f'Device detected: {devices[0]}')
            return devices[0]  # Only one device detected, returning the device
        else:
            return devices  # Multiple devices detected, returning the device list

    except Exception as e:
        logging.error(e)

def check_package_installed(device, package_name):
    try:
        # Run the adb shell command to check if the specified package is installed
        result = subprocess.run(
            ['adb', '-s', device, 'shell', 'pm', 'list', 'packages', package_name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if package_name in result.stdout:
            return True
        else:
            return False

    except Exception as e:
        logging.error(e)
        return False


@pytest.fixture(scope='session')
def android_setting():
    PACKAGE_NAME = 'hko.MyObservatory_v1_0'
    ACTIVITY_NAME = '.AgreementPage'
    NO_RESET =  False

    devices = get_android_devices()
    if devices is None:
        raise Exception('No device detected. Please check if the device is connected.')
    elif isinstance(devices, list):
        raise Exception('Multiple devices detected. Please connect only one device.')
    else:
        if not check_package_installed(devices, PACKAGE_NAME):
            raise Exception(f'The device does not have the {PACKAGE_NAME} application installed')

    logging.info(f'Use the device: {devices}')

    options = AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '14')
    options.set_capability('deviceName', devices)
    options.set_capability('automationName', 'uiautomator2')
    options.set_capability('appPackage', PACKAGE_NAME)
    options.set_capability('appActivity', ACTIVITY_NAME)
    options.set_capability('noReset', NO_RESET)
    options.set_capability('autoGrantPermissions', True)
    options.set_capability('enableMultiWindows', True)
    options.set_capability('shouldTerminateApp', True)
    options.set_capability('disableWindowAnimation', True)
    options.set_capability('waitForIdleTimeout', 100)

    return options
