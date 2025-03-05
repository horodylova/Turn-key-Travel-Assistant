import os
import logging
from datetime import datetime, timedelta
from typing import Optional, Type, Any
from pydantic.v1 import BaseModel, Field
from crewai_tools import BaseTool

class FlightAnalyzerSchema(BaseModel):
    departure: str = Field(..., description="Departure city from trip_plan.departure")
    destination: str = Field(..., description="Destination city from trip_plan.location")

class FlightPriceAnalyzer(BaseTool):
    name = "flight_price_analyzer"
    description = """Direct tool to analyze flight options between cities.
    Required: Use this tool directly with data from trip_plan:
    1. Get departure from trip_plan.departure
    2. Get destination from trip_plan.location
    3. Call this tool with both values
    Do not delegate - use tool directly!
    
    Example usage:
    flight_price_analyzer(departure="London", destination="Paris")
    
    Output will be flight details with prices and dates."""
    args_schema: Type[BaseModel] = FlightAnalyzerSchema
    
    def _run(
        self,
        departure: str,
        destination: str,
        **kwargs: Any,
    ) -> dict:
        try:
            return {
                "flight_details": {
                    "route": {
                        "from": departure,
                        "to": destination,
                        "airports": {
                            "departure": f"{departure} International Airport",
                            "arrival": f"{destination} International Airport"
                        }
                    },
                    "options": {
                        "price_range": {
                            "min": 200,
                            "max": 600,
                            "currency": "EUR"
                        },
                        "best_dates": self._get_next_dates(),
                        "duration": "estimated flight time"
                    }
                }
            }
        except Exception as e:
            return {"error": f"Failed to analyze flight prices: {str(e)}"}

    def _get_next_dates(self) -> list:
        current = datetime.now()
        return [(current + timedelta(days=x)).strftime("%Y-%m-%d") 
                for x in range(7, 37, 7)]

    def _arun(self, query_data: str):
        raise NotImplementedError("Async not implemented")