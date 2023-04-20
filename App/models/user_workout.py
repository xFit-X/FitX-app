from App.database import db

class UserWorkout(db.Model):   
    uwId = db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(30),default="My Workout")
    workoutId = db.Column(db.Integer, db.ForeignKey('workout.workoutId'))
    sets = db.Column(db.Integer, nullable=False, default=3)
    reps = db.Column(db.Integer, nullable=False,default=8)
    weight = db.Column(db.String(30),default="body")
    day = db.Column(db.String(30), nullable=False)
    pub = db.Column(db.Boolean, default=False)

    def __init__(self, userId, workoutId,name, sets, reps, weight, day,pub=False):
        self.userId = userId
        self.workoutId = workoutId
        self.name=name
        self.sets=sets
        self.reps = reps
        self.weight = weight
        self.day = day
        self.pub = pub

    def __repr__(self):
        return f'<user_workout {self.uwId} user: {self.userId} workout: {self.workoutId}>'

    def toJSON(self):
        return{
        'userId' : self.userId,
        'workoutId' : self.workoutId,
        'name':self.name,
        'sets' : self.sets,
        'reps' : self.reps ,
        'weight' : self.weight ,
        'day' : self.day,
        'pub' : self.pub
        }

    