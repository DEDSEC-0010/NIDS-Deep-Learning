import csv
from confluent_kafka import Producer, Consumer

def read_config():  # No changes needed here
    config = {}
    with open("client.properties") as fh:
      for line in fh:
        line = line.strip()
        if len(line) != 0 and line[0] != "#":
          parameter, value = line.strip().split('=', 1)
          config[parameter] = value.strip()
    return config

def produce(topic, config, csv_file):  # Added a csv_file parameter
    producer = Producer(config)

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)  # Use DictReader for headers
        for row in reader:
            key = row.get('Label')  # Adjust if you have a 'key' column
            value = str(row)  # Convert the entire row to string
            producer.produce(topic, key=key, value=value)
            print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")

    producer.flush()


def main():
    config = read_config()
    topic = "singlestore_topic"
    csv_file = "/content/drive/MyDrive/project/result03012018.csv"  # Replace with the path to your CSV file

    produce(topic, config, csv_file)  # Pass the CSV filename

main()
