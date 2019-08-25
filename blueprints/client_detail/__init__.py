# import random

# class Client():

#     def __init__(self):
#         self.reset()

#     def reset(self):
#         self.client_id = 0
#         self.client_key = None
#         self.client_secret = None
#         self.status = None

#     def serialize(self):
#         return {
#             'client_id': self.client_id,
#             'client_key': self.client_key,
#             'client_secret': self.client_secret,
#             'status': self.status
#         }

# class ClientList():

#     client_list = []

#     def __init__(self):
#         for i in range(1, 6):
#             client = Client()
#             client.client_id = i
#             client.client_key = 'CLIENT0{}'.format(i)
#             client.client_secret = 'SECRET0{}'.format(i)
#             client.status = random.choice([True, False])
#             self.client_list.append(client.serialize())

#     def list(self):
#         return self.client_list

#     def get_by_id(self, id):
#         for _, v in enumerate(self.client_list):
#             if v['client_id'] == int(id):
#                 return v
#         return None

#     def add_new(self, str_serialized):
#         self.client_list.append(str_serialized)

#     def update(self, id, client_key, client_secret, client_status):
#         for k, v in enumerate(self.client_list):
#             if v['client_id'] == int(id):
#                 client = Client()
#                 client.client_id = int(id)
#                 client.client_key = client_key
#                 client.client_secret = client_secret
#                 client.status = client_status
#                 self.client_list[k] = client.serialize()
#                 return self.client_list[k]
#         return None 

#     def delete(self, id):
#         for k, v in enumerate(self.client_list):
#             if v['client_id'] == int(id):
#                 self.client_list.pop(k)
#         return None








    
    