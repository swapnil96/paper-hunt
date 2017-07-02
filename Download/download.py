from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shutil import move
import time
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display
import glob

# Start the browser with the following properties

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/swapnil/Documents/Work/Python/Project/Download/PDF')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
profile.set_preference("pdfjs.disabled",True)

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox(firefox_profile=profile)
browser.get("https://scholar.google.co.in/scholar?hl=en&q=association+mining")

# Function to delay the execution so to download the papers
def delay(t):
    time.sleep(t)

# Function to download a paper
def download(link):

    # print link
    link = "window.open('"+link+"', 'new_window')"
    browser.execute_script(link)
    browser.switch_to_window(browser.window_handles[1])
    delay(4)
    browser.close()
    browser.switch_to_window(browser.window_handles[0])

# Direct pdf link from Google
def first_option(top_element):

    try:
        direct_download = top_element.find_element_by_class_name("gs_ggs")
        name = find_name(top_element)
        link = direct_download.find_element_by_tag_name("a").get_attribute("href")
        download(link)
        change_name(name+" direct")

    except Exception as e:
        raise e

# Download from IEEE page
def second_option(top_element):
    flag = 0
    try:
        first_link = top_element.find_element_by_class_name("gs_rt")
        name = find_name(top_element)
        link = first_link.find_element_by_tag_name("a").get_attribute("href")
        link = "window.open('"+link+"', 'new_window')"
        browser.execute_script(link)
        browser.switch_to_window(browser.window_handles[1])
        flag = 1
        # while True:
        #     try:
        #         down = browser.find_element_by_class_name("doc-actions-link")
        #         break
        #
        #     except Exception as e:
        #         pass
        delay(10)
        down = browser.find_element_by_class_name("doc-actions-link")

        link = down.get_attribute("href")
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        download(link)
        change_name(name+" ieee")

    except Exception as e:
        if flag == 1:
            browser.close()
            browser.switch_to_window(browser.window_handles[0])

        raise e

# From science direct website
def third_option(top_element):

    flag = 0
    try:
        first_link = top_element.find_element_by_class_name("gs_rt")
        name = find_name(top_element)
        link = first_link.find_element_by_tag_name("a").get_attribute("href")
        link = "window.open('"+link+"', 'new_window')"
        browser.execute_script(link)
        browser.switch_to_window(browser.window_handles[1])
        flag = 1
        # while True:
        #     try:
        #         down = top_element.find_element_by_class_name("extendedPdfBox")
        #         break
        #
        #     except Exception as e:
        #         pass

        delay(10)
        down = top_element.find_element_by_class_name("extendedPdfBox")
        down = down.find_element_by_class_name("pdfLink")
        link = down.find_element_by_tag_name("a")
        link = link.get_attribute("pdfurl")
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        download(link)
        change_name(name+" science direct")

    except Exception as e:
        if flag == 1:
            browser.close()
            browser.switch_to_window(browser.window_handles[0])

        raise e

# From emarald website
def fourth_option(top_element):
    flag = 0
    try:
        first_link = top_element.find_element_by_class_name("gs_rt")
        name = find_name(top_element)
        link = first_link.find_element_by_tag_name("a").get_attribute("href")
        link = "window.open('"+link+"', 'new_window')"
        browser.execute_script(link)
        browser.switch_to_window(browser.window_handles[1])
        flag = 1
        # while True:
        #     try:
        #         down = browser.find_element_by_class_name("tools1")
        #         break
        #
        #     except Exception as e:
        #         pass

        delay(10)
        down = browser.find_element_by_class_name("tools1")

        link = down.find_elements_by_tag_name("li")
        link = link[1].find_element_by_tag_name("a")
        link = link.get_attribute("href")
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        download(link)
        change_name(name+" emarald")

    except Exception as e:
        if flag == 1:
            browser.close()
            browser.switch_to_window(browser.window_handles[0])

        raise e


def find_name(top_element):

    name_element = top_element.find_element_by_class_name("gs_rt")
    name_element = name_element.find_element_by_tag_name("a")
    name = name_element.text
    return name


def recent():

    newest = max(glob.iglob('/home/swapnil/Documents/Work/Python/Project/Download/PDF/*.pdf'), key=os.path.getctime)
    return newest

def change_name(name):

    newest = recent()
    time.sleep(20)
    move(newest, os.getcwd()+"/PDF/"+name+".pdf")


def process(top_element):

    try:
        first_option(top_element)
        return 1

    except Exception as e:
        try:
            second_option(top_element)
            return 1

        except Exception as e:
            try:
                third_option(top_element)
                return 1

            except Exception as e:
                try:
                    fourth_option(top_element)
                    return 1

                except Exception as e:
                    return 0

delay(2)

main_pdf = browser.find_element_by_class_name("gs_r")
process(main_pdf)

second_link = main_pdf.find_element_by_class_name("gs_ri")
second_link = second_link.find_element_by_class_name("gs_fl")
link = second_link.find_element_by_tag_name("a").get_attribute("href")
browser.get(link)
while True:
    try:
        all_search = browser.find_elements_by_class_name("gs_r")
        break
    except Exception as e:
        pass

counter = 1
done  = len(all_search)
while counter < 40:
    print done, counter
    if done < 1:
        nav = browser.find_element_by_id("gs_n")
        nav = nav.find_elements_by_tag_name("a")
        nav = nav[-1]
        link = nav.get_attribute("href")
        browser.get(link)
        while True:
            try:
                all_search = browser.find_elements_by_class_name("gs_r")
                break
            except Exception as e:
                pass

        done = len(all_search)

        # nav = browser.find_element_by_id("gs_nm")
        # nav = nav.find_elements_by_tag_name("button")
        # nav = nav[-1]
        # link = nav.get_attribute("href")
        # browser.get(link)
        # nav.click()
        # while True:
        #     try:
        #         all_search = browser.find_elements_by_class_name("gs_r")
        #         break
        #     except Exception as e:
        #         pass
        #
        # done = len(all_search)


    else:
        for search in all_search:
            done -= 1
            print counter, done, "down"
            counter += process(search)

time.sleep(3)
browser.close()
display.stop()