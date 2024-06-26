# simpleDataAnalysis
A simple data analysis tool to solve some specific problems   

## 1. Data preprocessing:

1. Removing invalid data rows
2. Keeping the consistency of the data, e.g. capitalizing the first letter of the company name
3. tagging sold units regarding their odometer values

### Usage

Run the following code.

```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install pip
pip install pandas matplotlib seaborn
python3 dataProcessor.py
```

This script `dataProcessor.py` will create a folder named `result` and save the processed data into this folder and name it as `result.csv`.

## 2. Data Visualization

1. Displays the sales volume, sales amount, and the percentage of sales volume and sales amount in the whole year of the top five companies in 2015 (other companies are set as Others and are also displayed)
2. The following table shows the mileage distribution of the top three exterior color sales in 2014 and 2015 (stacked bar chart, grouped by mileage label).
3. Display the average sales amount from Monday to Sunday

Run the following code.

```
python3 viz.py
```

This script will create a folder named `plots` under the current repository, generates and save 3 plots, which are named `q1.png`, `q2.png` and `q3.png` corresponding to 3 subtasks, into the folder `plots`.