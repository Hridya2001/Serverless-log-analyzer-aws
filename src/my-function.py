import json
import logging

# Step 1: Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # You can change this to DEBUG, WARNING, etc.

# Step 2: Main Lambda function handler
def lambda_handler(event, context):
    print("Hello from print() - basic log message.")
    
    logger.debug("DEBUG log: Used for detailed troubleshooting.")
    logger.info("INFO log: Function started successfully.")
    logger.warning("WARNING log: Something might be wrong.")
    logger.error("ERROR log: Something went wrong!")

    # Step 3: Return a response (seen in test results, not logs)
    return {
        'statusCode': 200,
        'body': json.dumps('Log messages were sent to CloudWatch!')
    }


