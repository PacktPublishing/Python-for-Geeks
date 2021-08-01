from kafka import KafkaConsumer
import json, sys
host_id = '10.52.90.101:9092'
topic_id = 'NSP-EQUIPMENT'
consumer = KafkaConsumer(bootstrap_servers=['10.52.90.101:9092'],
                                     auto_offset_reset='earliest',
                                     consumer_timeout_ms=1000,
                                    api_version=(0, 10, 1))
consumer.subscribe([topic_id])
print(consumer)
try:
    for message in consumer:
        print(message)
        if message is None:
            continue
        else:
            msg = json.loads(message.value)
            print(json.dumps(msg, indent=4, sort_keys=True))


except KeyboardInterrupt:
    sys.stderr.write('++++++ Aborted by user ++++++++\n')

finally:
    consumer.close()
