import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
import io
from PIL import Image

# Set app title and icon
icon = Image.open("icon.png")
st.set_page_config(page_title="Matrix", page_icon=icon)

# Function to display instructions
def show_instructions():
    st.markdown("""
    ### Instructions
    1. **Upload File**: Click on "Choose a data file" to upload an Excel file (.xlsx or .xls).
    2. **Select Sheet**: Choose the sheet you want to work with from the uploaded file.
    3. **Select Matrix Column**: Select the column you want to use for creating the matrix.
    4. **Use Filter Columns**: Optionally, you can choose to filter the data by selecting "Use filter columns".
        - If you select this option, you can choose one filter column and its values to filter the data.
    5. **Set Match Threshold**: Use the slider to set the match threshold for fuzzy matching.
    6. **Generate Report**: Click on "Generate Report" to create an Excel report with two sheets:
        - **Summary**: Contains the count of matches for each value in the selected filter.
        - **Metadata**: Contains the table of matches that satisfy the threshold along with the filter column values.
    7. **Download Report**: Click on "Download Report" to download the generated report as an Excel file.
    """)

st.title("Welcome To The Matrix")

# Instruction button
if st.button("Show Instructions"):
    show_instructions()

# Upload file
uploaded_file = st.file_uploader("Choose a data file", type=["xlsx", "xls"])

if uploaded_file:
    # Load the Excel file with all columns as strings
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names

    # Select sheet
    sheet = st.selectbox("Select the sheet", sheet_names)
    if sheet:
        df = pd.read_excel(uploaded_file, sheet_name=sheet, dtype=str)
        columns = df.columns.tolist()

        # Select matrix column
        matrix_column = st.selectbox("Select the matrix column", columns)

        # Option to use filter
        use_filter = st.checkbox("Use filter columns")

        # Optional filter column
        filter_column = st.multiselect("Select filter columns (optional)", columns) if use_filter else []

        # Apply filters if any
        if filter_column:
            if len(filter_column) > 1:
                st.error("Please select only one filter column.")
            else:
                filter_col = filter_column[0]
                unique_values = df[filter_col].unique()
                selected_values = st.radio(f"Filter {filter_col}", unique_values, horizontal=True)
                if selected_values:
                    filtered_df = df[df[filter_col].isin([selected_values])]
                else:
                    filtered_df = df
        else:
            filtered_df = df

        # Display the matrix column (filtered or not)
        st.write(f"Matrix Column: {matrix_column}")
        st.write(filtered_df[matrix_column])

        # Create a matrix using the selected column and apply fuzzy matching
        matrix_values = filtered_df[matrix_column].tolist()
        matrix_size = len(matrix_values)
        matrix = pd.DataFrame(index=matrix_values, columns=matrix_values)

        for i in range(matrix_size):
            for j in range(matrix_size):
                if i != j:
                    ratio = fuzz.ratio(matrix_values[i], matrix_values[j])
                    matrix.iloc[i, j] = ratio
                else:
                    matrix.iloc[i, j] = 100  # Perfect match with itself

        # Add a slider for match threshold
        match_threshold = st.slider("Set match threshold", 0, 100, 80)

        # Highlight values in the matrix that are above the threshold
        def highlight_values(val):
            color = '#ff4b4b' if val >= match_threshold else ''
            return f'background-color: {color}'

        st.write("Matching Matrix")
        st.write(matrix.style.map(highlight_values))

        # Find matches that satisfy the threshold
        matches = []
        for i in range(matrix_size):
            for j in range(matrix_size):
                if i != j and matrix.iloc[i, j] >= match_threshold:
                    matches.append((matrix.index[i], matrix.columns[j], matrix.iloc[i, j]))

        # Display matches in a tabular form
        if matches:
            matches_df = pd.DataFrame(matches, columns=["Value 1", "Value 2", "Match Ratio"])
            st.write("Matches that satisfy the threshold")
            st.write(matches_df)

            # Display the count of matches
            st.write(f"Count of matches: {len(matches)}")

        # Generate report
        if st.button("Generate Report"):
            summary_data = []
            metadata_data = []

            if filter_column:
                filter_col = filter_column[0]
                for value in unique_values:
                    temp_df = df[df[filter_col] == value]
                    matrix_values = temp_df[matrix_column].tolist()
                    matrix_size = len(matrix_values)
                    matrix = pd.DataFrame(index=matrix_values, columns=matrix_values)

                    for i in range(matrix_size):
                        for j in range(matrix_size):
                            if i != j:
                                ratio = fuzz.ratio(matrix_values[i], matrix_values[j])
                                matrix.iloc[i, j] = ratio
                            else:
                                matrix.iloc[i, j] = 100  # Perfect match with itself

                    matches = []
                    for i in range(matrix_size):
                        for j in range(matrix_size):
                            if i != j and matrix.iloc[i, j] >= match_threshold:
                                matches.append((matrix.index[i], matrix.columns[j], matrix.iloc[i, j]))

                    summary_data.append([value, len(matches)])
                    for match in matches:
                        metadata_data.append([value] + list(match))

                summary_df = pd.DataFrame(summary_data, columns=[filter_col, "Match Count"])
                metadata_df = pd.DataFrame(metadata_data, columns=[filter_col, "Value 1", "Value 2", "Match Ratio"])
            else:
                matrix_values = df[matrix_column].tolist()
                matrix_size = len(matrix_values)
                matrix = pd.DataFrame(index=matrix_values, columns=matrix_values)

                for i in range(matrix_size):
                    for j in range(matrix_size):
                        if i != j:
                            ratio = fuzz.ratio(matrix_values[i], matrix_values[j])
                            matrix.iloc[i, j] = ratio
                        else:
                            matrix.iloc[i, j] = 100  # Perfect match with itself

                matches = []
                for i in range(matrix_size):
                    for j in range(matrix_size):
                        if i != j and matrix.iloc[i, j] >= match_threshold:
                            matches.append((matrix.index[i], matrix.columns[j], matrix.iloc[i, j]))

                summary_data.append(["All Data", len(matches)])
                for match in matches:
                    metadata_data.append(["All Data"] + list(match))

                summary_df = pd.DataFrame(summary_data, columns=["Filter", "Match Count"])
                metadata_df = pd.DataFrame(metadata_data, columns=["Filter", "Value 1", "Value 2", "Match Ratio"])

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
                metadata_df.to_excel(writer, sheet_name='Metadata', index=False)

            st.download_button(
                label="Download Report",
                data=output.getvalue(),
                file_name="report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        # End of the app
        st.markdown("*****")
        st.markdown("Got something to say? Share your feedback or a testimonial here: himalaya.datta@pwc.com / himalaya.datta@gmail.com")
