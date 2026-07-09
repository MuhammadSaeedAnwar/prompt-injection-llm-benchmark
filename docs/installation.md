# Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip or conda
- Git

## Quick Start

```bash
# Clone repository
git clone https://github.com/MuhammadSaeedAnwar/Prompt-Injection-LLM-Benchmark.git
cd Prompt-Injection-LLM-Benchmark

# Install dependencies
pip install -r requirements.txt

# Or with conda
conda env create -f environment.yml
conda activate prompt-injection-benchmark

# Verify installation
python -c "from src.data import DatasetLoader; print('✓ Installation successful!')"
```

## Development Setup

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Format code
black src/ tests/
isort src/ tests/

# Lint
flake8 src/ tests/
```

## Environment Configuration

1. Copy `.env.example` to `.env`
2. Add your API keys:
   ```bash
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   GOOGLE_API_KEY=...
   ```

## Troubleshooting

### Import Errors
```bash
# Reinstall package
pip install -e . --force-reinstall
```

### Missing Dependencies
```bash
# Update pip and reinstall
pip install --upgrade pip
pip install -r requirements.txt
```

### API Key Issues
- Verify `.env` file exists and is in project root
- Check API key format and validity
- Ensure `python-dotenv` is installed

## Next Steps

- Read [Usage Guide](usage.md)
- Explore [Examples](examples/)
- Check [Reproducibility Guide](docs/reproducibility_guide.md)
