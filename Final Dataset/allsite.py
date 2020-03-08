
from bs4 import BeautifulSoup
import requests
import time
import threading

# output csv file declared here
filename = "data.csv"

f = open(filename, 'w', encoding='utf-8-sig')

headers = "Product_Title,Price,Shop_Name,URL,Image_Url,Product_Code,Category_Id\n"

f.write(headers)

def webscrapBdstall():
    pages = [1,2]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.bdstall.com/graphics-card/{}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('div', class_='row product-cat-box s-top')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find(
                'div', class_='six columns product-cat-box-text')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='product-price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div',class_='six columns product-cat-box-text')
            
            link = product_link.a['href']

            image_url = product.find('div', class_='seven columns')

            url = image_url.img['src']

            data =title + "," + tk + "," + "BDSTALL" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)



def webscrapCvillage():

    pages = [1,2,3,4,5,6,7,8,9]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/graphics-card/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = soup.find_all('li',class_='col-sm-3')


        # using loop for grabing whole page data

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper()

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div', class_='pro-name')

            link = product_link.a['href']

            image_url = product.find('div', class_='img-box')

            url = image_url.img['src']
            
            data =title + "," + tk + "," + "COMPUTER VILLAGE" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)



def webscrapDolphin():
    source_link = requests.get('http://dolphin.computer/products?category=graphics-card').text

    # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
    soup = BeautifulSoup(source_link, 'lxml')

    # search element from specified url html

    body = soup.find('body')

    # here product-thumb is a css class so that i used it as a variable for better understanding

    product_thumb = body.find_all('a', class_='product-card')

    # using loop for grabing whole page data

    for product in product_thumb:

        product_name = product.find('span', class_='product-name')

        title = product_name.text.upper()

        product_price = product.find('span', class_='product-price')

        tk = product_price.text.replace(",", "").replace("Tk", "")

        link = product['href']
        
        image_url = product.find('div',class_='image-holder')

        url = image_url.img['src']

        data =title + "," + tk + "," + "DOLPHIN" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

        f.write(data)

    time.sleep(5)



def webscrapRyans():
    pages = [1,2,3,4,5,6,7]
    for page in pages:
        source_link = requests.get(
            'https://ryanscomputers.com/grid/desktop-component-graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_info = body.find_all('div', class_='product-box')

        # using loop for grabing whole page data

        for product in product_info:

            product_name = product.find('div', class_='product-content-info')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price')

            tk = product_price.text.replace("Tk","").replace(",","").replace("BDT","").strip()

            product_link = product.find('div', class_='product-content-info')

            link = product_link.a['href']

            image_url = product.find('div', class_='product-thumb')
            url = image_url.img['src']

            data =title + "," + tk + "," + "RYANS" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)
        time.sleep(5)



def webscrapStartech():
    pages = [1,2,3,4,5]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/component/graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper().replace(",","")

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            product_link = product.find('h4', class_='product-name')

            link = product_link.a['href']

            image_url = product.find('div',class_ = 'img-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "STARTECH" + ","+ link + "," + url + "," + "1" + "," + "1" + "\n"

            f.write(data)
        time.sleep(5)


def webscrapTechland():

    pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page={}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = soup.find_all('div', class_='product-thumb')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.strip()

            product_price = product.find('div', class_='price')

            tk = product_price.span.text

            product_link = product.find('div', class_='name')

            link = product_link.a['href']

            image_url = product.find('a', class_='product-img')

            url = image_url.img['src']



            data = (title + "," + tk.replace("৳","").replace(",","") + "," + "TECHLAND" + ","+ link +"," + url + "," + "1" + ","+ "1"+"\n")

            f.write(data)

        time.sleep(5)


def bdstallKeyboard():
    pages = [1,2]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.bdstall.com/computer-keyboard/{}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('div', class_='row product-cat-box s-top')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find(
                'div', class_='six columns product-cat-box-text')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='product-price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div',class_='six columns product-cat-box-text')
            
            link = product_link.a['href']

            image_url = product.find('div', class_='seven columns')

            url = image_url.img['src']

            data =title + "," + tk + "," + "BDSTALL" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

            f.write(data)
        time.sleep(5)


