from kafka import KafkaConsumer
import json, sys
host_id = '10.52.90.10:9092'
topicid = 'ns-eg-ff15a252-f927-48c7-a98f-2965ab6c187d'
consumer = KafkaConsumer(topicid,
                         group_id='120',
                         bootstrap_servers=['10.52.90.10:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         api_version=(0, 10, 1))

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
    
