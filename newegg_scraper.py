from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=virtual+reality&N=-1&isNodeId=1'
#opens connection and grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name\n"
f.write(headers)



for container in containers:
	brand = container.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text.strip()
	#price_container = container.findAll("li", {"class":"price-current"})
	#product_price = price_container[0].text.strip()


	print("brand: " + brand)
	print("product_name: " + product_name)
	#print("product_price: " + product_price)

	f.write(brand + "," + product_name.replace(",", "|") + "\n")
f.close()