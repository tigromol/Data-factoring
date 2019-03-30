import axios from "axios";
import {
	POST_FILE_REQUEST,
	POST_FILE_SUCCESS,
	POST_FILE_FAILURE,
} from "../types/index";

export const uploadFile = file => async dispatch => {
	dispatch({ type: POST_FILE_REQUEST });
	try {
		const { data } = await axios.post(`/api/data/`, file);
		dispatch({ type: POST_FILE_SUCCESS, payload: data });
	} catch (err) {
		dispatch({ type: POST_FILE_FAILURE });
	}
};
