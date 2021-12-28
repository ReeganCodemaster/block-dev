import csv
from time import *
from hashlib import *
import sys
sys.path.insert(1, '../block-dev/Block')

from Block import Block

i = 1
Transaction_list = []
class Transaction:
    Sender = ''
    Reciever = ''
    Amount = 0
    Tag = f''
    Cur = ''
    list_1 = []

    def __init__(self,To,From,Amnt,Tag,Currency):
        self.Sender = From
        self.Reciever = To
        self.Amount = Amnt
        self.Tag = Tag
        self.Cur = Currency
        self.list_1 = [self.Sender,self.Reciever,str(self.Amount),self.Tag,self.Cur]

    def get(self):
        Ledger = {
            "From" : uName,
            "To"   : Reciever ,
            "Amount" : Amnt,
            "Currency": Cuurency,
            "Tag" : Tag

        }

        print(Ledger)

    def post(self):
        time_stamp = ctime()
        Tra_file = open('Transaction.csv','a',newline='')
        post = (uName,Reciever,Amnt,Tag,Cuurency,time_stamp)
        writer = csv.writer(Tra_file)
        writer.writerow(post)



for i in range(10):
    prompt = input(f'Do you want to enter a new transaction: (Y) (n) ')
    if prompt.upper() == 'Y':
        uName = input('Enter your user name: ')
        Reciever = input('Enter user name of the reciever of the payment: ')
        Amnt = int(input('Enter amount: '))
        Cuurency = input('Enter currency: ')
        Tag = input('Enter Reason for transaction: ')
        Transact = Transaction(Reciever,uName,Amnt,Cuurency,Tag)
        print(Transact.list_1)
        print('Transaction {} :\n'.format(i) , Transact.Sender , 'payed {} to {} \n'.format(Transact.Amount,Transact.Reciever))
        Transaction_list.insert(i,Transact.list_1)
    elif prompt.upper() == 'N':
        print(Transaction_list)
        save_to_block = input('Do you want to save transactions to block?')
        if save_to_block == 'yes':
            joint_first_trancation = '-'.join(Transaction_list[0])
            previous_hash = sha256(joint_first_trancation.encode('utf-8'))
            block = Block.Block(previous_hash, Transaction_list)
            block.mine(10)
            block.__str__()
            exit()
    else:
        print('Invalid operation')






