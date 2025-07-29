import os
import cv2
import gradio as gr
import threading
from speech_to_text import record_audio, transcribe_with_groq
from ai_agent import ask_agent
from text_to_speech import text_to_speech_with_elevenlabs

# Constants
audio_filepath = "audio_question.mp3"

# --- Chat Processing ---
def process_single_turn(chat_history):
    # Record audio
    record_audio(file_path=audio_filepath)
    user_input = transcribe_with_groq(audio_filepath)

    # Handle no input
    if not user_input:
        return chat_history, "📢 Didn't catch that. Please try again."

    # Exit on goodbye
    if "goodbye" in user_input.lower():
        return chat_history, "👋 Goodbye!"

    # Generate response
    response = ask_agent(user_query=user_input)

    # Save TTS output without playing
    if os.path.exists("final.mp3"):
        os.remove("final.mp3")
    text_to_speech_with_elevenlabs(input_text=response, output_filepath="final.mp3")

    # Update chat history
    new_history = chat_history + [
        {"role": "user", "content": f"🧑‍💬 {user_input}"},
        {"role": "assistant", "content": f"🤖 {response}"}
    ]
    return new_history, ""

# --- Webcam in Background Thread ---
camera = None
last_frame = None
stop_event = None
video_thread = None

def initialize_camera():
    global camera, last_frame, stop_event, video_thread
    if camera is None:
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            camera.set(cv2.CAP_PROP_FPS, 30)
            stop_event = threading.Event()
            def video_loop():
                global last_frame
                while not stop_event.is_set():
                    ret, frame = camera.read()
                    if ret:
                        last_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_thread = threading.Thread(target=video_loop, daemon=True)
            video_thread.start()
    return camera is not None and camera.isOpened()

def start_webcam():
    if not initialize_camera():
        return None
    return last_frame

def stop_webcam():
    global camera, stop_event, video_thread, last_frame
    if stop_event:
        stop_event.set()
    if video_thread:
        video_thread.join(timeout=1)
    if camera is not None:
        camera.release()
        camera = None
    last_frame = None
    return None

def get_webcam_frame():
    return last_frame

# --- Gradio UI ---
with gr.Blocks(css=".webcam { border: 2px solid #ccc; border-radius: 8px; }") as demo:
    gr.Markdown("<h1 style='color: orange; text-align: center; font-size: 3em;'>🤖 VIORA – Your AI Companion</h1>")
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📷 Webcam Feed")
            with gr.Row():
                start_cam = gr.Button("Start Camera")
                stop_cam = gr.Button("Stop Camera")
            webcam_output = gr.Image(label="Webcam", streaming=True, show_label=True, elem_classes="webcam", width=640, height=480)
            webcam_timer = gr.Timer(0.033)
        with gr.Column(scale=1):
            gr.Markdown("### 💬 Chat Interface")
            chatbot = gr.Chatbot(type="messages", label="Conversation", height=400)
            record_btn = gr.Button("🎤 Record & Ask")
            status = gr.Textbox(label="Status", interactive=False)
            clear_btn = gr.Button("Clear Chat")
    # Event bindings
    start_cam.click(fn=start_webcam, outputs=webcam_output)
    stop_cam.click(fn=stop_webcam, outputs=webcam_output)
    webcam_timer.tick(fn=get_webcam_frame, outputs=webcam_output, show_progress=False)
    record_btn.click(fn=process_single_turn, inputs=[chatbot], outputs=[chatbot, status])
    clear_btn.click(lambda: ([], ""), outputs=[chatbot, status])

# Launch
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False, debug=True)
