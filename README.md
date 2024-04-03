# S3 CSV Transformation 

This project aims to analyse fish market data from a CSV file, clean and transform the data to calculate averages per fish species, and then save the processed data to a new CSV file. Additionally, the project involves uploading the new CSV file to an S3 bucket on AWS.

## Project Steps

1. **Read Fish CSV**: The project starts by reading the fish data which is done using boto3 to read the original fish market csv file.

2. **Clean Data and Transformation**: Data cleaning and transformation are performed using pandas to remove unneccesary values and calculate averages per fish species.

3. **Upload to S3 Object**: The new CSV file is uploaded to an S3 bucket.

## Implementation Details

- **Scrum Project**: The project follows a Scrum framework, allowing for iterative development and regular feedback.

- **Kanban**: A Kanban board was used to manage project tasks and workflow, enabling easy tracking of progress and identifying bottlenecks.

- **User Stories**: User stories are used to define project requirements and prioritize tasks based on user needs.

- **Implemented Individually**: Each team member implements their assigned tasks individually.

## Installation 
Run the following to install all required packages.

```
pip install boto3 
pip install pandas
pip install io
```

