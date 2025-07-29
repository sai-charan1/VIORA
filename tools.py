import cv2
import base64
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

def capture_image() -> str:

    """
    captures image from webcam and resizes the image 
    encodes it into a BASE64 raw string 
    """
    for idx in range(4):
        cap = cv2.VideoCapture(idx,cv2.CAP_DSHOW )
        if cap.isOpened():
            for _ in range(10):
                cap.read()
            ret , frame = cap.read()
            cap.release()
            if not ret:
                continue
            cv2.imwrite("sample.jpg",frame)
            ret, buf = cv2.imencode('.jpeg',frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')
    raise RuntimeError("Could not open web Cam (tried indices 0-3)")



def analyze_image_with_query(query: str) -> str:
    """"
    expeccts a string with the query
    captures the image and send image with query to the groq vision chat api and returns the analysis
    """
    img_64 = capture_image()
    model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    if not query or not img_64:
        return "Error: Both Image and Query feilds required"
    
    client = Groq()
    messages = [{
        "role" : "user",
        "content" : [
            {
                "type" : "text",
                "text" : query
            },
            {
                "type" : "image_url",
                "image_url" : {
                    "url" : f"data:image/jpeg;base64,{img_64}",
                },
            },
        ],
    }]

    chat_complition = client.chat.completions.create(
        messages = messages,
        model = model
    )

    return chat_complition.choices[0].message.content


## query = "how many people do you see ?"
## print(analyze_image_with_query(query))