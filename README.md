![Edulance](https://github.com/bhaswata08/Edulance/assets/106006087/33db5a20-3ebd-46c6-b5d5-b48f860798d3)
<p align="center">
    <h1 align="center">EDULANCE</h1>
</p>
<p align="center">
    <em>OCR & AI Learn Together or Transform Docs into Interactive Learning" could be engaging slogans for the Edulance project while encapsulating its purpose (applying optical character recognition and AI to documents) and value proposition (generating lessons and quizzes based on the content).</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/bhaswata08/Edulance?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/bhaswata08/Edulance?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/bhaswata08/Edulance?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/bhaswata08/Edulance?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

Edulance is an open-source project that utilizes advanced technologies such as OCR, machine learning models, and APIs to transform text documents and PDFs into interactive educational resources. The software accepts user-uploaded files, applies optical character recognition (OCR) for text documents, or extracts valuable content from PDFs. It then generates lessons, quizzes, and lesson plans based on the content using its Lesson Graph model and agents like LessonGenerator, LessonPlanner, OCRAgent, PdfAgent, QuizAgent, and TogetherLLM. Edulance provides an immersive learning experience, enabling effective teaching and interactive knowledge acquisition.

---


##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | Edulance is a Python-based project using FastAPI as the web framework and Uvicorn for runtime serving. The application leverages containers with Docker for deployment, installing required dependencies from `requirements.txt`. It utilizes libraries like LangChain, PikePDF, PyTesseract for OCR, and TogetherAI's LLM models. |
| 🔩 | **Code Quality**  | The codebase follows a modular structure with clearly defined agents and graph files, ensuring high cohesion and low coupling. Python style guides are followed consistently, including PEP8 and PEP534. There is adequate usage of comments throughout the codebase. |
| 📄 | **Documentation** | Comprehensive documentation exists for each file and agent. The `README.md` provides a high-level overview and installation instructions, while inline documentation in files clarifies complex functionality. |
| 🔌 | **Integrations**  | Key integrations include Docker for deployment, LangChain libraries, TogetherAI's LLM models. |
| 🧩 | **Modularity**    | The Edulance project is designed as a modular system, with distinct agents (lesson_generator, lesson_planner, quiz_agent, etc.) responsible for specific tasks in the document processing and generation pipeline. This leads to enhanced code reusability and maintainability.|
| 📦 | **Dependencies**  | Main dependencies include FastAPI, Docker, Python 3.10, requirements.txt, LangChain package, PikePDF, PyTesseract, and related tools.|

---

##  Repository Structure

```sh
└── Edulance/
    ├── Dockerfile
    ├── README.md
    ├── agents
    │   ├── lesson_generator.py
    │   ├── lesson_planner.py
    │   ├── ocr_agent.py
    │   ├── pdf_agent.py
    │   └── quiz_agent.py
    ├── graphs
    │   └── main_graph.py
    ├── init.py
    ├── main.py
    ├── ocr.txt
    ├── requirements.txt
    ├── togetherchain.py
    └── transcript.txt
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                    | Summary                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                     | ---                                                                                                                                                                                                                                                                                                                          |
| [Dockerfile](https://github.com/bhaswata08/Edulance/blob/master/Dockerfile)             | Sets base Python runtime, installs dependencies from requirements.txt, and copies application code into container for execution, exposing port 7002.                                                                                                                                                                         |
| [init.py](https://github.com/bhaswata08/Edulance/blob/master/init.py)                   | Sets environment variables for application accessing Together API using OS environment. In Edulance project architecture, this initialization function, located in init.py, enables secure interaction between the app and Togethers platform.                                                                               |
| [main.py](https://github.com/bhaswata08/Edulance/blob/master/main.py)                   | This FastAPI application accepts user-uploaded text documents, applies optical character recognition (OCR) to them, and then generates lessons and quizzes based on the content using the Lesson Graph model and Quiz Agent. Additionally, it supports generating a lesson plan and a quiz from PDF files.                   |
| [ocr.txt](https://github.com/bhaswata08/Edulance/blob/master/ocr.txt)                   | An example OCR File                                                                                |
| [requirements.txt](https://github.com/bhaswata08/Edulance/blob/master/requirements.txt) | In this repository, the requirements.txt file specifies essential libraries for Edulance project's functioning. Notably, it includes LangChain and related packages, FastAPI and Uvicorn web frameworks, OCR tools like PikePDF and PyTesseract.                                           |
| [togetherchain.py](https://github.com/bhaswata08/Edulance/blob/master/togetherchain.py) | Creates a custom Language Model (LLM) named `TogetherLLM` that integrates with the Together chat API using its client. This LLM allows the application to generate responses based on given prompts, utilizing temperature and max tokens settings.                                                                          |
| [transcript.txt](https://github.com/bhaswata08/Edulance/blob/master/transcript.txt)     | Example transcript file |

</details>

<details closed><summary>agents</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                |
| [lesson_generator.py](https://github.com/bhaswata08/Edulance/blob/master/agents/lesson_generator.py) | Generate a detailed and engaging lesson based on document contents as an expert teacher. Understand documents deeply and explain each concept in detail without creating quizzes or generating lesson plans. User proficiency and expected topics provided. Interacting with language model using ChatGroq to generate the lesson. |
| [lesson_planner.py](https://github.com/bhaswata08/Edulance/blob/master/agents/lesson_planner.py)     | Our Lesson Planner Agent processes documents, identifying topics and objectives for effective teaching. Using LLM, it constructs lesson structures adhering to specified formats. Key components include document understanding, main topic identification, and structured lesson generation.                                      |
| [ocr_agent.py](https://github.com/bhaswata08/Edulance/blob/master/agents/ocr_agent.py)               | Transform documents into educational lessons with precision using the OCR agent, residing in `ocr_agent.py`. This script integrates Together LLM Models to parse OCR text, understand concepts in detail, and generate captivating lessons for optimal learning experiences.                                    |
| [pdf_agent.py](https://github.com/bhaswata08/Edulance/blob/master/agents/pdf_agent.py)               | The `pdf_agent.py` script acts as an intelligent agent within the Edulance repository, utilizing TogetherAI and Langchain technologies to extract valuable lessons and summaries from provided PDF documents.                                                                                                                          |
| [quiz_agent.py](https://github.com/bhaswata08/Edulance/blob/master/agents/quiz_agent.py)             | Generate quiz questions and answers based on document analysis, tailored for user proficiency. Utilize an LLM model to create varied, engaging, and assessing quizzes without deviating from specified format. (agents/quiz_agent.py)                                                                                              |

</details>

<details closed><summary>graphs</summary>

| File                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                |
| [main_graph.py](https://github.com/bhaswata08/Edulance/blob/master/graphs/main_graph.py) | This file defines and sets up a state graph using the provided `AgentState` and two main nodes-lesson_planner and lesson_generator. The lesson_planner node processes document input along with user proficiency to generate LessonStructure, which is passed to the lesson_generator for generating custom lessons. The compiled graph serves as a blueprint for this functionality in the Edulance architecture. |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the Edulance repository:
>
> ```console
> $ git clone https://github.com/bhaswata08/Edulance
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd Edulance
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run Edulance using the command below:
> ```console
> $ python main.py
> ```


---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/bhaswata08/Edulance/issues)**: Submit bugs found or log feature requests for the `Edulance` project.
- **[Submit Pull Requests](https://github.com/bhaswata08/Edulance/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/bhaswata08/Edulance/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/bhaswata08/Edulance
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/bhaswata08/Edulance/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=bhaswata08/Edulance">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
