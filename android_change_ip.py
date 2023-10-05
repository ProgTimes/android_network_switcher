import os
import sys

BASE_DIR = os.path.dirname(sys.argv[0])
adb_path = os.path.join(BASE_DIR, 'adb', 'adb.exe')


def change_ip():
    os.system(f"{adb_path} shell settings put global airplane_mode_on 1")
    os.system(f"{adb_path} shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
    os.system(f"{adb_path} shell settings put global airplane_mode_on 0")
    os.system(f"{adb_path} shell am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")

change_ip()