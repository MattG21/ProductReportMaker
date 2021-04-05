from Product import Product
from ProductSalesCSVReader import ProductSalesCSVReader

class Products:
    #to do -> add a way to update individual product
    def __init__(self):
        self.productList = {}
    
    def fill_product_list(self, csvProductList):
        for listProduct in csvProductList:
            productToAdd = Product(listProduct, csvProductList[listProduct][0], csvProductList[listProduct][1], csvProductList[listProduct][2])
            self.productList[productToAdd.id] = productToAdd

    def update_product_sales(self, csvSaleList):
        for sale in csvSaleList:
            productId, saleQuantity = csvSaleList[sale][0], float(csvSaleList[sale][2])
            product = self.productList[productId]

            totalUnitsToAdd = self.calculate_total_units(saleQuantity, float(product.lotSize))
            grossRevenueToAdd = self.calculate_gross_revenue(float(product.price), float(totalUnitsToAdd))
            
            product.add_gross_revenue(grossRevenueToAdd)
            product.add_total_units(totalUnitsToAdd)

    def sorted_product_report(self): # function to sort product report dict
        nonSorted = []
        for prod in self.productList: #created list of 3-tuple from product report dict then sort it 
            nonSorted.append((self.productList[prod].name,  self.productList[prod].grossRevenue, self.productList[prod].totalUnits))  # (k:v) -> [v1,v2]) => [(k,v1,v2)] 
        return (sorted(nonSorted, key = lambda x: x[1], reverse=True)) # Then sort the 3-tuple by descending order.  
                    
    def add_product(self, product):
        if self.productList[product.id] is not None:
            self.productList[product.id] = product
        else:
            print("Product with that id already exists")

    def get_product_by_id(self, productId):
        return self.productList[productId]
    
    def print_product(self, productId):
        print(self.productList[productId].name)

    def calculate_total_units(self, quantity, lotSize): # function to return total units
        try:
            return quantity * lotSize
        except:
            raise ValueError("Invalid input for total units")

    def calculate_gross_revenue(self, price, totalUnits): # function to return gross revenue
        try:
            return price * totalUnits
        except:
            raise ValueError("Invalid input for gross revenue")

    


