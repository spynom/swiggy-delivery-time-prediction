
# Business Problem:
In the competitive food delivery market, on-time delivery is critical for customer satisfaction, retention, and operational efficiency. Delays can lead to:

1. **Loss of customers:** Late deliveries lead to unhappy customers who may opt for competitors, thus affecting business revenue.

2. **Brand damage:** Consistent delays hurt the company's reputation, leading to negative reviews and damaging trust.

3**Inefficient resource allocation:** Without accurate prediction of delivery times, resources (drivers, food preparation) cannot be properly allocated, causing waste and inefficiency.

## Stakeholders and Their Problems:
### Customers:

* **Expectations:** Customers expect their food to arrive hot, fresh, and on time. A delayed delivery directly affects their experience and satisfaction.

* **Problem:** Customers face frustration when deliveries are late, leading to decreased loyalty. If food arrives late or in poor condition, it impacts their overall trust in the service.

* **Impact:** Delays can result in negative reviews, lost business, and reduced willingness to use the service again.

### Businesses (Food Delivery Companies):

* **Expectations:** Businesses aim to deliver a smooth and efficient service, ensuring timely food deliveries and maintaining customer satisfaction. They rely on accurate delivery time predictions to optimize their operations.

* **Problem:** Businesses often struggle with predicting accurate delivery times due to various dynamic factors such as traffic, weather, delivery route inefficiencies, and order volume.

* **Impact:** Incorrect predictions lead to resource mismanagement, dissatisfied customers, higher operational costs, and ultimately, lower profitability.

### Delivery Personnel:

- **Expectations:** Delivery personnel (drivers/riders) expect clear, manageable routes and timely deliveries to ensure efficiency, minimize downtime, and increase their earnings.

- **Problem:** Without accurate estimates of delivery times, they face uncertainty regarding their schedules, potentially leading to missed deliveries, excessive idle time, and disorganization in their workday.

- **Impact:** Delayed deliveries can harm the driver's reputation, affect their earning potential (due to penalties or lower tips), and result in frustration, leading to high turnover in the workforce.

### Food Preparation Staff:

- **Expectations**: The kitchen staff needs accurate delivery times to prepare food efficiently and to prevent overcooking or undercooking.

* **Problem:** Inaccurate predictions cause them to prepare food too early or too late, resulting in wasted food, or food that is no longer fresh by the time it reaches the customer.

* **Impact:** This leads to food waste, inefficient use of resources, and a poor customer experience.


# Our Solution

The company wants to optimize
delivery time predictions to improve customer experience by providing accurate
estimated delivery times (ETAs) and to manage resources effectively. Accurate
predictions of delivery time can also allow the business to:

### 1. **Improve Delivery Efficiency:**
Identifying factors that slow down deliveries
enables better resource allocation, such as more reliable scheduling for
delivery personnel.

### **2. Enhance Customer Satisfaction:**

Reliable delivery ETAs can improve the
customer experience by reducing wait-time uncertainty.

### **3. Optimize Operational Costs:**

If the model can predict scenarios with higher
delays, additional resources (like more drivers or prioritizing specific orders)
can be allocated.


# Workflow
**1. Data collection**<br>
**2. Data Preprocessing**<br>
**3. EDA**<br>
**4. Model building, Hyperparameter Tuning & Evaluation alongside Experiment Tracking**<br>
**5. Building a DVC pipeline**<br>
**6. Registering the model**<br>
**7. Building the API using Fastapi**<br>
**8. Setting up CI/CD pipeline**<br>
**9. Testing**<br>
**10. Building the Docker image and pushing to ECR**<br>
**11. Deployment on EKS cluster**<br>
**12. Monitoring and Alerting with the use of prometheus and grafana**


# Technologies

## **1. Version Control and Collaboration**

* ### Git 

  - **Purpose:** Distributed version control system for tracking changes in source code.<br>
  - **Usage:** Manage codebase, track changes, and collaborate with team members.

* ### GitHub

    - **Purpose:** Hosting service for Git repositories with collaboration features.<br>
    - **Usage:** Store repositories, manage issues, pull requests, and facilitate team
    collaboration.

## **2. Data Management and Versioning**

* ### DVC (Data Version Control)
    - **Purpose:** Version control system for tracking large datasets and machine learning
models.<br>
    - **Usage:** Version datasets and machine learning pipelines, enabling reproducibility and
collaboration.

