# Matrix

Matrix is a Streamlit-based web application that allows users to upload an Excel file, select a sheet and column, and perform fuzzy matching on the selected column. The app provides options to filter the data, set a match threshold, and generate a report with the results.

## Features

- Upload an Excel file (.xlsx or .xls)
- Select a sheet from the uploaded file
- Choose a column to create a matrix
- Optionally filter the data by a selected column
- Set a match threshold for fuzzy matching
- Generate a report with summary and metadata
- Download the generated report as an Excel file

## File Structure

```
Matrix/
│
├── main.py
├── icon.png
└── README.md
```

- `main.py`: The main application script that contains the Streamlit app code.
- `icon.png`: The icon used for the Streamlit app.
- `README.md`: This README file.

## How to Use

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

## Contact

For any questions or feedback, please contact:
himalaya.datta@gmail.com