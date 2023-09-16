# vtc - Uber Ride Fee Prediction

This project is aimed at predicting the fee of a Uber ride using machine learning techniques. It is organized into the following sections:

## 1. Training

### Repository
- The `training` directory contains a Jupyter Notebook (`model_training.ipynb`) where the machine learning model is developed and trained.
- To reproduce the model or experiment with different data, navigate to the `training` directory and follow the instructions in the notebook.

## 2. App

The App is designed as following:

![image](https://github.com/C-BdB/vtc/assets/137887330/c25dcdb1-13b2-4f17-82e6-10324fb13d17)

#### Stage 1: Trigger

- **Description**: This stage serves as the initial trigger point for the workflow.
- **Trigger Event**: It can be initiated by an event such as a user's action (e.g., requesting a ride) or through a scheduled job.

#### Stage 2: Put in Queue

- **Description**: After the trigger event, the workflow places the task or job into a queue.
- **Purpose**: Queues are used for managing asynchronous tasks and ensuring efficient processing.

#### Stage 3: Trigger Second App

- **Description**: This stage trigger the second application that makes the real process.

#### Stage 4: Call External API to Get Meteo Data (Not developed yet)

- **Description**: In this stage, the workflow makes an HTTP request to an external API to retrieve meteorological (weather) data.

#### Stage 5: Read Model into Data Lake

- **Description**: This stage reads the model into the data lake.

#### Stage 6: Send Callback

- **Description**: The workflow concludes by sending a callback or notification.

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

1. Clone this repository to your local machine, preferrably on VSCode:

   ```bash
   git clone https://github.com/C-BdB/vtc.git

2. Install dependancies of the requirements.txt
3. Install Azurite Extension on VSCode, Azure Functions Core tools
4. Use Postman to send requests (see the body of a typical request in the app/api_definition repository
5. Prepare a webhook to receive the asynchronous response
6. Run the code
   ```bash
   func host start
