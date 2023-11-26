## Description

Demonstrate `mediapipe.Image` issue.

For some images ([link](images/7b25e4ba-1c18-45b3-b5ff-4065a144bf65.jpg), [link](images/66d001c4-bf9d-4883-be03-0fa230669838.jpg), [link](images/a3b2c6af-9995-4d60-b3ab-e4e32345797f.jpg), [link](images/fa920889-37db-4915-abde-7287f6de1ad6.jpg)):
* create Image from `ndarray`: crash
* create Image using `Image.create_from_file`: weird results with high scores

For some images ([link](images/000000006.png), [link](images/000000007.png), [link](images/000000008.png), [link](images/000000009.png)):
* create Image from `ndarray`: no detections
* create Image using `Image.create_from_file`: no problem

JavaScript package works fine for the same images and model.

## Environment

* Windows 10
* Python 3.11.6

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch:

```bash
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).