import api_complibot
from random import randint


update_id = None


# importing compliments
def import_compliments():
    file = open('compliment_list.txt','r')
    compliments = file.read().splitlines()
    compliment = compliments[randint(0,len(compliments)-1)]
    file.close()
    return compliment


def make_reply(msg):
    if msg is not None:
        reply = import_compliments()
    return reply


while  __name__ == '__main__':
    print("...")
    updates = api_complibot.get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            api_complibot.send_message(reply, from_)
