import os
import pathlib

def create_project_structure():
    # Define the base directories
    directories = [
        'data',
        'notebooks',
        'src'
    ]
    
    # Create each directory
    for dir_name in directories:
        pathlib.Path(dir_name).mkdir(exist_ok=True)
    
    # Create requirements.txt with initial dependencies
    requirements = """
pandas==2.1.0
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
jupyterlab==4.0.3
scikit-learn==1.3.0
    """.strip()
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    # Create README.md with project description
    readme = """
# Social Media Marketing Performance Analysis

## Project Overview
This project analyzes social media marketing performance data to derive actionable business insights.

## Project Structure
- `data/`: Contains the datasets
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code for the project

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Analysis Goals
- Analyze engagement patterns
- Identify best-performing content types
- Determine optimal posting times
- Calculate ROI metrics
    """.strip()
    
    with open('README.md', 'w') as f:
        f.write(readme)

if __name__ == "__main__":
    create_project_structure()
