from ProductSalesCSVReader import ProductSalesCSVReader
from Products import Products

import sys

def main():
    myArgs = sys.argv
    
    if len(myArgs) != 4: # if we don't pass in 3 args as filenames we will not write report
        print("Invalid argument length")
    else:
        try: 
            myCSVReader = ProductSalesCSVReader()
            
            productList = myCSVReader.productlist_from_productCSV(myArgs[1]) #get product dict
            saleList = myCSVReader.salelist_from_saleCSV(myArgs[2]) # get sale dict
            
            myProducts = Products()
            myProducts.fill_product_list(productList)
            myProducts.update_product_sales(saleList)
            productReport = myProducts.sorted_product_report()

            myCSVReader.product_report_to_CSV(myArgs[3], productReport) # write product report to csv file
        except TypeError:
            print("Missing csv files to run program")
main()

# could be made into a class