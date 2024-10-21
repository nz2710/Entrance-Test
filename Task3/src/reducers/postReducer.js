import { FETCH_POSTS, ADD_POST } from '../actions/postActions';

const initialState = {
  posts: []
};

export default function postReducer(state = initialState, action) {
  switch (action.type) {
    case FETCH_POSTS:
      return {
        ...state,
        posts: action.payload
      };
    case ADD_POST:
      return {
        ...state,
        posts: [action.payload, ...state.posts]
      };
    default:
      return state;
  }
}