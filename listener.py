import redis

pool = redis.ConnectionPool(max_connections=500,
                            host="localhost",
                            db=1,
                            port=6379)

connection = redis.Redis(connection_pool=pool)
pubsub = connection.pubsub()
channel = 'TEST_CHANNEL'
pubsub.psubscribe(channel)

for message in pubsub.listen():
    print message
