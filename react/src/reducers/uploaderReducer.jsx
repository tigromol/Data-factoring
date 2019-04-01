import {
	POST_FILE_REQUEST,
	POST_FILE_FAILURE,
	POST_FILE_SUCCESS,
} from "../types";

const initialState = {
	error: false,
	file: {},
};

export default (state = initialState, action) => {
	switch (action.type) {
		case POST_FILE_REQUEST:
			return { error: false };

		case POST_FILE_SUCCESS:
			return { error: false, ...action.payload };

		case POST_FILE_FAILURE:
			return { error: true };

		default:
			return state;
	}
};
