import axios from "axios";
import {
	FETCH_CHART_FAILURE,
	FETCH_CHART_REQUEST,
	FETCH_CHART_SUCCESS,
} from "../types/index";

export const getChart = chartId => dispatch => {
	dispatch({ type: FETCH_CHART_REQUEST });
	try {
		const { data } = axios.get(`/api/data/${chartId}`);
		dispatch({
			type: FETCH_CHART_SUCCESS,
			payload: data,
		});
	} catch (err) {
		dispatch({ type: FETCH_CHART_FAILURE });
	}
};
