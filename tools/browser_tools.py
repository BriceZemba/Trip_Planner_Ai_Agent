from crewai.tools import BaseTool
from unstructured.partition.html import partition_html
import requests, os, json

class ScrapeAndSummarizeWebsiteTool(BaseTool):
    name: str = "ScrapeAndSummarizeWebsite"
    description: str = (
        "Scrape any web page via Browserless.io and return a concise summary of ten lines maximun."
    )

    def _run(self, website: str) -> str:
        url = (
            "https://chrome.browserless.io/content"
            f"?token={os.environ['BROWSERLESS_API_KEY']}"
        )
        payload = json.dumps({"url": website})
        headers = {"cache-control": "no-cache", "content-type": "application/json"}
        response = requests.post(url, headers=headers, data=payload)
        elements = partition_html(text=response.text)
        content = "\n\n".join([str(el) for el in elements])
        return content[:8000] + "..." if len(content) > 8000 else content