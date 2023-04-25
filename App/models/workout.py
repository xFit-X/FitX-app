from App.database import db

class Workout(db.Model):
    workoutId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    muscle = db.Column(db.String(200), nullable=False)
    equipment = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.String(100000), nullable=False)

    def __init__(self, name, type, muscle, equipment, difficulty, instructions):
        self.name = name
        self.type = type
        self.muscle = muscle
        self.equipment = equipment
        self.difficulty = difficulty
        self.instructions = instructions

    def __repr__(self):
        return f'<Workout {self.workoutId} - {self.name} - {self.difficulty} - {self.type}>' 

    def toJSON(self):
        return {
            'workoutId': self.workoutId,            
            'name': self.name,
            'type': self.type,
            'muscle': self.muscle,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'instructions': self.instructions,            
        }

