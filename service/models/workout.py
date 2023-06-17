import sqlite3


class Workout:
    _id = 0
    _name = ""
    _descreption = ""
    _coach = ""
    _duration = ""

    def from_args_database(self, arguments):
        try:
            _name = arguments['name']
            _descreption = arguments['description']
            _coach = arguments['coach']
            _duration = arguments['duration']
            conn = sqlite3.connect('database/database.db', check_same_thread=False)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO project (name, description, duration, coach) VALUES (?, ?, ?, ?)",
                           (_name, _descreption, _duration, _coach))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False

    def get_workout(self, id):
        conn = sqlite3.connect('database/database.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project WHERE id = ?", (id,))
        workout = cursor.fetchone()
        if workout is None:
            return None
        conn.close()
        return workout

    def get_all_workouts(self):
        conn = sqlite3.connect('database/database.db', check_same_thread=False)
        cursor = conn.cursor()
        query = "SELECT * FROM project"
        cursor.execute(query)
        workouts = cursor.fetchall()
        all = []
        for workout in workouts:
            dish_dict = {
                'id': workout[0],
                'name': workout[1],
                'description': workout[2],
                'duration': workout[3],
                'coach': workout[4],
            }
            all.append(dish_dict)
        conn.close()
        return all

    def delete_workout(self, id):
        conn = sqlite3.connect('database/database.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM project WHERE id = ?", (id,))
        dish = cursor.fetchone()
        if dish is None:
            return False
        query = "DELETE FROM project WHERE id=?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return True

    def update_workout(self, id, arguments):
        try:
            _name = arguments['name']
            _descreption = arguments['description']
            _coach = arguments['coach']
            _duration = arguments['duration']
            conn = sqlite3.connect('database/database.db', check_same_thread=False)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM project WHERE id = ?", (id,))
            workout = cursor.fetchone()
            if workout is None:
                return False
            query = "UPDATE project SET name=?, description=?, duration =?, coach =? WHERE id=?"
            cursor.execute(query, (_name, _descreption, _duration, _coach, id))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False