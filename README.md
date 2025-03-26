# Students performance


![](data/images/unnamed.jpg)
#### created virtual environment
`conda create -p ./stdenv python=3.8`
#### activate virtual environment 
`conda activate D:\dataanalysis\students_performance\stdenv`

# Project Directory Structure

```bash
# Students Performance Project Directory Structure

```bash

students_performance/
│-- setup.py
│-- requirements.txt
│-- README.md
│-- app.py
│-- templates/              # Contains HTML templates (if applicable)
│-- data/                   # Stores raw and processed data
│
└── src/
    │-- logger.py           # Handles logging
    │-- customexception.py  # Custom exception handling
    │-- utils.py            # Utility functions
    │
    ├── pipeline/           # Pipeline scripts for end-to-end processing
    │   │-- data_ingestion_pipeline.py
    │   │-- data_transformation_pipeline.py
    │   │-- model_training_pipeline.py
    │   │-- prediction_pipeline.py
    │
    ├── components/         # Core functional components
    │   │-- data_ingestion.py
    │   │-- data_transformation.py
    │   │-- model_training.py
    │   │-- prediction.py

```