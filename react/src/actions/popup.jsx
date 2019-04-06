import { POPUP_OPEN, POPUP_CLOSE } from "../types/index";

export const popupOpen = componentId => ({
  type: POPUP_OPEN,
  payload: componentId
});

export const popupClose = () => ({
  type: POPUP_CLOSE
});
