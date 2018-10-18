#!/usr/bin/env python3

import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='./')
    # app = Flask(__name__)
    app.add_api('swagger.yaml', arguments={'title': 'Hello World Example'})
    app.run()