import { combineReducers } from "redux";
import chartReducer from "./chartReducer";
import functionsReducer from "./functionsReducer";
import uploaderReducer from "./uploaderReducer";

export default combineReducers({
	charts: chartReducer,
	functions: functionsReducer,
	file: uploaderReducer,
});
