from confluent_kafka import Producer
import time
import json

kafka_config = {
    'bootstrap.servers':'*****',
    'sasl.mechanisms':'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username':'****',
    'sasl.password':'****'
}

p = Producer(**kafka_config)

def delivery_report(err,msg):
    # Called once for each message produced to indicate delivery result.
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')
        
with open('user_data.json','r') as f:
    for line in f:
        record = json.loads(line)
        p.produce('user_data_topic',key = str(record['id']),value = json.dumps(record),callback=delivery_report)
        print("Message Published -> ",record)
        p.flush()
        time.sleep(3)   #Send one message per 20 seconds
        