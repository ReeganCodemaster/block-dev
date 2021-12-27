from hashlib import *

class Block:
    i = 0
    def __init__(self,previous_hash,transaction_list):
        self.previous_hash = previous_hash
        self.transaction_list = transaction_list
        self.nonce = 0
        for i in range(len(transaction_list)):
            transaction_list = '-'.join(transaction_list[i])
            i += 1
        block_data = '-'.join(transaction_list)
        self.block_hash = ''

    def mine(self,difficulty):
        self.block_hash = sha256()
        self.block_hash.update(str(self).encode('utf-8'))
        while int(self.block_hash.hexdigest(), 16) > 2 ** (256-difficulty):
            self.nonce += 1
            self.block_hash = sha256()
            self.block_hash.update(str(self).encode('utf-8'))

    def __str__(self):
        return '{} {}'.format(self.block_hash,self.nonce)
