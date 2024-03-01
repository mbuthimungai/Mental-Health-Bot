# Mental-Health-Bot
This is a bot that tracks mental health cases in social media platforms



### 1. Use Case Diagram

```plantuml
@startuml
left to right direction
skinparam packageStyle rectangle

actor "Social Media User"
actor "System Administrator"
actor "Healthcare Professional"
actor "General Public/User"

rectangle System {
  usecase (Collect Data) as UC1
  usecase (Configure Bot) as UC2
  usecase (Generate Insights) as UC3
  usecase (View Insights) as UC4
  usecase (Analyze Data) as UC5
  usecase (Process Data) as UC6

  "Social Media User" --> UC1
  "System Administrator" --> UC2
  UC3 .> UC4 : <<include>>
  UC5 .> UC3 : <<include>>
  UC6 .> UC5 : <<include>>
  UC1 .> UC6 : <<include>>
  "Healthcare Professional" --> UC4
  "General Public/User" --> UC4
}
@enduml
```

This diagram represents the following use cases and their interactions:
- **Collect Data**: Social media users create content that the system collects.
- **Configure Bot**: The system administrator configures and manages the bot.
- **Generate Insights**: The bot analyzes the collected data to generate insights.
- **View Insights**: Healthcare professionals and the general public can view the generated insights.
- **Analyze Data**: The bot processes the data to analyze it.
- **Process Data**: The bot preprocesses the collected data for analysis.

### 2. Class Diagram

```mermaid
%%{init: {'theme': 'default'}}%%
classDiagram
  class SocialMediaScraper {
    +String platform_name
    +Dictionary api_keys
    +fetch_posts()
  }
  class DataProcessor {
    -raw_data
    +clean_data()
    +tokenize_text()
  }
  class NLPAnalyzer {
    -processed_data
    +analyze_sentiment()
    +detect_topics()
  }
  class InsightGenerator {
    -analysis_results
    +generate_trends()
    +compile_report()
  }
  class Dashboard {
    -reports
    -visualizations
    +display_insights()
  }

  SocialMediaScraper --> DataProcessor : feeds
  DataProcessor --> NLPAnalyzer : feeds
  NLPAnalyzer --> InsightGenerator : feeds
  InsightGenerator --> Dashboard : displays
```

### 3. Sequence Diagram

```mermaid
%%{init: {'theme': 'default'}}%%
sequenceDiagram
  participant SystemAdmin as "System Administrator"
  participant SocialMediaScraper as "Social Media Scraper"
  participant DataProcessor
  participant NLPAnalyzer
  participant InsightGenerator
  participant Dashboard

  SystemAdmin->>SocialMediaScraper: Initiate Data Collection
  SocialMediaScraper->>DataProcessor: Feed Raw Data
  DataProcessor->>NLPAnalyzer: Processed Data
  NLPAnalyzer->>InsightGenerator: Analysis Results
  InsightGenerator->>Dashboard: Generate Insights
  Dashboard->>SystemAdmin: Display Insights
```

### 4. Component Diagram

```mermaid
%%{init: {'theme': 'default'}}%%
componentDiagram
  package "Data Collection Component" {
    [Social Media APIs]
    [Scraping Services]
  }
  package "Data Processing Component" {
    [Text Cleaning]
    [Normalization]
  }
  package "NLP Analysis Component" {
    [Sentiment Analysis]
    [Topic Detection]
  }
  package "Insight Generation Component" {
    [Trend Aggregation]
    [Report Generation]
  }
  package "User Interface Component" {
    [Web Dashboard]
  }

  [Social Media APIs] ..> [Text Cleaning] : Data Flow
  [Scraping Services] ..> [Text Cleaning] : Data Flow
  [Text Cleaning] ..> [Normalization] : Data Flow
  [Normalization] ..> [Sentiment Analysis] : Data Flow
  [Sentiment Analysis] ..> [Trend Aggregation] : Data Flow
  [Topic Detection] ..> [Trend Aggregation] : Data Flow
  [Trend Aggregation] ..> [Web Dashboard] : Data Flow
```
