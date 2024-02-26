import streamlit as st
import pandas as pd
import altair as alt

def main():
    st.title("Data Visualization Tool")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the DataFrame
        st.write("Preview of the uploaded data:")
        st.write(df.head())

        # Select features for comparison
        selected_features = st.multiselect("Select features for comparison", df.columns)

        if not selected_features:
            st.warning("Please select at least one feature for comparison.")
        else:
            # Choose the type of chart
            chart_type = st.selectbox("Select the type of chart", ["Line Chart", "Bar Chart", "Scatter Plot"])

            # Generate and display the chart based on user selections
            if chart_type == "Line Chart":
                generate_line_chart(df, selected_features)
            elif chart_type == "Bar Chart":
                generate_bar_chart(df, selected_features)
            elif chart_type == "Scatter Plot":
                generate_scatter_plot(df, selected_features)

def generate_line_chart(df, selected_features):
    chart = alt.Chart(df).mark_line().encode(
        x="index",
        y=selected_features
    ).properties(
        width=800,
        height=500
    )
    st.altair_chart(chart, use_container_width=True)

def generate_bar_chart(df, selected_features):
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("index", title="Index"),
        y=alt.Y(selected_features, title="Values"),
        column=alt.Column("variable", title="Features")
    ).properties(
        width=800,
        height=500
    )
    st.altair_chart(chart, use_container_width=True)

def generate_scatter_plot(df, selected_features):
    chart = alt.Chart(df).mark_circle().encode(
        x=selected_features[0],
        y=selected_features[1],
        tooltip=selected_features
    ).properties(
        width=800,
        height=500
    )
    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()
