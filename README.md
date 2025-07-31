# Log Monitoring Pipeline using AWS

This project demonstrates how to build and deploy a ClodWatch Log Monitoring pipeline using AWS services. the pipeline generates and captures logs from a lambda function, stores them in Amazon S3, make queriable with Athena, and send alerts using SNS based on custom thresholds.

---

## Services and Technologies Used

|AWS Lambda        |for log generation, transformation, and alerting
|
|Amazon CloudWatch – captures logs from Lambda
|
|Amazon S3 – stores raw log files
|
|AWS Glue – crawler to catalog log files
|
|Amazon Athena – queries logs using SQL
|
|Amazon SNS – sends alerts when error thresholds are exceeded


## Features

- Collects Lambda logs via CloudWatch subscription
- Stores structured logs in S3 (partitioned by date)
- Uses AWS Glue crawler to build schema
- Queries logs with Athena (e.g. error counts)
- Sends alerts when error count is high (future)

---

##  Project Structure

| Folder        | Description                          |
|---------------|--------------------------------------|
| `lambda/`     | Contains log processing Lambda code  |
| `glue/`       | Glue crawler + job documentation     |
| `athena/`     | SQL queries for log analysis         |
| `diagrams/`   | Architecture diagrams                |

---


##  Tools & Services Used
    
- AWS Lambda
- CloudWatch Logs
- S3
- Glue
- Athena
- SNS (for alerts)

---
