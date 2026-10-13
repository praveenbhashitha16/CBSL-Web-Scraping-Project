# Central Bank of Sri Lanka (CBSL) Web Scraping Project

## 📌 Project Overview

This is an academic group project focused on web scraping, data extraction, and visualization using information published on the official website of the Central Bank of Sri Lanka (CBSL).

The project focuses on three main areas: **CBSL News, Inflation, and Monetary Policy**. Using Python web scraping techniques, we collect relevant information, organize datasets, process PDF documents, and visualize inflation trends.

🌐 **Data Source:** [Central Bank of Sri Lanka](https://www.cbsl.gov.lk/)

## 🎯 Project Objectives

- 🔎 Extract relevant links and information from the CBSL website.
- 📰 Collect and organize CBSL news information.
- 📊 Collect and analyze available inflation data from 2020 to 2026.
- 🏦 Identify monetary policy-related information and PDF documents.
- 📄 Extract relevant content and images from PDF documents.
- 💾 Store extracted information in structured CSV files.
- 📈 Visualize CCPI and NCPI headline and core inflation trends.

## 📚 Project Areas

### 📰 1. CBSL News

- Identify and extract relevant news information from the CBSL website.
- Organize collected news information in a structured CSV dataset.
- Save the collected news data in `CSV_folder/cbsl_news.csv`.

### 📈 2. Inflation Data

- Collect and organize available inflation data for the years 2020, 2021, 2022, 2024, 2025, and 2026.
- Store yearly inflation datasets as CSV files.
- Combine available inflation datasets into `all-inflation.csv`.
- Explore the following inflation indicators:
  - Colombo Consumer Price Index (CCPI) Headline Inflation
  - Colombo Consumer Price Index (CCPI) Core Inflation
  - National Consumer Price Index (NCPI) Headline Inflation
  - National Consumer Price Index (NCPI) Core Inflation
- Create visualizations to explore inflation trends over time.

**Note:** Inflation data for 2023 is not included in the collected datasets.

### 🏦 3. Monetary Policy

- Identify relevant monetary policy information published by CBSL.
- Collect links to monetary policy-related PDF documents.
- Store relevant links in CSV files.
- Process the monetary policy PDF and extract selected images where required.

## 🛠️ Technologies and Libraries

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🐼 Pandas | Data manipulation and CSV processing |
| 🌐 Requests | Sending HTTP requests to retrieve web content |
| 🥣 Beautiful Soup | Parsing HTML and extracting information |
| 🕷️ Scrapy | Web scraping framework for collecting website links |
| 🔍 lxml | HTML and XML parsing |
| 🌐 html5lib | HTML parsing |
| 📄 PyPDF | Reading and extracting content from PDF documents |
| 🖼️ Pillow (PIL) | Image processing |
| 🔠 Tesseract OCR (`pytesseract`) | Extracting text from images using OCR |
| 📊 Matplotlib | Creating data visualizations |
| 🔎 Regular Expressions (Regex) | Searching and extracting text patterns |
| 🔗 `urllib.parse` | Joining and parsing URLs |
| 📓 Jupyter Notebook | Developing and running the project workflow |

## 📂 Repository Structure

```text
CBSL-Web-Scraping-Project/
│
├── CSV_folder/
│   ├── 2020-inflation.csv
│   ├── 2021-inflation.csv
│   ├── 2022-inflation.csv
│   ├── 2024-inflation.csv
│   ├── 2025-inflation.csv
│   ├── 2026-inflation.csv
│   └── cbsl_news.csv
│
├── cbsl_scraper/
│   ├── cbsl_scraper/
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   └── cbsl_links.py
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   └── settings.py
│   └── scrapy.cfg
│
├── extracted_pdf_images/
│   ├── page_1_image_1.png
│   ├── page_5_image_1.png
│   ├── page_9_image_1.png
│   ├── page_9_image_2.png
│   ├── page_9_image_3.png
│   ├── page_9_image_4.png
│   ├── page_9_image_5.png
│   ├── page_9_image_6.png
│   ├── page_9_image_7.png
│   ├── page_9_image_8.png
│   ├── page_11_image_1.png
│   ├── page_11_image_2.png
│   ├── page_11_image_3.png
│   ├── page_11_image_4.png
│   ├── page_11_image_5.png
│   ├── page_12_image_1.png
│   ├── page_12_image_2.png
│   ├── page_12_image_3.png
│   ├── page_12_image_4.png
│   ├── page_16_image_1.png
│   ├── page_16_image_2.png
│   ├── page_16_image_3.png
│   ├── page_16_image_4.png
│   ├── page_18_image_1.png
│   ├── page_18_image_2.png
│   ├── page_22_image_1.png
│   ├── page_22_image_2.png
│   ├── page_22_image_3.png
│   ├── page_22_image_4.png
│   ├── page_22_image_5.png
│   ├── page_24_image_1.png
│   ├── page_24_image_2.png
│   ├── page_24_image_3.png
│   ├── page_24_image_4.png
│   ├── page_25_image_1.png
│   ├── page_36_image_1.png
│   └── page_51_image_1.png
│
├── plots/
│   ├── 2020-to-2026-all-inflation-analysis.png
│   ├── CCPI-Core-Inflation-Trend.png
│   ├── CCPI-Headline-Inflation-Trend.png
│   ├── NCPI-Core-Inflation-Trend.png
│   └── NCPI-Headline-Inflation-Trend.png
│
├── CBSL_All_Links.csv
├── CBSL_Monetary_Policy.pdf
├── CBSL_Monetary_Policy_PDF_Links.csv
├── CBSL_Relevant_Links.csv
├── Group_assignment.ipynb
├── all-inflation.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Git
- Jupyter Notebook
- Tesseract OCR, if OCR functionality is required

### 1. Clone the Repository

```bash
git clone https://github.com/praveenbhashitha16/CBSL-Web-Scraping-Project.git
```

### 2. Navigate to the Project Directory

```bash
cd CBSL-Web-Scraping-Project
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

Install the required Python libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Note:** Tesseract OCR is a separate application and must be installed independently if required by the project.

### 5. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open `Group_assignment.ipynb` and execute the notebook cells in the appropriate order.

### 6. Run the Scrapy Spider

Navigate to the Scrapy project directory:

```bash
cd cbsl_scraper
```

Run the spider and export the collected links to a CSV file:

```bash
scrapy crawl cbsl_links -O ../CBSL_All_Links.csv
```

The `-O` option overwrites the output file if it already exists.

## 📊 Project Outputs

### 📁 CSV Datasets

| File | Description |
|---|---|
| `CBSL_All_Links.csv` | Collected CBSL website links |
| `CBSL_Relevant_Links.csv` | Links identified as relevant to the project |
| `CBSL_Monetary_Policy_PDF_Links.csv` | Links to monetary policy PDF documents |
| `CSV_folder/cbsl_news.csv` | Collected news information |
| `CSV_folder/` yearly CSV files | Available yearly inflation datasets |
| `all-inflation.csv` | Combined inflation dataset |

### 📈 Inflation Visualizations

The `plots/` folder contains the following visualizations:

- CCPI Headline Inflation Trend
- CCPI Core Inflation Trend
- NCPI Headline Inflation Trend
- NCPI Core Inflation Trend
- Overall Inflation Analysis from 2020 to 2026, based on the available collected data

These plots help illustrate changes in inflation indicators over time.

### 📄 PDF Processing

The project includes `CBSL_Monetary_Policy.pdf` and an `extracted_pdf_images/` folder containing images extracted from selected PDF pages.

## 🎓 Learning Outcomes

Through this project, we gained practical experience in:

- Web scraping and data extraction
- HTML parsing and URL handling
- Working with Python scraping libraries
- Data manipulation and CSV processing using Pandas
- Extracting content from PDF documents
- Image processing and OCR techniques
- Creating data visualizations using Matplotlib
- Organizing datasets for further analysis
- Collaborative software development and teamwork

## ⚖️ Ethical Considerations

This project is intended for educational and academic purposes. Data collection should respect the CBSL website's terms of use, access restrictions, and applicable policies. Web requests should be made responsibly to avoid placing unnecessary load on the website.

## 👥 Group Members

1. **Dunura Ranaweera**
2. **Praveen Bhashitha**
3. **Janith Umayanga**
4. **Nethmini Padukka**

## 🔗 GitHub Repository

[**CBSL Web Scraping Project — GitHub Repository**](https://github.com/praveenbhashitha16/CBSL-Web-Scraping-Project)

---

⭐ If you find this project interesting, feel free to explore the repository and its datasets.
