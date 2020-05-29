#!/usr/bin/env python
import json
import random
import time
import uuid

from kafka import KafkaProducer


def main():
    producer = KafkaProducer(bootstrap_servers='localhost:9093')
    for _ in range(100):
        data = json.dumps({
            'a_int': random.randint(0, 1_000_000),
            'a_str': str(uuid.uuid4()),
            'a_bool': random.choice([True, False])
        })
        producer.send('to_cassandra', data.encode('utf-8'))
        time.sleep(1)


if __name__ == '__main__':
    main()
