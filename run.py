import gradio as gr

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

future_pred = gr.Interface(
    fn=greet,
    inputs=None,
    outputs="text",
    title="Title of the Gradio Interface",
    description="This is a simple Gradio Interface that returns a greeting.",
    article="<p style='text-align: center'>Welcome to this Gradio Interface!</p>"
)

data_analysis = gr.Interface(
    fn=greet,
    inputs=None,
    outputs="text",
    title="Title of the Gradio Interface",
    description="This is a simple Gradio Interface that returns a greeting.",
    article="<p style='text-align: center'>Welcome to this Gradio Interface!</p>"
)

details_page = gr.HTML(details_html_content)

about_us = gr.HTML(aboutus_html_content)

demo = gr.TabbedInterface([readme, data_analysis, future_pred, details_page, about_us], ["Introduction", "Data Analysis", "Future Prediction", "Details", "About Us"])

if __name__ == "__main__":
    demo.launch()
