from shops.Takealot import Takealot

takealot = Takealot()
# takealot.phones()
data = takealot.getAllproducts('https://www.takealot.com/all')
print(data)