* ### AWS S3 (Simple Storage Service)
    - **Purpose:** Scalable cloud storage service.<br>
    - **Usage:** Store datasets, pre-processed data, and model artifacts tracked by DVC.

## **3. Machine Learning and Experiment Tracking**

* ### Python
  - **Purpose**: Programming language for backend development and machine learning.
  - **Usage**: Implement data processing scripts, machine learning models, and backend services.

* ### Scikit-learn
  - **Purpose**: Library for classical machine learning algorithms.
  - **Usage**: Implement baseline models and preprocessing techniques.


* ### Mlflow
  - **Purpose**: Platform for managing the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry.
  - **Usage**: Track experiments, log parameters, metrics, and artifacts; manage model versions.

* ### MLflow Model Registry
  - **Purpose**: Component of MLflow for managing the full lifecycle of ML models.
  - **Usage**: Register models, manage model stages (e.g., staging, production), and collaborate on model development.

* ### Optuna
  - **Purpose**: Hyperparameter tuning.

## 4. Continuous Integration/Continuous Deployment (CI/CD)

* ### GitHub Actions
  - **Purpose**: Automation platform that enables CI/CD directly from GitHub repositories.
  - **Usage**:
    - Automate testing, building, and deployment pipelines.
    - Trigger workflows on events like code commits or pull requests.

Here's a revised version with some refinements for clarity and consistency:

---

## 5. Cloud Services and Infrastructure

### AWS (Amazon Web Services)
AWS provides a comprehensive suite of cloud computing services that can be leveraged for scalable and reliable infrastructure to support the application.

### AWS EC2 (Elastic Compute Cloud)
- **Purpose**: Scalable virtual servers in the cloud.
- **Usage**: Hosts backend services, APIs, and model servers, enabling the application to scale based on demand.

### AWS ECR (Elastic Container Registry)
- **Purpose**: A fully managed Docker container registry for storing and managing container images.
- **Usage**: Store container images for the application.
### AWS EKS (Elastic Kubernetes Service)
- **Purpose**: Managed Kubernetes service for automating the deployment, scaling, and management of containerized applications.
- **Usage**: Orchestrates containers to run the application in a highly available and scalable manner, ensuring efficient resource management and load balancing.

### AWS IAM (Identity and Access Management)
- **Purpose**: Securely manage access to AWS services and resources.
- **Usage**: Controls access permissions for users, groups, and services, ensuring that only authorized entities can interact with specific AWS resources.

## 6. Testing and Quality Assurance Tools

* ### Pytest
  - **Purpose**: Python testing framework.
  - **Usage**: Write unit tests for Python code.

## 7. API Development and Testing

* ### Frameworks:

* ### FastAPI
  - **Purpose**: Modern, fast web framework for building APIs with Python.
  - **Usage**: Develop high-performance APIs efficiently.

* ### API Testing Tools:

* ### Postman
  - **Purpose**: API development environment.
  - **Usage**: Design, test, and document APIs.

* ### Code Editors and IDEs:

* ### Pycharm
  - **Purpose**: Source code editor.
  - **Usage**: Write and edit code for development.

## 9. Additional Tools and Libraries

* ### Matplotlib
  - **Purpose**: Plotting library for Python.
  - **Usage**: Create static, animated, and interactive visualizations.

* ### Seaborn
  - **Purpose**: Statistical data visualization.
  - **Usage**: Generate high-level interface for drawing attractive graphics.

* ### Data Serialization Formats:

* ### JSON
  - **Purpose**: Lightweight data interchange format.
  - **Usage**: Transfer data between frontend and backend services.

* ### Docker
  - **Purpose**: Containerization platform.
  - **Usage**: Package applications and dependencies into containers for consistent
deployment.

# Experiments
In this project, we conducted several experiments to evaluate the performance of the model on different algo with hyperparameters and options.

## 1. Base Model Metrics
| Model      | MAE_train_error | MAE_test_error | r2_train_score | r2_test_score | cv_test_scores | cv_test_std_scores |
|------------|-----------------|----------------|----------------|---------------|----------------|--------------------|
| Base Model | 4.705           | 4.690          | 0.601          | 0.597         | 0.600          | 0.004              |

## 2. Methods to handel missing values

