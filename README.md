# 🤖 Smart Text Analyzer

A sophisticated text analysis application built with Gradio and TextBlob, providing real-time sentiment analysis, text summarization, and comprehensive text insights through an intuitive web interface.

## 🚀 Live Demo
[Try it live on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/smart-text-analyzer)

## 🏗️ Architecture

This project implements a clean separation between the core analysis logic and the web interface:

- **Frontend**: Gradio-based web interface with real-time processing
- **Backend**: TextBlob NLP engine for sentiment analysis and text processing
- **Deployment**: Automated sync to Hugging Face Spaces via GitHub Actions

## ✨ Features

- **Sentiment Analysis**: Polarity (-1 to 1) and subjectivity (0 to 1) scoring
- **Text Summarization**: Intelligent extraction of key sentences
- **Text Insights**: Word count, character count, readability metrics
- **Real-time Processing**: Instant analysis as you type
- **Example Dataset**: Pre-loaded examples for testing

## 🛠️ Technology Stack

- **Python 3.13+**: Core runtime
- **Gradio 5.44+**: Web interface framework
- **TextBlob 0.19+**: Natural language processing
- **NLTK**: Tokenization and corpus data
- **GitHub Actions**: CI/CD pipeline
- **Hugging Face Spaces**: Deployment platform

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/smart-text-analyzer.git
cd smart-text-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK data**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('brown')"
```

5. **Run the application**
```bash
python app.py
```

The application will be available at `http://localhost:7860`

## 🔧 Configuration

### Environment Variables
- No environment variables required for basic operation
- Optional: Configure custom port via Gradio's `launch()` parameters

### Customization
- Modify `analyze_text()` function in `app.py` for custom analysis logic
- Update Gradio interface components for UI changes
- Extend with additional NLP libraries as needed

## 🚀 Deployment

### Hugging Face Spaces
This project includes automated deployment to Hugging Face Spaces:

1. **Set up HF Token**: Add `HF_TOKEN` to your GitHub repository secrets
2. **Create HF Space**: Create a new space on Hugging Face with the same name
3. **Push to main**: Any push to main branch triggers automatic deployment

The `hf_space/` directory contains the Hugging Face-specific configuration.

### Manual Deployment
```bash
# Deploy to Hugging Face Spaces manually
huggingface-cli login
huggingface-cli repo create --type=space --space_sdk=gradio smart-text-analyzer
git clone https://huggingface.co/spaces/YOUR_USERNAME/smart-text-analyzer
cp -r hf_space/* smart-text-analyzer/
cd smart-text-analyzer && git add . && git commit -m "Initial deployment" && git push
```

## 📁 Project Structure

```
smart-text-analyzer/
├── .github/workflows/
│   └── sync-to-hf.yml          # Auto-sync to HF Spaces
├── hf_space/
│   ├── README.md              # HF Space configuration
│   ├── app.py                 # Symlink to main app
│   └── requirements.txt       # Dependencies for HF
├── venv/                      # Virtual environment
├── app.py                     # Main Gradio application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .gitignore                # Git ignore rules
```

## 🧪 Testing

### Manual Testing
1. Run the application locally
2. Test with provided examples
3. Verify sentiment scores are within expected ranges
4. Check text insights accuracy

### Automated Testing
```bash
# Run basic import tests
python -c "from app import analyze_text; print('✅ Imports successful')"

# Test core functionality
python -c "from app import analyze_text; result = analyze_text('I love this!'); print('✅ Analysis working:', len(result) == 3)"
```

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to new functions
- Update requirements.txt for new dependencies
- Test locally before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TextBlob**: For providing excellent NLP capabilities
- **Gradio**: For the intuitive web interface framework
- **Hugging Face**: For the amazing deployment platform
- **NLTK**: For natural language processing tools
