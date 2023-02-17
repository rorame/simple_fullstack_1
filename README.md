# How to run using Docker
1. `docker-compose up`
2. to complete - `docker-compose down`

# How to run without Docker
## Backend
1. `git clone git@github.com:rorame/simple_fullstack_1.git -b main`
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py runserver`

## Frontend
1. `cd frontend`
2. `npm install`
3. `npm start`

Ports:
- Backend: 8000
- Frontend: 3000