class Product:
    
    def __init__(self, id, name, price, lotSize):
        self.id = id
        self.name = name
        self.price = price
        self.lotSize = lotSize
        self.totalUnits = 0
        self.grossRevenue = 0
    
    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.name, self.price, self.lotSize, self.grossRevenue , self.totalUnits)

    def set_id(self, newId):
        self.id = newId
    
    def set_name(self, newName):
        self.name = newName
    
    def set_price(self, newPrice):
        self.price = newPrice
    
    def set_lotsize(self, newLotSize):
        self.lotSize = newLotSize
    
    def add_total_units(self, newTotalUnits):
        self.totalUnits += newTotalUnits
    
    def add_gross_revenue(self, newGrossRevenue):
        self.grossRevenue += newGrossRevenue
    