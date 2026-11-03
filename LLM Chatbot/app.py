import gradio as gr
from chatbot import chat

ROLL_NOS = "24BAD039"


def to_pairs(history):

    pairs = []
    pending_user = None

    for item in history or []:

        if isinstance(item, dict):

            role = item.get("role")
            content = item.get("content", "")

            if isinstance(content, list):
                content = " ".join(
                    str(x.get("text", "")) if isinstance(x, dict)
                    else str(x)
                    for x in content
                )

            if role == "user":
                pending_user = str(content)

            elif role == "assistant" and pending_user is not None:
                pairs.append((pending_user, str(content)))
                pending_user = None

        else:
            pairs.append((str(item[0]), str(item[1])))

    return pairs


def respond(message, history, temperature, max_tokens):

    pairs = to_pairs(history)

    return chat(
        message,
        pairs,
        temperature,
        max_tokens
    )


demo = gr.ChatInterface(
    fn=respond,

    title="LLM Chatbot (Qwen2.5-0.5B-Instruct)",

    description=(
        "Transformer-based chatbot using Hugging Face "
        f"Transformers and Gradio. Roll Nos: {ROLL_NOS}"
    ),

    additional_inputs=[
        gr.Slider(
            0.1, 1.5,
            value=0.7,
            step=0.1,
            label="Temperature"
        ),

        gr.Slider(
            32, 512,
            value=200,
            step=16,
            label="Maximum New Tokens"
        )
    ],

    examples=[
        ["Explain Transformers in simple words.", 0.7, 200],
        ["What is Artificial Intelligence?", 0.5, 150]
    ]
)


if __name__ == "__main__":
    demo.launch()