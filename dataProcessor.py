import pandas as pd
import os


class dataProcessor:

    def __init__(self, dpath:str=None) -> None:
        
        """ Initializer, take data path and load data from the given path """
        
        # Assign datapath
        if dpath and os.path.exists(dpath):
            self.dpath = dpath
        else:
            self.dpath = "simpleDataAnalysis/data/car_prices_3.csv"
        
        # Get data
        self.getData()


    def getData(self):
        """ Get data from the given datapath """
        if self.dpath.endswith('.csv'):
            self.data = pd.read_csv(self.dpath)

    def removeEmpty(self, subset:list[str] = None):
        """ Remove rows with empty company, odometer, color, sellingprice """
        if not subset:
            subset = ['COMPANY', 'odometer', 'color', 'Sale year', 'sellingprice']
        self.data.dropna(subset=subset)
    
    def dataWashing(self):
        """ Data reformalization, keep consistency """
        self.data['COMPANY'] = self.data['COMPANY'].str.capitalize()

    def dataTagging(self):
        """ Give tag to data referring to the value of the odometer """
        self.data["tag"] = self.data["odometer"].apply(self.tagBaseOdometer)
        
    def dataSave(self, outputPath:str=None, index:bool=False, sep:str=","):
        """ Save the processed data under the given path """
        if not outputPath:
            outputPath = "simpleDataAnalysis/result"
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        self.data.to_csv(os.path.join(outputPath, "result.csv"), index=index, sep=sep)

    @staticmethod
    def tagBaseOdometer(od) -> str:
        if od < 1e4:
            tag = "<10K"
        elif 1e4 <= od < 5e4:
            tag = "10K-50K"
        elif 5e4 <= od < 1e5:
            tag = "50K-100K"
        else:
            tag = ">100K"
        return tag



if __name__ == "__main__":
    """ Test """
    # Customize the data path
    dpath = "../data/car_prices_3.csv"
    # Initialize the dummy data processor
    dproc = dataProcessor(dpath=dpath)
    # 1. remove data with empty info, 
    # categories to be evaluated can be customized, default -> ['COMPANY', 'odometer', 'color', 'Sale year', 'sellingprice']
    dproc.removeEmpty()
    # 2. capitalize the first letter of the company
    dproc.dataWashing()
    # 3. tag data based on the odometer values
    dproc.dataTagging()
    # 4. save result to the result folder
    dproc.dataSave(index=False)

