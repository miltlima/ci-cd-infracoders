import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 


app = FastAPI()

colors = [ 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple']

@app.get('/changeColor', response_class=HTMLResponse)
def change_color():
    color = random.choice(colors)
    return f'''
        <html>
            <head>
                <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
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
                <h1>Mudar é preciso!</h1>
            </body>
        </html>
    '''


