import producer_server
import sys


def run_kafka_server():
	# TODO get the json file path
    
    my_main_in_file = "police-department-calls-for-service.json"
    my_test_in_file = "police-62items.json"
    
    if use_small_file:
        input_file = my_test_in_file
    else:
        input_file = my_main_in_file

    print("my input-data-file:", input_file)

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police_calls_v3",
        bootstrap_servers="localhost:9092",
        client_id="my_police1",
        batch_size = 16
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()
    #print("closing producer")
    #producer.close()


if __name__ == "__main__":
    print("my kafka_server.py started")
    le = len(sys.argv)
    arg1 = ""
    if le > 1:
        arg1 = sys.argv[1] 

    use_small_file = ( 
        True if arg1 == "--use-small-file"
        else False )
    
    print("option  --use-small-file:", use_small_file)

    feed()