| Model                      | Method                     | Negative_test_MAE | Negative_train_MAE | Test_r2_score | Train_r2_score | CV_test_scores | CV_test_negative_std_scores |
|----------------------------|----------------------------|-------------------|---------------------|----------------|-----------------|-----------------|-----------------------------|
| RandomForestRegressor      | Iterative Imputer Method   | -3.076            | -1.155              | 0.828          | 0.976           | 0.826           | -0.001                      |
| RandomForestRegressor | KNN Imputer Method         | -3.092            | -1.155              | 0.827          | 0.976           | 0.826           | -7.095e-4                   |
| RandomForestRegressor | Center Value Fill Method   | -3.088            | -1.154              | 0.827          | 0.976           | 0.827           | -0.001                      |
| RandomForestRegressor | Drop Null Method           | -3.090            | -1.154              | 0.827          | 0.976           | 0.826           | -0.002                      |

## 3. Best model searching experiment

![image](/reports/figures/newplot.png)

## 4. LGBM Hyper parameter tuning
**Model with the best score after optimizing with optuna**:

| Model | n_estimators | Max Depth | Learning Rate | Subsample | Min Child Weight | Min Split Gain | Reg Lambda | Test MAE | CV Score | Test R² | Train MAE | Train R² | CV Std Error |
|--------|--------------|-----------|----------------|------------|------------------|----------------|------------|----------|----------|----------|------------|-----------|-------------|
| LGBM   | 195          | 12        | 0.1100         | 0.7996     | 20               | 0.0193         | 1.2891     | 3.0745   | 0.8302   | 0.8300   | 2.9159     | 0.8497     | 0.0016      |


## 5. RF Hyper parameter tuning
**Model with the best score after optimizing with optuna**:

| Model        | n_estimators | Max Depth | Max Features | Min Samples Split | Min Samples Leaf | Max Samples | Test MAE | CV Score | Test R² | Train MAE | Train R² | CV Std Error |
|--------------|--------------|-----------|---------------|--------------------|-------------------|-------------|----------|----------|----------|------------|-----------|---------------|
| RF Regressor | 277          | 14        | None          | 4                  | 3                 | 0.6858      | 3.0490   | 0.8324   | 0.8334   | 2.4388     | 0.8934     | 0.0013         |

## 5. stacking Regressor(with LGBM and RF Regressor)
**Model with the best score after optimizing with optuna**:

| Final Model     | Test MAE | CV Score | Test R² | Train MAE | Train R² | CV Std Error |
|-----------------|----------|----------|---------|-----------|----------|---------------|
| LinearRegressor | 3.024    | 0.8369   | 0.8371  | 2.641     | 0.8769   | 0.0019         |


# Project Organization

```
.
├── Makefile                 <- Convenience commands for development workflow
├── README.md                <- Top-level project overview and instructions
├── deployment.yaml          <- Kubernetes deployment configuration
├── Dockerfile               <- Containerization instructions for application
├── dvc.yaml                 <- DVC pipeline stages configuration
├── dvc.lock                 <- DVC lock file to ensure reproducibility
├── logs.log                 <- Output logs from training or inference runs
├── params.yaml              <- Model or pipeline parameters
├── pyproject.toml           <- Project configuration and metadata
├── requirements.txt         <- Python dependencies for reproducing the environment
├── run_information.json     <- Metadata or tracking info from model runs
│
├── .github/                 <- GitHub-specific workflows or configuration
│
├── data/                    <- Input data used for model training/testing
│   ├── raw/                 <- Raw data from source
│   ├── processed/           <- Preprocessed, cleaned datasets
│   └── interim/               <- Final dataset used for training models
│
├── fastapi_app/             <- Code related to the FastAPI backend deployment
│   ├── app.py              <- Entry point for FastAPI app
│   └── ...                  <- Other API routes, schemas, and utils
│
├── models/                  <- Trained models, serialized artifacts
│
├── notebooks/               <- Jupyter notebooks with experiments, EDA, etc.
│
├── references/              <- Reference material (e.g., data dictionaries, research)
│
├── reports/                 <- Generated analysis or reporting output
│   └── figures/             <- Plots or visualizations for reports
│
├── src/                     <- Source code for model pipeline
│   ├── __init__.py          <- Makes src a module
│   ├── data_preparation.py    <- Handles data loading
│   ├── data_cleanig.py     <- Data cleaning and transformation
│   ├── data_preprocessing_and_model_building.py            <- Model training script
│   ├── evaluate.py          <- Evaluate and log model performance
│   └── registry_model.py          <- Save, load, or register models
│
└── test/                    <- Unit or integration tests for various modules


```

--------

