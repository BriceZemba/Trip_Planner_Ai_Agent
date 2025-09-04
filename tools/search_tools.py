from crewai.tools import BaseTool
import requests, os, json

class SearchInternetTool(BaseTool):
    name: str = "search_internet"
    description: str = "Search the internet with Serper/Google and return the three top results."

    def _run(self, query: str) -> str:
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json"
        }
        resp = requests.post(url, headers=headers, data=payload)
        results = resp.json().get("organic", [])
        lines = []
        for r in results[:4]:
            lines.append(
                f"Title: {r.get('title')}\n"
                f"Link: {r.get('link')}\n"
                f"Snippet: {r.get('snippet')}\n"
                "-----------------"
            )
        return "\n".join(lines)