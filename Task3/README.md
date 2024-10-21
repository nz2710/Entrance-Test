# Redux Post App

This project is a simple React application that uses Redux for state management and interacts with the JSONPlaceholder API to fetch and display posts.

## Features
- Fetches and displays posts from `https://jsonplaceholder.typicode.com/posts`.
- Allows users to add new posts.
- Uses Redux for state management and Redux Thunk for async API calls.

## Installation
1. Clone the repository:
### git clone https://github.com/nz2710/Entrance-Test.git
2. Navigate to the project directory
### cd Task3
3. Install dependencies:
### npm install

## Usage
To start the development server, run:
### npm start
The application will be available at http://localhost:3000.

## Technologies Used
- React
- Redux
- Redux-Thunk
- Axios

## File Structure
- **actions/**: Contains action creators for fetching and adding posts.
- **reducers/**: Contains reducers to handle actions.
- **components/**: Contains React components for displaying posts and adding new posts.

## API
This project uses the JSONPlaceholder API to fetch and post data:
https://jsonplaceholder.typicode.com/posts

## License
This project is licensed under the MIT License.