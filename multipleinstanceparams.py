import os

PRODUCT_NONE = '1'
PRODUCT_P4C = '2'
PRODUCT_P4C_REMOTE = '3'
PRODUCT_MERGEME = '4'
PRODUCT_MERGEME_REMOTE = '5'
PRODUCT_WINCALC = '6'
PRODUCT_WINCALC_REMOTE = '7'
PRODUCT_TEST_INVISIBLE_ELEMENTS = '8'
PRODUCT_NOTEPAD = '9'
PRODUCT_IEXPLORE = '10'
PRODUCT_FIREFOX = '11'
PRODUCT_CHROME = '12'
LOCAL_P4C_USERNAME = 'username'
LOCAL_P4C_PASSWORD = 'password'
REMOTE_P4C_USERNAME = 'username'
REMOTE_P4C_PASSWORD = 'password'
PRODUCTS = {
    PRODUCT_NONE: {
        'apps_path': '',
        'apps_process_name': ''
    },
    PRODUCT_P4C: {
        'apps_path': os.path.join(os.environ.get('LOCALAPPDATA'), 'Personify', 'Omni', 'PersonifyLauncher.exe')#,
        #'apps_process_name': 'Personify'
    },
    PRODUCT_P4C_REMOTE: {
        'apps_path': u'C:/Users/psytest/AppData/Local/Personify/Omni/PersonifyLauncher.exe',
        'apps_process_name': 'Personify'
    },
    PRODUCT_MERGEME: {
        'apps_path': os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Personify', 'Live', 'PersonifyLive.exe'),
        'apps_process_name': ''
    },
    PRODUCT_MERGEME_REMOTE: {
        'apps_path': u'C:/Program Files (x86)/Personify/Live/bin/PersonifyLive.exe',
        'apps_process_name': ''
    },
    PRODUCT_WINCALC: {
        'apps_path': os.path.join(os.environ.get('WINDIR'), 'System32', 'calc.exe'),
        'apps_process_name': 'Calculator'
    },
    PRODUCT_WINCALC_REMOTE: {
        'apps_path': u'C:/Windows/System32/calc.exe',
        'apps_process_name': 'Calculator'
    },
    PRODUCT_TEST_INVISIBLE_ELEMENTS: {
        'apps_path': os.path.join(os.getcwd(), 'AppContainInvisibleElems', 'AppToTestInvisibleElement.exe'),
        'apps_process_name': 'AppToTestInvisibleElement'
    },
    PRODUCT_NOTEPAD: {
        'apps_path': os.path.join(os.environ.get('WINDIR'), 'System32', 'notepad.exe'),
        'apps_process_name': 'Notepad'
    },
    PRODUCT_IEXPLORE: {
        'apps_path': os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Internet Explorer', 'iexplore.exe'),
        'apps_process_name': 'iexplore'
    },
    PRODUCT_FIREFOX: {
        'apps_path': os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Mozilla Firefox', 'firefox.exe'),
        'apps_process_name': 'firefox'
    },
    PRODUCT_CHROME: {
        'apps_path': os.path.join(os.environ.get('PROGRAMFILES(X86)'), 'Google', 'Chrome', 'Application', 'chrome.exe'),
        'apps_process_name': 'chrome'
    }
}
WINIUM_LOCAL_PATH = 'D:/Winium.Desktop.Driver.exe'
WINIUM_REMOTE_PATH = 'C:/ui_test/winiumdriver/Winium.Desktop.Driver.exe'
HUB_REMOTE = 'http://192.168.70.46:9999'
HUB_LOCAL = 'http://localhost:9999'
