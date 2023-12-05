import csv
import redis

# Connect to Redis
redis_host = 'localhost'  # Change this to your Redis server host
redis_port = 6379         # Change this to your Redis server port
redis_db = 0              # Change this to your Redis database index

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# CSV file path
csv_file_path = 'apple_products.csv'

# Function to migrate CSV to Redis
def migrate_csv_to_redis(csv_file_path):
	with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			product = row['Product Name']
			year = row['Launch Year']
			active = row['Status']
			description = row['What it does?']

			# Assuming you want to use a Redis hash for each product
			redis_key = f"product:{product}"
			redis_client.hset(redis_key, 'Year', year)
			redis_client.hset(redis_key, 'Active', active)
			redis_client.hset(redis_key, 'Description', description)

if __name__ == "__main__":
	migrate_csv_to_redis(csv_file_path)
