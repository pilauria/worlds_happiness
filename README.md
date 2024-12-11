# World Happiness Analysis 2015-2017

## 🌍 Project Overview

This comprehensive data science project explores global happiness trends across different regions from 2015 to 2017. By analyzing the World Happiness Report dataset, we uncover insights into the factors that influence happiness scores worldwide.

## 🎯 Project Objectives

- Analyze regional happiness variations
- Identify trends in happiness scores over three years
- Visualize happiness distributions across different geographical regions
- Provide data-driven insights into global well-being

## 📊 Key Findings

### Regional Happiness Overview

1. **Highest Happiness Regions**:
   - Australia and New Zealand (Avg: 7.30)
   - North America (Avg: 7.23)
   - Western Europe (Avg: 6.69)

2. **Lowest Happiness Regions**:
   - Sub-Saharan Africa (Avg: 4.14)
   - Southern Asia (Avg: 4.59)
   - Middle East and Northern Africa (Avg: 5.39)

### Happiness Trends (2015-2017)

- **Most Stable Region**: Western Europe (minimal change)
- **Declining Regions**: 
  - Latin America and Caribbean (-0.18)
  - North America (-0.12)
  - Sub-Saharan Africa (-0.12)
- **Improving Regions**:
  - Southeastern Asia (+0.12)
  - Central and Eastern Europe (+0.08)

### Performance Variability

- **Highest Variability**: Middle East and Northern Africa (Range: 4.27)
- **Most Consistent**: North America (Range: 0.43)

## 🛠 Technical Details

### Data Sources
- World Happiness Report (2015-2017)
- Comprehensive dataset covering multiple global regions

### Technologies Used
- Python 3.x
- Data Analysis: Pandas
- Visualization: Matplotlib, Seaborn
- Statistical Processing: NumPy

### Project Structure
```
World_Happiness_2015/
├── data/               # Processed data and outputs
│   ├── happiness_tables.txt    # Formatted analysis results
│   └── regional_happiness_stats.csv
├── notebooks/          # Analysis scripts
│   ├── happiness_by_region.py
│   ├── happiness_visualization.py
│   └── happiness_trend.py
├── src/                # Source code
├── tests/              # Unit tests
└── requirements.txt    # Project dependencies
```

## 📈 Visualization Outputs

- Bar Plots: Mean Happiness Scores by Region
- Box Plots: Happiness Score Distributions
- Line Plots: Happiness Score Trends
- Violin Plots: Score Distributions and Variability

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Analysis
```bash
python notebooks/happiness_by_region.py
```

## 🔍 Detailed Analysis

For a comprehensive breakdown, refer to:
- `data/happiness_tables.txt`: Detailed regional statistics
- `data/regional_happiness_stats.csv`: Raw statistical data

## 🧪 Testing

### Prerequisites
- Python 3.7+
- pip

### Install Development Dependencies
```bash
pip install -r requirements-dev.txt
```

### Running Tests
There are multiple ways to run tests:

#### Option 1: Using Python Test Runner
```bash
python run_tests.py
```
This will:
- Install development requirements
- Run all tests
- Generate a coverage report
- Create an HTML coverage report in `htmlcov/`

#### Option 2: Direct Pytest
```bash
pytest tests/
```

#### Option 3: Specific Test Files
```bash
# Run specific test file
pytest tests/test_data_loading.py

# Run specific test
pytest tests/test_data_loading.py::TestDataLoading::test_csv_files_exist
```

### Test Types
- **Data Loading Tests**: Verify data can be loaded correctly
- **Visualization Tests**: Check plot generation
- **Statistical Analysis Tests**: Validate calculation accuracy

### Coverage Report
After running tests, check the coverage report in:
- Console output
- `htmlcov/index.html` for detailed HTML report

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

MIT License

## 🙏 Acknowledgments

- World Happiness Report
- Our global data science community
