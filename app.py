from flask import Flask, render_template
import pandas as pd
from enum import Enum

app = Flask(__name__)

# enum cut and color
class Cut(Enum):
    Ideal = "Ideal"
    Premium = "Premium"
    Good = "Good"
    Very_Good = "Very Good"
    Fair = "Fair"

class Color(Enum):
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"

# Load the CSV file
file_path = 'diamond.csv'
diamonds_df = pd.read_csv(file_path)

# calculations
highest_price = diamonds_df['price'].max()
average_price = diamonds_df['price'].mean()
ideal_count = len(diamonds_df[diamonds_df['cut'] == Cut.Ideal.value])
unique_colors = diamonds_df['color'].nunique()
color_types = diamonds_df['color'].unique()
median_carat_premium = diamonds_df[diamonds_df['cut'] == Cut.Premium.value]['carat'].median()
average_carat_per_cut = diamonds_df.groupby('cut')['carat'].mean()
average_price_per_color = diamonds_df.groupby('color')['price'].mean()
clarity_count = diamonds_df['clarity'].value_counts()

@app.route('/')
def index():
    return render_template(
        'index.html',
        highest_price=highest_price,
        average_price=average_price,
        ideal_count=ideal_count,
        unique_colors=unique_colors,
        color_types=color_types.tolist(),
        median_carat_premium=median_carat_premium,
        average_carat_per_cut=average_carat_per_cut.to_dict(),
        average_price_per_color=average_price_per_color.to_dict(),
        clarity_count=clarity_count.to_dict() 
    )

if __name__ == '__main__':
    app.run(debug=True)
