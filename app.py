from shops.Takealot import Takealot
from shops.IncredibleConnection import IncredibleConnection
from shops.Evetech import Evetech

takealot = Takealot()
# incredibleConnection = IncredibleConnection()
# evetech = Evetech()

# data = evetech.getAllproducts('https://evetech.co.za/laptop-specials-for-sale-south-africa.aspx')

data = takealot.getAllproducts('https://www.takealot.com/all')
print(data)

# data = incredibleConnection.getAllproducts('https://www.incredible.co.za/products')