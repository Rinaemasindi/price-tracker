from shops.Takealot import Takealot
from shops.IncredibleConnection import IncredibleConnection
from shops.Evetech import Evetech

takealot = Takealot()
# incredibleConnection = IncredibleConnection()
# evetech = Evetech()
# data = evetech.getAllproducts('https://evetech.co.za/laptop-specials-for-sale-south-africa.aspx')

takealot_tv = "https://www.takealot.com/tv-audio-video/tvs-25953?sort=Relevance"
takealot_laptops = "https://www.takealot.com/tv-audio-video/tvs-25953?sort=Relevance"
takealot_gaming_laptops = "https://www.takealot.com/computers/gaming-29053?sort=Relevance"
takealot_gaming_netbooks = "https://www.takealot.com/computers/netbooks-29052?sort=Relevance"
takealot_phones = "https://www.takealot.com/cellular-gps/cellphones-26249"

data = takealot.getAllproducts("https://www.takealot.com/all?after=WzQyNy40NjcsNTQ0OTUwOTFd")
print(data)

# data = incredibleConnection.getAllproducts('https://www.incredible.co.za/products')