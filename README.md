# timesheet-calendar-generator

Programatically generate a "subscribable" ICS calendar for time-sheet notifications. Hosted via Vercel.

## Purpose

Most calendar systems (Apple, Google, Microsoft) do not support logic for repeating event criteria of "last business day of the month."  
To create reminders for timesheets that are due at month-end, a subscribable ICS link was my solution.

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
