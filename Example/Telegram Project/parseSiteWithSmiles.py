import requests
from bs4 import BeautifulSoup as BS

LEN_BTWN_Text_n_Code = 40
LEN_BTWN_Smile_n_Text = 4
URL = "https://emojio.ru"
HEADERS = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.82 Safari/537.36',
           'accept' : '*/*'}
HOST = "https://emojio.ru"

def format_string(smile,text,code):
    str = smile
    for i in range(LEN_BTWN_Smile_n_Text - len(smile)):
        str = str + " "
    str = str + text
    for i in range(LEN_BTWN_Text_n_Code - len(text)):
        str = str + " "

    str = str + code
    return str.encode("utf-8")

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_page_links(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('li', class_='nav-item')
    links = []
    for item in items:
        links.append({
            f'link': HOST + item.find('a').get('href')
        })

    links = links[2:]
    return links

def get_links(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_ = 'emj vkno btn btn-default')
    links = []
    for item in items:
        links.append({
            f'link' : HOST + item.find('a').get('href')
        })
    return links

def get_string(html):
    soup = BS(html, 'html.parser')
    items_code = soup.find_all('table', class_="table table-striped table-hover")
    items_text = soup.find_all('input', class_="form-control")
    items_smile = soup.find_all('input', class_='form-control unicode emojicode')
    code = items_code[1].find_all_next('tr')[6]
    code = code.find('td').get_text()
    text = items_text[-1].get('value')
    smile = items_smile[0].get('value')

    code = code.replace("0x", "%").replace(" ", "").replace(",", "")
    if text.find(':') == -1:
        text = ''

    return format_string(smile, text, code)

def get_text(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('input', class_ = "form-control")
    text = items[-1].get('value')
    if text.find(':') == -1:
        text = ''
    return text

def get_smile(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('button', class_="btn btn-info copy_anons d-none" )
    smile = items[0].get('data-clipboard-text')
    return smile

def get_code(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('table', class_="table table-striped table-hover")
    code = items[1].find_all_next('tr')[6]
    code = code.find('td').get_text()
    code = code.replace("0x", "%").replace(" ", "").replace(",", "")
    return code

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        f = open('Emoji list.txt', 'wb')
        i = 1
        page_links = get_page_links(html.text)
        for value in page_links:
            page_url = value.get('link')
            html = get_html(page_url)
            links = get_links(html.text)
            for link in links:
                string = get_string(get_html(link.get('link')).text)
                f.write(string + '\n'.encode('utf-8'))
                print(f'{i}. ' + string.decode('utf-8'))
                i = i + 1

        f.close()
    else:
        print("Error")

parse()
