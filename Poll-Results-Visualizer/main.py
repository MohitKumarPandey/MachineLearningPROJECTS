import os
from src.data_loader import create_dataset, load_data
from src.data_cleaning import clean_data
from src.analysis import overall_analysis, region_analysis, age_analysis
from src.visualization import plot_bar, plot_pie, plot_region
from src.insights import generate_insights

def main():
    # Load or create data
    if not os.path.exists("data/poll_data.csv"):
        df = create_dataset()
    else:
        df = load_data()

    # Clean data
    df = clean_data(df)

    # Analysis
    counts, percentages = overall_analysis(df)
    region_data = region_analysis(df)

    # Visualization
    plot_bar(counts)
    plot_pie(percentages)
    plot_region(region_data)

    # Insights
    generate_insights(percentages)

if __name__ == "__main__":
    main()