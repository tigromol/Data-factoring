import { POPUP_OPEN, POPUP_CLOSE } from "../types";

const initialState = {
  isOpen: false,
  componentId: null
};

export default (state = initialState, { type, payload }) => {
  switch (type) {
    case POPUP_OPEN:
      return { ...state, isOpen: true, componentId: payload };

    case POPUP_CLOSE:
      return { ...state, isOpen: false, componentId: null };

    default:
      return state;
  }
};
