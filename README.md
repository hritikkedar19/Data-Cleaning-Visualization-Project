# Data Cleaning & Visualization Project

## Project Aim
This project cleans a raw sales dataset and creates visual insights using Python.

## Features
- Handles missing values
- Removes duplicate rows
- Detects and removes outliers using IQR method
- Creates visual charts
- Builds an interactive Streamlit dashboard

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Plotly

## Folder Structure
```
data_cleaning_visualization_project/
│
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
│
├── outputs/
│   └── generated charts
│
├── data_cleaning.py
├── visualization.py
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

### Step 1: Install libraries
```bash
pip install -r requirements.txt
```

### Step 2: Clean the data
```bash
python data_cleaning.py
```

### Step 3: Generate charts
```bash
python visualization.py
```

### Step 4: Run dashboard
```bash
streamlit run app.py
```

## Expected Outcome
You will learn:
- Data cleaning
- Missing value handling
- Duplicate removal
- Outlier treatment
- Exploratory Data Analysis
- Dashboard creation
- Data storytelling

## Resume Line
Built a Data Cleaning and Visualization project using Python, Pandas, Matplotlib, Seaborn, and Streamlit to clean raw sales data, handle missing values, remove duplicates and outliers, and create interactive business dashboards.