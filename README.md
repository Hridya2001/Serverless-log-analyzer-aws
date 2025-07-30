# Serverless-log-analyzer-aws
# Serverless Log Analyzer (AWS)

 A fully serverless log analysis project to collect logs from AWS Lambda, store them in S3, and analyze using Glue + Athena.

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
| `diagrams/`   | Architecture diagrams (PNG or drawio)|

---


## 🛠 Tools & Services Used

- AWS Lambda
- CloudWatch Logs
- S3
- Glue
- Athena
- SNS (for alerts)

---
