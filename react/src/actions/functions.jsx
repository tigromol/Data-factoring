import axios from "axios";
import {
	FETCH_FUNCTIONS_REQUEST,
	FETCH_FUNCTIONS_SUCCESS,
	FETCH_FUNCTIONS_FAILURE,
} from "../types/index";

export const getFunctions = () => async dispatch => {
	dispatch({ type: FETCH_FUNCTIONS_REQUEST });

	try {
		const { data } = await axios.get(`/api/functions/`);
		dispatch({
			type: FETCH_FUNCTIONS_SUCCESS,
			payload: data,
		});
	} catch (err) {
		dispatch({ type: FETCH_FUNCTIONS_FAILURE });
	}
};
