from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?N=100007709%20601194948%20601202919%20601203901%20601203927%20601205646%20601294835%20601295933%20601296377%20601301599%20601305993%20601321572%20601323902%20601326374%20601331379%20601341679&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close() 

#html parsing
page_soup = soup(page_html, "html.parser")

#Saves all containers
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name, shipping\n"

f.write("headers")

for container in containers:
	brand = container.div.div.img["title"]
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	print("brand: " + brand)
	print("product name: " + product_name)
	print("shipping: " + shipping)

	f.write(brand + "," +  
product_name.replace(","," ") + "," + 
shipping + "\n")

f.close();


