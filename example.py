import math
from GitCommitChart import create_git_commit_chart
import random

if __name__ == "__main__":
    data = [random.random() for i in range(1, 745)]  # Example data for a year

    # Create the Git commit chart
    image = create_git_commit_chart(
        data,
        rows_per_column=24,
        vertical_labels=["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
        horizontal_labels=[str(i) for i in range(1, 31, 2)],
        label_font_size=30
    )
    image.save("test.png")
