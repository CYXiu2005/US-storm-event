# 🌪️ 2020 US Storm Events Spatio-Temporal Browser

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-orange.svg)](https://pep8.org/)

An interactive web application built with Streamlit for exploring and analyzing the spatio-temporal distribution patterns of storm events across the United States during 2020.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Research Questions](#-research-questions)
- [Visualizations](#-visualizations)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Data Source](#-data-source)
- [Technical Details](#-technical-details)
- [License](#-license)

## 🎯 Overview

This application provides an intuitive interface for analyzing over 48,000 storm events recorded in the United States during 2020. Users can interactively explore:

- **Temporal patterns**: Seasonal variations and monthly trends
- **Spatial patterns**: Geographic clustering and regional hotspots
- **Statistical insights**: Distribution characteristics across different dimensions
- **Multi-dimensional filtering**: Combine temporal, spatial, and view preferences for customized analysis
- **Performance optimization**: Smart sampling and caching for responsive user experience

## ✨ Features

### 📊 Core Analytics

1. **Seasonal Pattern Analysis**
   - Identifies peak and low periods for storm events
   - Visualizes monthly trends with interactive charts
   - Provides statistical summaries of event frequency
   - Optional advanced statistics (mean, std dev, coefficient of variation)

2. **Geographic Clustering Analysis**
   - Maps event locations across the United States
   - Identifies regional hotspots and concentration areas
   - Displays latitude/longitude distribution patterns
   - Supports location-based keyword search and latitude filtering

3. **Dynamic View Modes**
   - Comprehensive: All analyses displayed
   - Temporal Only: Focus on time-series patterns
   - Spatial Only: Focus on geographic distributions

### 📈 Visualization Types

The application implements **five distinct visualization types**:

1. **Line Chart** - Monthly trend analysis with markers and hover details
2. **Bar Chart** - Event count distribution by month with color coding
3. **Interactive Map** - Geographic point distribution with zoom/pan
4. **Histograms** - Latitude and longitude distributions (50 bins each)
5. **Scatter Plot** - Two-dimensional geographic patterns (sampled)

### 🎛️ Interactive Controls

**Six comprehensive filter widgets** enable multi-dimensional data exploration:

#### Temporal Filtering

1. **Month Range Slider** (`st.slider`)
   - Filter data by specific month ranges (1-12)
   - Real-time updates across all visualizations
   - Helps identify seasonal patterns and time-based trends

#### Spatial Filtering

2. **Location Search** (`st.text_input`)
   - Keyword-based location filtering
   - Case-insensitive partial matching
   - Quickly narrow down to specific geographic areas

3. **Latitude Range Inputs** (`st.number_input`)
   - Precise minimum/maximum latitude boundaries
   - Default range: 24°N to 50°N (US mainland)
   - Degree-level precision for regional analysis

#### Performance Optimization

4. **Map Display Limit Slider** (`st.slider`)
   - Control the number of points displayed on the map
   - Range: 100 to 10,000 points
   - Smart random sampling for representative visualization
   - Optimizes performance for large datasets

#### View Customization

5. **Analysis Focus Mode** (`st.radio`)
   - **Comprehensive**: All temporal and spatial analyses
   - **Temporal Only**: Time-series patterns and trends
   - **Spatial Only**: Geographic distribution and clustering
   - Streamlines interface based on analytical focus

6. **Advanced Statistics Toggle** (`st.checkbox`)
   - Enable/disable detailed statistical metrics
   - Includes mean, standard deviation, coefficient of variation
   - Adjustable analysis depth based on user expertise

#### Integrated Filtering System

All six widgets work seamlessly together, creating a powerful multi-dimensional filtering system. An **active filters indicator** displays currently applied filters, providing transparency and helping users understand the data scope. This transforms the application from a static dashboard into an adaptive analytical tool.

## 🔍 Research Questions

### Question 1: Seasonal Patterns

**Does storm event frequency show seasonal patterns?**

- **Methodology**: Group events by month and analyze frequency distribution
- **Visualization**: Line and bar charts showing monthly trends
- **Insights**: Automatic identification of peak and low periods
- **Advanced Analytics**: Optional display of mean, standard deviation, and coefficient of variation

### Question 2: Geographic Clustering

**Do storm events show geographic clustering?**

- **Methodology**: Plot event coordinates on an interactive map with spatial filtering
- **Visualization**: Point map with optional sampling for performance
- **Insights**: Visual identification of regional hotspots and patterns
- **Filtering Options**: Location-based search and latitude range selection

## 🎨 Filter Combinations & Use Cases

The application's six interactive widgets can be combined in powerful ways:

### Example Use Cases

1. **Summer Storm Analysis in Southern States**
   - Month Range: 6-8 (June to August)
   - Latitude Range: 24°N - 35°N
   - View Mode: Comprehensive

2. **Northern Winter Events**
   - Month Range: 12-2 (December to February)
   - Latitude Range: 40°N - 50°N
   - Advanced Statistics: Enabled

3. **Coastal Region Focus**
   - Location Search: "coast" or "beach"
   - View Mode: Spatial Only
   - Map Display: Maximum points for detail

4. **Quick Performance Overview**
   - View Mode: Temporal Only
   - Map Display: Minimal points (100-500)
   - Advanced Statistics: Disabled

## 📊 Visualizations

### 1. Time Series Analysis
- Monthly Storm Events Trend (Line Chart)
- X-axis: Months (1-12)
- Y-axis: Event Count
- Features: Markers, hover information

### 2. Distribution Charts
- Monthly Distribution (Bar Chart)
- Color-coded by event count
- Interactive tooltips

### 3. Geospatial Mapping
- Interactive Map
- Latitude/Longitude plotting
- Zoom and pan capabilities

### 4. Statistical Distributions
- Histograms (Latitude & Longitude)
- 50 bins for granular distribution
- Statistical summaries (mean, median, std)

### 5. Scatter Analysis
- Geographic Scatter Plot
- Up to 5,000 sampled points
- Opacity-adjusted for density visualization

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Steps

```bash
# Clone the repository
git clone https://github.com/CYXiu2005/streamlit-lab-10.git
cd streamlit-lab-10

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`.

### User Workflow

1. **Launch Application**: Start the Streamlit server
2. **Select View Mode**: Choose Comprehensive, Temporal Only, or Spatial Only
3. **Apply Filters**: Use sidebar controls to filter data
   - Adjust month range for temporal filtering
   - Enter location keywords for geographic filtering
   - Set latitude boundaries for regional focus
   - Control map display limits for performance
4. **Toggle Statistics**: Enable/disable advanced statistical displays
5. **Explore Visualizations**: Scroll through dynamic analysis sections
6. **Interact with Charts**: Hover, zoom, and pan on interactive plots
7. **Download Data**: Export filtered data as CSV for further analysis

## 📁 Project Structure

```
streamlit-lab-10/
│
├── app.py                          # Main application (PEP8 compliant)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── StormEvents_locations-*.csv    # Data file
```

## 📊 Data Source

**Dataset**: NOAA Storm Events Database (2020)  
**Records**: ~48,970 events  
**Format**: CSV

### Key Data Fields

| Field | Description | Type |
|-------|-------------|------|
| `YEARMONTH` | Year and month of event | Integer |
| `EVENT_ID` | Unique event identifier | Integer |
| `LATITUDE` | Event latitude | Float |
| `LONGITUDE` | Event longitude | Float |
| `LOCATION` | Location description | String |

## 🔧 Technical Details

### Technology Stack

- **Frontend Framework**: Streamlit 1.28+
- **Data Processing**: Pandas 2.0+
- **Visualization**: Plotly 5.17+
- **Language**: Python 3.8+

### Code Quality Standards - PEP 8 Compliance

This project strictly follows **PEP 8** style guidelines:

✅ **Naming Conventions**
- Functions and variables: `snake_case`
- Constants: `UPPER_CASE`
- Classes: `PascalCase`

✅ **Code Organization**
- Imports organized (standard → third-party → local)
- Module-level docstring
- Clear function separation

✅ **Documentation**
- Comprehensive docstrings for all functions
- Type hints where applicable
- Inline comments for complex logic

✅ **Formatting**
- Maximum line length: 79 characters
- 4-space indentation
- Two blank lines between top-level definitions

✅ **Code Structure**
- Modular design with separate functions
- Main execution guard (`if __name__ == "__main__"`)
- Consistent spacing and layout

### Key Functions

```python
load_data()                          # Load and preprocess data with caching
create_sidebar_filters()             # Create 6 interactive filter widgets
filter_data_by_month()              # Filter data by month range
apply_all_filters()                 # Apply combined temporal and spatial filters
display_key_metrics()               # Show summary statistics and active filters
analyze_seasonal_patterns()         # Seasonal analysis with optional advanced stats
analyze_geographic_clustering()     # Geographic analysis with sampling
display_geographic_distribution()   # Distribution histograms with statistics
display_scatter_plot()              # Scatter visualization (5000 sample)
display_data_preview()              # Data table preview and CSV export
display_footer()                    # Application footer information
main()                              # Main application controller with view modes
```

### Performance Optimizations

1. **Data Caching**: `@st.cache_data` decorator for one-time data loading
2. **Smart Sampling**: Dynamic sampling for map visualization (up to 10,000 points)
3. **Efficient Filtering**: Pandas vectorized operations for fast data filtering
4. **Lazy Rendering**: Charts render only when in view mode
5. **Multi-level Filtering**: Combined temporal and spatial filters applied efficiently
6. **Memory Management**: Sample-based visualizations for large datasets

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- **Data Source**: [NOAA Storm Events Database](https://www.ncdc.noaa.gov/stormevents/)
- **Framework**: [Streamlit](https://streamlit.io/)
- **Visualization Library**: [Plotly](https://plotly.com/)

## 📞 Contact

**Author**: CYXiu2005  
**Repository**: [streamlit-lab-10](https://github.com/CYXiu2005/streamlit-lab-10)

---

<div align="center">
  <p>Made with ❤️ using Streamlit</p>
  <p>⭐ Star this repository if you find it helpful!</p>
</div>
