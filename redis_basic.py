import redis

def main():

    #
    # Get Connection
    #
    try:
        redis_cli = redis.Redis(
            host='localhost',
            port='6379'
            )
    except Exception as e:
        print(str(e))
        return 1

    #
    # store value
    #
    redis_cli.set(key, value)

    #
    # Get keys
    #    
    key = redis_cli.get('key_name')
    print(key)
    
    s = redis_cli.keys('*') # all keys 
    print(s)

    #
    # Delete keys
    #    
    redis_cli.delete('key_name')
    
    redis_cli.delete(*s) # delete all keys


if __name__ == "__main__":
    main()
