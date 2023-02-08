import matplotlib.pyplot as plt
import pandas as pd

class TenderAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        
    def histogram(self, x_col, bins=10, color="green", edgecolor="black", linewidth=1.2, alpha=0.7, rwidth=0.85, align="mid"):
        x = self.df[x_col]
        plt.hist(x, bins=bins, color=color, edgecolor=edgecolor, linewidth=linewidth, alpha=alpha, rwidth=rwidth, align=align)
        plt.xlabel(x_col, labelpad=10, fontsize=10)
        plt.ylabel("Tenders Count", rotation=90, labelpad=10, fontsize=10)
        plt.title("Histogram of Tenders Over Time")
        plt.show()
        
    def pie_chart(self, groupby_col):
        occur = self.df.groupby([groupby_col]).size()
        print(occur)
        x = occur
        plt.pie(x), plt.axis('equal')
        plt.xlabel(f"{groupby_col} Frequency", labelpad=10, fontsize=10)
        plt.ylabel("Tenders Count", rotation=90, labelpad=10, fontsize=10)
        plt.title("Pie Chart of Tenders Over Time")
        plt.show()
        
    def scatter_plot(self, x_col, y_col):
        x = self.df[x_col].values.tolist()
        y = self.df[y_col].values.tolist()
        plt.scatter(x, y, marker='o', color='red', s=10)
        plt.xscale('linear')
        plt.xlabel(x_col, labelpad=10, fontsize=10)
        plt.show()

# usage
ta = TenderAnalysis("tenders.csv")
ta.histogram("e-Published Date")
ta.pie_chart("Organisation Chain")
ta.scatter_plot("Closing Date", "Opening Date")
