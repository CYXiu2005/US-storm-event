"""
2020 US Storm Events Spatio-Temporal Browser

A Streamlit web application for exploring and analyzing the distribution
patterns of storm events across time and space in the United States during 2020.

Author: CYXiu2005
Date: October 2025
Data Source: NOAA Storm Events Database
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Constants
DATA_FILE = 'StormEvents_locations-ftp_v1.0_d2020_c20201216.csv'
MONTH_NAMES = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}
MAX_MAP_POINTS = 10000
DEFAULT_MAP_POINTS = 2000
SCATTER_SAMPLE_SIZE = 5000


# Page Configuration
st.set_page_config(
    page_title="2020 US Storm Events Analysis",
    page_icon="🌪️",
    layout="wide"
)


@st.cache_data
def load_data():
    """
    Load and preprocess storm events data.

    Returns:
        pd.DataFrame: Cleaned and processed storm events data with
                      additional MONTH, YEAR, and MONTH_NAME columns.
    """
    df = pd.read_csv(DATA_FILE)

    # Data cleaning: ensure lat/lon are numeric, drop null values
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

    # Extract 'MONTH' and 'YEAR' from YEARMONTH
    df['MONTH'] = (df['YEARMONTH'] % 100)
    df['YEAR'] = (df['YEARMONTH'] // 100)

    # Create month names
    df['MONTH_NAME'] = df['MONTH'].map(MONTH_NAMES)

    return df


def create_sidebar_filters(df):
    """
    Create sidebar filter widgets.

    Args:
        df (pd.DataFrame): The loaded storm events dataframe.

    Returns:
        tuple: (selected_month_range, num_points_to_display)
    """
    st.sidebar.header('🔍 Data Filters')
    st.sidebar.markdown('---')

    # Widget 1: Month Range Slider
    st.sidebar.subheader('Month Range')
    selected_month_range = st.sidebar.slider(
        'Select month range to analyze:',
        min_value=1,
        max_value=12,
        value=(1, 12),
        help='Drag the slider to select month range'
    )

    # Widget 2: Map Display Sampling Slider
    st.sidebar.subheader('Map Display Settings')
    max_points = min(len(df), MAX_MAP_POINTS)
    num_points_to_display = st.sidebar.slider(
        'Maximum events to display on map:',
        min_value=100,
        max_value=max_points,
        value=min(DEFAULT_MAP_POINTS, max_points),
        step=100,
        help='Limit the number of points on the map to improve performance'
    )

    return selected_month_range, num_points_to_display


def filter_data_by_month(df, month_range):
    """
    Filter dataframe by month range.

    Args:
        df (pd.DataFrame): The storm events dataframe.
        month_range (tuple): Tuple of (min_month, max_month).

    Returns:
        pd.DataFrame: Filtered dataframe.
    """
    return df[
        (df['MONTH'] >= month_range[0]) &
        (df['MONTH'] <= month_range[1])
    ]


def display_key_metrics(df, filtered_df, month_range):
    """
    Display key metrics in columns.

    Args:
        df (pd.DataFrame): Original dataframe.
        filtered_df (pd.DataFrame): Filtered dataframe.
        month_range (tuple): Selected month range.
    """
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📊 Total Events", f"{len(df):,}")

    with col2:
        st.metric("✅ Filtered Events", f"{len(filtered_df):,}")

    with col3:
        st.metric(
            "📅 Time Range",
            f"Month {month_range[0]}-{month_range[1]}"
        )

    with col4:
        if len(filtered_df) > 0:
            avg_lat = filtered_df['LATITUDE'].mean()
            st.metric("🌐 Avg Latitude", f"{avg_lat:.2f}°")


def analyze_seasonal_patterns(filtered_df):
    """
    Analyze and visualize seasonal patterns of storm events.

    Args:
        filtered_df (pd.DataFrame): Filtered storm events dataframe.
    """
    st.header(
        '📈 Question 1: Does Storm Event Frequency Show Seasonal Patterns?'
    )
    st.markdown(
        '**Analysis Goal**: Explore the frequency of storm events '
        'across different months in 2020 and identify peak periods'
    )

    # Count events by month
    events_by_month = filtered_df.groupby('MONTH').size().reset_index(
        name='Event Count'
    )
    events_by_month['Month'] = events_by_month['MONTH']

    # Create two-column layout
    col_left, col_right = st.columns(2)

    with col_left:
        # Line chart
        fig_line = px.line(
            events_by_month,
            x='Month',
            y='Event Count',
            title='Monthly Storm Events Trend',
            markers=True,
            labels={'Month': 'Month', 'Event Count': 'Event Count'}
        )
        fig_line.update_traces(
            line_color='#FF6B6B',
            line_width=3,
            marker_size=10
        )
        fig_line.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            hovermode='x unified'
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col_right:
        # Bar chart
        fig_bar = px.bar(
            events_by_month,
            x='Month',
            y='Event Count',
            title='Monthly Storm Events Distribution',
            labels={'Month': 'Month', 'Event Count': 'Event Count'},
            color='Event Count',
            color_continuous_scale='Reds'
        )
        fig_bar.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # Display analysis conclusions
    if len(events_by_month) > 0:
        peak_month = events_by_month.loc[
            events_by_month['Event Count'].idxmax()
        ]
        low_month = events_by_month.loc[
            events_by_month['Event Count'].idxmin()
        ]

        st.info(f"""
        **📊 Key Findings**:
        - 🔴 Peak Period: Month {int(peak_month['Month'])}, with \
{int(peak_month['Event Count'])} events recorded
        - 🟢 Low Period: Month {int(low_month['Month'])}, with \
{int(low_month['Event Count'])} events recorded
        - 📈 Fluctuation: \
{int(peak_month['Event Count'] - low_month['Event Count'])} events difference
        """)


def analyze_geographic_clustering(filtered_df, num_points_to_display):
    """
    Analyze and visualize geographic clustering of storm events.

    Args:
        filtered_df (pd.DataFrame): Filtered storm events dataframe.
        num_points_to_display (int): Maximum number of points to display.
    """
    st.header('🗺️ Question 2: Do Storm Events Show Geographic Clustering?')
    st.markdown(
        '**Analysis Goal**: Identify hotspot regions and geographic '
        'distribution patterns of storm events'
    )

    if len(filtered_df) > 0:
        # Sample data for performance
        map_data = filtered_df[['LATITUDE', 'LONGITUDE']].copy()
        map_data = map_data.rename(
            columns={'LATITUDE': 'lat', 'LONGITUDE': 'lon'}
        )

        # Sample if data is too large
        if len(map_data) > num_points_to_display:
            map_data_display = map_data.sample(
                n=num_points_to_display,
                random_state=42
            )
            st.warning(
                f'⚠️ Large dataset detected. Displaying a random sample '
                f'of {num_points_to_display:,} events '
                f'(out of {len(map_data):,} total)'
            )
        else:
            map_data_display = map_data
            st.success(f'✅ Displaying all {len(map_data):,} event points')

        # Display map
        st.map(map_data_display, zoom=3)

        # Geographic distribution statistics
        col1, col2 = st.columns(2)
        with col1:
            lat_min = filtered_df['LATITUDE'].min()
            lat_max = filtered_df['LATITUDE'].max()
            st.metric("Latitude Range", f"{lat_min:.2f}° ~ {lat_max:.2f}°")

        with col2:
            lon_min = filtered_df['LONGITUDE'].min()
            lon_max = filtered_df['LONGITUDE'].max()
            st.metric("Longitude Range", f"{lon_min:.2f}° ~ {lon_max:.2f}°")
    else:
        st.warning('No data available for the current filter selection')


def display_geographic_distribution(filtered_df):
    """
    Display geographic distribution histograms for latitude and longitude.

    Args:
        filtered_df (pd.DataFrame): Filtered storm events dataframe.
    """
    st.header('📊 Exploratory Analysis: Geographic Distribution Patterns')
    st.markdown(
        '**Analysis Goal**: Deep dive into the distribution characteristics '
        'of storm events across latitude and longitude'
    )

    if len(filtered_df) > 0:
        col_lat, col_lon = st.columns(2)

        with col_lat:
            # Latitude distribution histogram
            fig_lat = px.histogram(
                filtered_df,
                x='LATITUDE',
                nbins=50,
                title='Storm Events Latitude Distribution',
                labels={'LATITUDE': 'Latitude (°)', 'count': 'Event Count'},
                color_discrete_sequence=['#4ECDC4']
            )
            fig_lat.update_layout(
                xaxis_title='Latitude (°)',
                yaxis_title='Event Count',
                showlegend=False
            )
            st.plotly_chart(fig_lat, use_container_width=True)

            # Latitude statistics
            lat_mean = filtered_df['LATITUDE'].mean()
            lat_median = filtered_df['LATITUDE'].median()
            lat_std = filtered_df['LATITUDE'].std()

            st.markdown(f"""
            **Latitude Statistics**:
            - Mean: {lat_mean:.2f}°
            - Median: {lat_median:.2f}°
            - Std Dev: {lat_std:.2f}°
            """)

        with col_lon:
            # Longitude distribution histogram
            fig_lon = px.histogram(
                filtered_df,
                x='LONGITUDE',
                nbins=50,
                title='Storm Events Longitude Distribution',
                labels={'LONGITUDE': 'Longitude (°)', 'count': 'Event Count'},
                color_discrete_sequence=['#FF6B6B']
            )
            fig_lon.update_layout(
                xaxis_title='Longitude (°)',
                yaxis_title='Event Count',
                showlegend=False
            )
            st.plotly_chart(fig_lon, use_container_width=True)

            # Longitude statistics
            lon_mean = filtered_df['LONGITUDE'].mean()
            lon_median = filtered_df['LONGITUDE'].median()
            lon_std = filtered_df['LONGITUDE'].std()

            st.markdown(f"""
            **Longitude Statistics**:
            - Mean: {lon_mean:.2f}°
            - Median: {lon_median:.2f}°
            - Std Dev: {lon_std:.2f}°
            """)


def display_scatter_plot(filtered_df):
    """
    Display scatter plot of geographic distribution.

    Args:
        filtered_df (pd.DataFrame): Filtered storm events dataframe.
    """
    st.header('🎯 Supplementary Analysis: Geographic Scatter Plot')
    st.markdown(
        '**Analysis Goal**: Visualize clustering patterns through a '
        'two-dimensional scatter plot of coordinates'
    )

    if len(filtered_df) > 0:
        # Use sampled data for performance
        scatter_sample = filtered_df.sample(
            n=min(SCATTER_SAMPLE_SIZE, len(filtered_df)),
            random_state=42
        )

        fig_scatter = px.scatter(
            scatter_sample,
            x='LONGITUDE',
            y='LATITUDE',
            title=(
                f'Storm Events Geographic Distribution '
                f'(showing {len(scatter_sample):,} samples)'
            ),
            labels={'LONGITUDE': 'Longitude (°)', 'LATITUDE': 'Latitude (°)'},
            opacity=0.6,
            color_discrete_sequence=['#FF6B6B']
        )
        fig_scatter.update_traces(marker=dict(size=4))
        fig_scatter.update_layout(
            height=600,
            xaxis_title='Longitude (°)',
            yaxis_title='Latitude (°)',
            hovermode='closest'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)


def display_data_preview(filtered_df, month_range):
    """
    Display raw data preview and download option.

    Args:
        filtered_df (pd.DataFrame): Filtered storm events dataframe.
        month_range (tuple): Selected month range.
    """
    st.header('📋 Data Preview')
    st.markdown('**View the first few rows of raw data**')

    # Add a selectbox to control number of rows displayed
    num_rows = st.selectbox(
        'Select number of rows to display:',
        [10, 25, 50, 100],
        index=0
    )

    # Display data
    st.dataframe(
        filtered_df.head(num_rows),
        use_container_width=True,
        height=400
    )

    # Data download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    file_name = (
        f'storm_events_filtered_month_{month_range[0]}_'
        f'to_{month_range[1]}.csv'
    )
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name=file_name,
        mime='text/csv',
    )


def display_footer():
    """Display footer information."""
    st.markdown('---')
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>📊 2020 US Storm Events Spatio-Temporal Browser</p>
        <p>Data Source: NOAA Storm Events Database</p>
        <p>Created with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application function."""
    # Load data
    with st.spinner('Loading data...'):
        df = load_data()

    # Create sidebar filters
    selected_month_range, num_points_to_display = create_sidebar_filters(df)

    # Filter data based on selections
    filtered_df = filter_data_by_month(df, selected_month_range)

    # Main page layout
    st.title('🌪️ 2020 US Storm Events Spatio-Temporal Browser')
    st.markdown(
        '### Exploring Storm Events Distribution Patterns '
        'Across Time and Space'
    )
    st.markdown('---')

    # Display key metrics
    display_key_metrics(df, filtered_df, selected_month_range)

    st.markdown('---')

    # Question 1: Seasonal patterns analysis
    analyze_seasonal_patterns(filtered_df)

    st.markdown('---')

    # Question 2: Geographic clustering analysis
    analyze_geographic_clustering(filtered_df, num_points_to_display)

    st.markdown('---')

    # Exploratory analysis: Geographic distribution
    display_geographic_distribution(filtered_df)

    st.markdown('---')

    # Supplementary analysis: Scatter plot
    display_scatter_plot(filtered_df)

    st.markdown('---')

    # Data preview and download
    display_data_preview(filtered_df, selected_month_range)

    # Footer
    display_footer()


if __name__ == "__main__":
    main()

