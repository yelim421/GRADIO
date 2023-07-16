import gradio as gr

tts_examples = [
    "I love learning machine learning",
    "How do you do?",
]

def greet():
    print("Hello, Gradio")
    return ""

readme = gr.Interface(
    fn=greet,
    inputs=None,
    outputs="text",
    title="Title of the Gradio Interface",
    description="This is a simple Gradio Interface that returns a greeting.",
    article="<p style='text-align: center'>Welcome to this Gradio Interface!</p>"
)

stt_demo = gr.load(
    "huggingface/facebook/wav2vec2-base-960h",
    title=None,
    inputs="mic",
    description="Let me try to guess what you're saying!",
)

future_pred = gr.load(
    "huggingface/facebook/fastspeech2-en-ljspeech",
    title=None,
    examples=tts_examples,
    description="Give me something to say!",
)

info_page = gr.load(
    "huggingface/facebook/fastspeech2-en-ljspeech",
    title=None,
    examples=tts_examples,
    description="Give me something to say!",
)

about_us = gr.load(
    "huggingface/facebook/fastspeech2-en-ljspeech",
    title=None,
    examples=tts_examples,
    description="Give me something to say!",
)

demo = gr.TabbedInterface([readme, stt_demo, future_pred, info_page, about_us], ["ReadMe", "Data Analysis", "Future Prediction", "More Information", "About Us"])

if __name__ == "__main__":
    demo.launch()
