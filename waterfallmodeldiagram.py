import matplotlib.pyplot as plt

def draw_waterfall_model():
    # Define the stages of the waterfall model
    stages = [
        "Maintenance",
        "Verification",
        "Implementation",
        "Design",
        "Requirements"
    ]
    
    # Define the number of stages
    num_stages = len(stages)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a bar for each stage
    for i, stage in enumerate(stages):
        ax.barh(stage, 1, left=i, color='skyblue')

    # Set the x-ticks to represent the stages
    ax.set_xticks(range(num_stages))
    ax.set_xticklabels(stages)

    # Set labels and title
    ax.set_xlabel("Stages")
    ax.set_title("Waterfall Model Diagram")

    # Show the grid for better visualization
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Show the diagram
    plt.tight_layout()
    plt.show()

# Call the function to draw the waterfall model
draw_waterfall_model()
