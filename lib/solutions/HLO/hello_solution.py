

# noinspection PyUnusedLocal
# friend_name = unicode string
#@return = a String containing a message
def hello(friend_name):
    friend_name.strip('\"')
    return ("Hello, %s!" % friend_name)


