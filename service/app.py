import logging
import sqlite3
from datetime import datetime, timedelta

from flask import Flask
from flask import jsonify, request

from service.models.workout import Workout
# Создаём экземпляр приложения.
app = Flask(__name__)
workout = Workout()


@app.route('/', methods=['GET'])
def hello():
    """
    Скажи привет!
    :return: Сообщение с приветствием!
    """
    return jsonify({'message': 'Hello!'}), 200


#
@app.route('/workouts', methods=['GET'])
def get_workouts():
    logging.debug(f"{get_workouts.__name__}: Получение всех тренировок!")
    data = workout.get_all_workouts()
    logging.debug(f"{get_workouts.__name__}: Получение информация {data}!")
    return jsonify({'workouts': data}), 200


@app.route('/workouts', methods=['POST'])
def add_workout():
    logging.debug(f"{add_workout.__name__}: Добавление тренировки!")
    data = request.get_json()
    status = workout.from_args_database(data)
    if not status:
        return jsonify({'error': 'Error on creation workout!'}), 400
    else:
        return jsonify(message='Created workout'), 200


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout_info(id):
    logging.debug(f"{get_workout_info.__name__}: Получение тренировки с id {id}!")
    status = workout.get_workout(id)
    if status is None:
        return jsonify({'error': 'Workout not found'}), 404
    else:
        return jsonify(status), 200

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout_info(id):
    logging.debug(f"{update_workout_info.__name__}: Обновление тренировки с id {id}!")
    data = request.get_json()
    status = workout.update_workout(id, data)
    if status is False:
        return jsonify({'error': 'Workout not found or error on updating!'}), 404
    else:
        return jsonify(message=status), 200

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    logging.debug(f"{delete_workout.__name__}: Удаление тренировки с id {id}!")
    status = workout.delete_workout(id)
    if status is False:
        return jsonify({'error': 'Workout not found'}), 404
    else:
        return jsonify(message='Workout deleted!'), 200