import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_client import Counter
from prometheus_client import make_asgi_app

c = Counter('change_color_counter_total', 'Count the color change', ['status_code'])


app = FastAPI()

colors = [ 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple']


@c.inc
@app.get('/changeColor', response_class=HTMLResponse)
def change_color():
    color = random.choice(colors)
    return f'''
        <html>
            <head>
                <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
                <style>
                    body {{
                        background-color: {color};
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                        margin: 0;
                        font-family: 'Roboto', sans-serif;
                    }}
                    h1 {{
                        font-size: 48px;
                        text-align: center;
                        color: white;
                    }}
                </style>
            </head>
            <body>
                <h1>Mudar é preciso com {color}!</h1>
            </body>
        </html>
    '''

metrics_app = make_asgi_app()
app.mount('/metrics', metrics_app)
