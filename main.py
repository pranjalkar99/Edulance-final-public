"""Usage instructions"""
from pprint import pprint
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile
from fastapi import FastAPI, File
from langchain_core.documents import Document
from graphs.main_graph import lesson_graph
from init import initialize_env
from agents.quiz_agent import quiz_runnable
from agents.ocr_agent import ocr_runnable
from agents.pdf_agent import pdf_runnable
from langchain_community.document_loaders import UnstructuredPDFLoader
from pathlib import Path


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
initialize_env()

content = '' 
ocr_sensible = ''

@app.post("/upload-txt")
async def upload_txt(file: UploadFile = File(...)):
    global content
    content = await file.read()
    return {
        "output" : str(content)
    }

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    ocr = await file.read()
    global ocr_sensible
    global content
    global final_txt
    ocr_sensible = ocr_runnable.invoke(
        {"document" : ocr}
    )

    final_txt = str(content)+str(ocr_sensible)
    return {
        "output": str(final_txt)
    }


@app.post("/generate-lesson")
async def generate_lesson(user_proficiency: str):
    state_input = {
        "document": Document(page_content=final_txt),
        "user_proficiency": user_proficiency
    }
    output = lesson_graph.invoke(state_input)
    response = {
        "lesson_planner_obj": output.get('lesson_planner_obj'),
        "lesson_generator_obj": output.get('lesson_generator_obj')
    }
    return response

@app.post("/generate-quiz")
async def generate_quiz(user_proficiency: str):
    state_input = {
        "document": Document(page_content=final_txt),
        "user_proficiency": user_proficiency
    }
    output = quiz_runnable.invoke(state_input)
    return output

@app.post("/pdf")
async def pdf_gen(user_proficiency: str, file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    file_path = Path("temp_pdf")
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    # Load the PDF file using UnstructuredPDFLoader
    loader = UnstructuredPDFLoader(file_path=file_path,
                                    mode="single",
                                    strategy = 'hi_res',
                                    infer_table_structure = True,
                                    hi_res_model_name = 'yolox',
                                    chunking_strategy = 'by_title',
                                    max_characters = 4000)
    docs = loader.load()
    file_path.unlink()
    # Make sense of the document
    output_from_pdf_agent = pdf_runnable.invoke(
        {
            "pdf_document": docs[0].page_content
        }
    )
    state_input = {
        "document": Document(page_content=output_from_pdf_agent),
        "user_proficiency": user_proficiency
    }
    output_from_lesson_generator = lesson_graph.invoke(state_input)
    output_from_quiz_generator = quiz_runnable.invoke(state_input)
    response = {
        "lesson_planner_obj": output_from_lesson_generator.get('lesson_planner_obj'),
        "lesson_generator_obj": output_from_lesson_generator.get('lesson_generator_obj'),
        "quiz": output_from_quiz_generator
    }
    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7002)
