import boto3
import time

athena = boto3.client('athena')
sns = boto3.client('sns')

DATABASE = 'log_analysis_db'
TABLE = 'logs_json'
SNS_TOPIC_ARN = ''
OUTPUT_BUCKET = ''
THRESHOLD = 5

def lambda_handler(event, context):
    query = f"""
        SELECT COUNT(*) AS error_count
        FROM {TABLE}
        WHERE message LIKE '%ERROR%'
          AND from_iso8601_timestamp(timestamp) > current_timestamp - interval '10' minute
    """

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': DATABASE},
        ResultConfiguration={'OutputLocation': OUTPUT_BUCKET}
    )
    
    query_execution_id = response['QueryExecutionId']

    while True:
        status = athena.get_query_execution(QueryExecutionId=query_execution_id)
        state = status['QueryExecution']['Status']['State']
        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(2)

    if state == 'SUCCEEDED':
        result = athena.get_query_results(QueryExecutionId=query_execution_id)
        error_count = int(result['ResultSet']['Rows'][1]['Data'][0]['VarCharValue'])

        if error_count > THRESHOLD:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='Log Error Alert from Athena',
                Message=f"{error_count} ERROR logs found in the last 10 minutes!"
            )

    return {
        'statusCode': 200,
        'message': 'Query executed, alert sent if needed'
    }


