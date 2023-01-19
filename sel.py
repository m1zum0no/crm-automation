from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
# file that contains the link for data to be parsed and login credentials
from credentials import login, password, link


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(link)
driver.maximize_window()
wait = WebDriverWait(driver, timeout=10)


# Logging in 
driver.find_element('name', 'login').send_keys(login)
driver.find_element('name', 'password').send_keys(password)
driver.find_element('xpath', "//*[@type='submit']").click()


def write_to_file():
    with open("orders.py", "a") as output:
        for order_entry in parsed_data:
            output.write(':'.join(order_entry) + '\n')


def parse_table():
    rows = len(driver.find_elements('xpath', '//*[@id="table_clients_orders"]/tr'))
    for tr in range(rows):
        try:
            #order_id = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr})').get_attribute("data-id")
            device_selector = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr}) > td:nth-child(10) > span.visible-lg')
            device = device_selector.get_attribute("title") if device_selector.get_attribute("title") else device_selector.text 
            client_name = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr}) > td:nth-child(14)').get_attribute("title")
            price_paid = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr}) > td:nth-child(13)').text
            phone_number = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr}) > td:nth-child(14) > div > a').text
            service_rendered = driver.find_element('css selector', f'#table_clients_orders > tr:nth-child({tr}) > td.hidden-xs.center.hide > i').get_attribute("title")
            if price_paid == '1000' or price_paid == '1500' and 'Диагностика' in service_rendered:
                continue 
            if phone_number not in clients_logged:
                parsed_data.append([phone_number, device, client_name])
                clients_logged.add(phone_number)
        except:
            pass


def table_loaded(driver: webdriver.Chrome):
    return driver.find_elements('class name', 'pagination')


parsed_data = []
clients_logged = set()
while True:
    wait.until(table_loaded)
    parse_table()
    next_button = driver.find_element('css selector', '.pagination > li:last-child > a')
    if next_button.get_attribute('href') == driver.current_url:
        write_to_file()
        quit()
    next_button.click()
