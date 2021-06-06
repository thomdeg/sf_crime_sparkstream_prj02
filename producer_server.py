from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            jsonList = json.load(f)
            print("json-list read, num of elems:", len(jsonList))
            sleep_secs = 0.2
            print("crime-events per second...", 1.0/sleep_secs)
            cnt = 0
            for jsObj in jsonList:
                message = self.dict_to_binary(jsObj)
                # TODO send the correct data
                print("message to send:", message)
                
                self.send(self.topic, value=message)
                
                print("event sent.")
                cnt = cnt + 1
                if cnt % 20 == 0:
                    print("flushing...")
                    self.flush()
                time.sleep(sleep_secs)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        # jsStr = json.dumps(json_dict)
        # jbyts = jsStr.encode('utf8')
        return json.dumps(json_dict).encode('utf8')
        

## my_in_file = "police-department-calls-for-service.json"
## my_test_file = "police-62items.json"
        
if __name__ == "__main__":
    print("Hello from my producer_server.py")
    
    
        