# Agent Template Customization Guide

This guide walks you through customizing the A2A agent template for your specific use case.

## Customization Checklist

### 1. Basic Information
- [ ] Replace `dataset-lie-detector` with your agent name
- [ ] Replace `Detects bias, imbalance, and misleading patterns in datasets` with your agent description
- [ ] Replace `dataset-lie-detector` with your container name (port is fixed at 5000)

### 2. Skills & Capabilities
- [ ] Replace `dataset_audit` with unique skill ID
- [ ] Replace `Dataset Audit` with human-readable skill name
- [ ] Replace `Analyzes dataset reliability` with skill description
- [ ] Replace `tags=["data", "analysis", "bias", "ml"],` with array of relevant tags
- [ ] Replace `[
    "Analyze this dataset for bias and imbalance",
    "Check if my dataset has missing values or duplicates",
    "Is this dataset reliable for machine learning?",
    "Find issues in this CSV dataset"
]` with array of usage examples

### 3. Toolset Configuration
- [ ] Replace `DatasetLieDetector` with your toolset class name
- [ ] Replace `dataset_toolset` with your toolset module name
- [ ] Replace `"Analyzes datasets to detect bias, missing values, duplicates, imbalance, and potential risks before machine learning"` with toolset description
- [ ] Rename `src/agent_toolset.py` to your module name

### 4. Implementation
- [ ] Update `{{SYSTEM_PROMPT}}` with your agent's system prompt
- [ ] Implement actual functions in your toolset
- [ ] Add required dependencies to pyproject.toml
- [ ] Update Dockerfile with additional dependencies
- [ ] Set up environment variables

### 5. Testing
- [ ] Test locally with `python -m src`
- [ ] Test Docker build and run
- [ ] Verify all functions work as expected

## Example Replacements

Here are example replacements for a weather agent:

```
dataset-lie-detector → "a2a-weather-agent"
Detects bias, imbalance, and misleading patterns in datasets → "An intelligent weather forecasting agent"
dataset-lie-detector → "a2a-weather"
# Port is fixed at 5000 for all agents
dataset_audit → "weather_forecasting"
Dataset Audit → "Weather Forecasting"
Analyzes dataset reliability → "Get weather information and forecasts"
tags=["data", "analysis", "bias", "ml"], → ['weather', 'forecast', 'temperature', 'humidity']
[
    "Analyze this dataset for bias and imbalance",
    "Check if my dataset has missing values or duplicates",
    "Is this dataset reliable for machine learning?",
    "Find issues in this CSV dataset"
] → [
    "What's the weather like in New York?",
    "Give me a 5-day forecast for London",
    "Is it going to rain tomorrow in Seattle?"
]
DatasetLieDetector → "WeatherToolset"
dataset_toolset → "weather_toolset"
"Analyzes datasets to detect bias, missing values, duplicates, imbalance, and potential risks before machine learning" → "Weather information and forecasting toolset"
{{SYSTEM_PROMPT}} → "You are a Weather Agent that helps users get current weather conditions and forecasts..."
```

## Tips

1. **Consistent Naming:** Use consistent naming patterns across all placeholders
2. **Clear Descriptions:** Make descriptions clear and specific to your agent's purpose
3. **Relevant Examples:** Provide examples that showcase your agent's main capabilities
4. **Port Management:** All agents use port 5000 internally; external routing is handled by the platform
5. **Environment Variables:** Plan your environment variables early in the customization process