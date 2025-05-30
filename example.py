from GitCommitChart import create_git_commit_chart
import random

if __name__ == "__main__":
    # Example data array with 365 elements
    # each with a random value between 0 and 100
    data = [random.randint(0, 10) for i in range(365)] 


    # Create the Git commit chart
    image = create_git_commit_chart(data, rows_per_column=7)
    image.save("test.png")