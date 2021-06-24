# coding=utf-8
# os.getenv(key, default=None)
#
#    Return the value of the environment variable key if it exists
#    Otherwise, returns the default value.
#
import os

key = 'HOME'
value = os.getenv(key)
print("Value of %s environment variable : %s " % (key, value))

key = 'S3'
value = os.getenv(key)
print("Value of %s environment variable : %s " % (key, value))
