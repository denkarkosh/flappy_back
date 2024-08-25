# FlappyScroll Backend

## Overview

This is the backend service for the FlappyScroll game, a blockchain-integrated gaming platform where users can mint and utilize NFTs as in-game assets. This backend is built using Python and FastAPI, handling user management, game data storage, and interactions with the Scroll blockchain.

## Features

- User Management: Register and manage user profiles, including wallet information and game data.
- Score Tracking: Store and retrieve player scores, supporting the leaderboard functionality.
- NFT Integration: Interface with smart contracts on the Scroll blockchain for NFT management.
- Leaderboard: Provide a global leaderboard showing player rankings based on scores.

## Tech Stack

- Python: Programming language.
- FastAPI: Web framework used for building the backend API.
- SQLAlchemy: ORM for database interactions.
- PostgreSQL: Relational database to store user profiles, scores, and other game-related data.
- Ethers.js: Used for interacting with the Scroll blockchain (if applicable).

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js (for blockchain interactions)

### Setup

1. Clone the repository:

   
    git clone https://github.com/yourusername/flappyscroll-backend.git
    cd flappyscroll-backend
    
2. Create a virtual environment:

   
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    
3. Install the dependencies:

   
    pip install -r requirements.txt
    
4. Set up environment variables:

    Create a .env file in the project root and add the following:

   
    DATABASE_URL=postgresql://username:password@localhost:5432/flappyscroll
    SECRET_KEY=your_secret_key
    
5. Apply database migrations:

   
    alembic upgrade head
    
6. Run the development server:

   
    uvicorn app.main:app --reload
    
    The API should now be running on http://127.0.0.1:8000.

## API Endpoints

- `POST /register`: Register a new user.
- `POST /login`: Authenticate a user and return a token.
- `GET /user/{id}`: Get details of a specific user.
- `POST /score`: Submit a new score.
- `GET /leaderboard`: Retrieve the global leaderboard.

## Database Schema

- User
  - id: UUID
  - username: String
  - email: String
  - wallet_address: String
  - created_at: Timestamp

- Score
  - id: UUID
  - user_id: UUID (ForeignKey)
  - score: Integer
  - created_at: Timestamp

## Blockchain Interaction

- Contract Deployment: The smart contracts for minting NFTs are deployed on the Scroll network. Interaction with these contracts should be handled primarily on the frontend using Ethers.js.

- NFT Management: While the backend stores references to NFTs in the user profile, minting and other interactions with NFTs are managed on the frontend.

## Deployment

1. Set up a PostgreSQL database on your hosting platform.
2. Set environment variables in your hosting environment.
3. Deploy the application using your preferred method (e.g., Docker, Heroku, AWS, etc.).
4. Run database migrations to set up the database schema.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
