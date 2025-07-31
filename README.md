# Log Monitoring Pipeline using AWS

This project demonstrates how to build and deploy a ClodWatch Log Monitoring pipeline using AWS services. the pipeline generates and captures logs from a lambda function, stores them in Amazon S3, make queriable with Athena, and send alerts using SNS based on custom thresholds.

---

## Services and Technologies Used

- **AWS Lambda** : for log generation, transformation, and alerting
- **Amazon CloudWatch** : captures logs from Lambda
- **Amazon S3** : stores raw log files
- **AWS Glue** : crawler to catalog log files
- **Amazon Athena** : queries logs using SQL
- **Amazon SNS** : sends alerts when error thresholds are exceeded

## Architecture Overview
![Architecture Diagram](Daigrams/image.png)


---
##  Project Structure

| Folder/File              | Description                                             |
|--------------------------|---------------------------------------------------------|
| `src/`                   | Source code including Lambda functions and SQL queries  |
| ├── `my_function.py`     | Lambda to generate log messages                         |
| ├── `log_shipper.py`     | Lambda to decode & push logs to S3                      |
| ├── `athena_alert_lambda.py` | Lambda to run Athena query & trigger SNS alerts    |
| └── `queries.sql`        | SQL queries for log analysis in Athena                  |
| `Diagrams/image.png`     | Architecture diagram for the pipeline                   |
| `README.md`              | Project documentation and setup guide                   |
| `.gitattributes`         | Git config for line endings                             |
| `LICENSE`                | MIT license for open-source use                         |

## Features

- Collects Lambda logs via CloudWatch subscription
- Stores structured logs in S3 (partitioned by date)
- Uses AWS Glue crawler to build schema
- Queries logs with Athena (e.g. error counts)
- Sends alerts when error count is high (future)

---



##  Tools & Services Used
    
- AWS Lambda
- CloudWatch Logs
- S3
- Glue
- Athena
- SNS (for alerts)

---
