# ResumeMatch – Resume Job Skill Matching and Gap Analysis System

## Project Overview

ResumeMatch is a Flask-based web application that analyzes a candidate's resume against one or more job descriptions.

The application extracts text from a PDF resume, identifies technical and professional skills, compares them with the skills required by a job description, and displays the matching and missing skills.

The system also allows the same resume to be compared with multiple job descriptions.

## Problem Statement

Job seekers often need to compare their resumes with different job requirements. Manually checking a resume against every job description can be time-consuming.

ResumeMatch provides a simple web-based solution to:

- Extract skills from a resume PDF
- Identify skills required by a job description
- Calculate a skill match percentage
- Display matched skills
- Display missing skills
- Compare one resume with multiple job descriptions
- Provide a JSON API for skill extraction
- Provide a health-check endpoint for deployment monitoring

## Key Features

### 1. Resume Upload

Users can upload their resume in PDF format.

### 2. Job Description Analysis

Users can enter a job description and compare it with their resume.

### 3. Skill Extraction

The application identifies skills from predefined categories such as:

- Programming
- Frameworks and Libraries
- Databases
- Cloud and DevOps
- Data and AI
- Software Development
- Networking
- Tools and Platforms

### 4. Skill Matching

The application calculates:

- Match percentage
- Matched skills
- Missing skills

### 5. Multiple Job Comparison

A single resume can be compared against multiple job descriptions to understand how well it matches different opportunities.

### 6. JSON API

The `/api/skills` endpoint accepts text and returns the detected skills as JSON.

### 7. Health Check

The `/health` endpoint returns:

```json
{
  "status": "ok"
}