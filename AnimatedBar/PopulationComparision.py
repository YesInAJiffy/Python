import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data Source
# https://www.macrotrends.net/global-metrics/countries/chn/china/population
# Create a pandas DataFrame from the data
data = {
    "Year": [int(x.split(',')[0].strip('"')) for x in open('Growth.csv').readlines()[1:]],
    "India Population": [int(x.split(',')[1].strip('"').replace(",", "")) for x in open('Growth.csv').readlines()[1:]],
    "China Population": [int(x.split(',')[2].strip('"').replace(",", "")) for x in open('Growth.csv').readlines()[1:]]
}
df = pd.DataFrame(data)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot([], [], label='China Population', color='blue')
line2, = ax.plot([], [], label='India Population', color='red')
ax.set_xlim(df['Year'].min(), df['Year'].max()+5)
ax.set_ylim(0, df[['India Population', 'China Population']].max().max() * 1.2)
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title('India and China Population Over Time (Animated)')
ax.legend()
ax.grid(True)

# Annotation text
annotation_text = ax.text(0.4, 0.6, '', transform=ax.transAxes, fontsize=12, ha='center')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    annotation_text.set_text('')
    return line1, line2, annotation_text

def update(frame):
    # Update the data for each frame
    line1.set_data(df['Year'][:frame+1], df['India Population'][:frame+1])
    line2.set_data(df['Year'][:frame+1], df['China Population'][:frame+1])
    
    # Update annotation
    annotation_text.set_text(f"Year: {df['Year'][frame]}, "
                             f"China: {df['India Population'][frame]:,}, "
                             f"India: {df['China Population'][frame]:,}")
    
    return line1, line2, annotation_text

# Create the animation
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, repeat=False)

plt.show()
