import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class viz:
    def __init__(self, dpath:str=None) -> None:
        self.data = None
        if dpath and dpath.endswith(".csv"):
            self.data = pd.read_csv(dpath)
        self.savepath = "plots"
        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)

    def q1(self, savepath:str=None) -> None:
        
        """ 展示2015年最畅销的5个公司的销量、销售金额以及它们在全年的占比 """
        
        data15 = self.data[self.data["Sale year"] == 2015]
        grouped = data15.groupby('COMPANY').agg({
            'sellingprice': 'sum',
            'Sale year': 'count'
        }).rename(columns={'Sale year': 'SalesCount'})
        top5 = grouped.nlargest(5, 'sellingprice')
        total_sales = top5['sellingprice'].sum()
        top5['SalesPercentage'] = top5['sellingprice'] / total_sales * 100

        # 将其余公司的销售金额汇总为一个名称为“其他”的行
        other_sales_counts = grouped.drop(top5.index)['SalesCount'].sum()
        other_sales = grouped.drop(top5.index)['sellingprice'].sum()
        other_sales_percentage = other_sales / total_sales * 100

        # 添加“其他”行到 top5 中
        top5.loc['Others'] = [other_sales, other_sales_counts, other_sales_percentage]

        # 制图
        plt.figure(figsize=(8, 8))
        plt.pie(top5['sellingprice'], labels=top5.index, autopct='%1.1f%%', startangle=140)

        plt.title('Top 5 Companies by Sales Amount in 2015')
        plt.legend()

        plt.axis('equal') 
        plt.show()
        plt.savefig(os.path.join(savepath, "q1.png") if savepath and os.path.exists(savepath) else os.path.join(self.savepath, "q1.png"))

    def q2(self, savepath:str=None) -> None:

        """ 分别展示2014和2015年2年，外观颜色销量前3的里程数分布情况（堆积柱状图，以里程数标签分组）。 """

        # 找到最畅销颜色并且取出对应的里程标签数据
        top_colors_14 = self.get_top_color(2014, 3)
        top_colors_15 = self.get_top_color(2015, 3)
        stacked_data_14 = self.prepare_stacked_data(top_colors_14)
        stacked_data_15 = self.prepare_stacked_data(top_colors_15)

        # 制图
        _, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

        stacked_data_14.plot(kind='bar', stacked=True, ax=axes[0], colormap='viridis')
        axes[0].set_title('Mileage Distribution by Top 3 Colors in 2014')
        axes[0].set_xlabel('Color')
        axes[0].set_ylabel('Count')

        stacked_data_15.plot(kind='bar', stacked=True, ax=axes[1], colormap='viridis')
        axes[1].set_title('Mileage Distribution by Top 3 Colors in 2015')
        axes[1].set_xlabel('Color')
        axes[1].set_ylabel('Count')

        plt.tight_layout()
        plt.show()
        plt.savefig(os.path.join(savepath, "q2.png") if savepath and os.path.exists(savepath) else os.path.join(self.savepath, "q2.png"))

    def q3(self, savepath:str=None) -> None:
        
        """ 2014年每周六平均销售金额是多少？（选一种合适的图表，展示周一到周日的销售平均金额）。 """

        data14 = self.data[self.data['Sale year'] == 2014]
        avg_sales = data14.groupby('sale Day')['sellingprice'].mean().reindex(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

        # 制图
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_sales.index, y=avg_sales.values, palette='viridis')
        plt.title('Average Selling Price by Day of the Week in 2014')
        plt.xlabel('Day of the Week')
        plt.ylabel('Average Selling Price')
        plt.show()
        plt.savefig(os.path.join(savepath, "q3.png") if savepath and os.path.exists(savepath) else os.path.join(self.savepath, "q3.png"))


    def get_top_color(self, year:int=2014, top_n:int=3) -> pd.DataFrame:
        
        """ 辅助方法，获取单年最畅销颜色 """

        data_yearly = self.data[self.data['Sale year'] == year]
        top_colors = data_yearly.groupby('color')['sellingprice'].sum().nlargest(top_n).index
        return data_yearly[data_yearly['color'].isin(top_colors)]
    

    def prepare_stacked_data(self, df_in:pd.DataFrame=None) -> pd.DataFrame:
        
        """ 辅助方法，数据叠加准备 """
        
        return df_in.groupby(['color', 'tag']).size().unstack().fillna(0)



if __name__ == "__main__":
    dpath = "result/result.csv"
    vizer = viz(dpath=dpath)
    vizer.q1()
    vizer.q2()
    vizer.q3()