# Install packages

!pip install pandas gapminder

# Import necessary libraries
import pandas as pd
from gapminder import gapminder

# Rename 'lifeExp' to 'life_expectancy' and 'gdpPercap' to 'gdp_per_capita'
gapminder = gapminder.rename(columns={'lifeExp': 'life_expectancy',
                                      'pop': 'population_millions', 
                                      'gdpPercap': 'gdp_per_capita'})

# Convert population to millions
gapminder['population_millions'] = gapminder['population_millions'] / 1_000_000

# Create a new pandas DataFrame from the modified gapminder data
gapminder_df = pd.DataFrame(gapminder)

# Save the DataFrame as a CSV file
gapminder_df.to_csv('gapminder.csv', index=False)
