from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
with open('inputfile.txt') as f:
     lines = f.readlines()

for line in lines:
   producer.send('test', line)