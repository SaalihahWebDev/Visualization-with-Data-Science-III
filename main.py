# Step 1 : Import the tools
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Country names
countries = [
    'India', 'China', 'USA', 'Indonesia', 'Brazil',
    'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Russia'
]

# Step 3: Population growth values (fake numbers for demo)
growth = [
    900000000, 800000000, 150000000, 140000000, 130000000,
    120000000, 110000000, 100000000, 95000000, 90000000
]

# Step 4: Make the bar graph
plt.figure(figsize=(12, 6))
sns.barplot(x=growth, y=countries, palette="pastel")


# Add title and labels
plt.title("Top 10 Countries by Population Growth (1952-2007)",fontsize=14)
plt.xlabel("Population Growth")
plt.ylabel("Country")
plt.tight_layout()

# Show the graph
plt.show()