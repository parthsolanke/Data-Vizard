import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

def generate_line_chart(df, selected_features):
    """
Generate a line chart based on the selected features from the given DataFrame.

Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - selected_features (list): The list of selected features for comparison.

Returns:
    None

Example Usage:
    generate_line_chart(df, selected_features)

The function generates a line chart by plotting the values of the selected features against the index of the DataFrame. Each selected feature is represented by a separate line on the chart. The x-axis represents the index of the DataFrame, and the y-axis represents the values of the features. The chart is displayed using the 'st.pyplot()' function from the Streamlit library.

Note: The function assumes that the DataFrame has an index column.

"""

    plt.figure(figsize=(10, 6))
    for feature in selected_features:
        plt.plot(df.index, df[feature], label=feature)

    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.title("Line Chart")
    plt.legend()
    st.pyplot()


def generate_bar_chart(df, selected_features):
    """
Generate a bar chart based on the selected features from the given DataFrame.

Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - selected_features (list): The list of selected features for comparison.

Returns:
    None

Example Usage:
    generate_bar_chart(df, selected_features)
"""

    fig = px.bar(df, x=df.index, y=selected_features, barmode="group")
    fig.update_layout(title="Bar Chart", xaxis_title="Index", yaxis_title="Values")
    st.plotly_chart(fig)


def generate_scatter_plot(df, selected_features):
    """
Generate a scatter plot based on the selected features.

Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    selected_features (list): The list of selected features for the scatter plot.

Returns:
    None

Example:
    generate_scatter_plot(df, ['feature1', 'feature2'])
"""
    fig = px.scatter(
        df,
        x=selected_features[0],
        y=selected_features[1],
        title="Scatter Plot",
        labels={
            selected_features[0]: selected_features[0],
            selected_features[1]: selected_features[1],
        },
    )
    st.plotly_chart(fig)


def generate_pie_chart(df, selected_features):
    """
Generate a pie chart based on the selected features from the given DataFrame.

Parameters:
    - df (pandas DataFrame): The DataFrame containing the data.
    - selected_features (list): The list of selected features for the pie chart.

Returns:
    None

Example Usage:
    generate_pie_chart(df, selected_features)
"""
    fig = px.pie(df, names=selected_features, title="Pie Chart", hole=0.3)
    st.plotly_chart(fig)


def generate_bubble_plot(df, x_feature, y_feature, size_feature):
    """
Generate a bubble plot based on the given DataFrame and selected features.

Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x_feature (str): The name of the feature to be plotted on the x-axis.
    y_feature (str): The name of the feature to be plotted on the y-axis.
    size_feature (str): The name of the feature to determine the size of the bubbles.

Returns:
    None

Example Usage:
    generate_bubble_plot(df, 'feature1', 'feature2', 'feature3')
"""
    # Creating the bubble plot
    fig, ax = plt.subplots()
    ax.scatter(df[x_feature], df[y_feature], s=df[size_feature] * 100, alpha=0.5)
    ax.set_xlabel(x_feature)
    ax.set_ylabel(y_feature)
    ax.set_title("Bubble Plot")
    st.pyplot(fig)


def generate_histogram(df, selected_feature):
    """
Generate a histogram based on a selected feature from a pandas DataFrame.

Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    selected_feature (str): The name of the feature to generate the histogram for.

Returns:
    None

Example Usage:
    generate_histogram(df, 'Age')
"""
    plt.figure(figsize=(10, 6))
    plt.hist(df[selected_feature], bins=20, edgecolor="black")
    plt.xlabel(selected_feature)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    st.pyplot()


def generate_heatmap(df, selected_features):
    """
Generate a heatmap based on the correlation matrix of selected features in a DataFrame.

Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    selected_features (list): The list of selected features for which the correlation matrix will be calculated and visualized.

Returns:
    None

Example Usage:
    generate_heatmap(df, selected_features)
"""
    fig = px.imshow(df[selected_features].corr(), title="Heatmap")
    st.plotly_chart(fig)


def generate_polar_chart(df, selected_features):
    """
Generate a polar chart based on the selected features.

Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    selected_features (list): The list of selected features for the polar chart.

Returns:
    None

Example Usage:
    generate_polar_chart(df, selected_features)
"""
    fig = px.line_polar(df, r=selected_features[0], theta=df.index, title="Polar Chart")
    st.plotly_chart(fig)