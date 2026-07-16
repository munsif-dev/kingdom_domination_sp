# Kingdom Domination (Socket Programming + Pygame)

## Project Summary
Kingdom Domination is a real-time multiplayer quiz strategy game built with Python, Pygame, and TCP socket programming. Two players connect to a server, compete to answer quiz questions, and claim territories on a shared map. The project demonstrates practical client-server architecture, synchronized game-state management, and interactive UI handling in Python.

## Why This Project Matters
This project reflects strong foundations in:
- Core Python software engineering
- Network programming and socket communication
- Real-time state synchronization between distributed clients
- Interactive application development with event-driven design

It also aligns with AI engineering workflows where reliable distributed communication, low-latency interactions, and robust application logic are essential.

## Problem Solved
Designed and implemented a multiplayer game experience where:
- Multiple users can connect and play in the same session
- The server acts as the single source of truth for game state
- Client actions are validated server-side
- Gameplay outcomes remain consistent across all connected clients

## Key Features
- **Multiplayer matchmaking:** Pairs players into game sessions
- **Real-time gameplay updates:** Clients continuously fetch synchronized game state
- **Interactive question overlays:** Territory can be claimed only by answering correctly
- **Server-authoritative validation:** Answer checking and territory ownership handled centrally
- **Score and winner detection:** Automatic winner/tie evaluation after all territories are claimed
- **Visual game interface:** Territory map rendering and user interaction using Pygame

## Technical Architecture
### Client (`Game/client.py`)
- Renders the game map and interactive elements (territory nodes, overlays, buttons)
- Captures player input (mouse clicks, answer selection)
- Sends gameplay commands to the server (`get`, `get_question`, `answer`)
- Updates local display from server responses

### Network Layer (`Game/network.py`)
- Encapsulates TCP socket connection logic
- Handles client connection and response exchange
- Provides a reusable abstraction for sending game requests

### Server (`Game/server.py`)
- Handles incoming socket connections
- Creates and manages multiplayer game rooms
- Spawns per-client threads for parallel request handling
- Maintains session-level game objects and authoritative state

### Game Logic (`Game/game.py`)
- Stores territory ownership and claim status
- Serves question payloads for selected territories
- Validates answers and updates ownership
- Calculates scores and determines final winner

### Question Bank (`Game/questions.py`)
- Structured question dataset used by game logic
- Supports question, options, and answer mapping

## Skills Demonstrated
### Python Engineering
- Object-oriented design
- Modular code organization
- Error handling and runtime control flow

### Network Programming
- TCP/IP socket communication
- Client-server protocol design using command messages
- Multi-client handling via threading
- Data serialization/deserialization with `pickle`

### Real-Time Systems Thinking
- Shared state coordination
- Server-authoritative consistency model
- Session lifecycle management (connect, play, disconnect)

### Game & UI Development
- Event-driven programming with Pygame
- Dynamic rendering and overlay logic
- User interaction design for competitive gameplay

## Tools & Technologies
- **Language:** Python
- **Libraries:** Pygame, socket, threading (`_thread`), pickle
- **Concepts:** Client-server architecture, concurrency, serialization, state synchronization

## Engineering Highlights
- Built a complete end-to-end multiplayer system (UI + networking + game logic)
- Separated concerns between rendering, communication, and domain logic
- Implemented an authoritative server pattern for fairness and consistency
- Delivered a practical project that combines software engineering and systems fundamentals

## AI Engineer Positioning
As an AI Engineer, this project demonstrates transferable strengths that are directly relevant to production AI systems:
- Building reliable Python services
- Designing networked applications with clear protocol boundaries
- Managing concurrent client interactions safely
- Handling stateful workflows and deterministic outcomes

These are core capabilities for deploying and scaling AI-powered applications in real-world, multi-user environments.

## Suggested LinkedIn Project Entry
**Title:** Kingdom Domination – Multiplayer Quiz Strategy Game  
**Role:** AI Engineer / Python Developer  
**Description:** Built a real-time multiplayer quiz game in Python using Pygame and TCP sockets. Implemented a client-server architecture with threaded connection handling, server-authoritative game-state management, question-answer validation, synchronized territory control, and final score/winner computation. Demonstrates strong foundation in Python engineering, network programming, and distributed state management.

## Repository
- `/home/runner/work/kingdom_domination_sp/kingdom_domination_sp`
