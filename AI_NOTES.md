
# AI Usage Notes
## AI Tool Used
- ChatGPT (OpenAI)


## 1. Which parts of the code were AI-generated vs. written by me
### AI-assisted
I used ChatGPT as a development assistant throughout the project. It helped me by:
- Suggesting the initial project structure.
- Generating draft implementations for:
  - FastAPI routes
  - Pydantic models
  - Service layer
  - JSON storage layer
- Suggesting custom exception classes.
- Generating an initial Pytest test suite.

### My Contributions
I was responsible for:
- Designing and organizing the project structure.
- Integrating all components into a working application.
- Correcting implementation mistakes in AI-generated code.
- Fixing import, routing, and configuration issues.
- Revising API endpoints to match the assignment requirements.
- Writing and improving validation logic.
- Expanding the automated test suite to 20 test cases.
- Testing every endpoint using Swagger UI.
- Ensuring the application behaved correctly before submission.

## 2. What I validated, tested, or changed in the AI output, and why
I reviewed every AI-generated suggestion before including it in the project.
The following changes were made after validation:
- Modified the API endpoint design to better match the assignment requirements and improve clarity.
- Replaced generic exceptions with custom exceptions to improve error handling and code readability.
- Expanded the automated test suite from a few basic tests to **20 test cases** covering successful operations, validation errors, and edge cases.
- Verified every endpoint manually using FastAPI Swagger UI.
- Ran the complete Pytest suite after each significant change to ensure existing functionality was not broken.
- Reviewed all generated code to ensure it matched the required functionality before keeping it in the final implementation.

## 3. AI suggestions I decided not to use, and why
Not every AI suggestion was included in the final project.
Some suggestions I intentionally rejected were:
- Using query parameters for category filtering instead of dedicated category endpoints. I chose the endpoint structure that best matched the final API design.
- Adding logging and global exception handlers after the project was already complete. These improvements were useful but unnecessary for the assignment and would have added extra complexity.
- Introducing additional production features such as database integration, authentication, pagination, or Docker support. The assignment only required JSON file storage, so I kept the implementation focused on the stated requirements.
- Making further architectural changes after all tests were passing. I decided not to refactor a stable implementation to avoid introducing unnecessary risk before submission.

## Testing and Verification
Before submission, I verified that:
- The application starts successfully using Uvicorn.
- All API endpoints function correctly through FastAPI Swagger UI.
- The complete automated test suite passes successfully (**20/20 tests**).
- The installation, server startup, and testing commands documented in the README work as expected.

## Summary
AI was used as a development assistant to accelerate implementation and provide guidance. However, every generated solution was reviewed, integrated, tested, and, where necessary, modified before being included in the final submission.
