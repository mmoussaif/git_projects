# Import KafkaProducer from Kafka library
from kafka import KafkaProducer

# Import JSON module to serialize data
import json

# Initialize producer variable and set parameter for JSON encode
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send data in JSON format
producer.send('Topic', {'name': 'Amine','email':'Amine@gmail.com'})
 
# Print message
print("Message Sent to Topic")
# block until all async messages are sent
producer.flush()