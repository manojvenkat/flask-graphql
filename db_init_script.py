from application.models import TrackingRecord
from datetime import datetime
from application import create_app
from flask_sqlalchemy import SQLAlchemy


def create_all():
    app = create_app()
    db = SQLAlchemy(app)
    csv_file = open("./dataset.csv")
    lines = csv_file.readlines()[1:]
    for line in lines:
        line = line.replace('\n', '').split(',')
        tr = TrackingRecord(
            date=datetime.strptime(line[0], '%Y-%m-%d'),
            channel=line[1],
            country=line[2],
            os=line[3],
            impressions=line[4],
            clicks=int(line[5]),
            installs=int(line[6]),
            spend=float(line[7]),
            revenue=float(line[8]),
        )
        db.session.add(tr)

    db.session.commit()
    print("DB initialized successfully.. Exiting..")


if __name__ == "__main__":
    create_all()
