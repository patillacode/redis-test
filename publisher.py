import redis

pool = redis.ConnectionPool(max_connections=500,
                            host="localhost",
                            db=1,
                            port=6379)

connection = redis.Redis(connection_pool=pool)
data = {'test_key': 'test_value'}
channel = 'TEST_CHANNEL'
connection.publish(channel, data)
