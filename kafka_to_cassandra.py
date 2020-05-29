#!/usr/bin/env python
import json

from cassandra.cluster import Cluster
from kafka import KafkaConsumer


def main():
    consumer = KafkaConsumer('to_cassandra', bootstrap_servers='localhost:9093', group_id='group_to_cassandra')

    cluster = Cluster()
    session = cluster.connect("a_kayspace")

    for msg in consumer:
        data = json.loads(msg.value.decode('utf-8'))
        print(data)

        session.execute(
            """
            INSERT INTO a_table (a_int, a_str, a_bool)
            VALUES (%s, %s, %s)
            """,
            (data['a_int'], data['a_str'], data['a_bool'])
        )


if __name__ == '__main__':
    main()
