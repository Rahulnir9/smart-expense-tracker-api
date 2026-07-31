
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
- Reviewing and improving the README.

### My Contributions
I was responsible for:
- Creating and organizing the complete project structure.
- Integrating the generated code into a working application.
- Connecting the routes, models, service layer, and storage layer.
- Debugging import issues and project configuration problems.
- Modifying endpoint designs to better fit the assignment.
- Running and validating the application using Swagger UI.
- Expanding and verifying the automated test suite.
- Preparing the repository for submission.

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