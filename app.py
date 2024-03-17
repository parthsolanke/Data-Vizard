import streamlit as st
import pandas as pd

from utils.helper import (
    generate_line_chart,
    generate_bar_chart,
    generate_scatter_plot,
    generate_bubble_plot,
    generate_pie_chart,
    generate_histogram,
    generate_heatmap,
    generate_polar_chart,
)

# config
st.set_option("deprecation.showPyplotGlobalUse", False)


def main():
    """
    This function is the main function of the Data Visualization Tool. It allows the user to upload a CSV file, select features for comparison, and choose the type of chart to generate and display based on the selected features.

    Parameters:
        None

    Returns:
        None

    Example Usage:
        main()
    """

    st.title("Data Visualization Tool")
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the DataFrame
        st.set_option("deprecation.showPyplotGlobalUse", False)
        st.write("Preview of the uploaded data:")
        st.write(df.head())

        # Select features for comparison
        selected_features = st.multiselect("Select features for comparison", df.columns)

        if not selected_features:
            st.warning("Please select at least one feature for comparison.")

        else:
            # Type checking
            if not all(
                df[feature].dtype in (int, float) for feature in selected_features
            ):
                st.error("Selected features must be numeric for visualization.")
            else:
                # Choose the type of chart
                chart_type = st.selectbox(
                    "Select the type of chart",
                    [
                        "Line Chart",
                        "Bar Chart",
                        "Scatter Plot",
                        "Bubble Plot",
                        "Pie Chart",
                        "Histogram",
                        "Heatmap",
                        "Polar Chart",
                    ],
                )

                # Generate and display the chart based on user selections
                if chart_type == "Line Chart":
                    generate_line_chart(df, selected_features)
                elif chart_type == "Bar Chart":
                    generate_bar_chart(df, selected_features)
                elif chart_type == "Scatter Plot":
                    generate_scatter_plot(df, selected_features)
                elif chart_type == "Bubble Plot":
                    x_feature = selected_features[0]
                    y_feature = selected_features[1]
                    size_feature = selected_features[2]
                    generate_bubble_plot(df, x_feature, y_feature, size_feature)
                elif chart_type == "Pie Chart":
                    generate_pie_chart(df, selected_features)
                elif chart_type == "Histogram":
                    generate_histogram(df, selected_features[0])
                elif chart_type == "Heatmap":
                    generate_heatmap(df, selected_features)
                elif chart_type == "Polar Chart":
                    generate_polar_chart(df, selected_features)


if __name__ == "__main__":
    main()
