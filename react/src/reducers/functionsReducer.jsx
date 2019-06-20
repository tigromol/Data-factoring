import {
  FETCH_FUNCTIONS_REQUEST,
  FETCH_FUNCTIONS_SUCCESS,
  FETCH_FUNCTIONS_FAILURE
} from "../types";

const initialState = [];

export default (state = initialState, { type, payload }) => {
  switch (type) {
    case FETCH_FUNCTIONS_REQUEST:
      return state;

    case FETCH_FUNCTIONS_SUCCESS:
      return [...payload];

    case FETCH_FUNCTIONS_FAILURE:
      return state;

    default:
      return state;
  }
};
