from kafka import KafkaConsumer
import json, sys
host_id = '10.52.90.10:9092'
topicid = 'ns-eg-ff15a252-f927-48c7-a98f-2965ab6c187d'
consumer = KafkaConsumer(topic_id,
                         group_id='120',
                         bootstrap_servers=[host_id], value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         api_version=(0, 10, 1))
try:
    for message in consumer:
        if message is None:
            continue
        else:
            print(json.dumps(message.value, indent=4, sort_keys=True))

except KeyboardInterrupt:
    sys.stderr.write('++++++ Aborted by user ++++++++\n')

finally:
    consumer.close()
    
