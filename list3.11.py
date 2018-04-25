
import redis
import threading
import time
from time import sleep


conn = redis.Redis(host='localhost',port=6379,db=0)

def publisher(n):
  time.sleep(1)
  for i in range(n):
    conn.publish('channel',i)
    time.sleep(1)

def run_pubsub():
  threading.Thread(target=publisher,args=(3,)).start()
  pubsub=conn.pubsub()
  pubsub.subscribe(['channel'])
  count=0
  for item in pubsub.listen():
    print(item)
    count+=1
    if count==4:
      pubsub.unsubscribe()
    if count==5:
      break

run_pubsub()
