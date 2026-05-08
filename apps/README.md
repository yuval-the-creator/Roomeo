# repo structure
/RooMeo
├── apps/
│   ├── mobile/             # Expo / React Native project
│   │   ├── src/
│   │   │   ├── components/ # Swiper, Card, UI elements
│   │   │   ├── screens/    # Feed, Likes, Profile
│   │   │   ├── hooks/      # API fetching logic
│   │   │   └── types/      # Frontend-specific interfaces
│   │   ├── app.json        # Expo config
│   │   └── package.json
│   └── server/             # FastAPI / FastMCP project
│       ├── app/
│       │   ├── api/        # Endpoints (feed, swipe, user)
│       │   ├── core/       # Config and DB session
│       │   ├── models/     # SQLAlchemy or SQLModel classes
│       │   └── schemas/    # Pydantic serialization
│       ├── main.py         # Entry point
│       └── requirements.txt (or pyproject.toml for uv)
├── packages/
│   └── shared/             # (Optional) Shared constants/JSON schemas
├── docker-compose.yml      # Orchestrates Postgres and the API
├── .gitignore
└── README.md