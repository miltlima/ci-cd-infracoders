import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from prometheus_client import make_asgi_app, Counter, Summary, Histogram, generate_latest
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

colors = ["red", "green", "blue", "yellow", "orange", "pink", "purple"]
counter = Counter("change_color_counter_total", "Count the color change")
summary = Summary(
    "change_color_request_time_seconds",
    "Response time in seconds to change color request",
)
histogram = Histogram(
    "change_color_time_seconds",
    "Request latency in seconds to change color",
    )


@app.get("/changeColor", response_class=HTMLResponse)
async def change_color():
    color = random.choice(colors)
    counter.inc()
    with summary.time():
        with histogram.time():
            return f"""
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
            """

@app.get("/metrics")
async def get_metrics():
    return generate_latest()

if __name__ == '__main__':
    instrumentator.instrument(app).expose(app, port=8000)
