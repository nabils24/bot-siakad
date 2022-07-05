import pytz
import time
from datetime import datetime


def runscript(email, password, browser):
    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id")
    except:
        browser.close()
        return False

    emailinput, passinput, enter = browser.find_element_by_name('email'), browser.find_element_by_name('password'), browser.find_element_by_id('masuk')

    emailinput.send_keys(str(email))
    passinput.send_keys(str(password))
    enter.click()

    time.sleep(1)

    try:
        browser.get("https://siswa.smktelkom-mlg.sch.id/presnow")
    except:
        browser.close()
        return False

    while True:
        time_now = datetime.now(pytz.timezone('Asia/Jakarta'))
        if time_now.strftime('%H') == '06':
            return absen(browser)


def absen(browser):
    try:
        browser.refresh()
        inputabsen, simpan = browser.find_element_by_xpath('//label[@for="M"]'), browser.find_element_by_id("simpan")
        inputabsen.click()
        simpan.click()
    except:
        pass

    return cek_absen(browser)
    


def cek_absen(browser):
    try:
        tmp = browser.find_element_by_class_name('number')
        if tmp.text == 'Masuk':
            logout(browser)
            return True
        else:
            logout(browser)
            return False
    except:
        browser.refresh()
        return cek_absen(browser)


def logout(browser):
    browser.get("https://siswa.smktelkom-mlg.sch.id/login/logout")
    browser.close()


def override(email, password, browser):
    while True:
        if runscript(email, password, browser) == True:
            return True
