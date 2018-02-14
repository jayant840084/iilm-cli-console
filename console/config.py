user_config = {
    'scope': {
        'admin': {},
        'guard': {},
        'director': {},
        'student': {},
        'hod': {},
        'warden': {}
    },
    'input_validation': {
            'uid': {
                'maxLength': 100,
                'minLength': 1
            },
            'name': {
                'maxLength': 50,
                'minLength': 5
            },
            'password': {
                'maxLength': 50,
                'minLength': 8
            },
            'gender': {},
            'phoneNumber': {
                'length': 10
            },
    }
}
