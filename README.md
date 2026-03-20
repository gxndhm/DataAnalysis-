# 5004CMD: US Mobility Big Data Analytics
**Student:** Arman Gandham (15611886)
**Project Title:** Investigating Big Data Analytics for US Mobility Statistics: A Parallel Computing Approach

## Project Overview
This project implements a parallel computing framework using **Dask** to process large-scale Bureau of Transportation Statistics (BTS) datasets. It evaluates computational efficiency across 1, 10, and 20 workers and provides predictive travel modeling using Linear Regression.

## Repository Structure
- `analysis_main.py`: Main Dask pipeline for data cleaning and filtering.
- `performance_benchmarking.py`: Script used to generate the 1 vs 10 vs 20 worker timings.
- `visualizations.py`: Code used to generate Figures 1-7 for the report.
- `requirements.txt`: List of necessary Python libraries.

## Key Results
- **Computational Gain:** 81.9% reduction in processing time (148.42s to 26.88s).
- **Model Accuracy:** R² score of 0.9457 and RMSE of 1,981,455.
- **Peak Week Identified:** August 4–10, 2019 (Week 32).

## Requirements
To run this project, install the following:
`pip install dask pandas scikit-learn matplotlib seaborn`
