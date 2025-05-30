from GitCommitChart import create_git_commit_chart
import random

if __name__ == "__main__":
    data = [random.randint(0, 10)
            for i in range(365)]  # Example data for a year

    # Create the Git commit chart
    image = create_git_commit_chart(
        data,
        rows_per_column=7,
        horizontal_labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        vertical_labels=["Sun", "Wed", "Sat"],
        label_font_size=40
    )
    image.save("test.png")
