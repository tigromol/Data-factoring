import { combineReducers } from "redux";
import functionsReducer from "./functionsReducer";
import popupReducer from "./popupReducer";
import uploaderReducer from "./uploaderReducer";

export default combineReducers({
  functions: functionsReducer,
  popup: popupReducer,
  file: uploaderReducer
});
