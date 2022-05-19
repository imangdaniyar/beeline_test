import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import FileResponse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


def get_file_path():
    return os.environ.get('FILE_NAME')


@app.get("/get_enumerated_content/")
async def get_enumerated_content():
    with open(get_file_path(), 'r') as file:
        records = file.read().split('\n')
        counter = range(len(records))
        return JSONResponse(dict(zip(counter, records)))


@app.get("/get_file_content/")
async def get_content():
    with open(get_file_path(), 'r') as file:
        return JSONResponse({'content': file.read()})


@app.get("/download_file/")
async def download_file():
    return FileResponse(get_file_path())


@app.get("/get_file_record/")
async def get_record(line: int = 0):
    with open(get_file_path(), 'r') as file:
        records = file.read().split('\n')
        if 0 <= line <= len(records):
            return JSONResponse({line: records[line]})
        else:
            return JSONResponse({'error_message': 'Line out of range'})


@app.delete("/delete_record/")
async def delete_record(line: int = 0):
    with open(get_file_path(), 'r') as file:
        records = file.read().split('\n')
        if 0 <= line < len(records) and records != ['']:
            deleted_record = records.pop(line)
            with open(get_file_path(), 'w') as output:
                output.write("\n".join(records))
            return JSONResponse({line: deleted_record})
        else:
            return JSONResponse({'error_message': 'Line out of range'})


@app.post("/replace_record/")
async def replace_record(line: int = 0, record: str = ''):
    with open(get_file_path(), 'r') as file:
        records = file.read().split('\n')
        if 0 <= line < len(records) and records != ['']:
            records[line] = record
            with open(get_file_path(), 'w') as output:
                output.write("\n".join(records))
            return JSONResponse({line: record})
        else:
            return JSONResponse({'error_message': 'Line out of range'})


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080, reload=True)
