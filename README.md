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

## ✨ Features

### 📊 Core Analytics

1. **Seasonal Pattern Analysis**
   - Identifies peak and low periods for storm events
   - Visualizes monthly trends with interactive charts
   - Provides statistical summaries of event frequency

2. **Geographic Clustering Analysis**
   - Maps event locations across the United States
   - Identifies regional hotspots and concentration areas
   - Displays latitude/longitude distribution patterns

### 📈 Visualization Types

The application implements **five distinct visualization types**:

1. **Line Chart** - Monthly trend analysis with markers
2. **Bar Chart** - Event count distribution by month
3. **Interactive Map** - Geographic point distribution
4. **Histograms** - Latitude and longitude distributions
5. **Scatter Plot** - Two-dimensional geographic patterns

### 🎛️ Interactive Controls

Two primary filter widgets allow dynamic data exploration:

1. **Month Range Slider**
   - Filter data by specific month ranges (1-12)
   - Real-time updates across all visualizations
   - Helps identify seasonal patterns

2. **Map Display Sampler**
   - Control the number of points displayed on the map
   - Optimizes performance for large datasets
   - Range: 100 to 10,000 points

## 🔍 Research Questions

### Question 1: Seasonal Patterns

**Does storm event frequency show seasonal patterns?**

- **Methodology**: Group events by month and analyze frequency distribution
- **Visualization**: Line and bar charts showing monthly trends
- **Insights**: Automatic identification of peak and low periods

### Question 2: Geographic Clustering

**Do storm events show geographic clustering?**

- **Methodology**: Plot event coordinates on an interactive map
- **Visualization**: Point map with optional sampling for performance
- **Insights**: Visual identification of regional hotspots and patterns

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
2. **Adjust Filters**: Use sidebar controls to filter data
3. **Explore Visualizations**: Scroll through different analysis sections
4. **Interact with Charts**: Hover, zoom, and pan on interactive plots
5. **Download Data**: Export filtered data as needed

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
load_data()                          # Load and preprocess data
create_sidebar_filters()             # Create interactive filters
filter_data_by_month()              # Filter data by month range
display_key_metrics()               # Show summary statistics
analyze_seasonal_patterns()         # Seasonal analysis
analyze_geographic_clustering()     # Geographic analysis
display_geographic_distribution()   # Distribution histograms
display_scatter_plot()              # Scatter visualization
display_data_preview()              # Data table and export
main()                              # Main application controller
```

### Performance Optimizations

1. **Data Caching**: `@st.cache_data` decorator for data loading
2. **Smart Sampling**: Limits map points for better performance
3. **Efficient Filtering**: Pandas vectorized operations
4. **Lazy Loading**: Charts render only when visible

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
