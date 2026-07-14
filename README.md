# Cortex - AI Powered Email Intelligence Assistant

## Overview

Cortex is an AI-powered email intelligence assistant that automatically reads unread Gmail messages, extracts actionable tasks using Llama 3, stores organizational knowledge in a vector database, and generates intelligent daily briefings.

The project combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), LangGraph multi-agent workflows, FastAPI, and Streamlit into a production-oriented AI application.

---

## Features

### Email Intelligence

* Gmail API Integration
* Automatic unread email retrieval
* Email priority detection
* Security alert detection

### AI Task Extraction

* Llama 3 powered task extraction
* Deadline identification
* Task categorization
* Duplicate task prevention

### Retrieval-Augmented Generation (RAG)

* ChromaDB vector database
* Semantic email memory
* Historical email retrieval
* Context-aware task extraction

### Multi-Agent Workflow (LangGraph)

* Supervisor Agent
* Email Agent
* Task Agent
* Priority Agent
* Briefing Agent

### Productivity Management

* SQLite task storage
* Task completion tracking
* Productivity metrics
* Daily briefing generation

### Backend & Frontend

* FastAPI REST API
* Streamlit Dashboard
* Frontend/Backend separation
* Real-time task updates

### Software Engineering

* Environment-based configuration
* Centralized logging
* Pytest automated testing
* Git/GitHub workflow

---

## Architecture

Gmail API

↓

Email Fetching Layer

↓

LangGraph Supervisor Agent

↓

Email Agent

↓

Task Agent (Llama 3 + RAG)

↓

Priority Agent

↓

Briefing Agent

↓

SQLite Database + ChromaDB Vector Store

↓

FastAPI Backend

↓

Streamlit Dashboard

---

## Tech Stack

### AI & LLM

* Ollama
* Llama 3
* LangGraph

### RAG & Memory

* ChromaDB
* Sentence Transformers

### Backend

* FastAPI
* Python

### Frontend

* Streamlit

### Database

* SQLite

### Integrations

* Gmail API

### Testing

* Pytest

### Version Control

* Git
* GitHub

---

## Current Project Status

### Completed

* Gmail Integration
* Email Classification
* Priority Detection
* Daily Briefing Agent
* Email Draft Generation
* Task Extraction
* SQLite Task Storage
* Workflow Automation
* Streamlit Dashboard
* FastAPI Backend
* Task Completion Workflow
* Productivity Analytics
* RAG Memory System
* LangGraph Multi-Agent Workflow
* Environment Configuration
* Logging System
* Automated Testing

### In Progress

* Docker Deployment
* CI/CD Pipeline

---

## Future Enhancements

* Docker Containerization
* GitHub Actions CI/CD
* Cloud Deployment
* Calendar Integration
* Slack Integration
* Advanced Analytics Dashboard

---

## Learning Outcomes

This project demonstrates:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Multi-Agent Systems
* API Development
* Full Stack Development
* Software Testing
* Production Engineering
* System Design
