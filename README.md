# vtc - Uber Ride Fee Prediction

This project is aimed at predicting the fee of a Uber ride using machine learning techniques. It is organized into the following sections:

## 1. Training

### Repository
- The `training` directory contains a Jupyter Notebook (`model_training.ipynb`) where the machine learning model is developed and trained.
- To reproduce the model or experiment with different data, navigate to the `training` directory and follow the instructions in the notebook.

## 2. App

The App is designed as following: 
![image](https://github.com/C-BdB/vtc/assets/137887330/fe3eab85-188c-48d6-bce5-32455202e6db)

### Azure App
- The `app` directory includes an Azure web application designed to make predictions based on the trained machine learning model.
- You can deploy this app on Azure to provide a user-friendly interface for predicting Uber ride fees.

## 3. DevOps

### Continuous Integration and Continuous Deployment (CI/CD)
- The `devops` directory contains the necessary configuration and scripts for implementing CI/CD for the Azure app.
- We use Azure DevOps to automate the build and deployment processes.

## 4. Infrastructure

### Infrastructure as Code (IaC)
- The `infra` directory holds the infrastructure as code (IaC) scripts that define the resources needed to run the Azure app.
- These scripts can be used with tools like Terraform to provision and manage the required infrastructure.

## Getting Started

Follow these steps to get started with the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/C-BdB/vtc.git
