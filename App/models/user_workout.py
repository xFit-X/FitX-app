from App.database import db

class UserWorkout(db.Model):   
    uwId = db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    workoutId = db.Column(db.Integer, db.ForeignKey('workout.workoutId'))
    sets = db.Column(db.Integer, nullable=False, default=3)
    reps = db.Column(db.Integer, nullable=False,default=8)
    weight = db.Column(db.String(30), nullable=False,default="10lbs")
    day = db.Column(db.String(30), nullable=False)

    def __init__(self, userId, workoutId, sets, reps, weight, day):
        self.userId = userId
        self.workoutId = workoutId
        self.sets=sets
        self.reps = reps
        self.weight = weight
        self.day = day

    def __repr__(self):
        return f'<user_workout {self.uwId} user: {self.userId} workout: {self.workoutId}>'

    def toJSON(self):
        return{
        'userId' : self.userId,
        'workoutId' : self.workoutId,
        'sets' : self.sets,
        'reps' : self.reps ,
        'weight' : self.weight ,
        'day' : self.day
        }

    