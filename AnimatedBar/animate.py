import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Read the CSV data from a file
df = pd.read_csv('/Users/yes.in.a.jiffy/Downloads/Wins.csv')

# Check for the 'IndRes' column
if 'IndRes' not in df.columns:
    raise KeyError("'IndRes' column not found in the DataFrame")


# Prepare the data for plotting by year
# Assuming 'Win', 'Loss', and 'Draw' are correctly set in the IndRes column
counts = df.groupby(['Year', 'IndRes']).size().unstack(fill_value=0)
# Make sure 'Won', 'Lost', 'Draw' are in the index properly
# If not found explicitly, rename them accordingly
counts.rename(index={"Win": "Won", "Loss": "Lost", "Draw": "Draw"}, inplace=True)
counts = counts.fillna(0)  # Fill any missing values with 0

print(counts)

# Prepare a list of years and results numpy array
years = counts.index.tolist()
results = counts.to_numpy()
print(results)
n_years = len(years)

# Calculate cumulative sums for Wins, Losses, and Draws
cumulative_results = np.zeros_like(results)  # Create an empty array to hold cumulative results
cumulative_results[0] = results[0]  # Set first year results

for i in range(1, n_years):
    cumulative_results[i] = cumulative_results[i - 1] + results[i]
# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a single set of bars for total matches
bars = ax.bar(['Draw', 'Lost', 'Won'], [0, 0, 0], color=['orange', 'red', 'green'])

# Setting up the title and labels
ax.set_ylim(0, cumulative_results.max() * 1.1)  # Set y-limit based on the max cumulative value
ax.set_title('Cumulative Match Results - All Matches')
ax.set_ylabel('Cumulative Number of Matches')

year_text = ax.text(0.5, cumulative_results.max() * 1.05, '', ha='left', fontsize=15,fontweight='bold')
cumulative_won_text = ax.text(0.5, cumulative_results.max() * 1.01, '', ha='left', fontsize=12, color='orange',fontweight='bold')
cumulative_lost_text = ax.text(0.5, cumulative_results.max() * 0.97, '', ha='left', fontsize=12, color='red',fontweight='bold')
cumulative_draw_text = ax.text(0.5, cumulative_results.max() * 0.93, '', ha='left', fontsize=12, color='green',fontweight='bold')

branding = ax.text(1.4, cumulative_results.max() * 1.06, '', ha='left', fontsize=8, color='blue',fontweight='bold')
branding.set_text("https://www.youtube.com/@NurtureLearning")
# Animation function
def update(year_index):
    # Ensure that we do not exceed the number of years available
    if year_index < n_years:
        # Update the heights of the bars
        for i, bar in enumerate(bars):
            bar.set_height(cumulative_results[year_index, i])  # Update each bar's height

        # Clear previous text from the bars
        for text in ax.texts:
            if text not in [year_text, cumulative_won_text, cumulative_lost_text, cumulative_draw_text,branding]:
                text.remove()

        # Adding cumulative values on the bars
        ax.text(0, cumulative_results[year_index, 0] + 1, cumulative_results[year_index, 0], ha='center', fontsize=12, color='black')
        ax.text(1, cumulative_results[year_index, 1] + 1, cumulative_results[year_index, 1], ha='center', fontsize=12, color='black')
        ax.text(2, cumulative_results[year_index, 2] + 1, cumulative_results[year_index, 2], ha='center', fontsize=12, color='black')

        # Update the year and cumulative text labels
        year_text.set_text(f'Year: {years[year_index]}')
        cumulative_won_text.set_text(f'Cumulative Draw: {cumulative_results[year_index, 0]}')
        cumulative_lost_text.set_text(f'Cumulative Lost: {cumulative_results[year_index, 1]}')
        cumulative_draw_text.set_text(f'Cumulative Won: {cumulative_results[year_index, 2]}')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_years, interval=1000, repeat=False)
# Save the animation as an MP4 file
ani.save('cumulative_match_results_AllMatches.gif', writer='pillow', fps=5)

ani.save('cumulative_match_results_AllMatches.mp4', writer='ffmpeg', fps=10)
plt.show()
