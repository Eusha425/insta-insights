<p align="center">
  <img src="assets/insta_insights_gradient.svg" alt="Insta Insights" />
</p>

Keeping a track of instagram followers and following can be tricky, ***insta insights*** is an open source comprehensive tool for analysing your Instagram follower relationships. Discover who follows you back, who doesn't, and track changes over time with detailed visualisations and reports locally with no sign in required. 

<p align="">
  <!-- Tech stack -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/CLI-Argparse-4B8BBE?style=for-the-badge&logo=gnubash&logoColor=white" />
  <img src="https://img.shields.io/badge/Instagram%20Data-833AB4?style=for-the-badge&logo=instagram&logoColor=white" />

  <!-- Project meta -->
  <img src="https://img.shields.io/github/v/release/Eusha425/insta-insights?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/Eusha425/insta-insights?style=for-the-badge" />
  <!-- <img src="https://img.shields.io/github/stars/Eusha425/insta-insights?style=for-the-badge" /> -->
  <!-- <img src="https://img.shields.io/github/issues/Eusha425/insta-insights?style=for-the-badge" /> -->
</p>

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Getting Your Instagram Data](#getting-your-instagram-data)
- [Usage Guide](#usage-guide)
- [Understanding Your Results](#understanding-your-results)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)
- [Live Demo](#live-demo)

## Features

### Core Analysis
- **Non-Followers**: See who you follow but doesn't follow you back
- **Unrequited Followers**: Find followers you haven't followed back
- **Mutual Followers**: Identify your mutual connections
- **Visual Summaries**: Pie charts showing your follower breakdown

### Advanced Features
- **Snapshot System**: Save and compare follower data over time
- **Change Tracking**: Monitor follower gains/losses between snapshots
- **Multiple Export Formats**: Export data as CSV or TXT files
- **Dual Interface**: Both GUI (Streamlit) and CLI versions available

### Privacy-First Design
- **100% Local Processing**: All analysis happens on your device
- **No Data Upload**: Your Instagram data never leaves your computer
- **Secure**: No login required, works with Instagram's official data export

## Quick Start

### Prerequisites
- Python 3.11 or higher
- Your Instagram data export (see [Getting Your Data](#-getting-your-instagram-data) below)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Eusha425/insta-insights.git
   cd insta-insights
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit matplotlib pandas
   ```

3. **Run the application**
   
   **GUI Version (Recommended for beginners):**
   ```bash
   streamlit run app.py
   ```
   
   **CLI Version (For advanced users):**
   ```bash
   python cli.py --followers followers_1.json --following following.json
   ```

## Getting Your Instagram Data

To use this application, you need to download your Instagram data first:

1. **Access Instagram Settings**
   - Open Instagram app or go to instagram.com
   - Go to Settings → Privacy and Security → Data Download

2. **Request Your Data**
   - Click "Request Download"
   - Select "JSON" format (important!)
   - Choose date range (recommend "All time" for complete analysis)
   - Enter your email and click "Next"

3. **Download and Extract**
   - Instagram will email you a download link (usually within 48 hours)
   - Download the ZIP file and extract it
   - Look for these files:
     - `followers_1.json` (or `followers.json`)
     - `following.json`

**Official Instagram Guide**: [How to download your information](https://help.instagram.com/181231772500920)

## Usage Guide

### Web Interface (Streamlit)

1. **Launch the app**
   ```bash
   streamlit run app.py
   ```

2. **Upload your files**
   - Upload your `followers_1.json` file
   - Upload your `following.json` file
   - Click "Analyse data"

3. **View results**
   - Browse through the different categories
   - Check the visual summary
   - Export your data if needed

4. **Advanced features**
   - Save snapshots for future comparison
   - Compare with previous snapshots to track changes
   - View detailed metrics and insights

**Note:**
Snapshots are saved in the `snapshots/` folder with timestamps (e.g. `snapshot_2025-07-29_12-30.json`) for easy identification. Snapshot comparison is shown directly in the Streamlit app when you select a previous snapshot from the dropdown.

### Command Line Interface

**Basic analysis:**
```bash
python cli.py --followers followers_1.json --following following.json
```

**With visualisation:**
```bash
python cli.py --followers followers_1.json --following following.json --visualise
```

**Export to CSV:**
```bash
python cli.py --followers followers_1.json --following following.json --export csv
```

**Summary only:**
```bash
python cli.py --followers followers_1.json --following following.json --summarise
```

**All CLI options:**
```bash
python cli.py --help
```

## Understanding Your Results

### Categories Explained

- **Not Following You Back (One-sided)**
  People you follow who don't follow you back. Consider unfollowing if you want a more balanced ratio.

- **You're Not Following Back (Unreciprocated)**
  Your followers that you haven't followed back. Great for discovering potential connections.

- **Mutual Followers (Following Each Other)**
  People who follow you and you follow back. Your core Instagram community.

### Snapshot Comparison Features

- **New Followers**: People who started following you
- **Lost Followers**: People who unfollowed you
- **Mutuals Gained**: New mutual connections
- **Mutuals Lost**: Lost mutual connections
- **Net Change**: Overall follower growth/decline

## Project Structure

```
instagram-follower-insights/
├── app.py                  # Streamlit web interface
├── cli.py                  # Command-line interface
├── analyser.py             # Core analysis logic
├── data_loader.py          # JSON file processing
├── visualiser.py           # Chart generation
├── exporter.py             # Data export functionality
├── snapshot_manager.py     # Snapshot system
├── legacy_main.py          # Original simple version
└── README.md               
```

## Technical Details

### File Format Requirements
- Files must be in JSON format (Instagram's standard export format)
- `followers_1.json`: Contains your follower list
- `following.json`: Contains accounts you follow

### Dependencies
- **streamlit**: Web interface framework
- **matplotlib**: Visualisation library
- **json**: JSON file processing (built-in)
- **csv**: CSV export functionality (built-in)
- **argparse**: CLI argument parsing (built-in)

### Data Processing
1. JSON files are parsed to extract usernames
2. Set operations identify relationships between lists
3. Results are categorized and presented
4. Optional snapshot storage for temporal analysis

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/Eusha425/insta-insights.git

# Install development dependencies
pip install streamlit matplotlib pandas
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

- This tool is for personal use only
- Respect Instagram's Terms of Service
- Your data privacy is maintained - no data is sent to external servers
- Use responsibly and don't spam or harass other users

## Troubleshooting

### Common Issues

**"Invalid JSON file format" error:**
- Ensure you downloaded the correct files from Instagram
- Make sure files are in JSON format, not HTML

**"Files could not be properly analysed" error:**
- Verify both files are uploaded/specified
- Check file permissions and paths
- Ensure files aren't corrupted
- Check that files exist in the same directory when running the CLI version or navigate to the correct directory

**Missing visualisations:**
- Install matplotlib: `pip install matplotlib`
- For CLI: add `--visualise` flag

### Getting Help

1. Check the [Issues](https://github.com/Eusha425/insta-insights/issues) page
2. Create a new issue with:
   - Error message (if any)
   - Steps to reproduce
   - Your operating system
   - Python version

## Roadmap

- [ ] Web Dashboard deployment option
- [ ] Advanced Analytics (engagement rates, growth trends)
- [ ] Multi-account Support
- [ ] Batch Processing for multiple data exports
- [ ] Enhanced Visualisations (timeline charts, growth graphs)

## Acknowledgements

- Instagram for providing data export functionality
- Streamlit team for the excellent web framework
- Python community for amazing libraries

## Live Demo
Check out the live demo [here](https://insta-insights.streamlit.app/)
