import datetime
import time
import hashlib
from binascii import unhexlify, hexlify

class Block:
    def __init__(self, prev_hash, transaction, amount):
        self.next = None
        current_time = datetime.datetime.now().time()

        self.__data = {
            "prev_hash": prev_hash,
            "transaction": transaction,
            "amount": amount,
            "hash": "",
            "time": current_time.strftime("%H:%M:%S")
        }
        self.__data['hash'] = self.make_hash()

    def get_data(self):
        return self.__data

    def make_hash(self):
        start = time.time()

        test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf-8")
        while test_hash[:3] != "000":
            test_hash = hexlify(hashlib.sha256(unhexlify(test_hash)).digest()).decode("utf-8")
        
        finish = time.time() - start
        print(f"Ушло: {finish}")

        return test_hash
    
    def add_data(self, transaction, amount):
        n = self
        while n.next:
            n = n.next
        prev_hash = n.get_data()['hash']
        end = Block(prev_hash, transaction, amount)
        n.next = end


def print_blocks(block):
    node = block
    print(node.get_data())
    while node.next:
        node = node.next
        print(node.get_data())

test_block = Block('000746bd11a3a38ad2ac56a51cec7be5ce5930da347d8b31b5ef505568182a49', 'Ivan', 100)
test_block.add_data("Boris", 1042)
print_blocks(test_block)
