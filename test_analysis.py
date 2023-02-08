import unittest
import matplotlib.pyplot as plt
import pandas as pd

class TestDataVisualization(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("tenders.csv")
        
    def test_histogram(self):
        x = self.df["e-Published Date"]
        hist = plt.hist(x, bins=10, color="green", edgecolor="black", linewidth=1.2, alpha=0.7, rwidth=0.85, align="mid")
        self.assertEqual(hist[1][0], x.min())
        self.assertEqual(hist[1][-1], x.max())
        self.assertGreater(hist[0].sum(), 0)
        
    def test_pie_chart(self):
        occur = self.df.groupby(['Organisation Chain']).size()
        pie = plt.pie(occur, labels=occur.index)
        self.assertEqual(len(pie[0]), len(occur))
        self.assertEqual(len(pie[1]), len(occur))
        
    def test_scatter_plot(self):
        x = self.df["Closing Date"].values.tolist()
        y = self.df["Opening Date"].values.tolist()
        scatter = plt.scatter(x, y, marker='o', color='red', s=10)
        self.assertEqual(scatter.get_sizes().shape, (len(x),))
        self.assertEqual(scatter.get_offsets().shape, (len(x), 2))

if __name__ == '__main__':
    unittest.main()
