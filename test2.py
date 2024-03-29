from requests import get, post

print(post('http://localhost:5000/api/jobs',
           json={'id': 9, 'job': 'installation of radiation protection', 'team_leader': 1, 'work_size': 45,
                 'collaborators': '6, 4, 7', 'is_finished': False}).json())  # id=9 exists
print(post('http://localhost:5000/api/jobs',
           json={'id': 10, 'job': 'installation of radiation protection'}).json())  # not full list of characters
print(post('http://localhost:5000/api/jobs').json())  # empty request
print(post('http://localhost:5000/api/jobs',
           json={'id': 8,
                 'job': 'installing a long-distance communication antenna',
                 'work_size': 5,
                 'collaborators': '6, 3',
                 'start_date': '',
                 'end_date': '',
                 'is_finished': True,
                 'team_leader': 4
                 }).json())  # cool request
print(get('http://localhost:5000/api/jobs').json())
