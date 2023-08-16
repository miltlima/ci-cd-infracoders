const express = require('express');
const app = express();
const port = 3000;


const prom = require('prom-client');
const register = prom.register;

// Count change color config 
const counter = new prom.Counter({
  name: 'change_color_total',
  help: 'Count the color change',
  labelNames: ['statusCode']
}) 

// Histogram
const histogram = new prom.Histogram({
  name: 'change_color_time_seconds',
  help: 'Response time in seconds API',
  buckets: [ 0.1, 0.2, 0.3, 0.4, 0.5]
})

// Summary
const summary = new prom.Summary({
  name: 'change_color_request_time_seconds',
  help: 'Response time in seconds to change color request',
  percentiles: [0.01, 0.1, 0.5, 0.9, 0.99]
});


const colors = ['red', 'green', 'blue', 'yellow', 'orange']
app.get('/changeColor', (req, res) => {
    const randomIndex = Math.floor(Math.random() * colors.length);
    const color = colors[randomIndex];
    
    const time = Math.random();
    
    counter.labels('200').inc();
    histogram.observe(time);
    summary.observe(time);

    res.send(`
    <html>
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
            <style>
                body {
                    background-color: ${color};
                    font-family: 'Font Name', sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    font-size: 48px;
                    text-align: center;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>Mudar é preciso com Node.js e express</h1>
            
        </body>
    </html>
`);
});

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

app.listen(port, () => {
    console.log(`Servidor em execução em http://localhost:${port}`);
});