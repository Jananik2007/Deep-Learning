# Interactive LLM-Based Chatbot

An interactive conversational application developed using a pre-trained Transformer-based Large Language Model (LLM), Qwen2.5-0.5B-Instruct. The application uses Hugging Face Transformers for text generation and Gradio for providing a web-based conversational interface.

## 1. Project Overview

Large Language Models enable computers to understand and generate human-like text based on user prompts. This project demonstrates the integration of a pre-trained instruction-tuned language model into an interactive chatbot application.

The chatbot accepts user queries, processes them using the language model, and generates contextually relevant responses. It also incorporates conversation history and adjustable generation parameters to improve user interaction.

## 2. Objectives

- To understand response generation using pre-trained Transformer-based language models.
- To integrate an instruction-tuned LLM using the Hugging Face Transformers library.
- To develop an interactive chatbot interface using Gradio.
- To implement conversation history for contextual response generation.
- To study the influence of temperature on text generation.
- To deploy the chatbot application using Hugging Face Spaces.

## 3. Technologies and Tools

| Technology | Application |
|---|---|
| Python | Application development |
| PyTorch | Deep learning model execution |
| Hugging Face Transformers | Model loading and text generation |
| Qwen2.5-0.5B-Instruct | Pre-trained language model |
| Gradio | User interface development |
| Hugging Face Spaces | Cloud deployment |
| GitHub | Source code management |

## 4. System Architecture

The application follows a prompt-processing and response-generation workflow.

```text
       User Input
           |
           v
   Gradio Chat Interface
           |
           v
   Conversation History
           |
           v
    Prompt Preparation
           |
           v
   Qwen2.5-0.5B-Instruct
           |
           v
    Token Generation
           |
           v
   Response Decoding
           |
           v
   Display Response
```

## 5. Model Configuration

**Model:** Qwen/Qwen2.5-0.5B-Instruct

The application uses an instruction-tuned Transformer-based language model. The model processes the input prompt along with relevant conversation history and generates a response through autoregressive token prediction.

The following parameters are used during response generation:

- **Temperature:** Controls the randomness of token selection.
- **Top-p:** Controls token sampling based on cumulative probability.
- **Maximum New Tokens:** Specifies the maximum number of tokens generated in a response.

## 6. Application Features

- Interactive conversational interface.
- Context-aware responses using conversation history.
- Adjustable temperature for controlling response variability.
- Configurable maximum response length.
- Pre-trained LLM integration without training a model from scratch.
- Cloud-based application accessibility.

## 7. Deployment

The application is deployed using Hugging Face Spaces with Gradio as the application SDK.

**Deployment URL:** https://huggingface.co/spaces/jananikamaraj/llm_chatbot

## 8. Results and Observations

The chatbot was successfully developed and integrated with the Qwen2.5-0.5B-Instruct model. It accepts user prompts and generates responses through the Gradio interface.

Conversation history enables the chatbot to maintain context across multiple interactions. Different temperature values produce variations in response generation, demonstrating the effect of sampling parameters on LLM outputs.

The application was deployed using Hugging Face Spaces, demonstrating the integration of a pre-trained language model with a cloud-hosted web interface.

## 9. Limitations

1. **Hallucination:** The model may generate inaccurate or misleading information while presenting it confidently.
2. **Context Limitations:** Only a limited number of previous conversation turns are retained.
3. **Computational Requirements:** Model inference requires sufficient memory and processing resources.
4. **Knowledge Limitations:** The model may not provide reliable information about recent or future events.
5. **Response Variability:** Higher temperature settings may produce less predictable responses.
6. **Deployment Constraints:** Cloud execution is subject to hardware availability and platform usage limits.
