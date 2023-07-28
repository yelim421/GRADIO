import gradio as gr
from warningms import warning_message
import pathlib

def greet():
    print("Hello, Gradio")
    return ""


# HTML 코드가 저장된 파일 읽기
with open('readme.html', 'r', encoding='utf-8') as file:
    readme_html_content = file.read()

with open('aboutus.html', 'r', encoding='utf-8') as file:
    aboutus_html_content = file.read()

with open('details.html', 'r', encoding='utf-8') as file:
    details_html_content = file.read()


# Gradio HTML 인터페이스 만들기
readme = gr.HTML(readme_html_content)
details_page = gr.HTML(details_html_content)
about_us = gr.HTML(aboutus_html_content)

future_pred = gr.Interface(
    warning_message,
    [   gr.Radio(
            ["Kong-rey"], label = "Typhoon", info = "Which typhoon?"
        ),
        gr.Radio(
            ["Seoul", "Gangwon Province (Gangneung)", "Gyeongsang Province (Yeongdeok)", "Busan", "Southern Region (Namhae)", "Jeolla Province (Gwangju)", "Jeju Island"], label = "Location", info = "Where are you?"
        ),
        gr.Dropdown(
            ["October 5th, 2018", "October 6th, 2018", "October 7th, 2018"], label = "Dates", info = "Today's date"
        ),
        gr.Radio(
            ["00:00", "06:00", "12:00", "18:00"], label = "Time", info = "What's the time?"
        )
    ],
    #["text", "image"]
    [gr.Textbox(label = "Warning Message"), gr.Image(label = "picture")]

)


data_analysis = gr.Interface(
    lambda name: f"Greetings {name}!",
    inputs=None,
    outputs=gr.PlayableVideo(value="ezgif-4-101dbb433e.mp4")
)


demo = gr.TabbedInterface([readme, data_analysis, future_pred, details_page, about_us], ["Introduction", "Data Analysis", "Future Prediction", "Details", "About Us"])

if __name__ == "__main__":
    demo.launch(share=True)
