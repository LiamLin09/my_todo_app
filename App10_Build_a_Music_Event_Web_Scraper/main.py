import time
import requests
import selectorlib
import smtplib
import ssl


URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# scrape the page source from the URL
def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "liamlin5609@gmail.com"
    password = "bvdqqqetcxrryqvr"

    receiver = "liamlin5609@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(result):
    with open('data.txt', 'a') as file:
        file.write(result + '\n')


def read(result):
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    while True:
        result = extract(scrape(URL))
        print(result)

        content = read(result)
        if result != 'No upcoming tours':
            if result not in content:
                store(result)
                send_email(message='Hey, Ryan is super BAD!!')
        time.sleep(3)
