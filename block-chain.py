import json
from time import time
from flask import Flask, jsonify, request

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': "1234567890", 
        }
        
        self.current_transactions = [] 
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.chain[-1]['index'] + 1 

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = str(hash(guess))
        return guess_hash.startswith("1")


app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.chain[-1] 
    last_proof = last_block['proof']
    
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(sender="0", recipient="moje_adresa", amount=1)
    block = blockchain.new_block(proof)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transakce přidána'}), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
