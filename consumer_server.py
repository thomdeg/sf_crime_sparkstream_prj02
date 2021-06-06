from kafka import KafkaConsumer

## old file name: my_consumer.py
## uda suggested: consumer_server.py


my_topic = "police_calls_v3"

class MyConsumer(KafkaConsumer):
    def __init__(self, topic, **kwargs):
        super().__init__(**kwargs)
        self.topic = topic
        self.consumer = KafkaConsumer(
            bootstrap_servers="localhost:9092",
            request_timeout_ms=1000,
            auto_offset_reset="earliest",
            client_id="my_police1",            
            max_poll_records=5)

        self.consumer.subscribe(topics=[self.topic])
    
    def consume_and_print_data(self):
        try:
            ret = self.consumer.poll(timeout_ms=1000 )
            print("type:", type(ret))
            print("ret:", ret)
            #print("ret:", ret.items() )
            print("len:", len(ret))
        except Exception as e:
            print("exception:", e)
            self.consumer.close()


def consume_data():
    c = MyConsumer(topic=my_topic)
    c.consume_and_print_data()
        
if __name__ == "__main__":
    print("my_consumer.py is starting as __main__")
    print("topic to consume is:", my_topic)
    print("consuming...")
    consume_data()
    