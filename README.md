# Log Monitoring Pipeline using AWS

This project demonstrates how to build and deploy a ClodWatch Log Monitoring pipeline using AWS services. the pipeline generates and captures logs from a lambda function, stores them in Amazon S3, make queriable with Athena, and send alerts using SNS based on custom thresholds.

---
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
