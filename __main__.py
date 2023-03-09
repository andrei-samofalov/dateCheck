import datetime

from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(
    app,
    'DATE CHECK',
    description='For learning datetime formats visit '
                '[docs.python.org](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)'
)

date_check = api.namespace(
    'date_check'
)


@date_check.route('/')
@date_check.param('valid', description='Valid date format', default="%Y/%m/%d")
@date_check.param('check', description='Date string for check', default='2012/12/12')
class DateCheck(Resource):

    def get(self):
        valid = request.args.get('valid')
        check = request.args.get('check')

        if valid is None:
            valid = '%Y/%m/%d'

        response = {
                'date': {
                    'validation': f'{valid}',
                    'check': f'{check}'},
                'valid': False
            }

        try:
            datetime.datetime.strptime(check, valid)
            response['valid'] = True
            return response, 200
        except ValueError:
            return response, 400


@date_check.route('/admin')
@date_check.hide
class Admin(Resource):
    def get(self):
        return {"message": "Брысь!"}, 403


if __name__ == '__main__':
    app.run('0.0.0.0', port=5555)
