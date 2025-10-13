import os
from app import create_app

env = os.getenv('FLASK_ENV', 'development')

app = create_app(env)

if __name__ == "__main__":
    # for deployment on platforms like Heroku, uncomment the line below:
    # app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=(env=="development"))
    # for local use, uncomment the line below:
    app.run(host="127.0.0.1", port=8080, debug=(env == 'development'))