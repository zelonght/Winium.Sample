import os

PRODUCT_P4C = '1'
PRODUCT_P4C_REMOTE = '2'
PRODUCT_MERGEME = '3'
PRODUCT_MERGEME_REMOTE = '4'
PRODUCT_WINCALC = '5'
PRODUCT_WINCALC_REMOTE = '6'
PRODUCT_TEST_INVISIBLE_ELEMENTS = '7'
P4C_USERNAME = 'usename'
P4C_PASSWORD = 'password'
PRODUCTS = {
    PRODUCT_P4C: {
        'apps_path': os.path.join(os.environ.get('LOCALAPPDATA'), 'Personify', 'Omni', 'PersonifyLauncher.exe'),
        'apps_process_name': 'Personify'
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
        'apps_process_name': ''
    }
}
WINIUM_LOCAL_PATH = 'D:/Winium.Desktop.Driver.exe'
WINIUM_REMOTE_PATH = 'C:/ui_test/winiumdriver/Winium.Desktop.Driver.exe'
HUB_REMOTE = 'http://192.168.70.46:9999'
HUB_LOCAL = 'http://localhost:9999'