def bdstallMouse():

    pages = [1,2]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.bdstall.com/mouse/{}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('div', class_='row product-cat-box s-top')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find(
                'div', class_='six columns product-cat-box-text')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='product-price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div',class_='six columns product-cat-box-text')
            
            link = product_link.a['href']

            image_url = product.find('div', class_='seven columns')

            url = image_url.img['src']

            data =title + "," + tk + "," + "BDSTALL" + ","+ link + "," + url + "," + "1" + "," + "3" + "\n"

            f.write(data)

        time.sleep(5)


def bdstallMonitor():

    pages = [1,2,3,4]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.bdstall.com/monitor/{}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('div', class_='row product-cat-box s-top')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find(
                'div', class_='six columns product-cat-box-text')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='product-price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div',class_='six columns product-cat-box-text')
            
            link = product_link.a['href']

            image_url = product.find('div', class_='seven columns')

            url = image_url.img['src']

            data =title + "," + tk + "," + "BDSTALL" + ","+ link + "," + url + "," + "1" + "," + "4" + "\n"

            f.write(data)

        time.sleep(5)


def computervillageKeyboard():

    pages = [1,2,3,4,5,6,7]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/keyboard/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = soup.find_all('li',class_='col-sm-3')


        # using loop for grabing whole page data

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper()

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div', class_='pro-name')

            link = product_link.a['href']

            image_url = product.find('div', class_='img-box')

            url = image_url.img['src']
            
            data =title + "," + tk + "," + "COMPUTER VILLAGE" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

            f.write(data)

        time.sleep(5)


def computervillageMouse():

    pages = [1,2,3,4,5,6]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/mouse/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = soup.find_all('li',class_='col-sm-3')


        # using loop for grabing whole page data

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper()

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","")

            product_link = product.find('div', class_='pro-name')

            link = product_link.a['href']

            image_url = product.find('div', class_='img-box')

            url = image_url.img['src']
            
            data =title + "," + tk + "," + "COMPUTER VILLAGE" + ","+ link + "," + url + "," + "1" + "," + "3" + "\n"

            f.write(data)

        time.sleep(5)


def computervillageMonitor():

    pages = [1,2,3,4,5,6,7,8,9,10,11,12]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/monitor/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = soup.find_all('li',class_='col-sm-3')


        # using loop for grabing whole page data

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper().replace(",","")

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","").replace("Please call at 01713240766","0")

            product_link = product.find('div', class_='pro-name')

            link = product_link.a['href']

            image_url = product.find('div', class_='img-box')

            url = image_url.img['src']
            
            data =title + "," + tk + "," + "COMPUTER VILLAGE" + ","+ link + "," + url + "," + "1" + "," + "4" + "\n"

            f.write(data)

        time.sleep(5)


