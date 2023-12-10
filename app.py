from datetime import datetime, timedelta

import pytz as pytz
from fastapi import FastAPI, Response
from ics import Calendar, Event

from generate_calendar import calculate_last_weekday_for_next_two_years

app = FastAPI()


@app.get("/")
@app.get("/download_calendar")
def download_calendar():
    cal = Calendar()

    for last_weekday in calculate_last_weekday_for_next_two_years():
        event_begin = datetime(last_weekday.year, last_weekday.month, last_weekday.day,
                               hour=13, minute=0, tzinfo=pytz.timezone('America/Chicago'))

        event = Event()
        event.name = "Monthly Timesheet Due"
        event.begin = event_begin
        event.end = event.begin + timedelta(minutes=30)
        cal.events.add(event)

    # Serialize the calendar to a string
    calendar_data = cal.serialize()

    # Set response headers
    response = Response(content=calendar_data)
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    response.headers["Content-Type"] = "text/calendar"

    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
