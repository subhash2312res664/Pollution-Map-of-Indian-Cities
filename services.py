'''
Hello, This project is Design under Project-2 for 3-Months GUVI/HCL Internship.
Subhashkumar
Thanks.
'''

# Important Libraries
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import matplotlib.colors as mcolors

# Load CSV DATA
# Data:(21-08-2025 09:00:00) Not RealTime.
rcsvdf = pd.read_csv("3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv")

## Map Visualization using "Geopands+Matplotlib"

# File Path
shppath1 = "gadm41_IND_1.shp"   # State Boundry
india_gd1 = gpd.read_file(shppath1)

#Loading India shape data
india = gpd.read_file(shppath1)
# Loading Filtered pollution data
cities = pd.read_csv("cities_pm25.csv")

# Convert cities to GeoDataFrame
geometry = [Point(xy) for xy in zip(cities['Longitude'], cities['Latitude'])]
cities_gdf = gpd.GeoDataFrame(cities, geometry=geometry, crs="EPSG:4326")


# Define thresholds
low_thresh = 30
medium_thresh = 60

# Create categories
cities_gdf['Category'] = pd.cut(
    cities_gdf['PM25'],
    bins=[-1, low_thresh, medium_thresh, float('inf')],
    labels=['Low', 'Medium', 'High']
)

cities_gdf['Category'].value_counts()

# ***************************
#******************************
### Air Pollution (PM2.5) Across Indian Cities###
# custom green-orange-red colors
cmap = mcolors.ListedColormap(['green', 'orange', 'red'])
bounds = [0, 30, 60, cities_gdf['PM25'].max()]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

def fullviewpollutionmap():
    # Plot India map
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    india.boundary.plot(ax=ax, color="black", linewidth=0.8)

    cities_gdf.plot(
        ax=ax,
        column='PM25',
        cmap=cmap,
        norm=norm,
        edgecolor='w',
        legend=True,
        markersize=80
    )

    # City labels
    for x, y, label in zip(cities_gdf.geometry.x, cities_gdf.geometry.y, cities_gdf['city']):
        plt.text(x, y, label, fontsize=8)

    # Titles and cleanup
    ax.set_title("Air Pollution (PM2.5) Across Indian Cities", fontsize=16)
    plt.axis("off")

    # Save and show
    # plt.savefig("india_pollution_static04.png", dpi=300)
    return plt.show()
# fullviewpollutionmap()

def mostPollutadeCities():
    high_polluted = cities_gdf[cities_gdf['Category'] == 'High']

    fig, ax = plt.subplots(figsize=(10, 10))
    india.plot(ax=ax, color="white", edgecolor="black")
    high_polluted.plot(ax=ax, color="red", markersize=50)

    # Add city names
    for x, y, label in zip(high_polluted.geometry.x, high_polluted.geometry.y, high_polluted['city']):
        plt.text(x + 0.3, y + 0.3, label, fontsize=8, color="red")

    plt.title("High Pollution Cities (PM2.5 > 60)", fontsize=14)
    plt.savefig("indian_Cities_pollution_High.png", dpi=300)
    plt.show()

    high_polluted[['city', 'PM25']].sort_values(by='PM25', ascending=False).head()

    return
# mostPollutadeCities()

def medpollutionmap():
    medium_polluted = cities_gdf[cities_gdf['Category'] == 'Medium']

    fig, ax = plt.subplots(figsize=(10, 10))
    india.plot(ax=ax, color="white", edgecolor="black")
    medium_polluted.plot(ax=ax, color="orange", markersize=50)

    # Add city names
    for x, y, label in zip(medium_polluted.geometry.x, medium_polluted.geometry.y, medium_polluted['city']):
        plt.text(x + 0.3, y + 0.3, label, fontsize=8, color="orange")

    plt.title("Medium Pollution Cities (30 ≤ PM2.5 ≤ 60)", fontsize=14)
    plt.savefig("indian_Cities_pollution_Medium.png", dpi=300)
    plt.show()

    medium_polluted[['city', 'PM25']].sort_values(by='PM25', ascending=False).head()

    return
# medpollutionmap()

def lowpollutionmap():
    low_polluted = cities_gdf[cities_gdf['Category'] == 'Low']

    fig, ax = plt.subplots(figsize=(10, 10))
    india.plot(ax=ax, color="white", edgecolor="black")
    low_polluted.plot(ax=ax, color="green", markersize=50)

    # Add city names
    for x, y, label in zip(low_polluted.geometry.x, low_polluted.geometry.y, low_polluted['city']):
        plt.text(x + 0.3, y + 0.3, label, fontsize=8, color="green")

    plt.title("Low Pollution Cities (PM2.5 < 30)", fontsize=14)
    plt.savefig("indian_Cities_pollution_low.png", dpi=300)
    plt.show()

    low_polluted[['city', 'PM25']].sort_values(by='PM25', ascending=True).head()

    return
# lowpollutionmap()

def webviewmap():
    import webbrowser
    file_path = "india_pollution_map_final.html"
    webbrowser.open(file_path)  # Opens in default browser
    return
# webviewmap()

def ProjectInfo():
    msg1 = (
        "Indian Cities Pollution Map\n"
        "This project is created and submitted by **Mr. Subhash Kumar Rana** "
        "(subhash_2312res664@iitp.ac.in) as part of the **90-Day Internship** program by **GUVI (HCL)**.\n\n"
        "🎯 Project Objective:\n"
        "Using Geopandas and Matplotlib Display Indian Pollution across Cities.\n"
        "This is **Project-2** of the internship.\n"
    )
    print(msg1)

def AboutMe():
    aboutme = \
        (
        "👋 Hey Developers,\n"
        "I’m **Subhash Kumar Rana**, an aspiring Data Scientist and a Computer Science & Data Analytics undergraduate "
        "(Graduating in 2026).\n\n"
        "🔍 I have a strong foundation in data analysis, Python programming, and general computer science concepts. "
        "I enjoy working on real-world datasets and building insightful visualizations.\n\n"
        "📬 Let’s connect or collaborate!\n"
        "Email: subhash_2312res664@iitp.ac.in\n"
        "Phone: +91 62997 42348\n"
    )