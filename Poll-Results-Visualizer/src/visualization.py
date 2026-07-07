import matplotlib.pyplot as plt
import os

os.makedirs("outputs/plots", exist_ok=True)

def plot_bar(counts):
    counts.plot(kind='bar', title="Poll Results - Bar Chart")
    plt.savefig("outputs/plots/bar_chart.png")
    plt.close()

def plot_pie(percentages):
    percentages.plot(kind='pie', autopct='%1.1f%%', title="Poll Results - Pie Chart")
    plt.savefig("outputs/plots/pie_chart.png")
    plt.close()

def plot_region(region_data):
    region_data.plot(kind='bar', stacked=True, title="Region-wise Preferences")
    plt.savefig("outputs/plots/region_chart.png")
    plt.close()