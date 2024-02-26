import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def main():
    st.title("Data Visualization Tool")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the DataFrame
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write("Preview of the uploaded data:")
        st.write(df.head())

        # Select features for comparison
        selected_features = st.multiselect("Select features for comparison", df.columns)

        if not selected_features:
            st.warning("Please select at least one feature for comparison.")
        else:
            # Choose the type of chart
            chart_type = st.selectbox("Select the type of chart", ["Line Chart", "Bar Chart", "Scatter Plot", "Pie Plot","Bubble Plot"])

            # Generate and display the chart based on user selections
            if chart_type == "Line Chart":
                generate_line_chart(df, selected_features)
            elif chart_type == "Bar Chart":
                generate_bar_chart(df, selected_features)
            elif chart_type == "Scatter Plot":
                generate_scatter_plot(df, selected_features)
            elif chart_type == "Pie Plot":
                generate_pie_plot(df, selected_features)
            elif chart_type == "Bubble Plot":
                columns = df.columns.tolist()
                x_feature = selected_features[0]
                y_feature = selected_features[1]
                size_feature = selected_features[2] 
                generate_bubble_plot(df, x_feature, y_feature, size_feature)

            
            
def generate_line_chart(df, selected_features):
    
    plt.figure(figsize=(10, 6))
    for feature in selected_features:
        plt.plot(df.index, df[feature], label=feature)

    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.title("Line Chart")
    plt.legend()
    st.pyplot()

def generate_bar_chart(df, selected_features):
    
    fig = px.bar(df, x=df.index, y=selected_features, barmode="group")
    fig.update_layout(title="Bar Chart", xaxis_title="Index", yaxis_title="Values")
    st.plotly_chart(fig)

def generate_scatter_plot(df, selected_features):
    fig = px.scatter(df, x=selected_features[0], y=selected_features[1], title="Scatter Plot",
                     labels={selected_features[0]: selected_features[0], selected_features[1]: selected_features[1]})
    st.plotly_chart(fig)
    
def generate_pie_plot(df, selected_features):
    # Extracting data for selected features
    data = df[selected_features]
    feature_sums = data.sum()    
    fig, ax = plt.subplots()
    ax.pie(feature_sums, labels=feature_sums.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Pie Plot of Selected Features')
    
    # Showing the plot
    st.pyplot(fig)
    
def generate_bubble_plot(df, x_feature, y_feature, size_feature):
    # Creating the bubble plot
    fig, ax = plt.subplots()
    ax.scatter(df[x_feature], df[y_feature], s=df[size_feature]*100, alpha=0.5)
    ax.set_xlabel(x_feature)
    ax.set_ylabel(y_feature)
    ax.set_title('Bubble Plot')
    
    # Showing the plot
    st.pyplot(fig)

if __name__ == "__main__":
    main()
