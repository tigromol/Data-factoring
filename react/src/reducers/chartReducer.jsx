// гист., линия,
import {
	FETCH_CHART_FAILURE,
	FETCH_CHART_REQUEST,
	FETCH_CHART_SUCCESS,
} from "../types";
const initState = [
	{
		name: "123",
		type: 1,
		data: [
			["Date", "Value"],
			[new Date(1996, 1, 1), 2000 * Math.random()],
			[new Date(1997, 1, 1), 2000 * Math.random()],
			[new Date(1998, 1, 1), 2000 * Math.random()],
			[new Date(1999, 1, 1), 2000 * Math.random()],
			[new Date(2000, 1, 1), 2000 * Math.random()],
			[new Date(2001, 1, 1), 2000 * Math.random()],
			[new Date(2002, 1, 1), 2000 * Math.random()],
			[new Date(2003, 1, 1), 2000 * Math.random()],
			[new Date(2004, 1, 1), 2000 * Math.random()],
			[new Date(2005, 1, 1), 2000 * Math.random()],
			[new Date(2006, 1, 1), 2000 * Math.random()],
			[new Date(2007, 1, 1), 2000 * Math.random()],
			[new Date(2008, 1, 1), 2000 * Math.random()],
			[new Date(2009, 1, 1), 2000 * Math.random()],
		],
	},
];

export default (state = initState, action) => {
	switch (action.type) {
		case FETCH_CHART_REQUEST:
			return state;

		case FETCH_CHART_SUCCESS:
			return state;

		case FETCH_CHART_FAILURE:
			return state;

		default:
			return state;
	}
};
