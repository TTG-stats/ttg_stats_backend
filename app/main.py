from fastapi import FastAPI


app = FastAPI()


@app.get('/status')
def status():
    """ Simple status check endpoint. """
    return {'status': 'ok'}
