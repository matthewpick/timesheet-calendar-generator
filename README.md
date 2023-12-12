# timesheet-calendar-generator

## Purpose

Programatically generate a "subscribable" ICS calendar for time-sheet notifications. Hosted via Vercel.

## Usage

Subscribe to the following URL with your calendar (Apple Calendar, Outlook, etc.):  
`https://timesheet-calendar-generator.vercel.app/`

The calendar URL can be previewed via this website too: https://icscalendar.com/preview

## Development

```
pip install -r requirements.txt

python3 generate_calendar.py  # test end-of-month date calculation
python3 app.py  # run FastAPI service locally via uvicorn
```
