from App.database import db

class PersonalWorkout(db.Model):
    pwId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100),nullable = False)
    type = db.Column(db.String(100),nullable = False)
    muscle = db.Column(db.String(50),nullable = False)
    equipment = db.Column(db.String(50),nullable = False)
    difficulty = db.Column(db.String(50),nullable = False)
    sets = db.Column(db.Integer,nullable = False, default=3)
    reps = db.Column(db.Integer,nullable = False, default=8)
    weight = db.Column(db.String(30), nullable=False, default="10lbs")
    day = db.Column(db.String(10),nullable = False)
    pub = db.Column(db.Boolean, default=False)

    def __init__(self, userId,name, type, muscle, equipment, difficulty, sets, reps, day,weight,pub=False):
        self.name = name
        self.muscle = muscle
        self.type = type
        self.equipment = equipment
        self.difficulty = difficulty
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.day = day
        self.pub = pub

    def __repr__(self):
        return f"<PersonalWorkout {self.pwId}: {self.name}: {self.day}>"

    def toJSON(self):
        return {
            'pwId': self.pwId,
            'userId':self.userId,
            'name': self.name,
            'muscle': self.muscle,
            'type': self.type,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'sets': self.sets,
            'reps': self.reps,
            'weight':self.weight,
            'day': self.day,
            'pub': self.pub
        }