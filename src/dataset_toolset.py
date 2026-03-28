from typing import Any
import pandas as pd
from io import StringIO
import json
import os

class DatasetAnalyzerToolset:
    """Dataset Analyzer Toolset"""

    def __init__(self):
        pass

    async def analyze_dataset(self, data: str) -> str:
        """Analyze a CSV dataset, JSON dataset, or file path and return smart insights"""

        try:
            #detect input type
            if os.path.exists(data):
                # File path
                if data.endswith(".csv"):
                    df = pd.read_csv(data)
                elif data.endswith(".xlsx"):
                    df = pd.read_excel(data)
                else:
                    return "Unsupported file format"

            elif data.strip().startswith("{") or data.strip().startswith("["):
                # JSON input
                json_data = json.loads(data)
                df = pd.DataFrame(json_data)

            else:
                # Assume CSV text
                df = pd.read_csv(StringIO(data))


            # ---------------- BASIC INFO ----------------
            rows = int(df.shape[0])
            columns = int(df.shape[1])
            column_names = list(df.columns)

            # ---------------- MISSING VALUES ----------------
            missing_values = df.isnull().sum().to_dict()

            # ---------------- INSIGHTS ----------------
            insights = []
            recommendations = []

            numeric_cols = df.select_dtypes(include='number').columns

            for col in numeric_cols:
                mean_val = df[col].mean()
                std_val = df[col].std()

                # Insight: variation
                if std_val > mean_val * 0.5:
                    insights.append(f"{col} shows high variation")

                # Insight: outliers
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1

                outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]

                if len(outliers) > 0:
                    insights.append(f"{col} contains outliers")

            # ---------------- MISSING VALUE WARNINGS ----------------
            for col, val in missing_values.items():
                if val > 0:
                    percent = (val / rows) * 100
                    insights.append(f"{col} has {round(percent,2)}% missing values")

                    if percent > 30:
                        recommendations.append(f"Consider dropping or imputing column '{col}'")

            # ---------------- CORRELATION ----------------
            correlation_info = []

            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()

                for i in range(len(numeric_cols)):
                    for j in range(i + 1, len(numeric_cols)):
                        col1 = numeric_cols[i]
                        col2 = numeric_cols[j]
                        corr_val = corr_matrix.loc[col1, col2]

                        if abs(corr_val) > 0.7:
                            correlation_info.append(f"{col1} and {col2} are highly correlated ({round(corr_val,2)})")

            # ---------------- DATA QUALITY SCORE ----------------
            total_cells = rows * columns
            non_missing = total_cells - sum(missing_values.values())
            quality_score = round((non_missing / total_cells) * 100, 2)

            # ---------------- FINAL OUTPUT ----------------
            result = {
                "summary": {
                    "rows": rows,
                    "columns": columns,
                    "column_names": column_names,
                    "data_quality_score": f"{quality_score}%"
                },
                "missing_values": missing_values,
                "insights": insights,
                "correlations": correlation_info,
                "recommendations": recommendations
            }

            return str(result)

        except Exception as e:
            return str({"error": str(e)})

    def get_tools(self) -> dict[str, Any]:
        return {
            "analyze_dataset": self.analyze_dataset
        }