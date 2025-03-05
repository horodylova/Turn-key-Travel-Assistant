# Turn-key Travel Assistant 🌍✈️

## Project Overview

Turn-key Travel Assistant is an innovative travel planning solution that revolutionizes the way people explore the world. By leveraging an intelligent assembly of AI agents, this project simplifies the complex process of travel planning, transforming it from a time-consuming task into a seamless, personalized experience.

## Key Features

### Intelligent Travel Planning
- **Destination Finder**: Leverages web search to identify the perfect travel destination based on user preferences
- **Trip Planner**: Generates comprehensive 7-day itineraries with detailed daily activities
- **Flight Advisor**: Analyzes and suggests optimal flight options with price range insights

## Problem Solved

Travel planning often involves:
- Extensive research
- Balancing spontaneity with budget constraints
- Coordinating complex schedules

Turn-key Travel Assistant eliminates these pain points by creating a complete, randomized travel itinerary tailored to individual preferences.

## Technical Architecture

The project is implemented using the CrewAI platform, featuring three primary agents:

1. **DestinationFinder**
   - Utilizes `website_search_tool`
   - Analyzes user requests to select ideal travel locations
   - Considers unique aspects of user preferences

2. **TripPlanner**
   - Uses `scrape_website_tool`
   - Creates detailed day-by-day itineraries
   - Maximizes destination experience

3. **FlightAdvisor**
   - Employs custom `flight_price_analyzer`
   - Identifies nearby airports
   - Determines flight price ranges

## Demo

Check out the project in action! 

[![Turn-key Travel Assistant Demo](https://img.youtube.com/vi/lO6Jeit-Rak/0.jpg)](https://www.youtube.com/watch?v=lO6Jeit-Rak)

## Core Technologies

- CrewAI
- Web Search Tools
- Custom Flight Price Analyzer
- Python

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/your-username/turn-key-travel-assistant](https://github.com/your-username/turn-key-travel-assistant)