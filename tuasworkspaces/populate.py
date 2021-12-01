from app import app,db
from datetime import datetime
from app.models import *

# add team
team=Team(id=1,teamName='Admin')
db.session.add(team)
team=Team(id=2,teamName='Manage')
db.session.add(team)
team=Team(id=3,teamName='Ops')
db.session.add(team)
team=Team(id=4,teamName='Dev')
db.session.add(team)
team=Team(id=5,teamName='HR')
db.session.add(team)
team=Team(id=6,teamName='Market')
db.session.add(team)

# add admin & users
user=User(id=1,username='admin',fullname='admin',position='admin',teamId=1)
user.set_password('admin')
db.session.add(user)

user=User(id=2,username='apple',fullname='Apple',position='CEO',teamId=2)
user.set_password('apple')
db.session.add(user)
user=User(id=3,username='bob',fullname='Bob',position='CTO',teamId=4)
user.set_password('bob')
db.session.add(user)
user=User(id=4,username='cat',fullname='Cat',position='employee',teamId=3)
user.set_password('cat')
db.session.add(user)
user=User(id=5,username='dave',fullname='Dave',position='pm',teamId=4)
user.set_password('dave')
db.session.add(user)
user=User(id=6,username='eve',fullname='Eve',position='employee',teamId=6)
user.set_password('eve')
db.session.add(user)
user=User(id=7,username='frank',fullname='Frank',position='employee',teamId=5)
user.set_password('frank')
db.session.add(user)
user=User(id=8,username='george',fullname='George',position='manager',teamId=3)
user.set_password('george')
db.session.add(user)

# add rooms
room=Room(id=1,roomName='room1',telephone=True,projector=True,whiteboard=True) # POISTA COST
db.session.add(room)
room=Room(id=2,roomName='room2',telephone=False,projector=True,whiteboard=True)
db.session.add(room)
room=Room(id=3,roomName='room3',telephone=False,projector=False,whiteboard=True)
db.session.add(room)
room=Room(id=4,roomName='room4',telephone=False,projector=False,whiteboard=True)
db.session.add(room)

# add past meetings
meeting=Meeting(id=9,title='past meeting',teamId=3,roomId=2,bookerId=2,date=datetime(2018,2,15),startTime=10,endTime=14,duration=4)
db.session.add(meeting)

# add past meetings
meeting=Meeting(id=15,title='future meeting1',teamId=3,roomId=2,bookerId=2,date=datetime(2018,3,15),startTime=11,endTime=14,duration=3)
db.session.add(meeting)

meeting=Meeting(id=16,title='future meeting2',teamId=6,roomId=3,bookerId=6,date=datetime(2018,3,15),startTime=10,endTime=13,duration=3)
db.session.add(meeting)

meeting=Meeting(id=17,title='future meeting3',teamId=6,roomId=3,bookerId=6,date=datetime(2018,3,15),startTime=15,endTime=19,duration=4)
db.session.add(meeting)

participants_user=Participants_user(id=1,meeting='future meeting1',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=2,meeting='future meeting1',userId=4)
db.session.add(participants_user)
participants_partner=Participants_partner(id=1,meeting='future meeting1',partnerId=2)
db.session.add(participants_partner)

participants_user=Participants_user(id=3,meeting='future meeting2',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=4,meeting='future meeting2',userId=4)
db.session.add(participants_user)
participants_partner=Participants_partner(id=2,meeting='future meeting2',partnerId=2)
db.session.add(participants_partner)
participants_user=Participants_user(id=5,meeting='future meeting3',userId=7)
db.session.add(participants_user)
participants_user=Participants_user(id=6,meeting='future meeting3',userId=4)
db.session.add(participants_user)
participants_partner=Participants_partner(id=3,meeting='future meeting3',partnerId=1)
db.session.add(participants_partner)
participants_user=Participants_user(id=7,meeting='past meeting',userId=2)
db.session.add(participants_user)
participants_user=Participants_user(id=8,meeting='past meeting',userId=7)
db.session.add(participants_user)
participants_partner=Participants_partner(id=4,meeting='past meeting',partnerId=3)
db.session.add(participants_partner)

db.session.commit()