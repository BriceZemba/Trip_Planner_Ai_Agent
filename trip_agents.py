from crewai import Agent
from tools.search_tools import SearchInternetTool
from tools.browser_tools import ScrapeAndSummarizeWebsiteTool
from tools.calculator_tools import calculate  # if this is also a BaseTool subclass

search_internet = SearchInternetTool()
scrape_and_summarize_website = ScrapeAndSummarizeWebsiteTool()

class TripAgents:
    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices",
            backstory="An expert in analyzing travel data to pick ideal destinations",
            tools=[search_internet, scrape_and_summarize_website],
            llm="gemini/gemini-1.5-flash",
            verbose=True,
        )

    def local_expert(self):
        return Agent(
            role="Local Expert at this city",
            goal="Provide the BEST insights about the selected city",
            backstory="A knowledgeable local guide...",
            tools=[search_internet, scrape_and_summarize_website],
            llm="gemini/gemini-1.5-flash",
            verbose=True,
        )

    def travel_concierge(self):
        return Agent(
            role="Amazing Travel Concierge",
            goal="Create the most amazing travel itineraries...",
            backstory="Specialist in travel planning...",
            tools=[search_internet, scrape_and_summarize_website],
            llm="gemini/gemini-1.5-flash",
            verbose=True,
        )