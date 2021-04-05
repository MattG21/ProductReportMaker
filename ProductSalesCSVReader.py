import csv # csv from standard python library
import sys # sys from standard python library

class ProductSalesCSVReader:
    
    def productlist_from_productCSV(self, productCSV): # function to return a product list dict from a csv file
        productList = {}
        try:
            with open(productCSV, newline='') as csvFile:
                reader = csv.reader(csvFile, delimiter=',')
                for row in reader: # would be good to check for a valid product before adding it to products
                    productList[row[0]] = row[1:] # put each product into a dictionary
            return productList # return product dictionary
        except OSError:
            print("Could not open/read file")
            
    def salelist_from_saleCSV(self, saleCSV): # function to return a sale list dict from a csv file
        saleList = {}
        try:
            with open(saleCSV, newline='') as csvFile:
                reader = csv.reader(csvFile, delimiter=',')
                for row in reader: # should check for valid sale transaction before adding to sale list
                    saleList[row[0]] = row[1:] # put each product into a dictionary
            return saleList # return product dictionary
        except OSError:
            print("Could not open/read file")
                                                  

    def product_report_to_CSV(self, fileName, productReport): # function to create a product report csv from product report dict
        try:
            with open(fileName, 'w', newline='') as csvFile:
                fieldnames = ['Name', 'GrossRevenue', 'TotalUnits']
                writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
                for product in productReport: # for each 3-tuple in sorted product list, write to output file.
                    writer.writerow({'Name': product[0], 'GrossRevenue': product[1],'TotalUnits': product[2]}) # (k:v) -> [v1,v2]) => [(k,v1,v2)] 
    
        except OSError:
            print("Could not write to file")

