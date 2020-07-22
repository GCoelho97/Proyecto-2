class Client:

    cruise = 'Saman Caribbean'

    def __init__(self, name, decision, amount, number_people, id_num, age, cripple):

        self.name = name
        self.decision = decision
        self.amount = amount
        self.number_people = number_people
        self.id_num = id_num
        self.age = age
        self.cripple = cripple

    def leave(self, clients):

        del clients[f'{self.name}']