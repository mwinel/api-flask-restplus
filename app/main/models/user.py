class User(object):
    '''This class provides a way to store user data'''

    users = [
        {
			'id': 1,
			'username': u'mwinel',
			'email': u'mwinel@example.com',
			'password': u'code618'
		},
		{
			'id': 2,
			'username': u'lucy',
			'email': u'lucy@example.com',
			'password': u'lava12'
		}
    ]

    def __init__(self, id, username, email, password):
        '''Initialize user objects'''
        self.id = id,
        self.username = username,
        self.email = email,
        self.password = password,
