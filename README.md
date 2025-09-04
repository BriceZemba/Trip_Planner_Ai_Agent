# 🧳 CrewAI Trip-Planner  
**Autonomous AI agents that research, compare and build complete city itineraries for you.**

---

## 🚀 What it does
1. **City comparison** – ranks destinations by season, weather and flight cost.  
2. **Local insights** – scrapes Reddit, travel blogs, POI databases.  
3. **Itinerary generation** – day-by-day plan with budget, opening hours, travel time.  
4. **Price watching** – live flight + hotel quotes (Skyscanner, Booking, Expedia).  
5. **Calendar sync** – one-click push of final schedule to Google Calendar.

---

## 🏗️ Stack
| Layer | Tech |
|-------|------|
| Agent framework | [CrewAI](https://github.com/joaomdmoura/crewai) |
| LLM | Google Gemini 1.5 Flash (default) / Ollama (local) |
| Search | Serper.dev (Google) |
| Scraping | Browserless.io |
| Weather | OpenWeatherMap / Visual Crossing |
| FX rates | CurrencyLayer |
| Maps & routing | OpenStreetMap (OSRM) |
| Language | Python ≥ 3.10 |

---

## ⚙️ 1-Minute Setup
```bash
git clone https://github.com/your-username/crewai-trip-planner.git
cd crewai-trip-planner
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` in the project root:
```env
SERPER_API_KEY=xxxxxxxxxxxxxxxxxxxx
BROWSERLESS_API_KEY=xxxxxxxxxxxxxxxxxxxx
GOOGLE_API_KEY=xxxxxxxxxxxxxxxxxxxx
OPENWEATHER_API_KEY=xxxxxxxxxxxxxxxxxxxx   # optional
```

Run:
```bash
python main.py
```
Answer the interactive prompts (budget, dates, vibe, travellers) and watch the agents collaborate.

---

## 🧠 Agent Crew
| Agent | Specialty | Tools |
|-------|-----------|-------|
| `CitySelector` | Destination ranking | `search_internet`, `scrape_website`, `weather_trends` |
| `LocalWhisperer` | Cultural tips & hidden gems | `reddit_insights`, `youtube_vlogs`, `osm_pois` |
| `ItineraryEngineer` | Schedule optimisation | `osm_routing`, `google_calendar_sync`, `itinerary_dataset` |
| `PriceTracker` | Live prices & alerts | `skyscanner_search`, `booking_com`, `expedia_search`, `currency_layer` |
| `WeatherOracle` | Seasonality windows | `openweathermap`, `visual_crossing` |

---

## 📁 Project Layout
```
crewai-trip-planner/
├─ main.py               # CLI entry-point
├─ trip_agents.py        # Agent definitions
├─ trip_tasks.py         # Task prompts & expected outputs
├─ tools/
│  ├─ search_tools.py    # Serper wrapper
│  ├─ browser_tools.py   # Browserless scraper
│  ├─ calculator_tools.py
│  └─ weather_tools.py
├─ crews/
│  └─ trip_crew.py       # Crew assembly & kick-off logic
├─ requirements.txt
└─ README.md
```

---

## 🔧 Customising
- Swap LLM: change `llm=` line in any agent (OpenAI, Ollama, Claude, local GGUF…).  
- Add new tool: subclass `crewai_tools.BaseTool`, implement `_run(self, arg)`, drop into `tools/`, import into agent.  
- New task: copy any YAML block in `trip_tasks.py`, tweak prompt & output schema.

---

## 🧪 Example Output (abridged)
```json
{
  "city": "Lisbon",
  "score": 9.2,
  "avg_flight_price": 412,
  "best_weather_window": "15 Mar – 30 Apr",
  "itinerary": [
    {
      "day": 1,
      "activities": [
        {
          "time": "09:00",
          "name": "Pastéis de Belém tasting",
          "cost": 5,
          "lat": 38.6976,
          "lon": -9.2069,
          "booking_url": "https://..."
        }
      ]
    }
  ],
  "packing_list": ["Light jacket", "Comfortable sneakers", "Type-C plug"],
  "total_estimated_budget": 820
}
```

---

## 📄 License
MIT – feel free to fork and commercialise.

---

## 🤝 Contributing
PRs welcome!  
- Open an issue first for big changes.  
- Keep tools stateless and thread-safe.  
- Add a unit test under `tests/`.

Happy travels 🌍
