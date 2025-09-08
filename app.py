import gradio as gr
from textblob import TextBlob
import requests

def analyze_text(text):
    if not text.strip():
        return "Please enter some text to analyze.", "", ""
    
    # Basic sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    # Simple summary (first 3 sentences)
    sentences = text.split('.')[:3]
    summary = '. '.join(sentences) + '.' if sentences else text
    
    # Key insights
    word_count = len(text.split())
    char_count = len(text)
    polarity_label = "Positive" if sentiment.polarity > 0.1 else "Negative" if sentiment.polarity < -0.1 else "Neutral"
    
    sentiment_result = f"""
    **Sentiment Analysis:**
    - Polarity: {sentiment.polarity:.2f} ({polarity_label})
    - Subjectivity: {sentiment.subjectivity:.2f}
    """
    
    insights = f"""
    **Text Insights:**
    - Word Count: {word_count}
    - Character Count: {char_count}
    - Average Word Length: {char_count/word_count:.1f} chars
    - Readability: {'Easy' if word_count/len(sentences) < 15 else 'Complex'}
    """
    
    return sentiment_result, summary, insights

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter your text here for AI analysis..."),
    outputs=[
        gr.Markdown(label="Sentiment Analysis"),
        gr.Textbox(label="Summary"),
        gr.Markdown(label="Text Insights")
    ],
    title="🤖 Smart Text Analyzer",
    description="Analyze any text with AI-powered sentiment analysis, summarization, and insights!",
    examples=[
        ["I love this new technology! It's absolutely amazing and revolutionary."],
        ["The weather today is quite disappointing. It's been raining all day."],
        ["Machine learning is transforming industries across the globe with unprecedented innovation."]
    ]
)

if __name__ == "__main__":
    iface.launch()