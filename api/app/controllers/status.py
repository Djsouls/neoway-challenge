from flask import jsonify

from db.repositories import StatusRepository

class StatusController:
    def __init__(self):
        self.repository = StatusRepository()

    def uptime(self):
        return jsonify({'uptime': self.repository.uptime()})