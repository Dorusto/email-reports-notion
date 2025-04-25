class DataProcessor:
    @staticmethod
    def process_data(notion_data):
        # Example processing logic
        processed_data = []
        for item in notion_data.get("results", []):
            processed_data.append({
                "name": item["properties"].get("Name", {}).get("title", [{}])[0].get("text", {}).get("content", ""),
                "date": item["properties"].get("Date", {}).get("date", {}).get("start", "")
            })
        return processed_data