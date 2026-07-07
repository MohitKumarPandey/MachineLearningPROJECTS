def generate_insights(percentages):
    top_choice = percentages.idxmax()
    top_value = percentages.max()

    insight = f"Most preferred option is {top_choice} with {top_value:.2f}% votes."
    
    print("\n--- Insights ---")
    print(insight)

    return insight