def ryansKeyboard():
    pages = [1,2,3,4,5]
    for page in pages:
        source_link = requests.get(
            'https://ryanscomputers.com/grid/desktop-component-keyboard?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_info = body.find_all('div', class_='product-box')

        # using loop for grabing whole page data

        for product in product_info:

            product_name = product.find('div', class_='product-content-info')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price')

            tk = product_price.text.replace("Tk","").replace(",","").replace("BDT","").strip()

            product_link = product.find('div', class_='product-content-info')

            link = product_link.a['href']

            image_url = product.find('div', class_='product-thumb')
            url = image_url.img['src']

            data =title + "," + tk + "," + "RYANS" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

            f.write(data)
        time.sleep(5)


def ryansMouse():
    pages = [1,2,3,4,5,6,7]
    for page in pages:
        source_link = requests.get(
            'https://ryanscomputers.com/grid/desktop-component-mouse?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_info = body.find_all('div', class_='product-box')

        # using loop for grabing whole page data

        for product in product_info:

            product_name = product.find('div', class_='product-content-info')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price')

            tk = product_price.text.replace("Tk","").replace(",","").replace("BDT","").strip()

            product_link = product.find('div', class_='product-content-info')

            link = product_link.a['href']

            image_url = product.find('div', class_='product-thumb')
            url = image_url.img['src']

            data =title + "," + tk + "," + "RYANS" + ","+ link + "," + url + "," + "1" + "," + "3" + "\n"

            f.write(data)
        time.sleep(5)


def ryansMonitor():

    pages = [1,2,3,4,5,6,7]
    for page in pages:
        source_link = requests.get(
            'https://ryanscomputers.com/grid/all-monitor-all-brand?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_info = body.find_all('div', class_='product-box')

        # using loop for grabing whole page data

        for product in product_info:

            product_name = product.find('div', class_='product-content-info')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price')

            tk = product_price.text.replace("Tk","").replace(",","").replace("BDT","").strip()

            product_link = product.find('div', class_='product-content-info')

            link = product_link.a['href']

            image_url = product.find('div', class_='product-thumb')
            url = image_url.img['src'].replace(",","")

            data =title + "," + tk + "," + "RYANS" + ","+ link + "," + url + "," + "1" + "," + "4" + "\n"

            f.write(data)
        time.sleep(5)


def startechKeyboard():

    pages = [1,2,3,4,5,6,7,8]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/accessories/keyboards?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper().replace(",","")

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            product_link = product.find('h4', class_='product-name')

            link = product_link.a['href']

            image_url = product.find('div',class_ = 'img-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "STARTECH" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

            f.write(data)
        time.sleep(5)


def startechMouse():
    pages = [1,2,3,4,5,6,7,8,9]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/accessories/mouse?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            product_link = product.find('h4', class_='product-name')

            link = product_link.a['href']

            image_url = product.find('div',class_ = 'img-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "STARTECH" + ","+ link + "," + url + "," + "1" + "," + "3" + "\n"

            f.write(data)
        time.sleep(5)


def startechMonitor():
    pages = [1,2,3,4,5,6,7,8,9,10]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/monitor?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper().replace(",","")

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            product_link = product.find('h4', class_='product-name')

            link = product_link.a['href']

            image_url = product.find('div',class_ = 'img-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "STARTECH" + ","+ link + "," + url + "," + "1" + "," + "4" + "\n"

            f.write(data)
        time.sleep(5)


def techlandKeyboard():

    pages = [1,2,3,4,5,6,7,8,9,10]
    for page in pages:

        source_link = requests.get(
            'https://www.techlandbd.com/accessories/computer-keyboard?page={}'.format(page)).text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding


        product_thumb = soup.find_all('div', class_='product-thumb')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price-normal')
            if(product_price):
                tk = product_price.text.replace("Tk","").replace(",","").replace("৳ ","").strip()
            else:
                tk = '0000'

            product_link = product.find('div',class_='name')

            link = product_link.a['href']

            image_url = product.find('a',class_='product-img')

            url = image_url.img['src'].replace(",","")

            data = (title + "," + tk.replace("৳","").replace(",","") + "," + "TECHLAND" + ","+ link +"," + url + "," + "1" + ","+ "2"+"\n")

            f.write(data)

        time.sleep(5)


def techlandMouse():

    pages = [1,2,3,4,5,6,7,8,9,10,11,12]
    for page in pages:

        source_link = requests.get(
            'https://www.techlandbd.com/accessories/shop-computer-mouse?page={}'.format(page)).text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding


        product_thumb = soup.find_all('div', class_='product-thumb')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price-normal')
            if(product_price):
                tk = product_price.text.replace("Tk","").replace(",","").replace("৳ ","").strip()
            else:
                tk = '0000'

            product_link = product.find('div',class_='name')

            link = product_link.a['href']

            image_url = product.find('a',class_='product-img')

            url = image_url.img['src'].replace(",","")

            data = (title + "," + tk.replace("৳","").replace(",","") + "," + "TECHLAND" + ","+ link +"," + url + "," + "1" + ","+ "3"+"\n")

            f.write(data)

        time.sleep(5)


def techlandMonitor():

    pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for page in pages:

        source_link = requests.get(
            'https://www.techlandbd.com/computer-monitor?page={}'.format(page)).text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding


        product_thumb = soup.find_all('div', class_='product-thumb')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('div', class_='name')

            title = product_name.a.text.replace(",","").upper()

            product_price = product.find('span', class_='price-normal')
            if(product_price):
                tk = product_price.text.replace("Tk","").replace(",","").replace("৳ ","").strip()
            else:
                tk = '0000'

            product_link = product.find('div',class_='name')

            link = product_link.a['href']

            image_url = product.find('a',class_='product-img')

            url = image_url.img['src'].replace(",","")

            data = (title + "," + tk.replace("৳","").replace(",","") + "," + "TECHLAND" + ","+ link +"," + url + "," + "1" + ","+ "4"+"\n")

            f.write(data)

        time.sleep(5)


def dolphinKeyboard():

    source_link = requests.get('https://dolphin.computer/products?category=keyboard').text

    # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
    soup = BeautifulSoup(source_link, 'lxml')

    # search element from specified url html

    body = soup.find('body')

    # here product-thumb is a css class so that i used it as a variable for better understanding

    product_thumb = body.find_all('a', class_='product-card')

    # using loop for grabing whole page data

    for product in product_thumb:

        product_name = product.find('span', class_='product-name')

        title = product_name.text.upper()

        product_price = product.find('span', class_='product-price')

        tk = product_price.text.replace(",", "").replace("Tk", "")

        link = product['href']
        
        image_url = product.find('div',class_='image-holder')

        url = image_url.img['src']

        data =title + "," + tk + "," + "DOLPHIN" + ","+ link + "," + url + "," + "1" + "," + "2" + "\n"

        f.write(data)

    time.sleep(5)


def dolphinMonitor():

    pages = [1,2,3]
    for page in pages:
        source_link = requests.get('https://dolphin.computer/products?category=monitor&sort=latest&page={}'.format(page)).text

        # source_link = requests.get('https://www.techlandbd.com/shop-graphics-card?page=1').text
        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        product_thumb = body.find_all('a', class_='product-card')

        # using loop for grabing whole page data

        for product in product_thumb:

            product_name = product.find('span', class_='product-name')

            title = product_name.text.upper().replace(",", "")

            product_price = product.find('span', class_='product-price')

            tk = product_price.text.replace(",", "").replace("Tk", "").replace(".00 34000.00", "").replace(".00 6500.00", "")

            link = product['href']
            
            image_url = product.find('div',class_='image-holder')

            url = image_url.img['src']

            data =title + "," + tk + "," + "DOLPHIN" + ","+ link + "," + url + "," + "1" + "," + "4" + "\n"

            f.write(data)

        time.sleep(5)





threading.Thread(target = webscrapBdstall).start()

threading.Thread(target = webscrapCvillage).start()

threading.Thread(target = webscrapDolphin).start()
    
threading.Thread(target = webscrapRyans).start()

threading.Thread(target = webscrapStartech).start()
    
threading.Thread(target = webscrapTechland).start()

threading.Thread(target = bdstallKeyboard).start()

threading.Thread(target = bdstallMouse).start()

threading.Thread(target = bdstallMonitor).start()

threading.Thread(target = computervillageKeyboard).start()

threading.Thread(target = computervillageMouse).start()

threading.Thread(target = computervillageMonitor).start()

threading.Thread(target = ryansKeyboard).start()

threading.Thread(target = ryansMouse).start()

threading.Thread(target = ryansMonitor).start()


threading.Thread(target = startechKeyboard).start()

threading.Thread(target = startechMouse).start()


threading.Thread(target = startechMonitor).start()


threading.Thread(target = techlandKeyboard).start()

threading.Thread(target = techlandMouse).start()

threading.Thread(target = techlandMonitor).start()


threading.Thread(target = dolphinKeyboard).start()

threading.Thread(target = dolphinMonitor).start()

